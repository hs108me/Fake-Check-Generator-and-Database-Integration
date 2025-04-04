import psycopg2

class Database:
    def __init__(self, database, user, password, host, port):
        
        self.connection = psycopg2.connect(database=database, user=user, password=password,
                                                host=host, port=port)     
        self.cursor = self.connection.cursor()

    def insert_data(self, data):
        self.cursor.execute("""INSERT INTO cheque (doc_id, item, category, amount, price, discount)
            VALUES (%s, %s, %s, %s, %s, %s)""", data)
        self.connection.commit()

                
    def close_connection(self):
        self.cursor.close()
        self.connection.close()