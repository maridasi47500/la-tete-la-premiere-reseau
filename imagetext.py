# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Imagetext(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists imagetext(
        id integer primary key autoincrement,
        image_id text,
            text text
                    );""")
        self.con.commit()
        #self.con.close()
    def getallbyuserid(self,userid):
        self.cur.execute(" select message.id, imagetext.text, image.pic as pic, message.user_id from imagetext left join message on message.imagetext_id = imagetext.id left join image on image.id = imagetext.image_id where message.user_id = ?",(userid,))

        row=self.cur.fetchall()
        return row
    def getall(self):
        self.cur.execute("select * from imagetext")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from imagetext where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from imagetext where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into imagetext (image_id,text) values (:image_id,:text)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["imagetext_id"]=myid
        azerty["notice"]="votre imagetext a été ajouté"
        return azerty




