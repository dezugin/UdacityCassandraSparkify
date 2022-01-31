# UdacityCassandraSparkify
Project 2 of the udacity data engineering course

## Project description: Data Modeling with Cassandra

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.


## Project Overview

In this project, i've apply what i've learned on data modeling with Apache Cassandra and complete an ETL pipeline using Python. I modeled data by creating tables in Apache Cassandra to run queries. I was provideded with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.


## What I actually Did
- Processed the event_datafile_new.csv dataset to create a denormalized dataset
- Modeled the data tables keeping in mind the queries I needed to run
- Loaded the data into tables created in Apache Cassandra and run queries
- Iterate through each event file in event_data to process and create a new CSV file in Python
- Include Apache Cassandra CREATE and INSERT statements to load processed records into relevant tables in the data model
- Test by running SELECT statements after running the queries on the database
