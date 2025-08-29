import os
import json
import mysql.connector
from db_connection import SQLQuery

# creating the db
db_connection = SQLQuery()
db_connection.get_connection()
db_connection.create_db()
db_connection.create_tables()
