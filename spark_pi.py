from pyspark.sql import SparkSession
import time
import sys
from random import random
from operator import add
from pyspark.storagelevel import StorageLevel



def main(spark):  
  
  partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
  n = 100000 * partitions

  def f(_: int) -> float:
      x = random() * 2 - 1
      y = random() * 2 - 1
      return 1 if x ** 2 + y ** 2 <= 1 else 0

  count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
  print("Pi is roughly %f" % (4.0 * count / n))

  df = spark.range(1)
  df.persist(StorageLevel.DISK_ONLY)
  
  time.sleep(600)

  df.unpersist()

  
if __name__ == '__main__':
  # Create a Spark Session
  spark = SparkSession\
  .builder\
  .appName("SparkPiTestPersist")\
  .getOrCreate()
  
  main(spark)
  
  