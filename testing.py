import os
from Classes import employer, database, server, subject
import pyodbc

company = 'Google'
website = 'http://www.google.com'
desc = 'Do No Evil'


#ser = server('DESKTOP-F16R844')
#ser.ping_server()

t = employer()
#t.addEmployer(company,website, desc)
t.addEmployerLogo(1,'C:\Pics\Google.jpg')

#p = subject()
#p.searchSubject(forename = 'Mark')

"""
class connectDB(object):
	driver = '{ODBC Driver 13 for SQL Server}'
	server = 'DESKTOP-F16R844'
	db = 'CVDatabase'
	username = 'devtest'
	password = 'devtest'
	def __init__(self):
		print('opn')	
	def opnCur(self):
		connString = 'Driver={};Server={};Database={};Trusted_Connection=yes;'.format(self.driver,self.server,self.db)
		#connString = 'Driver={};Server={}Database={};User Id={};Password={};'.format(driver,server,db,username,password) #SQL Auth
		connect = pyodbc.connect(connString)
		conn = connect.cursor()
		return conn

con = connectDB()
c = con.opnCur()
for row in c.execute('SELECT * FROM dbo.Subject'):
	print(row)
"""
