from tkinter import *
from tkinter import ttk
import random
import datetime
import time;
import tkinter.messagebox
from math import sqrt as sqr

root=Tk()
root.geometry("1350x750+0+0")
root.title("Mini Cafe Management System")
root.configure(background="black")
#===========================Frames==============================================================================

Tops=Frame(root, width=1380, height=80, bd=2, relief="raise")
Tops.pack(side=TOP)

F1=Frame(root, width=1050, height=660, bd=2, relief="raise")
F1.pack(side=LEFT)
F2=Frame(root, width=300, height=660, bd=2, relief="raise")
F2.pack(side=RIGHT)

F1a=Frame(F1, width=1000, height=330, bd=2, relief="raise")
F1a.pack(side=TOP)
F1b=Frame(F1, width=1000, height=320, bd=2, relief="raise")
F1b.pack(side=BOTTOM)

F2a=Frame(F2, width=300, height=450, bd=2, relief="raise")
F2a.pack(side=TOP)
F2b=Frame(F2, width=300, height=250, bd=2, relief="raise")
F2b.pack(side=BOTTOM)

F1aa=Frame(F1a, width=353, height=330, bd=2, relief="raise")
F1aa.pack(side=LEFT)
F1bb=Frame(F1a, width=353, height=330, bd=2, relief="raise")
F1bb.pack(side=LEFT)
F1cc=Frame(F1a, width=353, height=330, bd=2, relief="raise")
F1cc.pack(side=RIGHT)

F2aa=Frame(F1b, width=353, height=330, bd=2, relief="raise")
F2aa.pack(side=LEFT)
F2bb=Frame(F1b, width=353, height=330, bd=2, relief="raise")
F2bb.pack(side=LEFT)
F2cc=Frame(F1b, width=353, height=330, bd=2, relief="raise")
F2cc.pack(side=RIGHT)
#===================================================================================================================

Tops.configure(background="black")
F1.configure(background="black")
F2.configure(background="black")

lblInfo=Label(Tops, font=('arial',50,'bold'), text="    Nepali Mini Cafe Management System     ", bd=2,anchor='w')
lblInfo.grid(row=0, column=0)
#==================================Variable Declaration==============================================================
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

    if (var29.get() == 1):
        txtPan_Cakes.configure(state=NORMAL)
    elif (var29.get() == 0):
        txtPan_Cakes.configure(state=DISABLED)
        E_Pan_Cakes.set("0")
    if (var30.get() == 1):
        txtAloo_Paratha.configure(state=NORMAL)
    elif (var30.get() == 0):
        txtAloo_Paratha.configure(state=DISABLED)
        E_Aloo_Paratha.set("0")
    if (var31.get() == 1):
        txtRosted_Salmons.configure(state=NORMAL)
    elif (var31.get() == 0):
        txtRosted_Salmons.configure(state=DISABLED)
        E_Rosted_Salmons.set("0")
    if (var32.get() == 1):
        txtStuffed_Poblanos.configure(state=NORMAL)
    elif (var32.get() == 0):
        txtStuffed_Poblanos.configure(state=DISABLED)
        E_Stuffed_Poblanos.set("0")
    if (var33.get() == 1):
        txtSnikers_Cake.configure(state=NORMAL)
    elif (var33.get() == 0):
        txtSnikers_Cake.configure(state=DISABLED)
        E_Snikers_Cake.set("0")
    if (var34.get() == 1):
        txtPeach_Pie.configure(state=NORMAL)
    elif (var34.get() == 0):
        txtPeach_Pie.configure(state=DISABLED)
        E_Peach_Pie.set("0")
    if (var35.get() == 1):
        txtPoached_Porks.configure(state=NORMAL)
    elif (var35.get() == 0):
        txtPoached_Porks.configure(state=DISABLED)
        E_Poached_Porks.set("0")
    if (var36.get() == 1):
        txtKimchi_Rice.configure(state=NORMAL)
    elif (var36.get() == 0):
        txtKimchi_Rice.configure(state=DISABLED)
        E_Kimchi_Rice.set("0")
    if (var37.get() == 1):
        txtChicken_Fajitas.configure(state=NORMAL)
    elif (var37.get() == 0):
        txtChicken_Fajitas.configure(state=DISABLED)
        E_Chicken_Fajitas.set("0")
    if (var38.get() == 1):
        txtPork_Tenderloin.configure(state=NORMAL)
    elif (var38.get() == 0):
        txtPork_Tenderloin.configure(state=DISABLED)
        E_Pork_Tenderloin.set("0")
    if (var39.get() == 1):
        txtBaked_Salmons.configure(state=NORMAL)
    elif (var39.get() == 0):
        txtBaked_Salmons.configure(state=DISABLED)
        E_Baked_Salmons.set("0")
    if (var40.get() == 1):
        txtNewari_Khaja_Set.configure(state=NORMAL)
    elif (var40.get() == 0):
        txtNewari_Khaja_Set.configure(state=DISABLED)
        E_Newari_Khaja_Set.set("0")
    if (var41.get() == 1):
        txtGreek_Yogurt.configure(state=NORMAL)
    elif (var41.get() == 0):
        txtGreek_Yogurt.configure(state=DISABLED)
        E_Greek_Yogurt.set("0")
    if (var42.get() == 1):
        txtPasta_Fried.configure(state=NORMAL)
    elif (var42.get() == 0):
        txtPasta_Fried.configure(state=DISABLED)
        E_Pasta_Fried.set("0")


        
def Receipt_Given():
    
    txtReceipt.delete("1.0",END)
    x= random.randint(100,100000)
    randomRef= str(x)
    txtReceipt.insert(END,"  \t    Nepali Mini Cafe     ")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"         Address: Nayabazzar,Gorkha")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"--------------------------------------------------------------")
    txtReceipt.insert(END," \n")
    Receipt_Ref.set("BILL_No :" + randomRef)
    txtReceipt.insert(END,Receipt_Ref.get() +"\t            \t"+Date_Of_Order.strftime("%d/%m/%Y %H:%M")+"\n")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"--------------------------------------------------------------")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"Customer Name :     \t\t" +Name.get()+"\n")
    txtReceipt.insert(END,"Table Number  :    \t\t" +Table_Number.get()+"\n")
    txtReceipt.insert(END,"Address  :     \t\t" +Address.get()+"\n")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"---------------------------------------------------------------")
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

    if(E_Pan_Cakes.get() >= str(1)):
        txtReceipt.insert(END,"Pan Cakes    \t\t\t" +E_Pan_Cakes.get() +"\n")
    if(E_Aloo_Paratha.get() >= str(1)):
        txtReceipt.insert(END,"Aloo Paratha    \t\t\t" +E_Aloo_Paratha.get() +"\n")
    if(E_Rosted_Salmons.get() >= str(1)):
        txtReceipt.insert(END,"Rosted Salmons    \t\t\t" +E_Rosted_Salmons.get() +"\n")
    if(E_Stuffed_Poblanos.get() >= str(1)):
        txtReceipt.insert(END,"Stuffed Poblanos    \t\t\t" +E_Stuffed_Poblanos.get() +"\n")
    if(E_Snikers_Cake.get() >= str(1)):
        txtReceipt.insert(END,"Snikers Cake    \t\t\t" +E_Snikers_Cake.get() +"\n")
    if(E_Peach_Pie.get() >= str(1)):
        txtReceipt.insert(END,"Peach Pie    \t\t\t" +E_Peach_Pie.get() +"\n")
    if(E_Poached_Porks.get() >= str(1)):
        txtReceipt.insert(END,"Poached Porks    \t\t\t" +E_Poached_Porks.get() +"\n")
    if(E_Kimchi_Rice.get() >= str(1)):
        txtReceipt.insert(END,"Kimchi Rice    \t\t\t" +E_Kimchi_Rice.get() +"\n")
    if(E_Chicken_Fajitas.get() >= str(1)):
        txtReceipt.insert(END,"Chicken Fajitas    \t\t\t" +E_Chicken_Fajitas.get() +"\n")
    if(E_Pork_Tenderloin.get() >= str(1)):
        txtReceipt.insert(END,"Pork Tenderloin    \t\t\t" +E_Pork_Tenderloin.get() +"\n")
    if(E_Baked_Salmons.get() >= str(1)):
        txtReceipt.insert(END,"Baked Salmons    \t\t\t" +E_Baked_Salmons.get() +"\n")
    if(E_Newari_Khaja_Set.get() >= str(1)):
        txtReceipt.insert(END,"Newari Khaja Set    \t\t\t" +E_Newari_Khaja_Set.get() +"\n")
    if(E_Greek_Yogurt.get() >= str(1)):
        txtReceipt.insert(END,"Greek Yogurt    \t\t\t" +E_Greek_Yogurt.get() +"\n")
    if(E_Pasta_Fried.get() >= str(1)):
        txtReceipt.insert(END,"Pasta Fried    \t\t\t" +E_Pasta_Fried.get() +"\n")
        
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"---------------------------------------------------------------")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"Cost of Meals     \t\t" +Cost_Of_Meals.get()+"\n")                  
    txtReceipt.insert(END,"Cost of Drinks     \t\t"+Cost_Of_Drinks.get()+"\n")
    txtReceipt.insert(END,"Cost of Foods     \t\t"+Cost_Of_Foods.get()+"\n")
    txtReceipt.insert(END,"Service Charge     \t\t"+Service_Charge.get()+"\n")
    txtReceipt.insert(END,"VAT     \t\t"+Vat_Paid.get() +"\n")
    txtReceipt.insert(END,"Discount  \t\t"+Discount.get() +"\n")
    txtReceipt.insert(END,"TAX     \t\t"+Tax.get() +"\n")
    txtReceipt.insert(END,"Sub Total    \t\t" +Sub_Total.get() +"\n")
    txtReceipt.insert(END,"Total Cost     \t\t"+Total_Cost.get() +"\n")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"---------------------------------------------------------------")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"          Thankyou For Visiting Us !!!     ")

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

    Item29=float(E_Pan_Cakes.get())
    Item30=float(E_Aloo_Paratha.get())
    Item31=float(E_Rosted_Salmons.get())
    Item32=float(E_Stuffed_Poblanos.get())
    Item33=float(E_Snikers_Cake.get())
    Item34=float(E_Peach_Pie.get())
    Item35=float(E_Poached_Porks.get())
    Item36=float(E_Kimchi_Rice.get())
    Item37=float(E_Chicken_Fajitas.get())
    Item38=float(E_Pork_Tenderloin.get())
    Item39=float(E_Baked_Salmons.get())
    Item40=float(E_Newari_Khaja_Set.get())
    Item41=float(E_Greek_Yogurt.get())
    Item42=float(E_Pasta_Fried.get())
    

    Price_Of_Meals=(Item1 * 70) + (Item2 * 60) +(Item3 * 80)+(Item4 * 70)+(Item5 * 40)+(Item6 * 220)+(Item7 * 120)\
                    +(Item8 * 35)+(Item9 * 90)+(Item10 * 20)+(Item21 * 100)+(Item22 * 120)+(Item23 * 60)+(Item27 * 160)
    Price_Of_Drinks=(Item11 * 35) + (Item12 * 30) +(Item13 * 20)+(Item14 * 10)+(Item15 * 50)+(Item16 * 20)+(Item17 * 100)\
                    +(Item18 * 300)+(Item19 * 350)+(Item20 * 380)+(Item24 * 220)+(Item25 * 180)+(Item26 * 280)+(Item28 * 150)

    Price_Of_Foods=(Item29 * 220) + (Item30 * 40) +(Item31 * 90)+(Item32 * 110)+(Item33 * 180)+(Item34 * 120)+(Item35 * 170)\
                    +(Item36 * 60)+(Item37 * 140)+(Item38 * 190)+(Item39 * 200)+(Item40 * 230)+(Item41 * 60)+(Item42 * 90)
    
    MealsPrice="Rs", str('%.2f'%(Price_Of_Meals))
    DrinksPrice="Rs", str('%.2f'%(Price_Of_Drinks))
    FoodsPrice="Rs", str('%.2f'%(Price_Of_Foods))
    
    Cost_Of_Meals.set(MealsPrice)
    Cost_Of_Drinks.set(DrinksPrice)
    Cost_Of_Foods.set(FoodsPrice)
    
    SC="Rs", str('%.2f'%((Price_Of_Drinks + Price_Of_Meals + Price_Of_Foods)*0.08))
    SC1=((Price_Of_Drinks + Price_Of_Meals + Price_Of_Foods)*0.08)
    Service_Charge.set(SC)

    Tax1="Rs", str('%.2f'%((Price_Of_Drinks + Price_Of_Meals + Price_Of_Foods+ SC1)*0.10))
    Tax.set(Tax1)
    
    TT=((Price_Of_Drinks + Price_Of_Meals + Price_Of_Foods+ SC1)*0.15)

    Vat="Rs", str('%.2f'%((Price_Of_Drinks + Price_Of_Meals + Price_Of_Foods +SC1)*0.13))
    Vat1=((Price_Of_Drinks + Price_Of_Meals + Price_Of_Foods +SC1)*0.13)
    Vat_Paid.set(Vat)

    Sub_Total_Of_Items="Rs",str('%.2f'%(Price_Of_Drinks + Price_Of_Meals + Price_Of_Foods+ SC1+Vat1+TT))
    Sub_Total.set(Sub_Total_Of_Items)
    
    TC="Rs", str('%.2f'%(Price_Of_Drinks + Price_Of_Meals+ Price_Of_Foods + SC1+Vat1+TT))
    TC1=(Price_Of_Drinks + Price_Of_Meals+ Price_Of_Foods + SC1+Vat1+TT)
    

    Discount_Amount=TC1*0.12
    Discount_Amountt="Rs", str('%.2f'%(TC1*0.12))
    Total_Discount=TC1-Discount_Amount
    Discount.set(Discount_Amountt)

    Total_Discount1="Rs", str('%.2f'%(TC1-Discount_Amount))
    Total_Cost.set(Total_Discount1)


def qExit():
    qExit1=tkinter.messagebox.askquestion("Quit System","Do you want to quit?")
    if qExit1 == "yes":
        root.destroy()

def Reset():
    Name.set("")
    Table_Number.set("")
    Address.set("")
    Tax.set("")
    Sub_Total.set("")
    Total_Cost.set("")
    Cost_Of_Meals.set("")
    Cost_Of_Drinks.set("")
    Cost_Of_Foods.set("")
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

    E_Pan_Cakes.set("0")
    E_Aloo_Paratha.set("0")
    E_Rosted_Salmons.set("0")
    E_Stuffed_Poblanos.set("0")
    E_Snikers_Cake.set("0")
    E_Peach_Pie.set("0")
    E_Poached_Porks.set("0")
    E_Kimchi_Rice.set("0")
    E_Chicken_Fajitas.set("0")
    E_Pork_Tenderloin.set("0")
    E_Baked_Salmons.set("0")
    E_Newari_Khaja_Set.set("0")
    E_Greek_Yogurt.set("0")
    E_Pasta_Fried.set("0")

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
    var29.set(0)
    var30.set(0)
    var31.set(0)
    var32.set(0)
    var33.set(0)
    var34.set(0)
    var35.set(0)
    var36.set(0)
    var37.set(0)
    var38.set(0)
    var39.set(0)
    var40.set(0)
    var41.set(0)
    var42.set(0)

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
    txtPan_Cakes.configure(state=DISABLED)
    txtAloo_Paratha.configure(state=DISABLED)
    txtRosted_Salmons.configure(state=DISABLED)
    txtStuffed_Poblanos.configure(state=DISABLED)
    txtSnikers_Cake.configure(state=DISABLED)
    txtPeach_Pie.configure(state=DISABLED)
    txtPoached_Porks.configure(state=DISABLED)
    txtKimchi_Rice.configure(state=DISABLED)
    txtChicken_Fajitas.configure(state=DISABLED)
    txtPork_Tenderloin.configure(state=DISABLED)
    txtBaked_Salmons.configure(state=DISABLED)
    txtNewari_Khaja_Set.configure(state=DISABLED)
    txtGreek_Yogurt.configure(state=DISABLED)
    txtPasta_Fried.configure(state=DISABLED)

#====================================================================================================================

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
var29=IntVar()
var30=IntVar()
var31=IntVar()
var32=IntVar()
var33=IntVar()
var34=IntVar()
var35=IntVar()
var36=IntVar()
var37=IntVar()
var38=IntVar()
var39=IntVar()
var40=IntVar()
var41=IntVar()
var42=IntVar()


Date_Of_Order=datetime.datetime.now()
#Date_Of_Order=StringVar()
Receipt_Ref=StringVar()
Name=StringVar()
Table_Number=StringVar()
Sub_Total=StringVar()
Total_Cost=StringVar()
Cost_Of_Meals=StringVar()
Cost_Of_Drinks=StringVar()
Cost_Of_Foods=StringVar()
Service_Charge=StringVar()
Vat_Paid=StringVar()
Discount=StringVar()
Tax=StringVar()
Address=StringVar()


#=====================================================================================================================


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

E_Pan_Cakes=StringVar()
E_Aloo_Paratha=StringVar()
E_Rosted_Salmons=StringVar()
E_Stuffed_Poblanos=StringVar()
E_Snikers_Cake=StringVar()
E_Peach_Pie=StringVar()
E_Poached_Porks=StringVar()
E_Kimchi_Rice=StringVar()
E_Chicken_Fajitas=StringVar()
E_Pork_Tenderloin=StringVar()
E_Baked_Salmons=StringVar()
E_Newari_Khaja_Set=StringVar()
E_Greek_Yogurt=StringVar()
E_Pasta_Fried=StringVar()






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
E_Fish_Fry.set("0")
E_Mushroom.set("0")
E_Cakes.set("0")
E_Laphing.set("0")

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
E_Beer.set("0")
E_Vodka.set("0")
E_Martini.set("0")
E_Apple_Cider.set("0")


E_Pan_Cakes.set("0")
E_Aloo_Paratha.set("0")
E_Rosted_Salmons.set("0")
E_Stuffed_Poblanos.set("0")
E_Snikers_Cake.set("0")
E_Peach_Pie.set("0")
E_Poached_Porks.set("0")
E_Kimchi_Rice.set("0")
E_Chicken_Fajitas.set("0")
E_Pork_Tenderloin.set("0")
E_Baked_Salmons.set("0")
E_Newari_Khaja_Set.set("0")
E_Greek_Yogurt.set("0")
E_Pasta_Fried.set("0")


Date_Of_Order.strftime("%d/%m/%Y %H:%M")
#====================================================================================================================


Momo= Checkbutton(F1aa, text="  Momo         \t", variable=var1, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Momo.grid(row=0, column=0,sticky=W)
Chowmin=Checkbutton(F1aa, text="  Chowmin       \t", variable=var2, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Chowmin.grid(row=1, column=0,sticky=W)
Masala_Dosa=Checkbutton(F1aa, text="  Masala Dosa    \t", variable=var3, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Masala_Dosa.grid(row=2, column=0,sticky=W)
Buff_Chilly=Checkbutton(F1aa, text="  Buff Chilly    \t", variable=var4, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Buff_Chilly.grid(row=3, column=0,sticky=W)
Special_Maggi=Checkbutton(F1aa, text="  Special Maggi    \t", variable=var5, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Special_Maggi.grid(row=4, column=0,sticky=W)
Pizza=Checkbutton(F1aa, text="  Pizza             \t", variable=var6, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Pizza.grid(row=5, column=0,sticky=W)
Burger=Checkbutton(F1aa, text="  Ham Burger         \t", variable=var7, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Burger.grid(row=6, column=0,sticky=W)
Spring_Roll=Checkbutton(F1aa, text="  Spring Roll    \t", variable=var8, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Spring_Roll.grid(row=7, column=0,sticky=W)
French_Fry=Checkbutton(F1aa, text="  French fry    \t", variable=var9, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
French_Fry.grid(row=8, column=0,sticky=W)
Sausage=Checkbutton(F1aa, text="  Sausage         \t", variable=var10, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Sausage.grid(row=9, column=0,sticky=W)
Fish_Fry=Checkbutton(F1aa, text="  Fish Fry         \t", variable=var21, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Fish_Fry.grid(row=10, column=0,sticky=W)
Mushroom=Checkbutton(F1aa, text="  Mushroom         \t", variable=var22, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Mushroom.grid(row=11, column=0,sticky=W)
Cakes=Checkbutton(F1aa, text="  Cakes         \t", variable=var23, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Cakes.grid(row=12, column=0,sticky=W)
Laphing=Checkbutton(F1aa, text="  Laphing         \t", variable=var27, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Laphing.grid(row=13, column=0,sticky=W)


txtMomo =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5,  textvariable=E_Momo, justify="left", state=DISABLED)
txtMomo.grid(row=0, column=1)
txtChowmin =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5,textvariable=E_Chowmin, justify="left", state=DISABLED)
txtChowmin.grid(row=1, column=1)
txtMasala_Dosa =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Masala_Dosa)
txtMasala_Dosa.grid(row=2, column=1)
txtBuff_Chilly =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Buff_Chilly)
txtBuff_Chilly.grid(row=3, column=1)
txtSpecial_Maggi =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Special_Maggi)
txtSpecial_Maggi.grid(row=4, column=1)
txtPizza =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Pizza)
txtPizza.grid(row=5, column=1)
txtBurger =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Burger)
txtBurger.grid(row=6, column=1)
txtSpring_Roll =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Spring_Roll)
txtSpring_Roll.grid(row=7, column=1)
txtFrench_Fry =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_French_Fry)
txtFrench_Fry.grid(row=8, column=1)
txtSausage =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Sausage)
txtSausage.grid(row=9, column=1)
txtFish_Fry =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Fish_Fry)
txtFish_Fry.grid(row=10, column=1)
txtMushroom =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Mushroom)
txtMushroom.grid(row=11, column=1)
txtCakes =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Cakes)
txtCakes.grid(row=12, column=1)
txtLaphing =Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Laphing)
txtLaphing.grid(row=13, column=1)


#============================================================================================================================




Coke=Checkbutton(F1bb, text="  Coke/Sprite      \t", variable=var11, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Coke.grid(row=0, column=0,sticky=W)
Frooti=Checkbutton(F1bb, text="  Frooti           \t", variable=var12, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Frooti.grid(row=1, column=0,sticky=W)
Coffee=Checkbutton(F1bb, text="  Coffee           \t", variable=var13, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Coffee.grid(row=2, column=0,sticky=W)
Tea=Checkbutton(F1bb, text="  Tea                 \t", variable=var14, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Tea.grid(row=3, column=0,sticky=W)
Lassi=Checkbutton(F1bb, text="  Gorkhali Lassi    \t", variable=var15, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Lassi.grid(row=4, column=0,sticky=W)
Ice_Cream=Checkbutton(F1bb, text="  Ice-Cream     \t", variable=var16, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Ice_Cream.grid(row=5, column=0,sticky=W)
Red_Bull=Checkbutton(F1bb, text="  Red Bull       \t", variable=var17, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Red_Bull.grid(row=6, column=0,sticky=W)
Whisky=Checkbutton(F1bb, text="  Whisky           \t", variable=var18, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Whisky.grid(row=7, column=0,sticky=W)
Wine=Checkbutton(F1bb, text="  Red Wine           \t", variable=var19, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Wine.grid(row=8, column=0,sticky=W)
Khukuri_Rum=Checkbutton(F1bb, text="  Khukuri Rum       \t", variable=var20, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Khukuri_Rum.grid(row=9, column=0,sticky=W)
Beer=Checkbutton(F1bb, text="  Beer         \t", variable=var24, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Beer.grid(row=10, column=0,sticky=W)
Vodka=Checkbutton(F1bb, text="  Vodka         \t", variable=var25, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Vodka.grid(row=11, column=0,sticky=W)
Martini=Checkbutton(F1bb, text="  Martini         \t", variable=var26, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Martini.grid(row=12, column=0,sticky=W)
Apple_Cider=Checkbutton(F1bb, text="  Apple Cider         \t", variable=var28, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Apple_Cider.grid(row=13, column=0,sticky=W)




txtCoke =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Coke)
txtCoke.grid(row=0, column=1)
txtFrooti =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Frooti)
txtFrooti.grid(row=1, column=1)
txtCoffee =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Coffee)
txtCoffee.grid(row=2, column=1)
txtTea =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Tea)
txtTea.grid(row=3, column=1)
txtGorkhali_Lassi =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Gorkhali_Lassi)
txtGorkhali_Lassi.grid(row=4, column=1)
txtIce_Cream =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Ice_Cream)
txtIce_Cream.grid(row=5, column=1)
txtRed_Bull =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Red_Bull)
txtRed_Bull.grid(row=6, column=1)
txtWhisky =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Whisky)
txtWhisky.grid(row=7, column=1)
txtWine =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Wine)
txtWine.grid(row=8, column=1)
txtKhukuri_Rum =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Khukuri_Rum)
txtKhukuri_Rum.grid(row=9, column=1)
txtBeer =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Beer)
txtBeer.grid(row=10, column=1)
txtVodka =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Vodka)
txtVodka.grid(row=11, column=1)
txtMartini =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Martini)
txtMartini.grid(row=12, column=1)
txtApple_Cider =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Apple_Cider)
txtApple_Cider.grid(row=13, column=1)

#=====================================================================================================================


Pan_Cakes= Checkbutton(F1cc, text="  Pan Cake \t", variable=var29, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Pan_Cakes.grid(row=0, column=0,sticky=W)
Aloo_Paratha=Checkbutton(F1cc, text="  Aloo Paratha \t", variable=var30, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Aloo_Paratha.grid(row=1, column=0,sticky=W)
Rosted_Salmons=Checkbutton(F1cc, text="  Rosted Salmons \t", variable=var31, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Rosted_Salmons.grid(row=2, column=0,sticky=W)
Stuffed_Poblanos=Checkbutton(F1cc, text="  Stuffed Pablanos \t", variable=var32, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Stuffed_Poblanos.grid(row=3, column=0,sticky=W)
Snikers_Cake=Checkbutton(F1cc, text="  Snikers Cake \t", variable=var33, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Snikers_Cake.grid(row=4, column=0,sticky=W)
Peach_Pie=Checkbutton(F1cc, text="  Peach Pie \t", variable=var34, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Peach_Pie.grid(row=5, column=0,sticky=W)
Poached_Porks=Checkbutton(F1cc, text="  Poached Porks \t", variable=var35, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Poached_Porks.grid(row=6, column=0,sticky=W)
Kimchi_Rice=Checkbutton(F1cc, text="  Kimchi Rice Bowls \t", variable=var36, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Kimchi_Rice.grid(row=7, column=0,sticky=W)
Chicken_Fajitas=Checkbutton(F1cc, text="  Chicken Fajitas \t", variable=var37, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Chicken_Fajitas.grid(row=8, column=0,sticky=W)
Pork_Tenderloin=Checkbutton(F1cc, text="  Pork Tenderloin \t", variable=var38, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Pork_Tenderloin.grid(row=9, column=0,sticky=W)
Baked_Salmons=Checkbutton(F1cc, text="  Grilled Salmons \t", variable=var39, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Baked_Salmons.grid(row=10, column=0,sticky=W)
Newari_Khaja_Set=Checkbutton(F1cc, text="  Newari Khaja Set \t", variable=var40, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Newari_Khaja_Set.grid(row=11, column=0,sticky=W)
Greek_Yogurt=Checkbutton(F1cc, text="  Greek Yogurt \t", variable=var41, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Greek_Yogurt.grid(row=12, column=0,sticky=W)
Pasta_Fried=Checkbutton(F1cc, text="  Pasta Fried \t", variable=var42, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Pasta_Fried.grid(row=13, column=0,sticky=W)


txtPan_Cakes =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5,  textvariable=E_Pan_Cakes, justify="left", state=DISABLED)
txtPan_Cakes.grid(row=0, column=1)
txtAloo_Paratha =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5,textvariable=E_Aloo_Paratha, justify="left", state=DISABLED)
txtAloo_Paratha.grid(row=1, column=1)
txtRosted_Salmons =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Rosted_Salmons)
txtRosted_Salmons.grid(row=2, column=1)
txtStuffed_Poblanos =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Stuffed_Poblanos)
txtStuffed_Poblanos.grid(row=3, column=1)
txtSnikers_Cake =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Snikers_Cake)
txtSnikers_Cake.grid(row=4, column=1)
txtPeach_Pie =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Peach_Pie)
txtPeach_Pie.grid(row=5, column=1)
txtPoached_Porks =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Poached_Porks)
txtPoached_Porks.grid(row=6, column=1)
txtKimchi_Rice =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Kimchi_Rice)
txtKimchi_Rice.grid(row=7, column=1)
txtChicken_Fajitas =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Chicken_Fajitas)
txtChicken_Fajitas.grid(row=8, column=1)
txtPork_Tenderloin =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Pork_Tenderloin)
txtPork_Tenderloin.grid(row=9, column=1)
txtBaked_Salmons =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Baked_Salmons)
txtBaked_Salmons.grid(row=10, column=1)
txtNewari_Khaja_Set =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Newari_Khaja_Set)
txtNewari_Khaja_Set.grid(row=11, column=1)
txtGreek_Yogurt =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Greek_Yogurt)
txtGreek_Yogurt.grid(row=12, column=1)
txtPasta_Fried =Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED,textvariable=E_Pasta_Fried)
txtPasta_Fried.grid(row=13, column=1)


#=====================================================================================================================

lblReceipt = Label(F2a,font=('arial',12,'bold'), text="Receipt:",bd=2,anchor='w')
lblReceipt.grid(row=0, column=0 ,sticky=W)
txtReceipt =Text(F2a, font=('arial',12,'bold'), bd=2, width=35,height=31,bg="black" )
txtReceipt.grid(row=1, column=0)

lblName=Label(F2aa, font=('arial',12,'bold'),text="   Name       ",bd=5,anchor='w')
lblName.grid(row=0,column=0,sticky=W)
txtName=Entry(F2aa, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Name,insertwidth=2)
txtName.grid(row=0,column=1,sticky=W)

lblTable_Number=Label(F2aa, font=('arial',12,'bold'),text="  Table Number       ",bd=5,anchor='w')
lblTable_Number.grid(row=1,column=0,sticky=W)
txtTable_Number=Entry(F2aa, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Table_Number,insertwidth=2)
txtTable_Number.grid(row=1,column=1,sticky=W)

lblAddress=Label(F2aa, font=('arial',12,'bold'),text="   Address       ",bd=5,anchor='w')
lblAddress.grid(row=2,column=0,sticky=W)
txtAddress=Entry(F2aa, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Address,insertwidth=2)
txtAddress.grid(row=2,column=1,sticky=W)

lblTax=Label(F2aa, font=('arial',12,'bold'),text="   Tax       ",bd=5,anchor='w')
lblTax.grid(row=3,column=0,sticky=W)
txtTax=Entry(F2aa, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Tax,insertwidth=2)
txtTax.grid(row=3,column=1,sticky=W)


lblCost_Of_Meals=Label(F2bb, font=('arial',12,'bold'),text="   Cost of Meals   ",bd=5,anchor='w')
lblCost_Of_Meals.grid(row=0,column=0,sticky=W)
txtCost_Of_Meals=Entry(F2bb, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Cost_Of_Meals,insertwidth=2)
txtCost_Of_Meals.grid(row=0,column=1,sticky=W)

lblCost_Of_Drinks=Label(F2bb, font=('arial',12,'bold'),text="   Cost of Drinks   ",bd=4,anchor='w')
lblCost_Of_Drinks.grid(row=1,column=0,sticky=W)
txtCost_Of_Drinks=Entry(F2bb, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Cost_Of_Drinks,insertwidth=2)
txtCost_Of_Drinks.grid(row=1,column=1,sticky=W)

lblCost_Of_Foods=Label(F2bb, font=('arial',12,'bold'),text="   Cost of Foods   ",bd=4,anchor='w')
lblCost_Of_Foods.grid(row=2,column=0,sticky=W)
txtCost_Of_Foods=Entry(F2bb, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Cost_Of_Foods,insertwidth=2)
txtCost_Of_Foods.grid(row=2,column=1,sticky=W)

lblService_Charge=Label(F2bb, font=('arial',12,'bold'),text="   Service Charge    ",bd=5,anchor='w')
lblService_Charge.grid(row=3,column=0,sticky=W)
txtService_Charge=Entry(F2bb, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Service_Charge,insertwidth=2)
txtService_Charge.grid(row=3,column=1,sticky=W)



lblVat_Paid=Label(F2cc, font=('arial',12,'bold'),text="   Vat Paid    ",bd=5,anchor='w')
lblVat_Paid.grid(row=0,column=0,sticky=W)
txtVat_Paid=Entry(F2cc, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Vat_Paid,insertwidth=2)
txtVat_Paid.grid(row=0,column=1,sticky=W)

lblDiscount=Label(F2cc, font=('arial',12,'bold'),text="   Discount       ",bd=5,anchor='w')
lblDiscount.grid(row=1,column=0,sticky=W)
txtDiscount=Entry(F2cc, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Discount,insertwidth=2)
txtDiscount.grid(row=1,column=1,sticky=W)

lblSub_Total=Label(F2cc, font=('arial',12,'bold'),text="   Sub Total     ",bd=5,anchor='w')
lblSub_Total.grid(row=2,column=0,sticky=W)
txtSub_Total=Entry(F2cc, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Sub_Total,insertwidth=2)
txtSub_Total.grid(row=2,column=1,sticky=W)

lblTotal_Cost=Label(F2cc, font=('arial',12,'bold'),text="   Total Cost    ",bd=5,anchor='w')
lblTotal_Cost.grid(row=3,column=0,sticky=W)
txtTotal_Cost=Entry(F2cc, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Total_Cost,insertwidth=2)
txtTotal_Cost.grid(row=3,column=1,sticky=W)

#========================================================================================================================
btnTotal_Cost=Button(F2b,padx=16,pady=1,bd=3,bg="black",font=('arial',12,'bold'),width=4,text="  Total  ",command=Cost_Of_Items)
btnTotal_Cost.grid(row=0,column=0)

btnReceipt=Button(F2b,padx=16,pady=1,bd=3,bg="black",font=('arial',12,'bold'),width=4,text="  Receipt   ",command=Receipt_Given)
btnReceipt.grid(row=0,column=1)

btnReset=Button(F2b,padx=16,pady=1,bd=3,bg="black",font=('arial',12,'bold'),width=4,text="  Reset   ",command=Reset)
btnReset.grid(row=0,column=2)

btnExit=Button(F2b,padx=16,pady=1,bd=3,bg="black",font=('arial',12,'bold'),width=4,text="  Exit ",command=qExit)
btnExit.grid(row=0,column=3)

#=============================================================================================================================
class Application(Frame):
   
    def __init__(self, master):
        
        Frame.__init__(self, master)
        self.entry = Entry(master, width=28, font=("Arial",25,"bold"),justify=RIGHT)
        self.entry.grid(row=0, column=0, columnspan=6, sticky="w",padx=45, pady = 45)
        self.entry.focus_set()
        self.entry.configure(state="disabled", disabledbackground="white", disabledforeground="black")
        self.create_widgets()
        self.bind_buttons(master)
        self.grid()
        
        
    def add_chr(self, char, btn=None):
    
        self.entry.configure(state="normal")
        self.flash(btn) # Flash a button correspond to keystroke
        if self.entry.get() == "Invalid Input":
            self.entry.delete(0,END)
        self.entry.insert(END, char)
        self.entry.configure(state="disabled")

    def backspace(self):
        
        self.entry.configure(state="normal")
        if self.entry.get() != "Invalid Input":
            # Clears full entry when "Invalid Input"
            text = self.entry.get()[:-1]
            self.entry.delete(0,END)
            self.entry.insert(0,text)
        else:
            self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def clear_all(self):

        self.entry.configure(state="normal")
        self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def factorial(self):

        self.entry.configure(state="normal")
        num=float(self.entry.get())
        y=math.factorial(num)
        self.entry.delete(0,END)
        self.entry.insert(0,y)

        self.entry.configure(state="disabled")

    def Sin_value(self):

        self.entry.configure(state="normal")
        sin=float(self.entry.get())
        angle=(sin*2*math.pi)/360.0
        a=math.sin(angle)
        self.entry.delete(0,END)
        self.entry.insert(0,a)
        self.entry.configure(state="disabled")


    def Cos_value(self):

        self.entry.configure(state="normal")
        cos=float(self.entry.get())
        angle=(cos*2*math.pi)/360.0
        a=math.cos(angle)
        self.entry.delete(0,END)
        self.entry.insert(0,a)
        self.entry.configure(state="disabled")

    def Tan_value(self):

        self.entry.configure(state="normal")
        tan=float(self.entry.get())
        angle=(tan*2*math.pi)/360.0
        a=math.tan(angle)
        self.entry.delete(0,END)
        self.entry.insert(0,a)
        self.entry.configure(state="disabled")


    def Log_value(self):
        
        self.entry.configure(state="normal")
        log1=float(self.entry.get())
        a=math.log(log1,10)
        self.entry.delete(0,END)
        self.entry.insert(0,a)
        self.entry.configure(state="disabled")

    def Ln_value(self):
        
        self.entry.configure(state="normal")
        ln1=float(self.entry.get())
        a=math.log(ln1)
        self.entry.delete(0,END)
        self.entry.insert(0,a)
        self.entry.configure(state="disabled")

    def Cube_Root(self):
        self.entry.configure(state="normal")
        cube=float(self.entry.get())
        z=math.pow(cube,1/3)
        self.entry.delete(0,END)
        self.entry.insert(0,z)
        self.entry.configure(state="disabled")

    def Inverse(self):
        self.entry.configure(state="normal")
        inverse=float(self.entry.get())
        x=1/inverse
        self.entry.delete(0,END)
        self.entry.insert(0,x)
        self.entry.configure(state="disabled")
        
        
    def qExit(self):
        self.qExit1=tkinter.messagebox.askquestion("Quit System","Do you want to quit?")
        if self.qExit1 == "yes":
            root.destroy()

    def calculate(self):
        
        self.entry.configure(state="normal")
        e = self.entry.get()
        e = e.replace("√","sqr")
        e = e.replace("×", "*")
        e = e.replace("²", "**2")
        e = e.replace("^", "**")
        e = e.replace("÷", "/")
        e = e.replace("^3", "**3")
        e = e.replace("e","*2.7182818285")
        e = e.replace("π","*3.1415926536")
    

        try:
            ans = eval(e)
        except Exception as ex:
            self.entry.delete(0,END)
            self.entry.insert(0, "Invalid Input")
        else:
            self.entry.delete(0,END)
            if len(str(ans)) > 20: # Alleviates problem of large numbers
                self.entry.insert(0, '{:.10e}'.format(ans))
            else:
                self.entry.insert(0, ans)
        self.entry.configure(state="disabled")

    def flash(self,btn):

        if btn != None:
            btn.config(bg="yellow")
            if btn == self.c_bttn:
                self.backspace()
                self.master.after(100, lambda: btn.config(bg="blue"))
            elif btn == self.eq_bttn:
                self.master.after(100, lambda: btn.config(bg="blue"))
                self.calculate()
            elif btn == self.ac_bttn:
                self.clear_all()
                self.master.after(100, lambda: btn.config(bg="blue"))
            else:
                self.master.after(100, lambda: btn.config(bg="blue"))
        else:
            pass

    def bind_buttons(self, master):
        
        master.bind("<Return>", lambda event, btn=self.eq_bttn: self.flash(btn))
        master.bind("<BackSpace>", lambda event, btn=self.c_bttn: self.flash(btn))
        master.bind("9", lambda event, char="9", btn=self.nine_bttn: self.add_chr(char, btn))
        master.bind("8", lambda event, char="8", btn=self.eight_bttn: self.add_chr(char, btn))
        master.bind("7", lambda event, char="7", btn=self.seven_bttn: self.add_chr(char, btn))
        master.bind("6", lambda event, char="6", btn=self.six_bttn: self.add_chr(char, btn))
        master.bind("5", lambda event, char="5", btn=self.five_bttn: self.add_chr(char, btn))
        master.bind("4", lambda event, char="4", btn=self.four_bttn: self.add_chr(char, btn))
        master.bind("3", lambda event, char="3", btn=self.three_bttn: self.add_chr(char, btn))
        master.bind("2", lambda event, char="2", btn=self.two_bttn: self.add_chr(char, btn))
        master.bind("1", lambda event, char="1", btn=self.one_bttn: self.add_chr(char, btn))
        master.bind("0", lambda event, char="0", btn=self.zero_bttn: self.add_chr(char, btn))
        master.bind("*", lambda event, char="×", btn=self.mult_bttn: self.add_chr(char, btn))
        master.bind("/", lambda event, char="÷", btn=self.div_bttn: self.add_chr(char, btn))
        master.bind("^", lambda event, char="^", btn=self.sqr_bttn: self.add_chr(char, btn))
        master.bind("%", lambda event, char="%", btn=self.mod_bttn: self.add_chr(char, btn))
        master.bind(".", lambda event, char=".", btn=self.dec_bttn: self.add_chr(char, btn))
        master.bind("-", lambda event, char="-", btn=self.sub_bttn: self.add_chr(char, btn))
        master.bind("+", lambda event, char="+", btn=self.add_bttn: self.add_chr(char, btn))
        master.bind("(", lambda event, char="(", btn=self.lpar_bttn: self.add_chr(char, btn))
        master.bind(")", lambda event, char=")", btn=self.rpar_bttn: self.add_chr(char, btn))
        master.bind("AC",lambda event, char="AC",btn=self.ac_bttn: self.flash(btn), self.clear_all)
        master.bind("Log",lambda event, char="Log", btn=self.Log_bttn: self.add_chr(char, btn))
        master.bind("Ln", lambda event, char="Ln", btn=self.Ln_bttn: self.add_chr(char, btn))
        master.bind("Pi", lambda event, char="Pi", btn=self.Pi_bttn: self.add_chr(char, btn))
        master.bind("Exp", lambda event, char="Exp", btn=self.Exp_bttn: self.add_chr(char, btn))
        master.bind("^3", lambda event, char="^3", btn=self.Cube_bttn: self.add_chr(char, btn))
        
        
    def create_widgets(self):

        self.seven_bttn = Button(self, text="7", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.seven_bttn["command"]=lambda: self.add_chr(7)
        self.seven_bttn.grid(row=2, column=0)

        self.eight_bttn = Button(self, text="8", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.eight_bttn["command"]=lambda: self.add_chr(8)
        self.eight_bttn.grid(row=2, column=1)

        self.nine_bttn = Button(self, text="9", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.nine_bttn["command"]=lambda: self.add_chr(9)
        self.nine_bttn.grid(row=2, column=2)

        self.ac_bttn = Button(self, text='AC', width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.ac_bttn["command"]=lambda: self.clear_all()
        self.ac_bttn.grid(row=2, column=3)

        self.c_bttn = Button(self, text='←', width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.c_bttn["command"]=lambda: self.backspace()
        self.c_bttn.grid(row=2, column=4 )

        self.Off_bttn = Button(self, text='OFF', width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Off_bttn["command"]=lambda: self.qExit()
        self.Off_bttn.grid(row=2, column=5 )

        self.four_bttn = Button(self, text="4", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.four_bttn["command"]=lambda: self.add_chr(4)
        self.four_bttn.grid(row=3, column=0)

        self.five_bttn = Button(self, text="5", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.five_bttn["command"]=lambda: self.add_chr(5)
        self.five_bttn.grid(row=3, column=1)

        self.six_bttn = Button(self, text="6", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.six_bttn["command"]=lambda: self.add_chr(6)
        self.six_bttn.grid(row=3, column=2)

        self.div_bttn = Button(self, text="÷", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.div_bttn["command"]=lambda: self.add_chr('/')
        self.div_bttn.grid(row=3, column=3)

        self.lpar_bttn = Button(self, text="(", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.lpar_bttn["command"]=lambda: self.add_chr('(')
        self.lpar_bttn.grid(row=3, column=4)

        self.rpar_bttn = Button(self, text=")", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.rpar_bttn["command"]=lambda: self.add_chr(')')
        self.rpar_bttn.grid(row=3, column=5)

        self.one_bttn = Button(self, text="1", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.one_bttn["command"]=lambda: self.add_chr(1)
        self.one_bttn.grid(row=4, column=0)

        self.two_bttn = Button(self, text="2", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.two_bttn["command"]=lambda: self.add_chr(2)
        self.two_bttn.grid(row=4, column=1)

        self.three_bttn = Button(self, text="3", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.three_bttn["command"]=lambda: self.add_chr(3)
        self.three_bttn.grid(row=4, column=2)

        self.sub_bttn = Button(self, text="-", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.sub_bttn["command"]=lambda: self.add_chr('-')
        self.sub_bttn.grid(row=4, column=3)

        self.mult_bttn = Button(self, text="×", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.mult_bttn["command"]=lambda: self.add_chr('×')
        self.mult_bttn.grid(row=4, column=4)

        self.sqr_bttn = Button(self, text="^", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.sqr_bttn["command"]=lambda: self.add_chr('^')
        self.sqr_bttn.grid(row=4, column=5)

        self.dec_bttn = Button(self, text=".", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.dec_bttn["command"]=lambda: self.add_chr('.')
        self.dec_bttn.grid(row=5, column=0)

        self.zero_bttn = Button(self, text="0", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.zero_bttn["command"]=lambda: self.add_chr(0)
        self.zero_bttn.grid(row=5, column=1)

        self.add_bttn = Button(self, text="+", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.add_bttn["command"]=lambda: self.add_chr('+')
        self.add_bttn.grid(row=5, column=2)

        self.mod_bttn = Button(self, text="%", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.mod_bttn["command"]=lambda: self.add_chr('%')
        self.mod_bttn.grid(row=5, column=3)

        self.sq_bttn = Button(self, text="√x", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.sq_bttn["command"]=lambda: self.add_chr('√(')
        self.sq_bttn.grid(row=5, column=4)

        self.root_Cube_bttn = Button(self, text=" ³√x", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.root_Cube_bttn["command"]=lambda: self.Cube_Root()
        self.root_Cube_bttn.grid(row=5, column=5)

        self.Log_bttn = Button(self, text="Log", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Log_bttn["command"]=lambda: self.Log_value()
        self.Log_bttn.grid(row=6, column=0)

        self.Ln_bttn = Button(self, text="ln", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Ln_bttn["command"]=lambda: self.Ln_value()
        self.Ln_bttn.grid(row=6, column=1)

        self.Inverse_bttn = Button(self, text="1/x", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Inverse_bttn["command"]=lambda: self.Inverse()
        self.Inverse_bttn.grid(row=6, column=2)

        self.Pi_bttn = Button(self, text="π", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Pi_bttn["command"]=lambda: self.add_chr('π')
        self.Pi_bttn.grid(row=6, column=3)

        self.Exp_bttn = Button(self, text="Exp", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Exp_bttn["command"]=lambda: self.add_chr('e')
        self.Exp_bttn.grid(row=6, column=4)

        self.Cube_bttn = Button(self, text="x^3", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Cube_bttn["command"]=lambda: self.add_chr('^3')
        self.Cube_bttn.grid(row=6, column=5)

        self.Sin_bttn = Button(self, text="Sin", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Sin_bttn["command"]=lambda: self.Sin_value()
        self.Sin_bttn.grid(row=7, column=0)

        self.Cos_bttn = Button(self, text="Cos", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Cos_bttn["command"]=lambda: self.Cos_value()
        self.Cos_bttn.grid(row=7, column=1)

        self.Tan_bttn = Button(self, text="Tan", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Tan_bttn["command"]=lambda: self.Tan_value()
        self.Tan_bttn.grid(row=7, column=2)

        self.Factorial_bttn = Button(self, text="!", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Factorial_bttn["command"]=lambda: self.factorial()
        self.Factorial_bttn.grid(row=7, column=3)
        
        self.eq_bttn = Button(self, text="=", width=20, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.eq_bttn["command"]=lambda: self.calculate()
        self.eq_bttn.grid(row=7, column=4, columnspan=2)



        

root = Tk()
root.geometry()
app = Application(root)
root.mainloop()



root.mainloop()


