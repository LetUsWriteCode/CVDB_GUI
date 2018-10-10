import pyodbc
import os

#driver = '{ODBC Driver 17 for SQL Server}'

class server(object):
	def __init__ (self,server):
		"""
		Server based operations
		"""
		self.server = server

	def ping_server(self):
		"""Pings the server name and tracks a response"""

		response = os.system("ping -c 1 " + self.server)
		if response == 0:
			message = '{} is reachable'.format(self.server)
		else:
			message = '{} is not reachable'.format(self.server)
		return print(message)


class connectDB(object):
	def __init__ (self, server, database, username, password, driver='{ODBC Driver 17 for SQL Server}'):
		"""
		Attempts connection to the specified server and database using username and password
		"""	

#		connString = 'Driver={};Server={};Database={};Trusted_Connection=yes;'.format(driver,server,database) #Windows Auth
		connString = 'Driver={};Server={}Database={};UID={};PWD={};'.format(driver,server,database,username,password) #SQL Auth
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

		conn = connectDB(server='192.168.1.161',database='CVDatabase',username='devtest',password='devtest')
		conn.execute(SQLCommand)
		conn.close()