import pymysql.cursors   
# La fonction renvoie une connexion.
def getConnection(): 
    # Vous pouvez changer les arguments de la connexion.
    connection = pymysql.connect(host='192.168.5.129',
                                 user='root',
                                 password='1234',                             
                                 db='simplehr',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

sql = "Select data From table "
try :
    cursor = connection.cursor() 
    # Exécutez sql et passez- lui un paramètre.
    cursor.execute(sql, ( 10 ) )  
    print ("cursor.description: ", cursor.description) 
    print() 
    for row in cursor:
        print (" ----------- ")
        print("Row: ", row)
        print ("Emp_No: ", row["Emp_No"])
        print ("Emp_Name: ", row["Emp_Name"])
        print ("Hire_Date: ", row["Hire_Date"] , type(row["Hire_Date"]) ) 
finally:
    # Achevez la connexion
    connection.close()
