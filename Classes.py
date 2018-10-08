import pyodbc
import os

#driver = '{ODBC Driver 17 for SQL Server}'

class connectDB(object):
	def __init__ (self, server, database, username, password, driver='ODBC Driver 13 for SQL Server'):
		"""
		Attempts connection to the specified server and database using username and password
		"""	
#		connString = 'Driver={};Server={};Database={};Trusted_Connection=yes;'.format(driver,server,database) #Windows Auth
		connString = 'Driver={};Server={};Database={};UID={};PWD={};'.format(driver,server,database,username,password) #SQL Auth
		connect = pyodbc.connect(connString)
		conn = connect.cursor()
		return conn

class employer(object):
	def __init__ (self):
		"""
		Allows Employer operations to the database
		"""

	def searchEmployer(self, searchString):
		"""
		Searches the database for employer
		and returns EmployerID or Not Found
		"""

	def addEmployer(self, CompanyName, Website=None, Description=None):
		"""
		Adds a new employer to the database
		"""
		SQLCommand = 'EXEC dbo.uspAddEmployer {}, {}, {}'.format(CompanyName,Website,Description)

		conn = connectDB(server='192.168.1.161,1433',database='CVDatabase',username='devtest',password='devtest')
		conn.execute(SQLCommand)
		conn.close()