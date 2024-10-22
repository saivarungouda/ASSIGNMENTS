'''DATE:- 22\10\2024'''
'''1. Write a python to determine grade of the student
A: score>=90
B:score>=80 and score<90
C:score>=70 and score<80
D:score>=60 and score<70
E:score<60'''

from tkinter import*
from tkinter import messagebox



window=Tk()
window.title("Checking Grade")
window.config(bg="#FF00FF")
window.geometry("350x400")
def grade():
    score=float(e1.get())
    if (score>90):
        messagebox.showinfo("result","A")
    elif (score>=80 and score<90):
        messagebox.showinfo("result","B")
    elif (score>=70 and score<80):
        messagebox.showinfo("result","C")
    elif (score>=60 and score<70):
        messagebox.showinfo("result","D")
    else:
        messagebox.showinfo("result","E")

l1=Label(window,text="ENTER THE SCORE:")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
b1=Button(window,text="Grade",command=grade)
b1.grid(row=2,column=0)

window.mainloop()

'''2. write a python program to calculate a discount for a customer  based on  the purchased amount
using tkinter
conditions:
purchase>=$500: 20% discount
purchase>=200 and <$500: 10% discount
purchase<$200: NO Discount
 '''

from tkinter import*
from tkinter import messagebox



window=Tk()
window.title("discount")
window.config(bg="#FF00FF")
window.geometry("350x400")

def purchase_discount():
    purchase_amount=int(e1.get())
    if (purchase_amount>=500):
        messagebox.showinfo("Discount","you will get 20% discount")
        total_ammnt=purchase_amount*0.2

    elif (purchase_amount>=200 and purchase_amount<500):
        messagebox.showinfo("Discount","you will get 10% discount")
        total_ammnt = purchase_amount * 0.1
    else:
        messagebox.showinfo("no discount","sorry you will not get discount")
        total_ammnt=purchase_amount

l1=Label(window,text="ENTER THE AMOUNT:")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
b1=Button(window,text="Discount",command=purchase_discount)
b1.grid(row=2,column=0)

window.mainloop()
