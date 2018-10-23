import pyodbc
import subprocess
import os

#subprocess.call(['./test.sh'])
def printWorkDirectory():
    cwd = os.getcwd()
    print(cwd)

def printDirectoty():
    result = str(subprocess.check_output("/bin/ls")).split("\\n") 
    for a in result:
        print(a)

def printDirectory2():
    result = subprocess.run(['odbcinst','-j'], stdout=subprocess.PIPE)
    tokens = result.stdout.decode('utf-8').split("\\n") 
    for a in tokens:
        print(a)

def show_odbc_sources():
	sources = pyodbc.drivers()
	#dsns = sources.keys()
	#sorted(dsns)
	sl = []
	for dsn in sources:
		sl.append('%s [%s]' % (dsn, sources[dsn]))
	print('\n'.join(sl))


if __name__ == '__main__':
	printDirectory2()