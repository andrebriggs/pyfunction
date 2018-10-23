import logging
import datetime
import os
import azure.functions as func
import sys
import pip
#from pip import get_installed_distributions
import pyodbc
import subprocess
from sys import platform
from shutil import copyfile
#import pymssql
import stat

SQL_SERVER = 'abrig-al.database.windows.net'
SQL_DB = 'image-track'
USERNAME = 'aladmin'
PASSWORD = 'REPLACE'


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    '''
    installed_packages = get_installed_distributions()
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
        for i in installed_packages])
    logging.info(installed_packages_list)

    
    logging.warning("****\t\tKEYS\t\t****")
    logging.warning("")
    for param in os.environ.keys():
        logging.info("%s: %s " % (param, os.environ[param]))
    logging.warning("")
    '''
    
    #logging.warning('copying files')
    #copyfile('/home/site/wwwroot/odbcinst.ini','/etc/odbcinst.ini')
    #copyfile('/home/site/wwwroot/pkgs/opt/microsoft/msodbcsql/lib64/libmsodbcsql-13.1.so.9.2','/opt/microsoft/msodbcsql/lib64/libmsodbcsql-13.1.so.9.2')
    #copyfile('pkgs/usr/lib/libmsodbcsql-13.so','/usr/lib/libmsodbcsql-13.so')
    #os.environ['ODBCINSTINI'] = '/home/site/wwwroot/odbcinst.ini'
   
    '''
    myLib = '/home/site/wwwroot/pkgs/opt/microsoft/msodbcsql/lib64/libmsodbcsql-13.1.so.9.2'
    printPermissions(myLib)

    st = os.stat(myLib)
    os.chmod(myLib, st.st_mode | stat.S_IEXEC)
    printPermissions(myLib)
    '''
    
    '''
    show_odbc_sources()

#    find . -name "foo*"
    #findFile('/', 'libmsodbcsql*')
    #findFile('/', 'msodbcsqlr17*')

    listDirectory('/')
    listDirectory('/opt/microsoft')
    listDirectory('/usr/lib')
    
    listDirectory('/usr')
    
    listDirectory('/usr/lib64')
    listDirectory('/usr/lib/x86_64-linux-gnu/')
    listDirectory('/root')
    listDirectory('/home')
    listDirectory('/home/user')
    listDirectory('/home/site')
    logging.info("\n\n")
    listDirectory('/opt')
    #listDirectory('/opt/microsoftmsodbcsql17') 
    
    listDirectory('/usr/local')
    logging.info("\n\n")
    listDirectory('/usr/local/lib/') 
   
    logging.info("\n\n")
    listDirectory('/usr/local/bin/')
    logging.info("\n\n")
    listDirectory('/usr/lib')
    logging.info("\n\n")
    listDirectory('/etc')
    logging.info("\n\n")
    listDirectory('/etc/ODBCDataSources')
    logging.info("\n\n")
    '''
    '''
    #odbc.ini & odbcinst.ini
    printFileAtPath('/etc/odbc.ini')
    logging.info("\n\n")
    printFileAtPath('/etc/odbcinst.ini')
    logging.info("\n\n")
    #printFileAtPath('/root/.profile')
    #printFileAtPath('/root/.bashrc')
    printDirectory()

    printWorkDirectory()

    printDirectory2()

    printExecOutput()

    printPlatform()

    printUName()
    '''

    '''
    os.environ['TDSDUMP'] = '/tmp/freetds.log'
    

    try:    
        printTSQL()
        print("Success!")
    except Exception as e: logging.error(e)

    try:
        validatedb()
        print("Success!")
    except Exception as e: logging.error(e)

    logging.info("\n\n")
    printFileAtPath('/tmp/freetds.log')
    #listDirectory('/tmp')
    logging.info("\n\n")
    '''
    driver= '{ODBC Driver 17 for SQL Server}' #Works for Mac OS https://stackoverflow.com/a/44538741
    # Open connection
    
    successCount = 0
    try:
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};PORT=1433;SERVER=abrig-al.database.windows.net;PORT=1443;DATABASE=image-track;UID=aladmin;PWD=pickleBeach1192')
        #cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};PORT=1433;SERVER='+SQL_SERVER+';PORT=1443;DATABASE='+SQL_DB+';UID='+USERNAME+';PWD='+ PASSWORD)
        logging.info("\t\tSUCCESS!!!!")
        successCount += 1
    except Exception as e: logging.error(e)
    
    try:
        cnxn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.2.so.0.1};PORT=1433;SERVER='+SQL_SERVER+';PORT=1443;DATABASE='+SQL_DB+';UID='+USERNAME+';PWD='+ PASSWORD)
        logging.info("\t\tSUCCESS!!!!")
        successCount += 1
    except Exception as e: logging.error(e)
    
    try:
        cnxn = pyodbc.connect('DRIVER={/usr/lib/libmsodbcsql-17.so};PORT=1433;SERVER='+SQL_SERVER+';PORT=1443;DATABASE='+SQL_DB+';UID='+USERNAME+';PWD='+ PASSWORD)
        logging.info("\t\tSUCCESS!!!!")
        successCount += 1
    except Exception as e: logging.error(e)

    printFileAtPath('/tmp/odbctrace.log')

    return func.HttpResponse(f"The weather is sunny at {datetime.datetime.now()} and ODBC Driver 17 connection is {successCount}!")


def show_odbc_sources():
    logging.warning(f"\t\tOutput of pyodbc.drivers()")
    sources = pyodbc.drivers()
    logging.info(sources)
	#dsns = sources.keys()
	#sorted(dsns)
    #sl = []
    #for dsn in sources:
    #    sl.append('%s [%s]' % (dsn, sources[dsn]))
    #logging.info('\n'.join(sl))

def printDirectory():
    result = str(subprocess.check_output("/bin/ls")).split("\\n") 
    for a in result:
        logging.info(a)

def printDirectory2():
    logging.warning(f"\t\tOutput of command odbcinst -j")
    result = subprocess.run(['odbcinst','-j'], stdout=subprocess.PIPE)
    tokens = result.stdout.decode('utf-8').split("\\n") 
    for a in tokens:
        logging.info(a)

def printExecOutput(): #odbcinst -q -d -n "ODBC Driver 11 for SQL Server"
    logging.warning(f"\t\tOutput of command: odbcinst -q -d -n 'ODBC Driver 17 for SQL Server'")
    result = subprocess.run(['odbcinst','-q','-d','-n','"ODBC Driver 11 for SQL Server"'], stdout=subprocess.PIPE)
    tokens = result.stdout.decode('utf-8').split("\\n") 
    for a in tokens:
        logging.info(a)

def printPermissions(filepath): #odbcinst -q -d -n "ODBC Driver 11 for SQL Server"
    logging.warning(f"\t\tOutput of command: ls -l {filepath}")
    result = subprocess.run(['ls','-l',filepath,], stdout=subprocess.PIPE)
    tokens = result.stdout.decode('utf-8').split("\\n") 
    for a in tokens:
        logging.info(a)

def printTSQL():
    result = subprocess.run(['tsql','-C'], stdout=subprocess.PIPE)
    tokens = result.stdout.decode('utf-8').split("\\n") 
    for a in tokens:
        logging.info(a)

#    find . -name "foo*"
def findFile(startDir, filePattern):
    logging.warning(f"\t\tFinding {filePattern} in {startDir}")
    result = subprocess.run(['find',startDir,'-name',filePattern], stdout=subprocess.PIPE)
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
def validatedb():
    os.environ["TDSVER"] = "8.0"
    conn = pymssql.connect(server=SQL_SERVER, user='aladmin', password=PASSWORD, database=SQL_DB,tds_version="8.0")  
    cursor = conn.cursor()  
    cursor.execute('SELECT * FROM tagstate')  
    row = cursor.fetchone()  
    logging.info('')
    while row:  
        logging.info(str(row[0]) + " " + str(row[1]))    
        row = cursor.fetchone()
'''
def listDirectory(path):
    logging.warning(f"\t\tListing directory {path}")
    try:
        files = sorted(os.listdir(path))
        for name in files:
            logging.info(name)
    except Exception as e: 
        logging.error(e)

def printFileAtPath(fname):
    logging.warning(f"\t\tReading file directory {fname}")
    try:
        with open(fname, 'r') as fin:
            logging.info(fin.read())
    except Exception as e: 
        logging.error(e)

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


