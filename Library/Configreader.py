import configparser

from Base.Initate_Browser import *
def readconfigData(section,key):
    cnf_reader=configparser.ConfigParser()
    cnf_reader.read("..\config\configfile.cfg")
  #  d=cnf_reader.get('Details','Application_url')
    cnf_reader.get(section,key)
    return cnf_reader.get(section,key)
def fetchElement(section,key):
    fetch_element=configparser.ConfigParser()
    fetch_element.read("..\config\Element.cfg")
    fetch_element.get(section,key)
    return  fetch_element.get(section,key)
print(fetchElement("Registration","username"))
print(fetchElement("Registration","password"))
print(fetchElement("Registration","button"))

print(fetchElement("WelcomePage","welcomeText"))
print(fetchElement("WelcomePage","errormsg"))


#print(readconfigData('Details','Application_url'))
#print(readconfigData('Details','Browser'))
