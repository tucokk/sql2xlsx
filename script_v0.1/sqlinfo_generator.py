import configparser as cpa
import os
def generateIniFile():
    config=cpa.ConfigParser()
    config.add_section('SQL_INFO')
    config.set('SQL_INFO', 'driver', 'SQL Server')
    config.set('SQL_INFO', 'server', '<put the servername here>')
    config.set('SQL_INFO', 'database', '<put the database here>')
    config.set('SQL_INFO', 'trust_connection', 'yes')
    config.set('SQL_INFO', 'uid', '<put the login here>')
    config.set('SQL_INFO', 'pws', '<put the password here>')

    os.makedirs('./config')
    with open(r'./config/sql_config.ini', 'w') as sqlinfo:
        config.write(sqlinfo)
        print('sql_config.ini successfuly generated.\nRun the program again.')
        exit()

    