import pypyodbc as odbc
import time
import sqlinfo_generator as generator
import sqlinfo_reader as reader
import os
import pandas as pd
import openpyxl
from datetime import datetime
# setting the config.ini data as the connection fields (server, database, login, password)
class Connection:
    def __init__(self, DRIVER, SERVER_NAME, DATABASE_NAME, UID, PSW):
        self.server = SERVER_NAME
        self.database = DATABASE_NAME
        self.uid = UID
        self.psw = PSW
        self.driver = DRIVER
        self.connection_string = f'''
DRIVER={{{self.driver}}};
SERVER={self.server};
DATABASE={self.database};
Trust_Connection=yes;
UID={self.uid};
PWD={self.psw};
                    '''
        Connection.connection = 'none'
        print(f'\nConnection data informed.\n {self.connection_string}')

    #starting the connection process. limit of 3x is setted 
    def connection_database(self):
        for cont in range(1, 6): 
            msg = f'[{cont}]'
            print('Trying connection... {}'.format(msg if cont > 1 else ''))
            try:
                #connection line
                connection_server = odbc.connect(self.connection_string)
                Connection.connection = connection_server
                print(f'Connection complete successfuly.\nSys_status: connected\n\n')  
                return connection
            #any error during the connection fill fall over here, giving the reconnect option
            except:
                if cont != 5:
                    try_again = input('Something went wrong. Try again? y/n\n')
                    if try_again == 'y':
                        print('\n')
                        continue
                    else:
                        exit()
                elif cont == 5:
                    print('Connection unsuccessful 5 times. Closing the program.')  
                    time.sleep(2)
                    exit()



class Querry(Connection):
    def __init__(self):
        self.connection = Connection.connection
    def querry(self):
        tabels = reader.readIniFile()[6]

        for i in range(len(tabels)):
            querry = reader.readIniFile()[5]
            querry = querry.replace('[tabel]', tabels[i])
            final_result = 0
            if tabels[-1] == tabels[i]:
                final_result = 1
            pd.set_option('display.max_rows', None)
            table = pd.read_sql_query(querry, self.connection)

            directory_exist = os.path.exists(r'./result')
            if directory_exist == False:
                os.makedirs('./result')
            with open(r'./result/data.txt', 'a') as sqlinfo:
                config = f'\n\n{table}'
                tabels_formated = tabels[i].replace(',', '')
                sqlinfo.write(f'\n\nDatabase: {tabels_formated}, \nResult:\n{config}')
            if final_result == 1:
                with open(r'./result/data.txt', 'a') as sqlinfo:
                    date = str(datetime.today())
                    sqlinfo.write(f'\n\n\nGenerated at: {date}\nDeveloper: https://github.com/tucokk')
            table.to_csv(f'./result/{tabels[i]}.csv')
            table.to_excel(f'./result/{tabels[i]}.xlsx')

        print('\nResult files successfuly generated. \nCheck: C:/configfile/script_result.txt')
    
#reading .ini file or creating it
file_exist = os.path.isfile(r'./config/sql_config.ini')
if file_exist == True:
    pass
else:
    generator.generateIniFile()


#calling the start of connecting process
connection = Connection(reader.readIniFile()[4],reader.readIniFile()[0], reader.readIniFile()[1], reader.readIniFile()[2], reader.readIniFile()[3])
connection_data = connection.connection_database()
querry = Querry()
executing_querry = querry.querry()
