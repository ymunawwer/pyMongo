import socket
import json
import sys
import pymongo as pm
data_payload = 2048
col = ""

def mongoConnect():
    client = pm.MongoClient('localhost',27017)
    db = client.ADS
    global col
    col= db.data
def reuse_socket_addr():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setblocking(1)
    s.bind(("",8805))
    socket_address=s.getsockname()
    print(socket_address)                                                                 #YASEEN MUNAWWER
    s.listen(2)
    ads = col.find({},{'_id':0})
    while (1) :
        s.listen(2)
        y,(client,address)=s.accept()
        x =(y.recv(1025)).decode()
        while x!='r':
            x = (y.recv(1025)).decode()
            print(x)
            
            for ads1 in ads:
                print(ads1)
                y.send((json.dumps(str(ads1),separators=(',',':'),indent = 4)).encode())
        #client.send("hello".encode())
        y.close()


if __name__ == "__main__":
    mongoConnect()
    reuse_socket_addr()
    
