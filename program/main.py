import pyodbc
import getpass
from view import View

def setup(username, password):
    server = 'IN-CSCI-MSSQL\SQLSERVER2016DEV'
    database = 'sb24'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    # cursor.execute("SELECT * FROM Sailor")
    # row = cursor.fetchone()
    # while(row):
    #     print(row)
    #     row = cursor.fetchone()

def main():
    username = input("Enter your database username: ")
    password = getpass.getpass("Enter your database password: ")
    # setup(username, password)
    view = View()

if __name__ == "__main__":
    main()
