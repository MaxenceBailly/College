#imports
from tkinter import *
import time

#variables
score = 0
question = 1

#création fenêtre
fen = Tk()
fen.config(bg="#999")
fen.title("True or False ?")

#boutton jouer
def jouer():
    Bjouer.place_forget()
    Lnbquestion.pack()
    Lscore.pack()
    Lreponse.pack()
    Lquestion.pack()
    Bvrai.pack()
    Bfaux.pack()
    question1()

#parcours
def parcour():
    global question
    question += 1
    Lnbquestion.config(text=(f"Question : \n{question}"))
    if question == 2:
        question2()
    elif question == 3:
        question3()
    elif question == 4:
        question4()
    elif question == 5:
        question5()
    elif question == 6:
        question6()
    elif question == 7:
        question7()

#réponse
def pasbon():
    Lreponse.config(text="Mauvaise réponse", bg="Red")
    fen.after(3000, parcour)
    Bvrai.config(command=0)
    Bfaux.config(command=0)
    
def bon():
    global score
    Lreponse.config(text="Bonne réponse", bg="Blue")
    score += 1
    Lscore.config(text=(f"Votre score :\n{score}"))
    fen.after(3000, parcour)
    Bvrai.config(command=0)
    Bfaux.config(command=0)

#questions    
def question1():
    Lquestion.config(text="La première guerre mondiale c'est passé entre 1939 et 1945.")
    Bvrai.config(command=pasbon)
    Bfaux.config(command=bon)

def question2():
    Lquestion.config(text="L'Amérique a été découverte par Christoffe Colomb en 1392.")
    Lreponse.config(text="", bg="#999")
    Bvrai.config(command=pasbon)
    Bfaux.config(command=bon)

def question3():
    Lquestion.config(text="La dengue est une maladie transmise par la piqûre d'une tique.")
    Lreponse.config(text="", bg="#999")
    Bvrai.config(command=pasbon)
    Bfaux.config(command=bon)

def question4():
    Lquestion.config(text="Un éthylabélophile collectionne les étiquettes de bouteilles d'alcool.")
    Lreponse.config(text="", bg="#999")
    Bvrai.config(command=bon)
    Bfaux.config(command=pasbon)

def question5():
    Lquestion.config(text="Elvis Presley interprète l'un de ses plus grands succès Love Me Tender dans le film de même nom.")
    Lreponse.config(text="", bg="#999")
    Bvrai.config(command=bon)
    Bfaux.config(command=pasbon)

def question6():
    Lquestion.config(text="Le premier être vivant à aller dans l'Espace est la chienne Laïka, envoyée par les Américains.")
    Lreponse.config(text="", bg="#999")
    Bvrai.config(command=pasbon)
    Bfaux.config(command=bon)

def question7():
    Lquestion.config(text="La constellation d'Orion est aussi appelée Le Chasseur.")
    Lreponse.config(text="", bg="#999")
    Bvrai.config(command=bon)
    Bfaux.config(command=pasbon)

def question8():
    Lquestion.config(text="")
    Lreponse.config(text="", bg="#999")
    Bvrai.config(command=bon)
    Bfaux.config(command=pasbon)

def question9():
    Lquestion.config(text="")
    Lreponse.config(text="", bg="#999")
    Bvrai.config(command=bon)
    Bfaux.config(command=pasbon)

def question10():
    Lquestion.config(text="")
    Lreponse.config(text="", bg="#999")
    Bvrai.config(command=bon)
    Bfaux.config(command=pasbon)

#création widgets
Bjouer = Button(fen, text="Jouer", font=16, command=jouer)
Lnbquestion = Label(fen, text=(f"Question : \n{question}"), font=16)
Lreponse = Label(fen, font=16, bg="#999")
Lquestion = Label(fen,text="", font=16)
Lscore = Label(fen, text=(f"Votre score :\n{score}"), font=16)
Bfaux = Button(fen, text="Faux", font=16)
Bvrai = Button(fen, text="Vrai", font=16)

Bjouer.place(relx=0, rely=0)

fen.mainloop()