#frontEnd
from tkinter import *
import tkinter.messagebox
import time
import backend
localtime=time.asctime(time.localtime(time.time()))




class Employee:
     def __init__(self,root):
       self.root= root
       self.root.geometry('1400x750+0+0')
       self.root.title('STUDENT MANAGEMENT SYSTEM')
       self.root.iconbitmap("boss.ico")
       
       sid=StringVar( )
       name=StringVar( )
       address=StringVar( )                                           
       age=StringVar( )
       DOB=StringVar( )
       mobile=StringVar( )
       Gender=StringVar( )

#======================function================================
       def iExit( ):
            iExit=tkinter.messagebox.askyesnocancel("payroll management system","confirm if you want to exit")
            if iExit > 0:
                 root.destroy()
                 return
       def Enterinfo( ):
           self.txtstudentdet.insert(END,"\t\t Student details\n\n")
           self.txtstudentdet.insert(END,'Student_ID:  \t\t' +  self.txtstdi.get( ) + "\n\n")
           self.txtstudentdet.insert(END,'Name:  \t\t' + self.name.get( ) + "\n\n")
           self.txtstudentdet.insert(END,'Age:  \t\t' +  self.txtage.get( ) + "\n\n")
           self.txtstudentdet.insert(END,'Date of Birth:  \t\t' + self.txtDate_Of_Birth.get( ) + "\n\n")
           self.txtstudentdet.insert(END,'Address:  \t\t' + self.txtaddres.get( ) + "\n\n")
           self.txtstudentdet.insert(END,'Gender:  \t\t' + self.txtgender.get( ) + "\n\n")
           self.txtstudentdet.insert(END,'Mobile:  \t\t' + self.txtmobile.get( ) + "\n\n")

       def cleardata( ):
           self.txtstdi.delete(0,END)
           self.name.delete(0,END)
           self.txtage.delete(0,END)
           self.txtDate_Of_Birth.delete(0,END)
           self.txtaddres.delete(0,END)
           self.txtgender.delete(0,END)
           self.txtmobile.delete(0,END)
           self.txtstudentdet.delete("1.0",END)

       def adddata( ):
           if(len(sid.get( ) ) !=0):
                backend.addsturec(sid.get( ),name.get( ),age.get( ),DOB.get( ),address.get( ),Gender.get( ),mobile.get( ) )
                studentlist.delete(0,END)
                studentlist.insert(END,sid.get( ),name.get( ),age.get( ),DOB.get( ),address.get( ),Gender.get( ),mobile.get( ))

       def  display( ):
                   studentlist.delete(0,END)
                   for row in backend.viewdata( ):
                        studentlist.insert(END,row,str(""))

       def sturec(event):
            global sd
            serachstu=studentlist.curselection( ) 
            sd=studentlist.get(serachstu)
            
            self.txtstdi.delete(0,END)
            self.txtstdi.insert(END,sd[1])
            self.name.delete(0,END)
            self.name.insert(END,sd[2])
            self.txtage.delete(0,END)
            self.txtage.insert(END,sd[3])
            self.txtDate_Of_Birth.delete(0,END)
            self.txtDate_Of_Birth.insert(END,sd[4])
            self.txtaddres.delete(0,END)
            self.txtaddres.insert(END,sd[5])
            self.txtgender.delete(0,END)
            self.txtgender.insert(END,sd[6])
            self.txtmobile.delete(0,END)
            self.txtmobile.insert(END,sd[7])

       def delete( ):
           if(len(sid.get( ) ) !=0):
                backend.deleterec(sd [0])
                cleardata( )
                display( )

       def searchdata( ):
             studentlist.delete(0,END)
             for row in backend.Search(sid.get( ),name.get( ),age.get( ),DOB.get( ),address.get( ),Gender.get( ),mobile.get( ) ):
                  studentlist.insert(END,row,str(" "))

       def updatedata( ):
            if(len(sid.get( ) )!=0):
                 backend.deleterec(sd [0])
            if(len(sid.get( ) )!=0):
                   backend.addsturec(sid.get( ),name.get( ),age.get( ),DOB.get( ),address.get( ),Gender.get( ),mobile.get( ))

                   studentlist.delete(0,END)
                   studentlist.insert(END,(sid.get( ),name.get( ),age.get( ),DOB.get( ),address.get( ),Gender.get( ),mobile.get( )))

           
#====================frame====================================
       frame=Frame(self.root,height=50,width=1350,bd=8,relief='raise',bg='cornsilk4')
       frame.pack(side=TOP)
       f1=Frame(self.root,height=600,width=600,bd=8,relief='raise',bg='dim gray',padx=10,pady=15)
       f1.pack(side=LEFT)
       f2=Frame(self.root,height=700,width=300,bd=8,relief='raise',bg='gray')
       f2.pack(side=RIGHT)
       f3=Frame(f1,height=200,width=600,bd=20,relief='raise')
       f3.pack(side=TOP)
       f4=Frame(f1,height=600,width=600,bd=20,relief='groove')
       f4.pack(side=TOP)
#================================================================
#=========================labels====================================
       self.lab=Label(frame,font=('arial',40,'bold'),text="                  student    management   system                  ",fg='steel blue3',bd=5);
       self.lab.grid(row=0,column=0)
       self.lab2=Label(frame,font=('arial',10),text=localtime,fg='steel blue').grid(row=1,column=0)
       self.stuid=Label(f3,font=('arial',14,'bold'),text="student_ID",fg='steel blue4',bd=8).grid(row=0,column=0)                
       self.name=Label(f3,font=('arial',14,'bold'),text="NAME",fg='steel blue4',bd=8).grid(row=1,column=0)
       self.Age=Label(f3,font=('arial',14,'bold'),text="Age",fg='steel blue4',bd=8).grid(row=2,column=0)
       self.Date_Of_Birth=Label(f3,font=('arial',14,'bold'),text="Date_Of_Birth",fg='steel blue4',bd=8).grid(row=3,column=0)
       self.address=Label(f3,font=('arial',14,'bold'),text="ADDRRESS",fg='steel blue4',bd=8).grid(row=4,column=0)
       self.gender=Label(f3,font=('arial',14,'bold'),text="GENDER",fg='steel blue4',bd=8).grid(row=5,column=0)
       self.mobile=Label(f3,font=('arial',14,'bold'),text="MOBILE",fg='steel blue4',bd=8).grid(row=6,column=0)
#=======================entry================================================
       self.txtstdi=Entry(f3,textvariable= sid,bd=16,font=('arial',14,'bold'),width=32,justify=RIGHT,bg="powder blue")  
       self.txtstdi.grid(row=0,column=1)
       self.name=Entry(f3,textvariable=name,bd=16,font=('arial',14,'bold'),width=32,justify=RIGHT,bg="powder blue")
       self.name.grid(row=1,column=1)
       self.txtage=Entry(f3,textvariable=age,bd=16,font=('arial',14,'bold'),width=32,justify=LEFT,bg="powder blue")         
       self.txtage.grid(row=2,column=1)
       self.txtDate_Of_Birth=Entry(f3,textvariable=DOB,bd=16,font=('arial',14,'bold'),width=32,justify=LEFT,bg="powder blue")
       self.txtDate_Of_Birth.grid(row=3,column=1)
       self.txtaddres=Entry(f3,textvariable=address,bd=16,font=('arial',14,'bold'),width=32,justify=RIGHT,bg="powder blue")
       self.txtaddres.grid(row=4,column=1)
       self.txtgender=Entry(f3,textvariable=Gender,bd=16,font=('arial',14,'bold'),width=32,justify=RIGHT,bg="powder blue")
       self.txtgender.grid(row=5,column=1)
       self.txtmobile=Entry(f3,textvariable=mobile,bd=16,font=('arial',14,'bold'),width=32,justify=RIGHT,bg="powder blue")
       self.txtmobile.grid(row=6,column=1)
#=================buttons===================================================
       but1=Button(f4,text='Add New',bg='light cyan',command=adddata,bd=8,height=3,width=10,font=('arial',10,'bold')).grid(row=0,column=1)
       lab=Label(f4).grid(row=0,column=2)
       but2=Button(f4,text='Display',bg='light cyan',command=display,bd=8,height=3,width=10,font=('arial',10,'bold')).grid(row=0,column=3)
       lab=Label(f4).grid(row=0,column=4)
       but3=Button(f4,text='Clear',bg='light cyan',command=cleardata,bd=8,height=3,width=10,font=('arial',10,'bold')).grid(row=0,column=5)
       lab=Label(f4).grid(row=0,column=6)
       but3=Button(f4,text='Delete',bg='light cyan',command= delete,bd=8,height=3,width=10,font=('arial',10,'bold')).grid(row=0,column=7)
       lab=Label(f4).grid(row=0,column=8)
       but4=Button(f4,text='Search',bg='light cyan',command=searchdata,bd=8,height=3,width=10,font=('arial',10,'bold')).grid(row=0,column=9)
       lab=Label(f4).grid(row=0,column=10)
       but5=Button(f4,text='Update',bg='light cyan',command=updatedata,bd=8,height=3,width=10,font=('arial',10,'bold')).grid(row=0,column=11)
       lab=Label(f4).grid(row=0,column=12)
       but6=Button(f4,text='student_info',command=Enterinfo,bg='light cyan',bd=8,height=3,width=10,font=('arial',10,'bold')).grid(row=0,column=13)
       lab=Label(f4).grid(row=0,column=14)
       but6=Button(f4,text='Exit',bg='light cyan',command= iExit,bd=8,height=3,width=10,font=('arial',10,'bold')).grid(row=0,column=15)
       lab=Label(f4).grid(row=0,column=16)
       

#====================listbox and scrollbar==================================
       lab=Label(f2,font=('arial',12,'bold'),text="student details",fg='peachpuff4').grid(row=0,column=0)
       self.txtstudentdet=Text(f2, width=45,height=20,font=('arial',10,'bold'),bd=10)
       self.txtstudentdet.grid(row=1,column=0)
       lab=Label(f2,font=('arial',10,'bold'),text="Search_Student",fg='peachpuff4').grid(row=2,column=0)

       scrollbar=Scrollbar(f2)
       scrollbar.grid(row=3,column=2)
       studentlist=Listbox(f2, width=35,height=8,font=('arial',12,'bold'),bd=12,yscrollcommand=scrollbar.set)
       studentlist.bind('<<ListboxSelect>>',sturec)
       studentlist.grid(row=3,column=0,padx=8)
       scrollbar.config(command=studentlist.yview)


if __name__=='__main__':
     root=Tk()
     application=Employee(root)
     root.mainloop()
