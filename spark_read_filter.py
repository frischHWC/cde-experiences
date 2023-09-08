from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import Row
from pyspark.sql.functions import col

def main(spark):  
  
  # Read Plants Files Generated by datagen
  df_plants = spark.read.parquet("/user/datagen/hdfs/industry/plant/")
  df_plants.printSchema()
  df_plants.show(1)
  
  
  # Filter to have only sensor of type speed and located in France
  df_france_plants = df_plants.filter(col("country")=='France')

  # Finally write this data to HDFS
  df_france_plants.write.mode("append")\
  .parquet("/user/francois/french_plants/")

  
if __name__ == '__main__':
  # Create a Spark Session
  spark = SparkSession\
  .builder\
  .appName("FrenchPlants")\
  .getOrCreate()
  
  main(spark)
  
  