import configparser as cpa
import os
def generateIniFile():
    config = cpa.ConfigParser(allow_no_value=True)
    config.add_section('SQL_INFO')
    config.set('SQL_INFO', 'driver', 'SQL Server')
    config.set('SQL_INFO', 'server', '<put the servername here>')
    config.set('SQL_INFO', 'database', '<put the database here>')
    config.set('SQL_INFO', 'trust_connection', 'yes')
    config.set('SQL_INFO', 'uid', '<put the login here>')
    config.set('SQL_INFO', 'pws', '<put the password here>')
    config.set('SQL_INFO', ";if there's not login or password, don't put anything in that fields.")
    config.set('SQL_INFO', ';EXAMPLE:')
    config.set('SQL_INFO', ';uid = ')

    config.add_section('SCRIPT_INFO')
    config.set('SCRIPT_INFO', 'querry', '<put the querry here>')
    config.set('SCRIPT_INFO', ';EXAMPLE:')
    config.set('SCRIPT_INFO', ';SELECT')
    config.set('SCRIPT_INFO', ';    * (4 whitespaces)')
    config.set('SCRIPT_INFO', ';FROM')
    config.set('SCRIPT_INFO', ';    [tabel] ')
    config.set('SCRIPT_INFO', ';(do NOT change [tabel], put table(s) in "tabel" section)')
    config.set('SCRIPT_INFO', 'tabel', '<put the table here (from <tabel>)>')
    config.set('SCRIPT_INFO', '; EXAMPLE: student, bank, grades')
    os.makedirs('./config')
    with open(r'./config/sql_config.ini', 'w') as sqlinfo:
        config.write(sqlinfo)
        print('sql_config.ini successfuly generated.\nRun the program again.')
        exit()

    