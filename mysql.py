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
