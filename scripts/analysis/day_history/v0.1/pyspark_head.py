## this script calculate a stock trend over a period
from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext,SparkSession
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from pyspark.sql.types import *
from pyspark.sql.functions import pandas_udf, PandasUDFType
import pandas as pd
import numpy as np
from davidyu_cfg import *
from functions.LinearReg import LinearReg
from pyspark.sql.functions import *

spark = SparkSession \
    .builder \
    .appName("davidyu") \
    .enableHiveSupport() \
    .getOrCreate()


