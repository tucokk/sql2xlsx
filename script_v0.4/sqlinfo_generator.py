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
    config.set('SQL_INFO', 'EXAMPLE0', '##let it clear if there is not uid or password.')
    config.set('SQL_INFO', 'EXAMPLE1', '##EXAMPLE:')
    config.set('SQL_INFO', 'EXAMPLE2', '##uid =')

    config.add_section('SCRIPT_INFO')
    config.set('SCRIPT_INFO', 'querry', '<put the querry here>')
    config.set('SCRIPT_INFO', 'EXAMPLE3', '##the querry must be in the first space after =')
    config.set('SCRIPT_INFO', 'EXAMPLE4', '##=select')
    config.set('SCRIPT_INFO', 'EXAMPLE5', '###    *')
    config.set('SCRIPT_INFO', 'EXAMPLE6', '###from')
    config.set('SCRIPT_INFO', 'EXAMPLE7', '###    [tabel]')
    config.set('SCRIPT_INFO', 'tabel', '<put the tabel(s) here>')
    config.set('SCRIPT_INFO', 'EXAMPLE8', '##EXAMPLE:')
    config.set('SCRIPT_INFO', 'EXAMPLE9', '##tabel = student, teacher, grade')


    os.makedirs('./config')
    with open(r'./config/sql_config.ini', 'w') as sqlinfo:
        config.write(sqlinfo)
        print('sql_config.ini successfuly generated.\nRun the program again.')
        exit()