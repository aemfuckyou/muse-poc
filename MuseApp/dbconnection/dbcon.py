from peewee import *

'''
    schema:
        dbname
        user="username"
        password="userpassword"
        host="hostaddress/localhost"
        port=5432
'''

pg_db = PostgresqlDatabase(
    'musedata',
    user='museuser',
    password='1234!',
    host='139.162.133.232',
    port=5432
)
