import logging
import datetime
import os
import azure.functions as func
import sys
import pip
from pip._internal.utils.misc import get_installed_distributions
import pyodbc
import subprocess
from sys import platform


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    #foo = str(os.environ['Foo'])
    #logging.info(f'Recieved appsetting value for "foo"\t\t{foo}')


    installed_packages = get_installed_distributions()
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
        for i in installed_packages])
    logging.info(installed_packages_list)

    #show_odbc_sources()

    printDirectory()

    printWorkDirectory()

    printDirectory2()

    printPlatform()

    printUName()

    SQL_SERVER = 'abrig-al.database.windows.net'
    SQL_DB = 'image-track'
    USERNAME = str(os.environ['USERNAME'])
    PASSWORD = str(os.environ['PASSWORD'])
    driver= '{ODBC Driver 17 for SQL Server}' #Works for Mac OS https://stackoverflow.com/a/44538741
    # Open connection
    '''
    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};PORT=1433;SERVER='+SQL_SERVER+';PORT=1443;DATABASE='+SQL_DB+';UID='+USERNAME+';PWD='+ PASSWORD)
        logging.info("\t\tSUCCESS!!!!")
    except Exception as e: logging.error(e)
   


    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};PORT=1433;SERVER='+SQL_SERVER+';PORT=1443;DATABASE='+SQL_DB+';UID='+USERNAME+';PWD='+ PASSWORD)
        logging.info("\t\tSUCCESS!!!!")
    except Exception as e: logging.error(e)

    try:
        cnxn = pyodbc.connect('DRIVER={/home/site/wwwroot/Weather/libmsodbcsql.17.dylib};PORT=1433;SERVER='+SQL_SERVER+';PORT=1443;DATABASE='+SQL_DB+';UID='+USERNAME+';PWD='+ PASSWORD)
        logging.info("\t\tSUCCESS!!!!")
    except Exception as e: logging.error(e)
    
    try:
        cnxn = pyodbc.connect('DRIVER={./libmsodbcsql.17.dylib};PORT=1433;SERVER='+SQL_SERVER+';PORT=1443;DATABASE='+SQL_DB+';UID='+USERNAME+';PWD='+ PASSWORD)
        logging.info("\t\tSUCCESS!!!!")
    except Exception as e: logging.error(e)

    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};PORT=1433;SERVER='+SQL_SERVER+';PORT=1443;DATABASE='+SQL_DB+';UID='+USERNAME+';PWD='+ PASSWORD)
        logging.info("\t\tSUCCESS!!!!")
    except Exception as e: logging.error(e)
    '''
    try:
        cnxn = pyodbc.connect('DRIVER={libmsodbcsql.17.dylib};PORT=1433;SERVER='+SQL_SERVER+';PORT=1443;DATABASE='+SQL_DB+';UID='+USERNAME+';PWD='+ PASSWORD)
        logging.info("\t\tSUCCESS!!!!")
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM Image_Info")
        row = cursor.fetchone()
        while row:
            logging.info(str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
    except Exception as e: logging.error(e)
    '''
    try:
        cnxn = pyodbc.connect('DRIVER={/bin/libmsodbcsql.17.dylib};PORT=1433;SERVER='+SQL_SERVER+';PORT=1443;DATABASE='+SQL_DB+';UID='+USERNAME+';PWD='+ PASSWORD)
        logging.info("\t\tSUCCESS!!!!")
    except Exception as e: logging.error(e)
    '''
    

    #except pyodbc.Error: logging.error("Could not connect to database. Not DB error")
    '''
    except TypeError:
        print ("Invalid Database query!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        with open('dataR.csv', 'w', newline='') as cf:
        print("Opening Read-CSV file")
        csvWrite = csv.writer(cf)
        print("Writing Work Order & Operator Id data from Table into Read-CSV file")
        err1 = ('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
        err2 = ('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
        err3 = ('0,0')
        err4 = ('0,0')
        err5 = ('0,0')
        csvWrite.writerow([err1])
        csvWrite.writerow([err2])
        csvWrite.writerow([err3])
        csvWrite.writerow([err4])
        csvWrite.writerow([err5])
    '''
    return func.HttpResponse(f"The weather is sunny at {datetime.datetime.now()}!")

def show_odbc_sources():
	sources = pyodbc.drivers()
	#dsns = sources.keys()
	#sorted(dsns)
	sl = []
	for dsn in sources:
		sl.append('%s [%s]' % (dsn, sources[dsn]))
	logging.info('\n'.join(sl))

def printDirectory():
    result = str(subprocess.check_output("/bin/ls")).split("\\n") 
    for a in result:
        logging.info(a)

def printDirectory2():
    result = subprocess.run(['odbcinst','-j'], stdout=subprocess.PIPE)
    tokens = result.stdout.decode('utf-8').split("\\n") 
    for a in tokens:
        logging.info(a)

def printWorkDirectory():
    cwd = os.getcwd()
    logging.info(cwd)

def printPlatform():
    logging.info(platform)

def printUName():
    logging.info(os.uname())


'''
try:
    con1 = pyodbc.connect('DRIVER={SQL Server};SERVER='+(l1)+';Port=1433;DATABASE='+(l3)+';UID='+(l5)+';PWD='+(l7)+'')
except pyodbc.DatabaseError: print("Could not connect to database.")
except TypeError:
    print ("Invalid Database query!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    with open('dataR.csv', 'w', newline='') as cf:
    print("Opening Read-CSV file")
    csvWrite = csv.writer(cf)
    print("Writing Work Order & Operator Id data from Table into Read-CSV file")
    err1 = ('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    err2 = ('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    err3 = ('0,0')
    err4 = ('0,0')
    err5 = ('0,0')
    csvWrite.writerow([err1])
    csvWrite.writerow([err2])
    csvWrite.writerow([err3])
    csvWrite.writerow([err4])
    csvWrite.writerow([err5])



        cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Image_Info")
    row = cursor.fetchone()
    while row:
        logging.info(str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()
'''


