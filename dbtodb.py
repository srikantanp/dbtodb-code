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
				 col_name1=[tuple[0] for tuple in c.description]
             if(k=='database2'):
                 name=v+".db"
                 conn2=dbConnect(name)
                 print("connection established with %s "%name)
             if(k=='table2'):
                 c = conn2.cursor()
                 c.execute("select * from {}".format(v))
                 result2 = c.fetchall() 
				 col_name2=[tuple[0] for tuple in c.description]				 
         res=comparison(result1,result2,col_name1,col_name2)
         convt_csv(section,res)
      except Exception as error:
         print(error)
      finally:
         conn1.close()
         conn2.close()		 
         print("connection closed")
def comparison(result1,result2,col_name1,col_name2):
   
	if len(col_name1)==len(col_name2):
		if len(result1)==len(result2):
			df_1 = pd.DataFrame(data=result1, columns=col_name1)
			df_1=df_1.reindex(sorted(df_1.columns), axis=1)
			print(df_1)
			df_2 = pd.DataFrame(data=result2, columns=col_name2)
			df_2=df_2.reindex(sorted(df_2.columns), axis=1)
			print(df_2)
			print(df_2.equals(df_1))
		else:
			print("Record count mismatch")
	else:
		print("Column count mismatch")
		
if __name__=="__main__":
	conf=readConfig("conf.ini")
    dbFetchData(conf)