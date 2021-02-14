"""
Process company relations data as a graph.

Description:

Methods:
1. extract_company_relations
2. create_graph_company_relations
3. process_company_hierarchy
"""
from graphframes import *
from pipelines.utils import configmanagement as cm
from pipelines.utils import transformations
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, lit, map_values, size, when

spark = SparkSession.builder.getOrCreate()


def extract_company_relations(filePath):
    """
    Read company relations csv.

    description:
    reads csv from a mounted path on the databricks workspace.

    paramters:
    1. filePath: String with a Databricks Mounter path.

    returns:
    company relations dataframe.
    """
    df = spark.read.format("csv").option("header", "true").load(filePath)
    df = df\
        .select(
            col("company_id").alias("id"),
            col("name").alias("company_name"),
            col("parent")
        )
    return df


def extract_land_ownership(filePath):
    """
    Read landownership csv.

    description:
    reads csv from a mounted path on the databricks workspace.

    paramters:
    1. filePath: String with a Databricks Mounter path.

    returns:
    landownership dataframe.
    """
    df = spark.read.format("csv").option("header", "true").load(filePath)

    df = df.withColumnRenamed("company_id", "c_id")

    df = df\
        .groupBy("c_id")\
        .agg(count(col("land_id")).alias("owned_lands"))

    return df


def create_graph_company_relations_land(
                                        df_company_relations,
                                        df_landownership
                                    ):
    """
    Create a graphframe from company_relations dataframe.

    description:
    reads csv from a mounted path on the databricks workspace.

    parameters:
    1. dataframe of company relations
    2. dataframe of landownership

    returns:
    company relations graphframe.
    """
    # select only required columns for creating vertices of graph
    vertices = df_company_relations\
        .select(
            col("company_id").alias("id"),
            col("name").alias("company_name")
        )

    # prepare vertices data
    edges = df_company_relations\
        .select(
            col("company_id").alias("dst"),
            col("parent").alias("src"),
            lit('parent_company_of').alias('relationship')
        )

    # Join landownership data to vertices
    vertices = vertices.join(
                    df_landownership,
                    vertices.id == df_landownership.c_id,
                    'left'
                    )
    # drop redundant columns
    vertices = vertices.drop("c_id")

    # build graphframes object
    gf = GraphFrame(vertices, edges)

    return gf


def get_hierarchy_landownership(company_id: str):
    """
    Print DataFrame with company relations and landownserhip details.

    parameters:
    1. company_id: String name of the company whoes hierarchy and
    landownership is to be printed

    returns:
    dataframe of ownership and company relations results.
    """
    # read company relations path is hardcoded for now
    df_cr = extract_company_relations(
        "dbfs:/FileStore/tables/company_relations.txt"
        )

    # read landownership path is hardcoded for now
    df_lo = extract_land_ownership(
        "dbfs:/FileStore/tables/land_ownership.txt"
        )

    # create graphframe for company relations and landownership
    gf = create_graph_company_relations_land(df_cr, df_lo)

    # using the shortest path algo to find distances between all nodes and
    # the one provided to process
    results = gf.shortestPaths(landmarks=[company_id])

    # create a hierarchy level based on distances in the shortest path
    # returned MapType field
    results = results.withColumn("hier_level", map_values("distances")[0])

    # filter all the results where the hierarchy is 0 or higher. Basically
    # removing all the NULL results.
    results = results.where("hier_level >= 0")
    return results
