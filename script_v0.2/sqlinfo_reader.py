import configparser as cpa

def readIniFile():
    config = cpa.ConfigParser()
    config.read(r'./config/sql_config.ini')
    SERVER_NAME = config['SQL_INFO']['server']
    DATABASE_NAME = config['SQL_INFO']['database']
    UID = config['SQL_INFO']['uid']
    PSW = config['SQL_INFO']['pws']
    DRIVER = config['SQL_INFO']['driver']
    QUERRY = config['SCRIPT_INFO']['querry']
    TABEL = [str(x) for x in config.get('SCRIPT_INFO', 'tabel').split(',')]
    return (SERVER_NAME, DATABASE_NAME, UID, PSW, DRIVER, QUERRY, TABEL)
