import pandas as pd
from pandas import read_sql_query
import pandasql

def select_first_50(aadhaar_data):
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.

    # Select out the first 50 values for "registrar" and "enrolment_agency"
    # in the aadhaar_data table using SQL syntax.
    #
    # Note that "enrolment_agency" is spelled with one l. Also, the order
    # of the select does matter. Make sure you select registrar then enrolment agency
    # in your query.
    #
    # You can download a copy of the aadhaar data that we are passing
    # into this exercise below:
    # https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/aadhaar_data.csv
    dataframe=aadhaar_data['namefirst']
    print(dataframe)

    #Execute your SQL command against the pandas frame
    # aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_data

if __name__=="__main__":
    aadhaar_data = pd.read_csv('aadhaar_data.csv')
    aadhaar_data.rename(columns=lambda x: x.replace(' ', '_').lower(), inplace=True)
    select_first_50(aadhaar_data)