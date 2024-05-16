import pymysql
# connection

config = {
    'user': 'admin',
    'password': 'admin',
    'host': 'mysql',
     'port': 3306,
    'database': 'db_flask'
}

connection = pymysql.connect(**config)
cursor = connection.cursor()
#inserting data to db
def add_text(text_value):
    cursor.execute("INSERT INTO mytable(ID, text_value) VALUES (DEFAULT, %s)", (text_value))
    connection.commit()
    return 1

def get_data():
    cursor.execute("SELECT * FROM mytable")
    rows = cursor.fetchall()    
    return rows