import ConfigParser
import sqlite3
#import mysql.connector
from sqlite3 import dbapi2 as sqlite
import pandas as pd
import datetime
from datetime import timedelta
datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
class dbtodb:	
	#function for reading the configuration file:-Edited By SreeSathya Loganathan
	def readConfig(self):
	   result1=[]
	   result2=[]
	   try:
		  config = ConfigParser.ConfigParser()
		  filepath=raw_input("Enter Config File location")	  
		  config.read(filepath)
		  return config
	   except Exception as error:
		  return error
	#function for connect to dataBase: - Edited by Srikantan Prakash,Krithika Gopalsamy,Nivetha Seenivasan
	def dbConnect(self,name,dbtype):
	   try:
		  if(dbtype=='sqlite3'):
			  name=name+'.db'
			  conn=sqlite3.connect('%s'%name)
			  return conn
		  if(dbtype=='mysql'):
			  conn=mysql.connector.connect(user="root",password="root",host="localhost",database=name)
			  print "in func",type(conn)
			  return conn
	   except Exception as error:
		   return error
	#Function for Fetching data from the database-Edited by Krithika Gopalsamy,Nivetha Seenivasan,Srikantan Prakash
	def dbFetchData(self,conf):
	   type1=""
	   type2=""
	   
	   for section in conf.sections():
		  try:
			 for k,v in conf.items(section):
				 if(k=='database1type'):
					 type1=v
				 if(k=='database1'):
					 name=v
					 conn1=self.dbConnect(name,type1)
					 #print("connection established with%s "%name)
				 if(k=='table1'):
					 c = conn1.cursor()
					 c.execute("select * from {}".format(v))
					 result1 = c.fetchall()	
					 col_name1=[tuple[0] for tuple in c.description]				 
				 if(k=='database2type'):
					 type2=v				 
				 if(k=='database2'):
					 name=v
					 conn2=self.dbConnect(name,type2)
					 #print("connection established with %s "%name)
				 if(k=='table2'):
					 c = conn2.cursor()
					 c.execute("select * from {}".format(v))
					 result2 = c.fetchall() 
					 col_name2=[tuple[0] for tuple in c.description]				 
			 res=self.comparison(result1,result2,col_name1,col_name2)
			 self.convt_csv(section,res)
		  except Exception as error:
			 print(error)
		  finally:
			 conn1.close()
			 conn2.close()		 
			 #print("connection closed")
	#Function for comparing the tables in the database - Edited by Joseph Antony Protus, Jayasri G	,SreeSathya Loganathan  
	def comparison(self,result1,result2,col_name1,col_name2):
		sor_res1=sorted(result1)
		sor_res2=sorted(result2)	
		if len(col_name1)==len(col_name2):
			if len(sor_res1)==len(sor_res2):
				df_1 = pd.DataFrame(data=sor_res1, columns=col_name1)
				df_1=df_1.reindex(sorted(df_1.columns), axis=1)
				df_2 = pd.DataFrame(data=sor_res2, columns=col_name2)
				df_2=df_2.reindex(sorted(df_2.columns), axis=1)
				if(df_2.equals(df_1)):
					return "True"
				else:
					return "False"
			else:
				#print("Record count mismatch")
				return "false"
		else:
			#print("Column count mismatch")
			return "False"
	#Function to print result in CSV file  - Edited by Jayashree Varadharajulu
	def convt_csv(self,section,res):	 
		  with open('OUTPUT6.csv','a') as obj:
			  obj.write(section+",")
			  obj.write(res)
			  obj.write("\n")
			  
	   
if __name__=="__main__":
    ts = datetime.datetime.now()   
    time = str(ts)
	obj=dbtodb()
	conf=obj.readConfig()
	obj.dbFetchData(conf)
	ts1 = datetime.datetime.now()
	time1 = str(ts1)
	time_diff = datetime.datetime.strptime(time1, datetimeFormat) - datetime.datetime.strptime(time, datetimeFormat)
	print("code running time %s"%time_diff)
		 