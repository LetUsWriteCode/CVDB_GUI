import os
from Classes import employer, connectDB, server

company = 'Google'
website = 'http://www.google.com'
desc = 'Do No Evil'


ser = server('192.168.1.161')
ser.ping_server()

t = employer()
t.addEmployer(company,website, desc)