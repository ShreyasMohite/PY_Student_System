import sqlite3
#backend
def studentdata( ):
     con=sqlite3.connect("student.db")
     cur=con.cursor(  )
     cur.execute("CREATE TABLE IF NOT EXISTS studentssss(id INTEGER PRIMARY KEY,sid text,name text,age text,DOB text,address text,Gender text,mobile text)")
     con.commit( )
     con.close( )
def addsturec(sid,name,age,DOB,address,Gender,mobile):                                                                                                        
     con=sqlite3.connect("student.db")                                                                                                                           
     cur=con.cursor( )
     cur.execute("INSERT INTO studentssss VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",(sid,name,age,DOB,address,Gender,mobile ))
     con.commit( )
     con.close( )

def viewdata( ):
     con=sqlite3.connect("student.db")                                                                                                                           
     cur=con.cursor(  )
     cur.execute("SELECT * FROM studentssss ")
     row=cur.fetchall( )
     con.close( )
     return row

def deleterec(id ):
     con=sqlite3.connect("student.db")                                                                                                                           
     cur=con.cursor(  )
     cur.execute("DELETE  FROM studentssss WHERE id=?",  (id,) )
     con.commit( )
     con.close( )

def Search(sid=" ",name=" ",address=" ",age=" " ,DOB="  ",mobile= " ",Gender=" "):
     con=sqlite3.connect("student.db")
     cur=con.cursor(  )
     cur.execute("SELECT * FROM studentssss WHERE sid=? OR name=? OR address=? OR age=? OR DOB=? OR mobile=? OR Gender=?",
                 (sid,name,address,age,DOB,mobile,Gender))
     row=cur.fetchall( )
     con.close( )
     return row

def update(id,sid=" ",name=" ",address=" ",age=" " ,DOB="  ",mobile= " ",Gender=" "):
     con=sqlite3.connect("student.db")
     cur=con.cursor(  )
     cur.execute("SELECT * FROM studentssss WHERE sid=? OR name=? OR address=? OR age=? OR DOB=? OR mobile=? OR Gender=?",
                 (sid,name,address,age,DOB,mobile,Gender,id))
     con.commit( )
     con.close( )

studentdata( )
