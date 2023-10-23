from distutils.cmd import Command
import sys
import os
from pdb import Restart
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image,ImageTk






direnc= Tk()
direnc.title("Direnc")
direnc.iconbitmap(r"C:\Users\samet\Documents\kod\py\direnc\icon1.ico")
direnc.geometry("+350+120")
direnc.resizable(0,0)

bgi1= ImageTk.PhotoImage(Image.open(r"C:\Users\samet\Documents\kod\py\direnc\bg.png"))
label1 = Label(image=bgi1)
label1.grid(row=0,column=0)




def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)




def dortbant():
    
     lab1= Label(text="  4 column resistance calculation:  ",fg="yellow",bg="black",font="Impact 10")
     lab1.place(x=10,y=50)

     mlist1=["Black","Brown","Red","Orange","Yellow","Green","Blue","Purple","Grey","White"]

     box1=Combobox(values=mlist1)
     box1.place(x=77,y=80,width=100)
     lab2= Label(text=" 1. col: ",fg="black",bg="yellow",font="Oswald 8 bold")
     lab2.place(x=25,y=80)

     lab3= Label(text=" 2. col: ",fg="black",bg="yellow",font="Oswald 8 bold")
     lab3.place(x=200,y=80)
     box2=Combobox(values=mlist1)
     box2.place(x=252,y=80,width=100)

     mlist3=["Black","Brown","Red","Orange","Yellow","Green","Blue","Purple","Gold","Silver"]

     lab4= Label(text=" 3. col: ",fg="black",bg="yellow",font="Oswald 8 bold")
     lab4.place(x=25,y=140)
     box3=Combobox(values=mlist3)
     box3.place(x=77,y=140,width=100)

     mlist4=["Brown","Red","Green","Blue","Purple","Grey","Gold","Silver","NOCLR"]

     lab5= Label(text=" 4. col: ",fg="black",bg="yellow",font="Oswald 8 bold")
     lab5.place(x=200,y=140)
     box4=Combobox(values=mlist4)
     box4.place(x=252,y=140,width=100)

     def islem():
          eslik_ser12={"Black":0,"Brown":1,"Red":2,"Orange":3,"Yellow":4,"Green":5,"Blue":6,"Purple":7,"Grey":8,"White":9}
          eslik_ser3={"Black":1,"Brown":10,"Red":100,"Orange":1000,"Yellow":10000,"Green":100000,"Blue":1000000,"Purple":10000000,"Gold":0.1,"Silver":0.01}
          eslik_ser4={"Brown":1,"Red":2,"Green":0.5,"Blue":0.25,"Purple":0.1,"Grey":0.05,"Gold":5,"Silver":10,"NOCLR":20}
          ser1=box1.get()
          ser2=box2.get()
          ser3=box3.get()
          ser4=box4.get()
          if len(box1.get())==0 or len(box2.get())==0 or len(box3.get())==0 or len(box4.get())==0 :
              messagebox.showinfo("ERROR!",message="It musn't has white space!!")
                            
          else:

              ohm="OHM:"+str(float(str(eslik_ser12[ser1])+str(eslik_ser12[ser2]))*float(str(eslik_ser3[ser3])))    
              tolerans="\nTOL:%"+str(float(str(eslik_ser4[ser4])))
              ot=str(ohm)+str(tolerans)
              label_ot= Label(text=ot,width=20)
              label_ot.place(x=360,y=200)  
        
             
             
         


     dokan= Button(text="Calculate!",bg="white",fg="red",font="Impact 8 ",border=5,command=islem)
     dokan.place(x=400,y=108)
     
     res_but= Button(text="CLR",fg="green",command=restart_program)
     res_but.place(x=100,y=10,width=70)



def besbant():

        lab1= Label(text="  5 column resistance calculation:  ",fg="yellow",bg="black",font="Impact 10")
        lab1.place(x=10,y=50)

        mlist1=["Black","Brown","Red","Orange","Yellow","Green","Blue","Purple","Grey","White"]

        box1=Combobox(values=mlist1)
        box1.place(x=77,y=80,width=100)
        lab2= Label(text=" 1. col: ",fg="black",bg="yellow",font="Oswald 8 bold")
        lab2.place(x=25,y=80)

        lab3= Label(text=" 2. col: ",fg="black",bg="yellow",font="Oswald 8 bold")
        lab3.place(x=200,y=80)
        box2=Combobox(values=mlist1)
        box2.place(x=252,y=80,width=100)

        mlist3=["Black","Brown","Red","Orange","Yellow","Green","Blue","Purple","Gold","Silver"]

        lab4= Label(text=" 4. col: ",fg="black",bg="yellow",font="Oswald 8 bold")
        lab4.place(x=200,y=140)
        box3=Combobox(values=mlist3)
        box3.place(x=252,y=140,width=100)

        mlist4=["Brown","Red","Green","Blue","Purple","Grey","Gold","Silver","NOCLR"]

        lab5= Label(text=" 5. col: ",fg="black",bg="yellow",font="Oswald 8 bold")
        lab5.place(x=25,y=200)
        box4=Combobox(values=mlist4)
        box4.place(x=77,y=200,width=100)
        
        
        lab6= Label(text=" 3. col: ",fg="black",bg="yellow",font="Oswald 8 bold")
        lab6.place(x=25,y=140)
        box5=Combobox(values=mlist1)
        box5.place(x=77,y=140,width=100)




        def islem():
            eslik_ser12={"Black":0,"Brown":1,"Red":2,"Orange":3,"Yellow":4,"Green":5,"Blue":6,"Purple":7,"Grey":8,"White":9}
            eslik_ser3={"Black":1,"Brown":10,"Red":100,"Orange":1000,"Yellow":10000,"Green":100000,"Blue":1000000,"Purple":10000000,"Gold":0.1,"Silver":0.01}
            eslik_ser4={"Brown":1,"Red":2,"Green":0.5,"Blue":0.25,"Purple":0.1,"Grey":0.05,"Gold":5,"Silver":10,"NOCLR":20}
            ser1=box1.get()
            ser2=box2.get()
            ser3=box3.get()
            ser4=box4.get()
            ser5=box5.get()
            if len(box1.get())==0 or len(box2.get())==0 or len(box3.get())==0 or len(box4.get())==0 :
                messagebox.showinfo("ERROR!",message="It musn't has white space!!")
             
            else:
                
                ohm="OHM:"+str(float(str(eslik_ser12[ser1])+str(eslik_ser12[ser5])+str(eslik_ser12[ser2]))*float(str(eslik_ser3[ser3])))    
                tolerans="\nTOL:%"+str(float(str(eslik_ser4[ser4])))
                ot=str(ohm)+str(tolerans)
                label_ot= Label(text=ot,width=20)
                label_ot.place(x=360,y=200)
                


        dokan= Button(text="Calculate!",bg="white",fg="red",font="Impact 8 ",border=5,command=islem)
        dokan.place(x=400,y=108)

        res_but= Button(text="CLR",fg="green",command=restart_program)
        res_but.place(x=10,y=10,width=70)
         

  






var=IntVar()

butoncuk1= Radiobutton(text="4 COL",value=1,variable=var,command=dortbant)
butoncuk1.place(x=10,y=10)

butoncuk1= Radiobutton(text="5 COL",value=2,variable=var,command=besbant)
butoncuk1.place(x=100,y=10)








     











direnc.mainloop()