"""Test data and test cases for landownership and company relations module."""
import pytest
from .context import pipelines
from pipelines.jobs import landownership
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


# TODO: I have added a basic idea of creating mock data instead of reading the
# actual dataset and then running it thorugh the different methods in module.
class Test_landownership(object):
    """Test data and test cases."""

    def mock_extract_company_relations():
        """Test data."""
        data = [
                ("C2013", "Acme Land Ltd", ""),
                ("C71299", "Jacksons Stores Limited", "C4012"),
                ("C4012", "J Sainsbury PLC", ),
                ("C45353", "Jacksons Stores Manchester Limited", "C71299")
            ]
        return spark.createDataFrame(data, ["company id", "name", "parent"])

    def mock_extract_landownership():
        """Test data."""
        data = [
                ("C2013", "Acme Land Ltd", ""),
                ("C71299", "Jacksons Stores Limited", "C4012"),
                ("C4012", "J Sainsbury PLC", ),
                ("C45353", "Jacksons Stores Manchester Limited", "C71299")
            ]
        return spark.createDataFrame(data, ["company id", "name", "parent"])

    def test_graphframe_creation(self):
        """Test for creating a graphframe object. just a dummy test."""
        df_cr = Test_landownership.mock_extract_company_relations()
        df_lo = Test_landownership.mock_extract_landownership()
        gf = landownership.create_graph_company_relations_land(df_cr, df_lo)
        assert gf.vertices.count() == 4
