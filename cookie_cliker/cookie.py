from tkinter import *
import pickle
import time

pricesell = 1
money = 0
parclick = 1
nbclick = 0

#fenêtre
fen = Tk()

#fen config
fen.geometry("1000x500")
fen.title("CookieClick")
fen.iconbitmap("College\cookie_cliker\cookie.ico")
fen.resizable(width=True, height=True)
fen.config(bg="#840")

#fonctions
def click():
    global parclick
    global nbclick
    nbclick += parclick
    Lcookies.config(text=(f"Number of cookies :\n{nbclick}"))

def play():
    Ltitle.place(relx=0.448, rely=0.01)
    Lcookies.place(relx=0.422, rely=0.2)
    Lmoney.place(relx=0.46, rely=0.5)
    Lmultiplier.place(relx=0, rely=0)
    Bclick.place(relx=0.458, rely=0.35)
    Bsell.place(relx=0.463, rely=0.6)
    Bquit.place(relx=0.47, rely=0.9)
    Bback.place(relx=0.10, rely=0.9)
    Bmultiplier.place(relx=0.8, rely=0.01)
    Bplay.place_forget()
    Bcredit.place_forget()
    
def credit():
    Lcredit.place(relx=0.255, rely=0.5)
    Bback.place(relx=0.10, rely=0.9)
    Bquit.place(relx=0.47, rely=0.9)
    Bplay.place_forget()
    Bcredit.place_forget()

def back():
    Bplay.place(relx=0.468, rely=0.5)
    Bcredit.place(relx=0.459, rely=0.6)
    Bquit.place(relx=0.47, rely=0.7)
    Bback.place_forget()
    Bclick.place_forget()
    Bsell.place_forget()
    Bmultiplier.place_forget()
    Lcredit.place_forget()
    Ltitle.place_forget()
    Lcookies.place_forget()
    Lmoney.place_forget()

def sell():
    global money
    global nbclick
    money += nbclick * pricesell
    nbclick -= nbclick
    Lcookies.config(text=(f"Number of cookies :\n{nbclick}"))
    Lmoney.config(text=(f"Money :\n{money}$"))

def multiplier():
    Bback.place_forget()
    Bclick.place_forget()
    Bsell.place_forget()
    Ltitle.place_forget()
    Lcookies.place_forget()
    Lmoney.place_forget()
    Bcancel.place(relx=0.454, rely=0.7)
    Lmoney.place(relx=0.8, rely=0.9)
    Bmultiplier1.place(relx=0.39, rely=0.1)
    Bmultiplier10.place(relx=0.378, rely=0.2)

def cancel():
    Ltitle.place(relx=0.448, rely=0.01)
    Lcookies.place(relx=0.422, rely=0.2)
    Lmoney.place(relx=0.46, rely=0.5)
    Bclick.place(relx=0.458, rely=0.35)
    Bsell.place(relx=0.463, rely=0.6)
    Bquit.place(relx=0.47, rely=0.9)
    Bback.place(relx=0.10, rely=0.9)
    Bplay.place_forget()
    Bcredit.place_forget()
    Bmultiplier.place(relx=0.8, rely=0.01)
    Bcancel.place_forget()
    Bmultiplier1.place_forget()
    Bmultiplier10.place_forget()

def multiplier1():
    global money
    global parclick
    if money < 49 :
        parclick += 1
        money -= 50
    Lmultiplier.config(text=(f"Multiplier :\n{parclick}"))
    Lmoney.config(text=(f"Money :\n{money}$"))

def multiplier10():
    global money
    global parclick
    if money < 499 :
        parclick += 10
        money -= 500
    Lmultiplier.config(text=(f"Multiplier :\n{parclick}"))
    Lmoney.config(text=(f"Money :\n{money}$"))

#widgets
Ltitle = Label(fen, text="CookieClick", font=("Arial",16), bg="#840")
Lcookies = Label(fen, text=(f"Number of cookies :\n{nbclick}"), font=("Arial",16), bg="#840")
Lmoney = Label(fen, text=(f"Money :\n{money}$"), font=("Arial",16), bg="#840")
Lcredit = Label(fen, text="This game was created by Maxence Bailly\n in a Python option for present him to a CEA people", font=("Arial",16))
Lmultiplier = Label(fen, text=(f"Multiplier :\n{parclick}"), font=("Arial",16), bg="#840")
Bclick = Button(fen, text="CLICK", font=("Arial",16), command=click)
Bplay = Button(fen, text="PLAY", font=("Arial",16), command=play)
Bquit = Button(fen, text="QUIT", font=("Arial",16), command=quit)
Bcredit = Button(fen, text="CREDIT", font=("Arial",16), command=credit)
Bback = Button(fen, text="<BACK", font=("Arial",16), command=back)
Bsell = Button(fen, text="SELL", font=("Arial",16), command=sell)
Bmultiplier = Button(fen, text="MULTIPLIER", font=("Arial",16), command=multiplier)
Bcancel = Button(fen, text="CANCEL", font=("Arial",16), command=cancel)
Bmultiplier1 = Button(fen, text="MULTIPLIER + 1 for 50$", font=("Arial",16), command=multiplier1)
Bmultiplier10 = Button(fen, text="MULTIPLIER + 10 for 500$", font=("Arial",16), command=multiplier10)

#pack widget
Bplay.place(relx=0.468, rely=0.5)
Bcredit.place(relx=0.459, rely=0.6)
Bquit.place(relx=0.47, rely=0.7)

#----
fen.mainloop()