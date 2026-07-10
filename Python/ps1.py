from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("My First PySpark Program") \
    .master("local[*]") \
    .getOrCreate()

# Sample data
data = [
    ("Shanmuk", 25, "Dallas"),
    ("John", 30, "New York"),
    ("Alice", 28, "Chicago")
]

# Create DataFrame
df = spark.createDataFrame(data, ["Name", "Age", "City"])

# Display DataFrame
df.show()

# Print Schema
df.printSchema()

# Stop Spark Session
spark.stop()