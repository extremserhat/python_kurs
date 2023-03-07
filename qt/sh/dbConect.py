#!/bin/env python3.11 
import psycopg2

hostname = 'xxxxxxxx'
database = 'xxxxxxxxx'
username = 'xxxxxxxxx'
pwd = 'xxxx'
port_id = 5432
conn = None
cur = None
try:
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)


    cur = conn.cursor()
    
    creat_script = ''' CREATE TABLE contacts (
                id          int Primary KEY,
                name        varchar(40) NOT NULL,
                lastname    varchar(40) NOT NULL,
                
            )'''
    cur.execute(creat_script)   

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


