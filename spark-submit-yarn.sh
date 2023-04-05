#!/usr/bin/env bash
export PYSPARK_PYTHON=python
spark-submit \
    --class spark_read.py \
    --master yarn \
    --deploy-mode client \
    --principal francois \
    --keytab /home/francois/francois.keytab \
    spark_read.py 