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
        self.get_connection()
        self.create_db()
        self.create_tables()

    def read_conifg(self):
        self.json_path = os.path.join(self.code_path, "config.json")
        self.config_data = json.load(open(self.json_path))
        self.host = self.config_data.get("host", "localhost")
        self.user = self.config_data.get("user", "root")
        self.password = self.config_data.get("password", "12345678")
        self.db = self.config_data.get("db", "cricbuzz")
    
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
    
    def create_tables(self):
        try:
            self.cursor.execute("""
                                    CREATE TABLE IF NOT EXISTS players (
                                                                        player_id INT PRIMARY KEY,
                                                                        name VARCHAR(100),
                                                                        matches INT,
                                                                        innings VARCHAR(50),
                                                                        runs INT,
                                                                        average FLOAT
                                                                        )
                                    """)
            self.connection.commit()
        except Exception as e:
            print(f"Error creating players table: {e}")
    
    def get_user_count(self):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        query = "SELECT COUNT(*) FROM players"
        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]
        return count
    
    def add_user(self, input_data):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        initial_count = self.get_user_count()
        query = "INSERT INTO players (player_id, name, matches, innings, runs, average) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (input_data.get("player_id"), input_data.get("name"), input_data.get("matches"), 
                input_data.get("innings"), input_data.get("runs"), input_data.get("average"))
        self.cursor.execute(query, data)
        self.connection.commit()
        final_count = self.get_user_count()
        return final_count > initial_count
    
    def get_users(self):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        query = "SELECT * FROM players"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        return users
    
    def update_user(self, input_data):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        query = "UPDATE players SET player_id=%s, name=%s, matches=%s, innings=%s, runs=%s, average=%s WHERE id=%s"
        data = (input.get("player_id"), input_data.get("name"), input_data.get("matches"), input_data.get("innings"), 
                input_data.get("runs"), input_data.get("average"), input_data.get("player_id"))
        self.cursor.execute(query, data)
        self.connection.commit()
        return True
    
    def delete_user(self, user_id):
        if not self.connection or not self.connection.is_connected() or not self.cursor:
            self.get_connection()
        initial_count = self.get_user_count()
        query = "DELETE FROM players WHERE id=%s"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
        final_count = self.get_user_count()
        return final_count < initial_count

