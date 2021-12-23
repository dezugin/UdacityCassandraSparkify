import pandas as pd
import cassandra
from cassandra.cluster import Cluster
import re
import os
import glob
import numpy as np
import json
import csv

def convertDataToCsv():
    """
    Converts the data in /event_data to a csv file named event_datafile_new.csv
    """
    # checking your current working directory
    print(os.getcwd())

    # Get your current folder and subfolder event data
    filepath = os.getcwd() + '/event_data'

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):

    # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root,'*'))
        print(file_path_list)
    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = [] 

    # for every filepath in the file path list 
    for f in file_path_list:

    # reading csv file 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            next(csvreader)

     # extracting each data row one by one and append it        
            for line in csvreader:
                #print(line)
                full_data_rows_list.append(line) 

    # get total number of rows 
    print("Total of rows:", len(full_data_rows_list))
    # uncomment the code below if you would like to check to see what the list of event data rows will look like
    #print(full_data_rows_list)

    # creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into the \
    # Apache Cassandra tables
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                    'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))
    # check the number of rows in your csv file
    with open('event_datafile_new.csv', 'r', encoding = 'utf8') as f:
        print("Total of rows in the csv file: ",sum(1 for line in f))
        
def runQuery(session, query):
    """Runs sql queries """
    try:
        session.execute(query)
    except Exception as e:
        print(e)
def runQueryRows(session, query):
    """Runs sql queries returning rows""" 
    try:
        rows = session.execute(query)
    except Exception as e:
        print(e)
    return rows
def runQueryParameters(session, query,queryParameters):
    """Runs sql queries with parameters"""
    try:
        session.execute(query,queryParameters)
    except Exception as e:
        print(e)
def insertIntoMusicLibrary(session, query):
    """ Inserts records in music library """
    # Set up the CSV file.
    file = 'event_datafile_new.csv'
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        count = 0
        for line in csvreader:
            ## Assign the INSERT statements into the `query` variable
            ## Assign which column element should be assigned for each column in the INSERT statement.
            runQueryParameters(session, query,(line[0],line[-2],float(line[5]),int(line[3]),int(line[-3])))
def insertIntoMusicLibrary1(session,query):
    """ Inserts records in music library 1 """
    # Set up the CSV file.
    file = 'event_datafile_new.csv'
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        count = 0
        for line in csvreader:
            ## Assign the INSERT statements into the `query` variable
            # Assign which column element should be assigned for each column in the INSERT statement.
            runQueryParameters(session, query, (line[0],line[-2],line[1]+line[4],int(line[3]),int(line[-1]),int(line[-3])))
def insertIntoMusicLibrary2(session,query):
    """ Inserts records in music library 1 """
    # Set up the CSV file.
    file = 'event_datafile_new.csv'
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        count = 0
        for line in csvreader:
            ## Assign the INSERT statements into the `query` variable
            ## Assign which column element should be assigned for each column in the INSERT statement.
            runQueryParameters(session,query, (line[-2],line[1]+line[4]))