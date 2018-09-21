#Function for Fetching data from the database-Edited by Krithika Gopalsamy
def dbFetchData(conf):
   
   for section in conf.sections():

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
