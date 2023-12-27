import pandas as pd
import cx_Oracle

#init def function
def generate_report(Sql_name):
    connection = cx_Oracle.connect("FRIOBOM/friobom147123@WINT")
    cursor = connection.cursor()

    Sql_path_s = 'L:\\Friobom\\Engineering\\consults\\'
    Sql_path_d_csv = 'L:\\Friobom\\Engineering\\data\\csv_files\\'
    Sql_path_d_excel = 'L:\\Friobom\\Engineering\\data\\excel_files\\'
    Sql_name = Sql_name
    
    Sql = ''
    with open (Sql_path_s + Sql_name + '.txt', 'r') as file:
        for line in file:
            Sql += line

    df = pd.read_sql_query(Sql, connection)
    df.to_csv((Sql_path_d_csv + Sql_name + '.csv'), index=False) 
    df.to_excel((Sql_path_d_excel + Sql_name + '.xlsx'), index=False) 

    cursor.close()
    connection.close()
