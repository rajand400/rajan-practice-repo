import boto3
import pandas as pd
import psycopg2

# Connect to S3
s3 = boto3.client('s3')
bucket_name = 'your_bucket_name'
file_name = 'your_file_name.csv'

# Download the file from S3
s3.download_file(bucket_name, file_name, 'local_file.csv')

# Perform data cleaning using pandas
df = pd.read_csv('local_file.csv')
# Perform your data cleaning operations here

# Connect to Redshift
conn = psycopg2.connect(
    host='your_redshift_host',
    port='your_redshift_port',
    user='your_redshift_user',
    password='your_redshift_password',
    database='your_redshift_database'
)

# Create a cursor
cur = conn.cursor()

# Create a table in Redshift
create_table_query = '''
    CREATE TABLE IF NOT EXISTS your_table_name (
        column1 datatype,
        column2 datatype,
        ...
    )
'''
cur.execute(create_table_query)
conn.commit()

# Insert cleaned data into Redshift
for index, row in df.iterrows():
    insert_query = '''
        INSERT INTO your_table_name (column1, column2, ...)
        VALUES (%s, %s, ...)
    '''
    values = (row['column1'], row['column2'], ...)
    cur.execute(insert_query, values)
    conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
