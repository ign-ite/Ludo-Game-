from tkinter import *
from tkinter import messagebox
import os
f=open("database_proj",'a+')
root = Tk()
root.title("Simple Pharmacy Managment System")
root.configure(width=1500,height=600,bg='BLACK')
var=-1

def additem():
    global var
    num_lines = 0
    with open("database_proj", 'r') as f10:
        for line in f10:
            num_lines += 1
    var=num_lines-1
    e1= entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    f.write('{0} {1} {2} {3} {4}\n'.format(str(e1),e2,e3,str(e4),e5))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)


def deleteitem():
    e1=entry1.get()
    with open(r"database_proj") as f, open(r"database_proj1", "w") as working:
        for line in f:
            if str(e1) not in line:
                working.write(line)
    os.remove(r"database_proj")
    os.rename(r"database_proj1", r"database_proj")
    f.close()
    working.close()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

def firstitem():
    global var
    var=0
    f.seek(var)
    c=f.readline()
    v=list(c.split(" "))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry1.insert(0,str(v[0]))
    entry2.insert(0,str(v[1]))
    entry3.insert(0,str(v[2]))
    entry4.insert(0,str(v[3]))
    entry5.insert(0,str(v[4]))

def nextitem():
    global var
    var = var + 1
    f.seek(var)
