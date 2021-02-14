# This solution uses the following Azure / AWS components 
1. Databricks (Managed Spark Compute Platform ) https://docs.databricks.com/index.html
2. Storage Account / S3 Bucket (To store and host the CSV files)

# The solution also relies on following spark library Graphframes
https://graphframes.github.io/graphframes/docs/_site/index.html

Steps:
1. We read our data and convert the dataframes to a graph
2. We process the graph using shortest path method from GraphFrames to identify
which nodes are connected based on company relations
3. We then filter based on the path length to only have the required nodes in the final dataframe
4. We return this dataframe to the calling method.
5. This can be scaled in Databricks by using the below CI/CD method to install the library on the cluster
6. The library can then be used interactively / called by other services like ADF i.e. Azure Datafactory or other cloud services.

# Developing with Databricks-Connect & Azure DevOps
A guide of how to build good Data Pipelines with Databricks Connect using best practices.
Details: https://datathirst.net/blog/2019/9/20/series-developing-a-pyspark-application

## About
This is a sample Databricks-Connect PySpark application that is designed as a template for best practice and useability.

The project is designed for:
* Python local development in an IDE (VSCode) using Databricks-Connect
* Well structured PySpark application 
* Simple data pipelines with reusable code
* Unit Testing with Pytest
* Build into a Python Wheel
* CI Build with Test results published
* Automated deployments/promotions

## Setup

Create a Conda Environment (open Conda prompt):
```
conda create --name dbconnectappdemo python=3.7
```

Activate the environment:
```
conda activate dbconnectappdemo
```

IMPORTANT: Open the requirements.txt in the root folder and ensure the version of databrick-connect matches your cluster runtime.

Install the requirements into your environments:
```
pip install -r requirements.txt
```

If you need to setup databricks-connect then run:
```
databricks-connect configure
```
https://docs.databricks.com/dev-tools/databricks-connect.html

## Setup Deployment
If you would like to deploy from your local PC to Databricks create a file in the root called MyBearerToken.txt and paste in a bearer token from the Databricks UI.