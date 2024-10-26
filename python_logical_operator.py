# NAME :- G SAI VARUN
# DATE :-23\10\2024
# PYTHON LOGICAL OPERATORS ASSIGNMENTS :

# 1. write python program using tkinter to to check speed of the car and give warning and then penality if the speed exceeded.
# business conditions :
# speed_limit=90 kmph
# speed <= speed_limit:no penalty
# speed <=speed_limit+20 : warning
# 3 speed>speed_limit+20 : penalty 2000

from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Checking Speed Limit")
window.config(bg="red")
window.geometry("350x400")

def speed_check():
    speed=int(e1.get())
    speed_limit = 90
    if (speed<=speed_limit):
        messagebox.showinfo("maximum speed","your maintaining minimum speed")
    elif (speed<=speed_limit+20):
        messagebox.showinfo("maximum speed","your are crossing the maximum speed limit slow down the speed of your vechial other wise you will get penalty")
    elif (speed>=speed_limit+20):
        messagebox.showinfo("maximum speed","you have crossed the maximum speed limit so you got the penalty of 2000")
    else:
        messagebox.showinfo("maximum speed","you are not mainating minimum speed")

l1 = Label(window, text="ENTER THE SPEED:")
l1.grid(row=0, column=0)
e1 = Entry(window)
e1.grid(row=0, column=1)
b1 = Button(window, text="Enter", command=speed_check)
b1.grid(row=2, column=0)

window.mainloop()

#Assignment2:
#Write a python program using tkinter for withdraw money from the ATM
#business conditions:
#balance=10000
#daily_limit=20000
#i. withdrawal amount <=balance
#ii. withdrawl notes should be multiples of 100
#iii. daily limit should not be exceeded

from tkinter import *
from tkinter import messagebox

window= Tk()
window.title("WELCOME TO SBI ATM")
window.config(bg="green")
window.geometry("350x400")


def Atm_operation():
    balance = 10000
    withdrawamnt = int(e1.get())
    if withdrawamnt <= balance and withdrawamnt % 100 == 0:
        messagebox.showinfo("withdrawl", "take your money in 100rs notes")
    elif withdrawamnt <= balance and withdrawamnt % 100 !=0:
        messagebox.showinfo("error check","dinomination of rs100/- is able to withdraw")
    elif withdrawamnt > balance:
        messagebox.showinfo("daily limit", "your daily limit have been completed")
    else:
        messagebox.showinfo("balance", "dinomination of rs100/- is able to withdraw")
        total_bal = withdrawamnt - balance
2500

def check_balance():
    balance = 10000
    withdrawamnt = int(e1.get())
    if withdrawamnt <= balance and withdrawamnt % 100 == 0:
        messagebox.showinfo("withdrawl",balance-withdrawamnt)
    elif withdrawamnt <= balance and withdrawamnt % 100 !=0:
        messagebox.showinfo("error check","dinomination of rs100/- is able to withdraw")
    elif withdrawamnt > balance:
        messagebox.showinfo("daily limit", "you have entered exceeding the maximum available balance ")
    else:
        messagebox.showinfo("balance", "denomination of rs100/- is able to withdraw")



l1 = Label(window, text="Enter the withdraw amnt")
l1.grid(row=0, column=0)
e1 = Entry(window)
e1.grid(row=0, column=1)

b1 = Button(window, text="withdraw", command=Atm_operation)
b1.grid(row=2, column=1)
b2 = Button(window, text="Balance", command=check_balance)
b2.grid(row=3, column=1)

window.mainloop()


# Assignment 3:
# write a python program using tkinter for checking customer is eligible for discount or not
# business condition:
# inputs: purchase_amt
# membership= True or False
# purchase_amt>5000 or membership==True: 20% discount avail


from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("DISCOUNT INFO")
window.config(bg="yellow")
window.geometry("350x400")

def check_discount():
    purchase_amount=int(e1.get())
    membership=True
    if purchase_amount>5000 and membership==True:
        messagebox.showinfo("discount info","congrats, you will get 20% discount on your purchase")
    else:
        messagebox.showinfo("discount info","sorry, we are not providing any discount on your purchase")

l1=Label(window,text="Total Purchase Amount")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)

b1=Button(window,text="Discount",command=check_discount)
b1.grid(row=2,column=1)



window.mainloop()
