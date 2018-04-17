import pyodbc
import getpass
from view import View

def setup(username, password):
    server = 'IN-CSCI-MSSQL\SQLSERVER2016DEV'
    database = 'sb24'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    return cnxn.cursor()

def main():
    usernameIn = input("Enter your database username: ")
    passwordIn = getpass.getpass("Enter your database password: ")
    cursor = setup(usernameIn, passwordIn)

if __name__ == "__main__":
    main()
