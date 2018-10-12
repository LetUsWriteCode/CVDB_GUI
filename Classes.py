import pyodbc
import os
from PIL import Image

class server(object):
	def __init__ (self,server):
		"""Server based operations"""
		self.server = server

	def ping_server(self):
		"""Pings the server name and tracks a response"""

		response = os.system("ping -c 1 " + self.server)
		if response == 0:
			message = '{} is reachable'.format(self.server)
		else:
			message = '{} is not reachable'.format(self.server)
		return print(message)


class database(object):
	def __init__ (self, server, database, username, password, driver=None):
		self.server = server
		self.database = database
		self.username = username
		if driver == None:
			self.driver = '{ODBC Driver 13 for SQL Server}'
		else:
			self.driver = driver
		return None
	def _openConnection (self):
		"""Attempts connection to the specified server and database using username and password"""
		connString = 'Driver={};Server={};Database={};Trusted_Connection=yes;'.format(self.driver,self.server,self.database) #Windows Auth
#		connString = 'Driver={};Server={}Database={};UID={};PWD={};'.format(driver,server,database,username,password) #SQL Auth
		connect = pyodbc.connect(connString, autocommit=True)
		conn = connect.cursor()
		return conn
	def sendSQL(self, statement):
		"""Sends the SQL Statement to the database. Doesn't return an output"""
		c = self._openConnection()
		c.execute(statement)
		c.close()

class employer(object):
	def __init__ (self):
		"""Allows Employer operations to the database"""

	def searchEmployer(self, searchString):
		"""Searches the database for employer and returns EmployerID or Not Found"""

	def addEmployer(self, CompanyName, Website=None, Description=None):
		"""Adds a new employer to the database"""
		SQLCommand = "EXEC dbo.uspAddEmployer '{}', '{}', '{}'".format(CompanyName,Website,Description)

		conn = database(server='DESKTOP-F16R844',database='CVDatabase',username='devtest',password='devtest')
		conn.sendSQL(SQLCommand)
	def addEmployerLogo(self,employerId,Image):
		f = open(Image, 'rb')
		ablob = f.read()
		#ablob = pyodbc.Binary(ablob)
		SQLCommand = 'INSERT INTO dbo.EmployerLogo (EmployerID, LogoBLOB) VALUES (?, ?)'.format(employerId, ablob)

		print(SQLCommand)
		conn = database(server='DESKTOP-F16R844',database='CVDatabase',username='devtest',password='devtest')
		c = conn._openConnection()
		c.execute(SQLCommand,employerId,pyodbc.Binary(ablob))
		c.close()


class subject(object):
	def __init__ (self):
		"""Allows Subject (person) operations to the database"""
		return None
	
	def returnSubjects(self):
		"""Returns all the subjects from the Subject table"""
		SQLCommand = 'SELECT * FROM dbo.Subject'

		conn = database(server='DESKTOP-F16R844',database='CVDatabase',username='devtest',password='devtest')
		c = conn._openConnection()
		for row in c.execute(SQLCommand):
			print(row)
		c.close()

	def searchSubject(self, forename=None, surname=None, dob=None):
		"""Searches for a subject by Forename, Lastname or DOB"""
		if forename == None:
			forename = '%'
		if surname == None:
			surname = '%'
		if dob == None:
			dob = '%'
		
		SQLCommand = "SELECT * FROM dbo.Subject WHERE Forename LIKE '{}'".format(forename)
		
		conn = database(server='DESKTOP-F16R844',database='CVDatabase',username='devtest',password='devtest')
		c = conn._openConnection()
		for row in c.execute(SQLCommand):
			print(row)
		c.close()
