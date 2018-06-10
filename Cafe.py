from tkinter import *
from tkinter import ttk
import random
import datetime
import time;
import tkinter.messagebox
from math import sqrt as sqr
import math

root=Tk()
root.geometry("1350x750+0+0")
root.title("Mini Cafe Management System")
root.configure(background="black")

Tops=Frame(root, width=1350, height=75, bd=3, relief="raise")
Tops.pack(side=TOP)

F1=Frame(root, width=620, height=650, bd=2, relief="raise")
F1.pack(side=LEFT)
F2=Frame(root, width=350, height=650, bd=2, relief="raise")
F2.pack(side=LEFT)
F3=Frame(root, width=420, height=700, bd=2, relief="raise")
F3.pack(side=RIGHT)

F1a=Frame(F1, width=900, height=330, bd=2, relief="raise")
F1a.pack(side=TOP)
F3a=Frame(F1, width=900, height=320, bd=2, relief="raise")
F3a.pack(side=BOTTOM)

Ft2=Frame(F3, width=440, height=450, bd=2, relief="raise")
Ft2.pack(side=TOP)
Fb2=Frame(F3, width=440, height=250, bd=2, relief="raise")
Fb2.pack(side=BOTTOM)


F1aa=Frame(F1a, width=400, height=330, bd=2, relief="raise")
F1aa.pack(side=LEFT)
F1ab=Frame(F1a, width=400, height=330, bd=2, relief="raise")
F1ab.pack(side=RIGHT)

F3aa=Frame(F3a, width=340, height=330, bd=2, relief="raise")
F3aa.pack(side=LEFT)
F3ab=Frame(F3a, width=340, height=300, bd=2, relief="raise")
F3ab.pack(side=RIGHT)
#=====================================================================================================
Tops.configure(background="black")
F1.configure(background="black")
F2.configure(background="black")
F3.configure(background="black")
#F3.configure(background="white")
#=====================================================================================================
lblInfo=Label(Tops, font=('arial',50,'bold'), text="          Mini Cafe Management System          ", bd=2,anchor='w')
lblInfo.grid(row=0, column=0)
#=====================================================================================================
def Receipt_Given():
    
    txtReceipt.delete("1.0",END)
    x= random.randint(100,100000)
    randomRef= str(x)
    txtReceipt.insert(END,"             Cafe Management System    ")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"--------------------------------------------------------------")
    txtReceipt.insert(END," \n")
    Receipt_Ref.set("BILL_No :" + randomRef)
    txtReceipt.insert(END,Receipt_Ref.get() +"\t             \t"+Date_Of_Order.strftime("%d/%m/%Y %H:%M")+"\n")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"Customer Name :     \t\t" +Name.get()+"\n")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"---------------------------------------------------------------")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END," \n")
    

    if(E_Momo.get() >= str(1)):
        txtReceipt.insert(END,'Momo  \t\t\t' +E_Momo.get() +"\n")
    if(E_Chowmin.get() >=str(1)):
        txtReceipt.insert(END,'Chowmin  \t\t\t' +E_Chowmin.get() +"\n")
    if(E_Masala_Dosa.get() >= str(1)):
        txtReceipt.insert(END,'Masala Dosa  \t\t\t' +E_Masala_Dosa.get() +"\n")
    if(E_Buff_Chilly.get() >= str(1)):
        txtReceipt.insert(END,"Buff Chilly  \t\t\t" +E_Buff_Chilly.get() +"\n")
    if(E_Special_Maggi.get() >= str(1)):
        txtReceipt.insert(END,"Special Maggi  \t\t\t" +E_Special_Maggi.get() +"\n")
    if(E_Pizza.get() >= str(1)):
        txtReceipt.insert(END,"Pizza    \t\t\t" +E_Pizza.get() +"\n")

    if(E_Burger.get() >= str(1)):
        txtReceipt.insert(END,"Burger   \t\t\t" +E_Burger.get() +"\n")
    if(E_Spring_Roll.get() >= str(1)):
        txtReceipt.insert(END,"Spring Roll  \t\t\t" +E_Spring_Roll.get() +"\n")
    if(E_French_Fry.get() >= str(1)):
        txtReceipt.insert(END,"French Fry   \t\t\t" +E_French_Fry.get() +"\n")
    if(E_Sausage.get() >= str(1)):
        txtReceipt.insert(END,"Sausage    \t\t\t" +E_Sausage.get() +"\n")
    if(E_Coke.get() >= str(1)):
        txtReceipt.insert(END,"Coke     \t\t\t" +E_Coke.get() +"\n")
    if(E_Frooti.get() >= str(1)):
        txtReceipt.insert(END,"Frooti    \t\t\t" +E_Frooti.get() +"\n")
    if(E_Coffee.get() >= str(1)):
        txtReceipt.insert(END,"Coffee   \t\t\t" +E_Coffee.get() +"\n")
    if(E_Tea.get() >= str(1)):
        txtReceipt.insert(END,"Tea       \t\t\t" +E_Tea.get() +"\n")
    if(E_Gorkhali_Lassi.get() >= str(1)):
        txtReceipt.insert(END,"Gorkhali Lassi   \t\t\t" +E_Gorkhali_Lassi.get() +"\n")
    if(E_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,"Ice Cream  \t\t\t" +E_Ice_Cream.get() +"\n")
    if(E_Red_Bull.get() >= str(1)):
        txtReceipt.insert(END,"Red Bull    \t\t\t" +E_Red_Bull.get() +"\n")
    if(E_Whisky.get() >= str(1)):
        txtReceipt.insert(END,"Whisky    \t\t\t" +E_Whisky.get() +"\n")
    if(E_Wine.get() >= str(1)):
        txtReceipt.insert(END,"Red Wine   \t\t\t" +E_Wine.get() +"\n")
    if(E_Khukuri_Rum.get() >= str(1)):
        txtReceipt.insert(END,"Khukuri Rum    \t\t\t" +E_Khukuri_Rum.get() +"\n")
    if(E_Fish_Fry.get() >= str(1)):
        txtReceipt.insert(END,"Fish Fry    \t\t\t" +E_Fish_Fry.get() +"\n")
    if(E_Mushroom.get() >= str(1)):
        txtReceipt.insert(END,"Mushroom    \t\t\t" +E_Mushroom.get() +"\n")
    if(E_Cakes.get() >= str(1)):
        txtReceipt.insert(END,"Cakes    \t\t\t" +E_Cakes.get() +"\n")
    if(E_Laphing.get() >= str(1)):
        txtReceipt.insert(END,"Laphing    \t\t\t" +E_Laphing.get() +"\n")
    if(E_Beer.get() >= str(1)):
        txtReceipt.insert(END,"Beer    \t\t\t" +E_Beer.get() +"\n")
    if(E_Vodka.get() >= str(1)):
        txtReceipt.insert(END,"Vodka    \t\t\t" +E_Vodka.get() +"\n")
    if(E_Martini.get() >= str(1)):
        txtReceipt.insert(END,"Martini    \t\t\t" +E_Martini.get() +"\n")
    if(E_Apple_Cider.get() >= str(1)):
        txtReceipt.insert(END,"Apple_Cider    \t\t\t" +E_Apple_Cider.get() +"\n")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"---------------------------------------------------------------")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"Cost of Meals     \t\t" +Cost_Of_Meals.get()+"\n")                  
    txtReceipt.insert(END,"Cost of Drinks     \t\t"+Cost_Of_Drinks.get()+"\n")
    txtReceipt.insert(END,"Service Charge     \t\t"+Service_Charge.get()+"\n")
    txtReceipt.insert(END,"VAT     \t\t"+Vat_Paid.get() +"\n")
    txtReceipt.insert(END,"Sub Total    \t\t" +Sub_Total.get() +"\n")
    txtReceipt.insert(END,"Total Cost     \t\t"+Total_Cost.get() +"\n")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"---------------------------------------------------------------")
    txtReceipt.insert(END,"        Thankyou for Visiting us!!!!")



    
def chkbutton_Value():
    if (var1.get() == 1):
        txtMomo.configure(state=NORMAL)
    elif var1.get() == 0:
        txtMomo.configure(state=DISABLED)
        E_Momo.set("0")
    if (var2.get() == 1):
        txtChowmin.configure(state=NORMAL)
    elif (var2.get() == 0):
        txtChowmin.configure(state=DISABLED)
        E_Chowmin.set("0")
    if (var3.get() == 1):
        txtMasala_Dosa.configure(state=NORMAL)
    elif (var3.get() == 0):
        txtMasala_Dosa.configure(state=DISABLED)
        E_Masala_Dosa.set("0")
    if (var4.get() == 1):
        txtBuff_Chilly.configure(state=NORMAL)
    elif (var4.get() == 0):
        txtBuff_Chilly.configure(state=DISABLED)
        E_Buff_Chilly.set("0")
    if (var5.get() == 1):
        txtSpecial_Maggi.configure(state=NORMAL)
    elif (var5.get() == 0):
        txtSpecial_Maggi.configure(state=DISABLED)
        E_Special_Maggi.set("0")
    if (var6.get() == 1):
        txtPizza.configure(state=NORMAL)
    elif (var6.get() == 0):
        txtPizza.configure(state=DISABLED)
        E_Pizza.set("0")
    if (var7.get() == 1):
        txtBurger.configure(state=NORMAL)
    elif (var7.get() == 0):
        txtBurger.configure(state=DISABLED)
        E_Burger.set("0")
    if (var8.get() == 1):
        txtSpring_Roll.configure(state=NORMAL)
    elif (var8.get() == 0):
        txtSpring_Roll.configure(state=DISABLED)
        E_Spring_Roll.set("0")
    if (var9.get() == 1):
        txtFrench_Fry.configure(state=NORMAL)
    elif (var9.get() == 0):
        txtFrench_Fry.configure(state=DISABLED)
        E_French_Fry.set("0")
    if (var10.get() == 1):
        txtSausage.configure(state=NORMAL)
    elif (var10.get() == 0):
        txtSausage.configure(state=DISABLED)
        E_Sausage.set("0")
    if (var21.get() == 1):
        txtFish_Fry.configure(state=NORMAL)
    elif (var21.get() == 0):
        txtFish_Fry.configure(state=DISABLED)
        E_Fish_Fry.set("0")
    if (var22.get() == 1):
        txtMushroom.configure(state=NORMAL)
    elif (var22.get() == 0):
        txtMushroom.configure(state=DISABLED)
        E_Mushroom.set("0")
    if (var23.get() == 1):
        txtCakes.configure(state=NORMAL)
    elif (var23.get() == 0):
        txtCakes.configure(state=DISABLED)
        E_Cakes.set("0")
    if (var27.get() == 1):
        txtLaphing.configure(state=NORMAL)
    elif (var27.get() == 0):
        txtLaphing.configure(state=DISABLED)
        E_Laphing.set("0")

        
    if (var11.get() == 1):
        txtCoke.configure(state=NORMAL)
    elif (var11.get() == 0):
        txtCoke.configure(state=DISABLED)
        E_Coke.set("0")
    if (var12.get() == 1):
        txtFrooti.configure(state=NORMAL)
    elif (var12.get() == 0):
        txtFrooti.configure(state=DISABLED)
        E_Frooti.set("0")
    if (var13.get() == 1):
        txtCoffee.configure(state=NORMAL)
    elif (var13.get() == 0):
        txtCoffee.configure(state=DISABLED)
        E_Coffee.set("0")
    if (var14.get() == 1):
        txtTea.configure(state=NORMAL)
    elif (var14.get() == 0):
        txtTea.configure(state=DISABLED)
        E_Tea.set("0")
    if (var15.get() == 1):
        txtGorkhali_Lassi.configure(state=NORMAL)
    elif (var15.get() == 0):
        txtGorkhali_Lassi.configure(state=DISABLED)
        E_Gorkhali_Lassi.set("0")
    if (var16.get() == 1):
        txtIce_Cream.configure(state=NORMAL)
    elif (var16.get() == 0):
        txtIce_Cream.configure(state=DISABLED)
        E_Ice_Cream.set("0")
    if (var17.get() == 1):
        txtRed_Bull.configure(state=NORMAL)
    elif (var17.get() == 0):
        txtRed_Bull.configure(state=DISABLED)
        E_Red_Bull.set("0")
    if (var18.get() == 1):
        txtWhisky.configure(state=NORMAL)
    elif (var18.get() == 0):
        txtWhisky.configure(state=DISABLED)
        E_Whisky.set("0")
    if (var19.get() == 1):
        txtWine.configure(state=NORMAL)
    elif (var19.get() == 0):
        txtWine.configure(state=DISABLED)
        E_Wine.set("0")
    if (var20.get() == 1):
        txtKhukuri_Rum.configure(state=NORMAL)
    elif (var20.get() == 0):
        txtKhukuri_Rum.configure(state=DISABLED)
        E_Khukuri_Rum.set("0")
    if (var24.get() == 1):
        txtBeer.configure(state=NORMAL)
    elif (var24.get() == 0):
        txtBeer.configure(state=DISABLED)
        E_Beer.set("0")
    if (var25.get() == 1):
        txtVodka.configure(state=NORMAL)
    elif (var25.get() == 0):
        txtVodka.configure(state=DISABLED)
        E_Vodka.set("0")
    if (var26.get() == 1):
        txtMartini.configure(state=NORMAL)
    elif (var26.get() == 0):
        txtMartini.configure(state=DISABLED)
        E_Martini.set("0")
    if (var28.get() == 1):
        txtApple_Cider.configure(state=NORMAL)
    elif (var28.get() == 0):
        txtApple_Cider.configure(state=DISABLED)
        E_Apple_Cider.set("0")


def Cost_Of_Items():
    Item1=float(E_Momo.get())
    Item2=float(E_Chowmin.get())
    Item3=float(E_Masala_Dosa.get())
    Item4=float(E_Buff_Chilly.get())
    Item5=float(E_Special_Maggi.get())
    Item6=float(E_Pizza.get())
    Item7=float(E_Burger.get())
    Item8=float(E_Spring_Roll.get())
    Item9=float(E_French_Fry.get())
    Item10=float(E_Sausage.get())
    Item21=float(E_Fish_Fry.get())
    Item22=float(E_Mushroom.get())
    Item23=float(E_Cakes.get())
    Item27=float(E_Laphing.get())

    Item11=float(E_Coke.get())
    Item12=float(E_Frooti.get())
    Item13=float(E_Coffee.get())
    Item14=float(E_Tea.get())
    Item15=float(E_Gorkhali_Lassi.get())
    Item16=float(E_Ice_Cream.get())
    Item17=float(E_Red_Bull.get())
    Item18=float(E_Whisky.get())
    Item19=float(E_Wine.get())
    Item20=float(E_Khukuri_Rum.get())
    Item24=float(E_Beer.get())
    Item25=float(E_Vodka.get())
    Item26=float(E_Martini.get())
    Item28=float(E_Apple_Cider.get())

    Price_Of_Meals=(Item1 * 70) + (Item2 * 60) +(Item3 * 80)+(Item4 * 70)+(Item5 * 40)+(Item6 * 220)+(Item7 * 120)\
                    +(Item8 * 35)+(Item9 * 90)+(Item10 * 20)+(Item21 * 100)+(Item22 * 120)+(Item23 * 60)+(Item27 * 160)
    Price_Of_Drinks=(Item11 * 35) + (Item12 * 30) +(Item13 * 20)+(Item14 * 10)+(Item15 * 50)+(Item16 * 20)+(Item17 * 100)\
                    +(Item18 * 300)+(Item19 * 350)+(Item10 * 380)+(Item24 * 220)+(Item25 * 180)+(Item26 * 280)+(Item28 * 150)

    MealsPrice="Rs", str('%.2f'%(Price_Of_Meals))
    DrinksPrice="Rs", str('%.2f'%(Price_Of_Drinks))
    Cost_Of_Meals.set(MealsPrice)
    Cost_Of_Drinks.set(DrinksPrice)
    SC="Rs", str('%.2f'%((Price_Of_Drinks + Price_Of_Meals)*0.08))
    SC1=((Price_Of_Drinks + Price_Of_Meals)*0.08)
    Service_Charge.set(SC)

    Vat="Rs", str('%.2f'%((Price_Of_Drinks + Price_Of_Meals)*0.13))
    Vat1=((Price_Of_Drinks + Price_Of_Meals)*0.13)
    Vat_Paid.set(Vat)

    Sub_Total_Of_Items="Rs",str('%.2f'%(Price_Of_Drinks + Price_Of_Meals + SC1+Vat1))
    Sub_Total.set(Sub_Total_Of_Items)

    #Tax="Rs", str('%.2f'%((Price_Of_Drinks + Price_Of_Meals + 25)*0.15))
    #Paid_Tax.set(Tax)
    
    #TT=((Price_Of_Drinks + Price_Of_Meals + 25)*0.15)
    
    
    
    TC="Rs", str('%.2f'%(Price_Of_Drinks + Price_Of_Meals + SC1+Vat1))
    TC1=(Price_Of_Drinks + Price_Of_Meals + SC1+Vat1)
    

    Discount_Amount=TC1*0.12
    Total_Discount=TC1-Discount_Amount
    Discount.set(Discount_Amount)

    Total_Discount1="Rs", str('%.2f'%(TC1-Discount_Amount))
    Total_Cost.set(Total_Discount1)

    
def qExit():
    qExit1=tkinter.messagebox.askquestion("Quit System","Do you want to quit?")
    if qExit1 == "yes":
        root.destroy()

def Reset():
    Name.set("")
    Sub_Total.set("")
    Total_Cost.set("")
    Cost_Of_Meals.set("")
    Cost_Of_Drinks.set("")
    Service_Charge.set("")
    Vat_Paid.set("")
    Discount.set("")
    txtReceipt.delete("1.0",END)

    E_Momo.set("0")
    E_Chowmin.set("0")
    E_Masala_Dosa.set("0")
    E_Buff_Chilly.set("0")
    E_Special_Maggi.set("0")
    E_Pizza.set("0")
    E_Burger.set("0")
    E_Spring_Roll.set("0")
    E_French_Fry.set("0")
    E_Sausage.set("0")
    E_Coke.set("0")
    E_Frooti.set("0")
    E_Coffee.set("0")
    E_Tea.set("0")
    E_Gorkhali_Lassi.set("0")
    E_Ice_Cream.set("0")
    E_Red_Bull.set("0")
    E_Whisky.set("0")
    E_Wine.set("0")
    E_Khukuri_Rum.set("0")
    E_Fish_Fry.set("0")
    E_Mushroom.set("0")
    E_Cakes.set("0")
    E_Beer.set("0")
    E_Vodka.set("0")
    E_Martini.set("0")
    E_Laphing.set("0")
    E_Apple_Cider.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)

    txtMomo.configure(state=DISABLED)
    txtChowmin.configure(state=DISABLED)
    txtMasala_Dosa.configure(state=DISABLED)
    txtBuff_Chilly.configure(state=DISABLED)
    txtSpecial_Maggi.configure(state=DISABLED)
    txtPizza.configure(state=DISABLED)
    txtBurger.configure(state=DISABLED)
    txtSpring_Roll.configure(state=DISABLED)
    txtFrench_Fry.configure(state=DISABLED)
    txtSausage.configure(state=DISABLED)
    txtCoke.configure(state=DISABLED)
    txtFrooti.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtGorkhali_Lassi.configure(state=DISABLED)
    txtIce_Cream.configure(state=DISABLED)
    txtRed_Bull.configure(state=DISABLED)
    txtWhisky.configure(state=DISABLED)
    txtWine.configure(state=DISABLED)
    txtKhukuri_Rum.configure(state=DISABLED)
    txtFish_Fry.configure(state=DISABLED)
    txtMushroom.configure(state=DISABLED)
    txtCakes.configure(state=DISABLED)
    txtBeer.configure(state=DISABLED)
    txtVodka.configure(state=DISABLED)
    txtMartini.configure(state=DISABLED)
    txtLaphing.configure(state=DISABLED)
    txtApple_Cider.configure(state=DISABLED)


    
#====================================================================================================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()





Date_Of_Order=datetime.datetime.now()
#Date_Of_Order=StringVar()
Receipt_Ref=StringVar()
Name=StringVar()
Sub_Total=StringVar()
Total_Cost=StringVar()
Cost_Of_Meals=StringVar()
Cost_Of_Drinks=StringVar()
Service_Charge=StringVar()
Vat_Paid=StringVar()
Discount=StringVar()

#=================================================================================================

E_Momo=StringVar()
E_Chowmin=StringVar()
E_Masala_Dosa=StringVar()
E_Buff_Chilly=StringVar()
E_Special_Maggi=StringVar()
E_Pizza=StringVar()
E_Burger=StringVar()
E_Spring_Roll=StringVar()
E_French_Fry=StringVar()
E_Sausage=StringVar()
E_Fish_Fry=StringVar()
E_Mushroom=StringVar()
E_Cakes=StringVar()
E_Laphing=StringVar()

E_Coke=StringVar()
E_Frooti=StringVar()
E_Coffee=StringVar()
E_Tea=StringVar()
E_Gorkhali_Lassi=StringVar()
E_Ice_Cream=StringVar()
E_Red_Bull=StringVar()
E_Whisky=StringVar()
E_Wine=StringVar()
E_Khukuri_Rum=StringVar()
E_Beer=StringVar()
E_Vodka=StringVar()
E_Martini=StringVar()
E_Apple_Cider=StringVar()







E_Momo.set("0")
E_Chowmin.set("0")
E_Masala_Dosa.set("0")
E_Buff_Chilly.set("0")
E_Special_Maggi.set("0")
E_Pizza.set("0")
E_Burger.set("0")
E_Spring_Roll.set("0")
E_French_Fry.set("0")
E_Sausage.set("0")
E_Coke.set("0")
E_Frooti.set("0")
E_Coffee.set("0")
E_Tea.set("0")
E_Gorkhali_Lassi.set("0")
E_Ice_Cream.set("0")
E_Red_Bull.set("0")
E_Whisky.set("0")
E_Wine.set("0")
E_Khukuri_Rum.set("0")
E_Fish_Fry.set("0")
E_Mushroom.set("0")
E_Cakes.set("0")
E_Beer.set("0")
E_Vodka.set("0")
E_Martini.set("0")
E_Laphing.set("0")
E_Apple_Cider.set("0")


Date_Of_Order.strftime("%d/%m/%Y %H:%M")

#=====================================================================================================

Momo= Checkbutton(F1aa, text="  Momo        \t", variable=var1, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Momo.grid(row=0, column=0,sticky=W)
Chowmin=Checkbutton(F1aa, text="  Chowmin      \t", variable=var2, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Chowmin.grid(row=1, column=0,sticky=W)
Masala_Dosa=Checkbutton(F1aa, text="  Masala Dosa   \t", variable=var3, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Masala_Dosa.grid(row=2, column=0,sticky=W)
Buff_Chilly=Checkbutton(F1aa, text="  Buff Chilly   \t", variable=var4, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Buff_Chilly.grid(row=3, column=0,sticky=W)
Special_Maggi=Checkbutton(F1aa, text="  Special Maggi   \t", variable=var5, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Special_Maggi.grid(row=4, column=0,sticky=W)
Pizza=Checkbutton(F1aa, text="  Pizza            \t", variable=var6, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Pizza.grid(row=5, column=0,sticky=W)
Burger=Checkbutton(F1aa, text="  Ham Burger        \t", variable=var7, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Burger.grid(row=6, column=0,sticky=W)
Spring_Roll=Checkbutton(F1aa, text="  Spring Roll   \t", variable=var8, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Spring_Roll.grid(row=7, column=0,sticky=W)
French_Fry=Checkbutton(F1aa, text="  French fry   \t", variable=var9, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
French_Fry.grid(row=8, column=0,sticky=W)
Sausage=Checkbutton(F1aa, text="  Sausage        \t", variable=var10, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Sausage.grid(row=9, column=0,sticky=W)
Fish_Fry=Checkbutton(F1aa, text="  Fish Fry        \t", variable=var21, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Fish_Fry.grid(row=10, column=0,sticky=W)
Mushroom=Checkbutton(F1aa, text="  Mushroom        \t", variable=var22, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Mushroom.grid(row=11, column=0,sticky=W)
Cakes=Checkbutton(F1aa, text="  Cakes        \t", variable=var23, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Cakes.grid(row=12, column=0,sticky=W)
Laphing=Checkbutton(F1aa, text="  Laphing        \t", variable=var27, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Laphing.grid(row=13, column=0,sticky=W)

#======================================================================================================

Coke=Checkbutton(F1ab, text="  Coke/Sprite     \t", variable=var11, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Coke.grid(row=0, column=0,sticky=W)
Frooti=Checkbutton(F1ab, text="  Frooti          \t", variable=var12, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Frooti.grid(row=1, column=0,sticky=W)
Coffee=Checkbutton(F1ab, text="  Coffee          \t", variable=var13, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Coffee.grid(row=2, column=0,sticky=W)
Tea=Checkbutton(F1ab, text="  Tea                \t", variable=var14, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Tea.grid(row=3, column=0,sticky=W)
Lassi=Checkbutton(F1ab, text="  Gorkhali Lassi   \t", variable=var15, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Lassi.grid(row=4, column=0,sticky=W)
Ice_Cream=Checkbutton(F1ab, text="  Ice-Cream    \t", variable=var16, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Ice_Cream.grid(row=5, column=0,sticky=W)
Red_Bull=Checkbutton(F1ab, text="  Red Bull      \t", variable=var17, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Red_Bull.grid(row=6, column=0,sticky=W)
Whisky=Checkbutton(F1ab, text="  Whisky          \t", variable=var18, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Whisky.grid(row=7, column=0,sticky=W)
Wine=Checkbutton(F1ab, text="  Red Wine          \t", variable=var19, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Wine.grid(row=8, column=0,sticky=W)
Khukuri_Rum=Checkbutton(F1ab, text="  Khukuri Rum      \t", variable=var20, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Khukuri_Rum.grid(row=9, column=0,sticky=W)
Beer=Checkbutton(F1ab, text="  Beer        \t", variable=var24, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Beer.grid(row=10, column=0,sticky=W)
Vodka=Checkbutton(F1ab, text="  Vodka        \t", variable=var25, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Vodka.grid(row=11, column=0,sticky=W)
Martini=Checkbutton(F1ab, text="  Martini        \t", variable=var26, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Martini.grid(row=12, column=0,sticky=W)
Apple_Cider=Checkbutton(F1ab, text="  Apple Cider        \t", variable=var28, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Apple_Cider.grid(row=13, column=0,sticky=W)


#=============================================================================================

txtMomo =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8,  textvariable=E_Momo, justify="left", state=DISABLED)
txtMomo.grid(row=0, column=1)
txtChowmin =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8,textvariable=E_Chowmin, justify="left", state=DISABLED)
txtChowmin.grid(row=1, column=1)
txtMasala_Dosa =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Masala_Dosa)
txtMasala_Dosa.grid(row=2, column=1)
txtBuff_Chilly =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Buff_Chilly)
txtBuff_Chilly.grid(row=3, column=1)
txtSpecial_Maggi =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Special_Maggi)
txtSpecial_Maggi.grid(row=4, column=1)
txtPizza =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Pizza)
txtPizza.grid(row=5, column=1)
txtBurger =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Burger)
txtBurger.grid(row=6, column=1)
txtSpring_Roll =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Spring_Roll)
txtSpring_Roll.grid(row=7, column=1)
txtFrench_Fry =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_French_Fry)
txtFrench_Fry.grid(row=8, column=1)
txtSausage =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Sausage)
txtSausage.grid(row=9, column=1)
txtFish_Fry =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Fish_Fry)
txtFish_Fry.grid(row=10, column=1)
txtMushroom =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Mushroom)
txtMushroom.grid(row=11, column=1)
txtCakes =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Cakes)
txtCakes.grid(row=12, column=1)
txtLaphing =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Laphing)
txtLaphing.grid(row=13, column=1)



#=============================================================================================

txtCoke =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Coke)
txtCoke.grid(row=0, column=1)
txtFrooti =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Frooti)
txtFrooti.grid(row=1, column=1)
txtCoffee =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Coffee)
txtCoffee.grid(row=2, column=1)
txtTea =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Tea)
txtTea.grid(row=3, column=1)
txtGorkhali_Lassi =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Gorkhali_Lassi)
txtGorkhali_Lassi.grid(row=4, column=1)
txtIce_Cream =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Ice_Cream)
txtIce_Cream.grid(row=5, column=1)
txtRed_Bull =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Red_Bull)
txtRed_Bull.grid(row=6, column=1)
txtWhisky =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Whisky)
txtWhisky.grid(row=7, column=1)
txtWine =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Wine)
txtWine.grid(row=8, column=1)
txtKhukuri_Rum =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Khukuri_Rum)
txtKhukuri_Rum.grid(row=9, column=1)
txtBeer =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Beer)
txtBeer.grid(row=10, column=1)
txtVodka =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Vodka)
txtVodka.grid(row=11, column=1)
txtMartini =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Martini)
txtMartini.grid(row=12, column=1)
txtApple_Cider =Entry(F1ab, font=('arial',16,'bold'), bd=4, width=8, justify="left", state=DISABLED,textvariable=E_Apple_Cider)
txtApple_Cider.grid(row=13, column=1)

#=====================================================================================================

lblReceipt = Label(Ft2,font=('arial',12,'bold'), text="Receipt:",bd=2,anchor='w')
lblReceipt.grid(row=0, column=0 ,sticky=W)
txtReceipt =Text(Ft2, font=('arial',12,'bold'), bd=2, width=39,height=30,bg="black" )
txtReceipt.grid(row=1, column=0)


lblCost_Of_Meals=Label(F3aa, font=('arial',12,'bold'),text="   Cost of Meals   ",bd=5,anchor='w')
lblCost_Of_Meals.grid(row=1,column=0,sticky=W)
txtCost_Of_Meals=Entry(F3aa, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Cost_Of_Meals,insertwidth=2)
txtCost_Of_Meals.grid(row=1,column=1,sticky=W)

lblCost_Of_Drinks=Label(F3aa, font=('arial',12,'bold'),text="   Cost of Drinks   ",bd=4,anchor='w')
lblCost_Of_Drinks.grid(row=2,column=0,sticky=W)
txtCost_Of_Drinks=Entry(F3aa, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Cost_Of_Drinks,insertwidth=2)
txtCost_Of_Drinks.grid(row=2,column=1,sticky=W)

lblService_Charge=Label(F3aa, font=('arial',12,'bold'),text="   Service Charge    ",bd=5,anchor='w')
lblService_Charge.grid(row=3,column=0,sticky=W)
txtService_Charge=Entry(F3aa, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Service_Charge,insertwidth=2)
txtService_Charge.grid(row=3,column=1,sticky=W)

lblVat_Paid=Label(F3ab, font=('arial',12,'bold'),text="   Vat Paid    ",bd=5,anchor='w')
lblVat_Paid.grid(row=0,column=0,sticky=W)
txtVat_Paid=Entry(F3ab, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Vat_Paid,insertwidth=2)
txtVat_Paid.grid(row=0,column=1,sticky=W)

lblName=Label(F3aa, font=('arial',12,'bold'),text="   Name       ",bd=5,anchor='w')
lblName.grid(row=0,column=0,sticky=W)
txtName=Entry(F3aa, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Name,insertwidth=2)
txtName.grid(row=0,column=1,sticky=W)

lblSub_Total=Label(F3ab, font=('arial',12,'bold'),text="   Sub Total     ",bd=5,anchor='w')
lblSub_Total.grid(row=2,column=0,sticky=W)
txtSub_Total=Entry(F3ab, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Sub_Total,insertwidth=2)
txtSub_Total.grid(row=2,column=1,sticky=W)

lblDiscount=Label(F3ab, font=('arial',12,'bold'),text="   Discount       ",bd=5,anchor='w')
lblDiscount.grid(row=1,column=0,sticky=W)
txtDiscount=Entry(F3ab, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Discount,insertwidth=2)
txtDiscount.grid(row=1,column=1,sticky=W)

lblTotal_Cost=Label(F3ab, font=('arial',12,'bold'),text="   Total Cost    ",bd=5,anchor='w')
lblTotal_Cost.grid(row=3,column=0,sticky=W)
txtTotal_Cost=Entry(F3ab, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Total_Cost,insertwidth=2)
txtTotal_Cost.grid(row=3,column=1,sticky=W)


#=====================================================================================================


#====================================================================================================

btnTotal_Cost=Button(Fb2,padx=16,pady=1,bd=3,bg="black",font=('arial',12,'bold'),width=4,text=" Total ",command=Cost_Of_Items)
btnTotal_Cost.grid(row=0,column=0)

btnReceipt=Button(Fb2,padx=16,pady=1,bd=3,bg="black",font=('arial',12,'bold'),width=4,text=" Receipt ",command=Receipt_Given)
btnReceipt.grid(row=0,column=1)

btnReset=Button(Fb2,padx=16,pady=1,bd=3,bg="black",font=('arial',12,'bold'),width=4,text=" Reset ",command=Reset)
btnReset.grid(row=0,column=2)

btnExit=Button(Fb2,padx=16,pady=1,bd=3,bg="black",font=('arial',12,'bold'),width=4,text=" Exit ",command=qExit)
btnExit.grid(row=0,column=3)
#==========================================================================================================
class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)


    def backspace(self):
        text=text_box.get()[:-1]#text_box.get()=self.entry.get()
        if text == " ":
            text = "0"
        self.current=text
        self.display(text)


    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())


    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)


    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "raise":
            self.total = self.total * self.total
        if self.op == "exp":
            self.total = self.total * 2.7182818285
        if self.op == "cube":
            self.total = self.total * self.total * self.total
        if self.op == "rootof":
            self.total = self.total ** (1/self.current)
        if self.op == "cuberoot":
            self.total = math.pow(self.total,1/3)
        if self.op == "fact":
            self.total=int(text_box.get())
            self.total=math.factorial(self.total)
        if self.op == "ln":
            self.total = math.log(self.total)
        if self.op == "log":
            self.total=math.log(self.total,10)
        if self.op == "sine":
            self.total=math.sin((self.total*2*math.pi)/360)
        if self.op == "cosine":
            self.total = math.cos((self.total*2*math.pi)/360)
        if self.op == "tangent":
            self.total = math.tan((self.total*2*math.pi)/360)
        if self.op == "Exp_Power":
            self.total = self.total * 2.7182818285 *2.7182818285
        if self.op == "inv":
            self.total = 1/self.total
        self.new_num = True
        self.op_pending = False
        self.display(self.total)


    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op= op
        self.eq = False


    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_clear(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

    def qExit(self):
        self.qExit1=tkinter.messagebox.askquestion("Quit System","Do you want to quit?")
        if self.qExit1 == "yes":
            root.destroy()


sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calculator")
text_box = Entry(F2, justify=RIGHT,width=26,font="Times 16 bold")
text_box.grid(row = 0, column = 0,columnspan = 8,padx=30, pady =30)
text_box.insert(0, "0")
text_box.focus()


numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(F2,height =3,width=4,padx=10, pady = 10, text = numbers[i],fg="blue",font=("arial",12,"bold"),bd=4))
        bttn[i]["bg"]= "orange"
        bttn[i].grid(row = j, column = k,padx=1,pady=1)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1
all_clear = Button(F2,height =3,width=4,padx=10, pady = 10, text = "AC",bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
all_clear["command"] = sum1.all_clear
all_clear.grid(row = 1, column = 3, padx=1, pady = 1)

Delete = Button(F2,height =3,width=4,padx=10, pady = 10, text = "Del",bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
Delete["command"] = sum1.backspace
Delete.grid(row = 1, column = 4, padx=1, pady = 1)

add = Button(F2,height =3,width=4,padx=10, pady = 10, text = "+",bg="steel blue",fg="blue",font=("arial",12,"bold"),bd=4)
add["command"] = lambda: sum1.operation("add")
add.grid(row = 2, column = 3,  padx=1, pady = 1)

mult = Button(F2,height =3,width=4,padx=10, pady = 10, text = "*",bg="steel blue",fg="blue",font=("arial",12,"bold"),bd=4)
mult["command"] = lambda: sum1.operation("times")
mult.grid(row = 2, column = 4,  padx=1, pady = 1)


minus = Button(F2,height =3,width=4,padx=10, pady = 10, text = "-",bg="steel blue",fg="blue",font=("arial",12,"bold"),bd=4)
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, padx=1, pady = 1)


log10 = Button(F2, height=3, width=4, padx=10, pady=10, text="log",bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
log10["command"]= lambda: sum1.operation("log")
log10.grid(row=3, column=4, padx=1 , pady=1)


point = Button(F2,height =2,width=4,padx=10, pady = 10, text = ".",bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 0, padx=1, pady = 1)


bttn_0 = Button(F2,height =2,width=4,padx=10, pady = 10, text = "0",bg="orange",fg="blue",font=("arial",12,"bold"),bd=4)
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 1,  padx=1, pady = 1)

neg= Button(F2,height =2,width=4,padx=10, pady = 10, text = "+/-",bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
neg["command"] = sum1.sign
neg.grid(row = 4, column = 2,  padx=1, pady = 1)


div = Button(F2,height =2,width=4,padx=10, pady = 10, text = "/",bg="steel blue",fg="blue",font=("arial",12,"bold"),bd=4)
div["command"] = lambda: sum1.operation("divide")
div.grid(row = 4, column = 3, padx=1, pady = 1)

loge = Button(F2, height=2, width=4, padx=10, pady=10, text="ln",bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
loge["command"] = lambda: sum1.operation("ln")
loge.grid(row=4, column=4, padx=1, pady=1)

power = Button(F2, height=2,width=4,padx=10,pady=10,text="x^2",bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
power["command"] = lambda: sum1.operation("raise")
power.grid(row=5,column = 0,padx=1,pady=1)

fact = Button(F2, height=2, width=4, padx=10, pady=10, text="!",bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
fact["command"] = lambda: sum1.operation("fact")
fact.grid(row=5,column=1, padx=1, pady=1)

inv = Button(F2, height=2, width=4, padx=10, pady=10, text="1/x", bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
inv["command"] = lambda: sum1.operation("inv")
inv.grid(row=5,column=2,padx=1,pady=1)

pi = Button(F2, height=2, width=4, padx=10, pady=10, text="Pi", bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
pi["command"] = lambda: sum1.operation("inv")
pi.grid(row=5,column=3,padx=1,pady=1)

Exponent = Button(F2, height=2, width=4, padx=10, pady=10, text="Exp", bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
Exponent["command"] = lambda: sum1.operation("exp")
Exponent.grid(row=5,column=4,padx=1,pady=1)



sine = Button(F2, height=2,width=4, padx=10,pady=10, text = "sin" , bg= "green",fg="blue",font=("arial",12,"bold"),bd=4)
sine["command"]=lambda: sum1.operation("sine")
sine.grid(row=6,column=0,padx=1,pady=1)

cosine = Button(F2, height=2,width=4, padx=10,pady=10, text = "cos" , bg= "green",fg="blue",font=("arial",12,"bold"),bd=4)
cosine["command"]=lambda: sum1.operation("cosine")
cosine.grid(row=6,column=1,padx=1,pady=1)

tangent = Button(F2, height=2,width=4, padx=10,pady=10, text = "tan" , bg= "green",fg="blue",font=("arial",12,"bold"),bd=4)
tangent["command"]=lambda: sum1.operation("tangent")
tangent.grid(row=6,column=2,padx=1,pady=1)

rootof = Button(F2, height=2, width=4, padx=10, pady=10, text="\/x", bg = "green",fg="blue",font=("arial",12,"bold"),bd=4)
rootof["command"] = lambda: sum1.operation("rootof")
rootof.grid(row=6, column=3, padx=1, pady=1)

Cubeof = Button(F2, height=2, width=4, padx=10, pady=10, text='\/3', bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
Cubeof["command"]=lambda: sum1.operation("cuberoot")
Cubeof.grid(row=6,column=4,padx=1,pady=1)



cube = Button(F2,height =2,width=4,padx=10, pady = 10, text = "x^3",bg="steel blue",fg="blue",font=("arial",12,"bold"),bd=4)
cube["command"] = lambda: sum1.operation("cube")
cube.grid(row = 7, column = 0,  padx=1, pady = 1)

Exp_Power = Button(F2,height =2,width=4,padx=10, pady = 10, text = "e^2",bg="steel blue",fg="blue",font=("arial",12,"bold"),bd=4)
Exp_Power["command"] = lambda: sum1.operation("Exp_Power")
Exp_Power.grid(row = 7, column = 1,  padx=1, pady = 1)


Off = Button(F2,height =2,width=4,padx=10, pady = 10, text = "OFF",bg="violet",fg="blue",font=("arial",12,"bold"),bd=4)
Off["command"] = sum1.qExit
Off.grid(row = 7, column = 2, padx=1, pady = 1)

equals = Button(F2,height =2,width=12,padx=10, pady = 10, text = "=",bg="green",fg="blue",font=("arial",12,"bold"),bd=4)
equals["command"] = sum1.calc_total
equals.grid(row = 7, column = 3,columnspan=2,rowspan=1,padx=1, pady = 1)


root.mainloop()
