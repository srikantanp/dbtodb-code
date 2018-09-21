import ConfigParser
import sqlite3
from sqlite3 import dbapi2 as sqlite
#function for reading the configuration file:-Edited By SreeSathya Loganathan
def readConfig(file):
   result1=[]
   result2=[]
   try:
      config = ConfigParser.ConfigParser()
      config.read(file)
      return config
   except Exception as error:
      return error


#Function for Fetching data from the database-Edited by Krithika Gopalsamy,Nivetha Seenivasan
def dbFetchData(conf):
   
   for section in conf.sections():
      try:
         for k,v in conf.items(section):
             if(k=='database1'):
                 name=v+".db"
                 conn1=dbConnect(name)
                 print("connection established with%s "%name)
             if(k=='table1'):
                 c = conn1.cursor()
                 c.execute("select * from {}".format(v))
                 result1 = c.fetchall()			 
             if(k=='database2'):
                 name=v+".db"
                 conn2=dbConnect(name)
                 print("connection established with %s "%name)
             if(k=='table2'):
                 c = conn2.cursor()
                 c.execute("select * from {}".format(v))
                 result2 = c.fetchall() 			 
         res=comparison(result1,result2)
         convt_csv(section,res)
      except Exception as error:
         print(error)
      finally:
         conn1.close()
         conn2.close()		 
         print("connection closed")
def comparison(r1,r2):
   
       if(sorted(r1)==sorted(r2)):
          return 'true'
       else:
          return 'false'