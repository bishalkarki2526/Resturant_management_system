#!/usr/bin/python3

import time
from tkinter import *
from math import sqrt as sqr
import tkinter.messagebox
import math



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

        self.seven_bttn = Button(self, text="7", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="orange")
        self.seven_bttn["command"]=lambda: self.add_chr(7)
        self.seven_bttn.grid(row=2, column=0)

        self.eight_bttn = Button(self, text="8", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="orange")
        self.eight_bttn["command"]=lambda: self.add_chr(8)
        self.eight_bttn.grid(row=2, column=1)

        self.nine_bttn = Button(self, text="9", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="orange")
        self.nine_bttn["command"]=lambda: self.add_chr(9)
        self.nine_bttn.grid(row=2, column=2)

        self.ac_bttn = Button(self, text='AC', width=9, height=3,padx=6, pady=6,bd=2,fg="yellow",font=("arial",12,"bold"),bg="green")
        self.ac_bttn["command"]=lambda: self.clear_all()
        self.ac_bttn.grid(row=2, column=3)

        self.c_bttn = Button(self, text='←', width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="violet")
        self.c_bttn["command"]=lambda: self.backspace()
        self.c_bttn.grid(row=2, column=4 )

        self.Off_bttn = Button(self, text='OFF', width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="red")
        self.Off_bttn["command"]=lambda: self.qExit()
        self.Off_bttn.grid(row=2, column=5 )

        self.four_bttn = Button(self, text="4", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="orange")
        self.four_bttn["command"]=lambda: self.add_chr(4)
        self.four_bttn.grid(row=3, column=0)

        self.five_bttn = Button(self, text="5", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="orange")
        self.five_bttn["command"]=lambda: self.add_chr(5)
        self.five_bttn.grid(row=3, column=1)

        self.six_bttn = Button(self, text="6", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="orange")
        self.six_bttn["command"]=lambda: self.add_chr(6)
        self.six_bttn.grid(row=3, column=2)

        self.div_bttn = Button(self, text="÷", width=9, height=3,padx=6, pady=6,bd=2,fg="yellow",font=("arial",12,"bold"),bg="green")
        self.div_bttn["command"]=lambda: self.add_chr('/')
        self.div_bttn.grid(row=3, column=3)

        self.lpar_bttn = Button(self, text="(", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="violet")
        self.lpar_bttn["command"]=lambda: self.add_chr('(')
        self.lpar_bttn.grid(row=3, column=4)

        self.rpar_bttn = Button(self, text=")", width=9, height=3,padx=6, pady=6,bd=2,fg="purple",font=("arial",12,"bold"),bg="cyan")
        self.rpar_bttn["command"]=lambda: self.add_chr(')')
        self.rpar_bttn.grid(row=3, column=5)

        self.one_bttn = Button(self, text="1", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="orange")
        self.one_bttn["command"]=lambda: self.add_chr(1)
        self.one_bttn.grid(row=4, column=0)

        self.two_bttn = Button(self, text="2", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="orange")
        self.two_bttn["command"]=lambda: self.add_chr(2)
        self.two_bttn.grid(row=4, column=1)

        self.three_bttn = Button(self, text="3", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="orange")
        self.three_bttn["command"]=lambda: self.add_chr(3)
        self.three_bttn.grid(row=4, column=2)

        self.sub_bttn = Button(self, text="-", width=9, height=3,padx=6, pady=6,bd=2,fg="yellow",font=("arial",12,"bold"),bg="green")
        self.sub_bttn["command"]=lambda: self.add_chr('-')
        self.sub_bttn.grid(row=4, column=3)

        self.mult_bttn = Button(self, text="×", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="violet")
        self.mult_bttn["command"]=lambda: self.add_chr('×')
        self.mult_bttn.grid(row=4, column=4)

        self.sqr_bttn = Button(self, text="^", width=9, height=3,padx=6, pady=6,bd=2,fg="purple",font=("arial",12,"bold"),bg="cyan")
        self.sqr_bttn["command"]=lambda: self.add_chr('^')
        self.sqr_bttn.grid(row=4, column=5)

        self.dec_bttn = Button(self, text=".", width=9, height=3,padx=6, pady=6,bd=2,fg="yellow",font=("arial",12,"bold"),bg="green")
        self.dec_bttn["command"]=lambda: self.add_chr('.')
        self.dec_bttn.grid(row=5, column=0)

        self.zero_bttn = Button(self, text="0", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="orange")
        self.zero_bttn["command"]=lambda: self.add_chr(0)
        self.zero_bttn.grid(row=5, column=1)

        self.add_bttn = Button(self, text="+", width=9, height=3,padx=6, pady=6,bd=2,fg="yellow",font=("arial",12,"bold"),bg="green")
        self.add_bttn["command"]=lambda: self.add_chr('+')
        self.add_bttn.grid(row=5, column=2)

        self.mod_bttn = Button(self, text="%", width=9, height=3,padx=6, pady=6,bd=2,fg="yellow",font=("arial",12,"bold"),bg="green")
        self.mod_bttn["command"]=lambda: self.add_chr('%')
        self.mod_bttn.grid(row=5, column=3)

        self.sq_bttn = Button(self, text="√x", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="violet")
        self.sq_bttn["command"]=lambda: self.add_chr('√(')
        self.sq_bttn.grid(row=5, column=4)

        self.root_Cube_bttn = Button(self, text=" ³√x", width=9, height=3,padx=6, pady=6,bd=2,fg="purple",font=("arial",12,"bold"),bg="cyan")
        self.root_Cube_bttn["command"]=lambda: self.Cube_Root()
        self.root_Cube_bttn.grid(row=5, column=5)

        self.Log_bttn = Button(self, text="Log", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="violet")
        self.Log_bttn["command"]=lambda: self.Log_value()
        self.Log_bttn.grid(row=6, column=0)

        self.Ln_bttn = Button(self, text="ln", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="violet")
        self.Ln_bttn["command"]=lambda: self.Ln_value()
        self.Ln_bttn.grid(row=6, column=1)

        self.Inverse_bttn = Button(self, text="1/x", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="violet")
        self.Inverse_bttn["command"]=lambda: self.Inverse()
        self.Inverse_bttn.grid(row=6, column=2)

        self.Pi_bttn = Button(self, text="π", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="violet")
        self.Pi_bttn["command"]=lambda: self.add_chr('π')
        self.Pi_bttn.grid(row=6, column=3)

        self.Exp_bttn = Button(self, text="Exp", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="violet")
        self.Exp_bttn["command"]=lambda: self.add_chr('e')
        self.Exp_bttn.grid(row=6, column=4)

        self.Cube_bttn = Button(self, text="x^3", width=9, height=3,padx=6, pady=6,bd=2,fg="purple",font=("arial",12,"bold"),bg="cyan")
        self.Cube_bttn["command"]=lambda: self.add_chr('^3')
        self.Cube_bttn.grid(row=6, column=5)

        self.Sin_bttn = Button(self, text="Sin", width=9, height=3,padx=6, pady=6,bd=2,fg="purple",font=("arial",12,"bold"),bg="cyan")
        self.Sin_bttn["command"]=lambda: self.Sin_value()
        self.Sin_bttn.grid(row=7, column=0)

        self.Cos_bttn = Button(self, text="Cos", width=9, height=3,padx=6, pady=6,bd=2,fg="purple",font=("arial",12,"bold"),bg="cyan")
        self.Cos_bttn["command"]=lambda: self.Cos_value()
        self.Cos_bttn.grid(row=7, column=1)

        self.Tan_bttn = Button(self, text="Tan", width=9, height=3,padx=6, pady=6,bd=2,fg="purple",font=("arial",12,"bold"),bg="cyan")
        self.Tan_bttn["command"]=lambda: self.Tan_value()
        self.Tan_bttn.grid(row=7, column=2)

        self.Factorial_bttn = Button(self, text="!", width=9, height=3,padx=6, pady=6,bd=2,fg="purple",font=("arial",12,"bold"),bg="cyan")
        self.Factorial_bttn["command"]=lambda: self.factorial()
        self.Factorial_bttn.grid(row=7, column=3)
        
        self.eq_bttn = Button(self, text="=", width=20, height=3,padx=6, pady=6,bd=2,fg="black",font=("arial",12,"bold"),bg="blue")
        self.eq_bttn["command"]=lambda: self.calculate()
        self.eq_bttn.grid(row=7, column=4, columnspan=2)



        

root = Tk()
root.geometry()
app = Application(root)
root.mainloop()

   
