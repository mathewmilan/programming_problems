#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:57:00 2018

@author: butterflyeffect
"""
from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import unittest

conf = SparkConf().setAppName("MovieDataBuilder").setMaster("local")
sc = SparkContext(conf=conf)
spark = SparkSession.builder.appName("MovieDataBuilder").config("spark.eventLog.enabled", "false").getOrCreate()


# Function that returns movie data frame from its csv file
# Read movies data from csv into dataframe with header set
# Define and Map non string columns in header into their corresponding datatypes
# Define and Map json columns in header to their corresponding types
def create_movies_dataframe():
    moviesDF = (
        spark.read.csv(
            "/Users/butterflyeffect/Downloads/tmdb-5000-movie-dataset/tmdb_5000_movies.csv",
            header=True,
            quote='"',
            escape='"'
        )
    )
    # Define non string columns into their corresponding datatypes
    cols = {
        "id": T.IntegerType,
        "budget": T.IntegerType,
        "popularity": T.FloatType,
        "release_date": T.DateType,
        "revenue": T.LongType,
        "vote_average": T.FloatType,
        "vote_count": T.IntegerType,
    }
    # Define json columns into their corresponding types
    json_cols = {
        "genres": T.ArrayType(T.StructType([
            T.StructField("id", T.IntegerType()),
            T.StructField("name", T.StringType()),
        ])),
        "keywords": T.ArrayType(T.StructType([
            T.StructField("id", T.IntegerType()),
            T.StructField("name", T.StringType()),
        ])),
        "production_companies": T.ArrayType(T.StructType([
            T.StructField("id", T.IntegerType()),
            T.StructField("name", T.StringType()),
        ])),
        "production_countries": T.ArrayType(T.StructType([
            T.StructField("iso_3166_1", T.StringType()),
            T.StructField("name", T.StringType()),
        ])),
        "spoken_languages": T.ArrayType(T.StructType([
            T.StructField("iso_639_1", T.StringType()),
            T.StructField("name", T.StringType()),
        ])),
    }
    # Map non string columns into their corresponding datatypes
    for col, schema in cols.items():
        moviesDF = moviesDF.withColumn(col, F.col(col).astype(schema()))
    # Map json columns into their corresponding datatypes
    for col, schema in json_cols.items():
        moviesDF = moviesDF.withColumn(col, F.from_json(col, schema))
    #Rename id column into movies_id for inner join with credits dataframe
    moviesDF = moviesDF.withColumnRenamed('id', 'movie_id')

    # Validate Schema
    # moviesDF.printSchema()

    # Validate Json Column data and type
    # print(moviesDF.select('production_countries.iso_3166_1').distinct().show(100, False))
    # print(moviesDF.select('production_countries.name').distinct().show(10, False))

    # Validate column names and types
    # print (moviesDF.columns)
    # print (moviesDF.dtypes)

    # Validate rows
    # moviesDF.show(2, False)
    return moviesDF


# Function that returns credits data frame from its csv file
# Read movies data from csv into dataframe with header set
# Define and Map non string columns into their corresponding datatypes
# Define and Map json columns into their corresponding types
def create_credits_dataframe():
    creditsDF = (
        spark.read.csv(
            "/Users/butterflyeffect/Downloads/tmdb-5000-movie-dataset/tmdb_5000_credits.csv",
            header=True,
            quote='"',
            escape='"',
        )
    )
    # Define non string columns into their corresponding datatypes
    credits_cols = {
        "movie_id": T.IntegerType,
    }
    # Define json columns into their corresponding types
    credits_json_cols = {
        "cast": T.ArrayType(T.StructType([
            T.StructField("cast_id", T.IntegerType()),
            T.StructField("character", T.StringType()),
            T.StructField("credit_id", T.StringType()),
            T.StructField("gender", T.IntegerType()),
            T.StructField("id", T.IntegerType()),
            T.StructField("name", T.StringType()),
            T.StructField("order", T.IntegerType()),
        ])),
        "crew": T.ArrayType(T.StructType([
            T.StructField("credit_id", T.StringType()),
            T.StructField("department", T.StringType()),
            T.StructField("gender", T.IntegerType()),
            T.StructField("id", T.IntegerType()),
            T.StructField("job", T.StringType()),
            T.StructField("name", T.StringType()),
        ])),
    }
    for col, schema in credits_cols.items():
        creditsDF = creditsDF.withColumn(col, F.col(col).astype(schema()))
    for col, schema in credits_json_cols.items():
        creditsDF = creditsDF.withColumn(col, F.from_json(col, schema))

    # Validate Schema
    # creditsDF.printSchema()

    # Validate column names and types
    # print (creditsDF.columns)
    # print (creditsDF.dtypes)

    # Validate Rows
    # creditsDF.show(2, False)
    return creditsDF


moviesDF = create_movies_dataframe()
creditsDF = create_credits_dataframe()

# Inner Join of dataframes: movies and credits using movie_id column
joinedDF = moviesDF.join(creditsDF, 'movie_id', 'inner')

# joinedDF.printSchema()
# print(moviesDF.count(), creditsDF.count(), joinedDF.count())

# Create Merged Table movies_credits from Joined Dataframes
joinedDF.createOrReplaceTempView("movies_credits")

# joinedDFQuery = spark.sql("select distinct production_countries.iso_3166_1 from movies_credits")
# joinedDFQuery.show(2, False)

# joinedDFsubset = joinedDF.select('production_countries.iso_3166_1').distinct()
# joinedDFsubset.show(2, False)


class DFTest(unittest.TestCase):
    def dataframe_schema_test(self):
        movies_cols = ['budget', 'genres', 'homepage', 'id', 'keywords', 'original_language', 'original_title', 'overview', 'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'vote_average', 'vote_count']
        credits_cols = ['movie_id', 'title', 'cast', 'crew']
        self.assertEqual(create_movies_dataframe().columns, movies_cols)
        self.assertEqual(create_credits_dataframe().columns, credits_cols)

#
# badDF = (
#     movieDF
#     .select('`_c20`', '`_c21`')
#     .where(F.col('_c20').isNotNull() | F.col('_c21').isNotNull())
#     )

# print('BAD ROWS: %d' % badDF.count())
# badDF.show(100, False)
