from pymongo import MongoClient
from datetime import datetime
def getDataFromFile(fname):
    # connect to the MongoDB on MongoLab
    # to learn more about MongoLab visit http://www.mongolab.com
    # replace the "" in the line below with your MongoLab connection string
    # you can also use a local MongoDB instance
    #conn=MongoClient('mongodb://%s:%s@127.0.0.1' % ('admin','admin123'))
    connection = MongoClient("127.0.0.1",27017)

    # connect to the students database and the ctec121 collection
    db = connection.test.diniraw
    
    fd=open(fname,'r').read().strip().split("\n")
    for line in fd:
        record=line.strip().split(",")
        print record
        record=[int(e) for e in record]
        post={"ph_no":record[0],"time":str(datetime.now()),"temp":record[1]}
        db.insert_one(post)
        
getDataFromFile('myrawdata.txt')
