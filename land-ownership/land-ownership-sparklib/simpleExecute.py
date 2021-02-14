from pipelines.jobs import planes, amazon
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
