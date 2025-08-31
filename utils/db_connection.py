import os
import json
import mysql.connector

class SQLQuery:
    def __init__(self, host=None, user=None, password=None, db=None):
        self.host = host
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.db = db
        self.code_path = os.path.dirname(os.path.abspath(__file__))
        self.project_data_path = os.path.join(os.path.dirname(self.code_path), "project_data")
        self.read_conifg()
        self.get_connection()
        self.create_db()
        self.create_tables()

    def read_conifg(self):
        self.json_path = os.path.join(self.project_data_path, "db_config.json")
        self.config_data = json.load(open(self.json_path))
        self.host = self.config_data.get("host", "localhost")
        self.user = self.config_data.get("user", "root")
        self.password = self.config_data.get("password", "12345678")
        self.db = self.config_data.get("db", "cricbuzz")
        self.table = self.config_data.get("players_table")
    
    def save_config(self):
        with open(self.json_path, 'w') as file:
            json.dump(self.config_data, file, indent=4)

    def get_connection(self):
        self.read_conifg()
        try:
            if self.db and self.check_dbs():
                self.connection = mysql.connector.connect(
                                                        host=self.host,
                                                        user=self.user,
                                                        password=self.password,
                                                        database=self.db
                                                    )
                self.cursor = self.connection.cursor()
            else:
                self.connection = mysql.connector.connect(
                                                            host=self.host,
                                                            user=self.user,
                                                            password=self.password
                                                        )
                self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Couldn't connect to the MySQL server due to the error: {e}")

    def execute_query(self, query):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        self.cursor.execute(query)
        return self.cursor
    
    def check_dbs(self):
        conn = mysql.connector.connect(
                                        host=self.host,
                                        user=self.user,
                                        password=self.password
                                    )

        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")

        databases = [db[0] for db in cursor.fetchall()]
        if self.db in databases:
            return True
        else:
            return False

    def create_db(self):
        if self.connection and self.cursor:
            try:
                self.db = "cricbuzz"
                self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db}")
                self.connection.commit()
                self.config_data["db"] = self.db
                self.save_config()
            except Exception as e:
                print(f"Error creating database: {e}")
    
    def create_tables(self, table=None):
        self.read_conifg()
        try:
            # print(table)
            # print(self.table)
            self.cursor.execute(table if table else self.table)
            self.connection.commit()
        except Exception as e:
            print(f"Error creating players table: {e}")

    def create_tables(self, table=None):
        self.read_conifg()
        try:
            # print(table)
            # print(self.table)
            return self.cursor.execute(table if table else self.table)
        except Exception as e:
            print(f"Error creating players table: {e}")
    
    def get_user_count(self, table):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        query = f"SELECT COUNT(*) FROM {table}"
        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]
        return count
    
    def add_user(self, input_data):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        initial_count = self.get_user_count(table="players")
        query = "INSERT INTO players (player_id, name, matches, innings, runs, average) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (input_data.get("player_id"), input_data.get("name"), input_data.get("matches"), 
                input_data.get("innings"), input_data.get("runs"), input_data.get("average"))
        self.cursor.execute(query, data)
        self.connection.commit()
        final_count = self.get_user_count(table="players")
        return final_count > initial_count
    
    def add_indian_user(self, input_data):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        initial_count = self.get_user_count(table="indian_players")
        query = "INSERT INTO indian_players (id, name, playing_role, batting_style, bowling_style) VALUES (%s, %s, %s, %s, %s)"
        data = (input_data.get("id"), input_data.get("name"), input_data.get("playing_role"), 
                input_data.get("batting_style"), input_data.get("bowling_style"))
        self.cursor.execute(query, data)
        self.connection.commit()
        final_count = self.get_user_count(table="indian_players")
        return final_count > initial_count
    
    def add_entry(self, input_data):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        table = input_data.get("table")
        initial_count = self.get_user_count(table=table)
        ids = input_data.get("columns")
        values = input_data.get("values")
        value_input = input_data.get("value_input")
        # print(table)
        # print(ids)
        # print(values)
        # query = f"INSERT INTO {table} {ids} VALUES {value_input}"
        query = f"REPLACE INTO {table} {ids} VALUES {value_input};"
        # print(query)
        self.cursor.execute(query, values)
        self.connection.commit()
        final_count = self.get_user_count(table="indian_players")
        return final_count > initial_count
    
    def get_users(self):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        query = "SELECT * FROM players"
        self.cursor.execute(query)
        
        # Get column names from cursor description
        columns = [desc[0] for desc in self.cursor.description]
        users = self.cursor.fetchall()
        
        # Convert to list of dictionaries with column names
        users_with_columns = []
        for user in users:
            user_dict = dict(zip(columns, user))
            users_with_columns.append(user_dict)
        
        return users_with_columns

    def update_user(self, input_data):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        
        # Use player_id in WHERE clause instead of id (since your table doesn't have 'id' column)
        query = "UPDATE players SET name=%s, matches=%s, innings=%s, runs=%s, average=%s WHERE player_id=%s"
        data = (input_data.get("name"), input_data.get("matches"), input_data.get("innings"), 
                input_data.get("runs"), input_data.get("average"), input_data.get("player_id"))
        self.cursor.execute(query, data)
        self.connection.commit()
        return True

    def delete_user(self, user_id):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        initial_count = self.get_user_count(table="players")
        query = "DELETE FROM players WHERE player_id=%s"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
        final_count = self.get_user_count(table="players")
        return final_count < initial_count

