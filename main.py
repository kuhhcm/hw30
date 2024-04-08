import psycopg2 
 
def connect_to_db(): 
    connect = psycopg2.connect(host = '127.0.0.1', port = 5432, dbname = 'postgres', user = 'postgres', password = 'postgres') 
    return connect 
 
connection = connect_to_db() 
cursor = connection.cursor() 
 
 
 
def insert(): 
    id = int(input("Enter id: ")) 
    name = input("Enter name: ") 
    year = int(input("Enter year: ")) 
    price = int(input("Enter price: ")) 
    create = f"insert into phones values ( {id}, '{name}', {year}, {price})" 
    cursor.execute(create) 
    connection.commit() 
 
 
def read_all(): 
    read = "select * from phones" 
    cursor.execute(read) 
    rows = cursor.fetchall() 
    print(rows) 
 
 
def read_one(): 
    id = int(input("Enter id you want to read: ")) 
    read_only_one =  f"select from phones where id = {id}" 
    cursor.execute(read_only_one) 
    row = cursor.fetchone() 
    print(row) 
     

def delete(): 
    id = int(input("Enter id you want to delete: ")) 
    delete = f"delete from phones where id = {id}" 
    cursor.execute(delete) 
    connection.commit() 

while True:
    choice = input("Select an action: \n\n1. Insert\n2. Read all rows\n3. Read one row\n4. Delete\n5. Exit\n\n") 
    match choice: 
        case "1": 
            insert() 
        case "2": 
            read_all() 
        case "3": 
            read_one() 
        case "4": 
            delete() 
        case "5": 
            break