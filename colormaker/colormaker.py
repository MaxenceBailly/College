from tkinter import *

#variables
rouge = 0
bleu = 0
vert = 0

#fenêtre
fen = Tk()
fen.config(bg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
fen.title("ColorMaker")

#rouge
def rougeplus():
    global rouge
    if rouge < 9 :
        rouge += 1
        fen.config(bg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
        code.config(text=(f"code couleur :\n#{int(rouge)}{int(bleu)}{int(vert)}"), fg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
    else:
        pass

def rougemoins():
    global rouge
    if rouge > 0 :
        rouge -= 1
        fen.config(bg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
        code.config(text=(f"code couleur :\n#{int(rouge)}{int(bleu)}{int(vert)}"), fg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
    else:
        pass

#bleu
def bleuplus():
    global bleu
    if bleu < 9 :
        bleu += 1
        fen.config(bg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
        code.config(text=(f"code couleur :\n#{int(rouge)}{int(bleu)}{int(vert)}"), fg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
    else:
        pass

def bleumoins():
    global bleu
    if bleu > 0 :
        bleu -= 1
        fen.config(bg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
        code.config(text=(f"code couleur :\n#{int(rouge)}{int(bleu)}{int(vert)}"), fg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
    else:
        pass

#vert
def vertplus():
    global vert
    if vert < 9 :
        vert += 1
        fen.config(bg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
        code.config(text=(f"code couleur :\n#{int(rouge)}{int(bleu)}{int(vert)}"), fg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
    else:
        pass

def vertmoins():
    global vert
    if vert > 0 :
        vert -= 1
        fen.config(bg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
        code.config(text=(f"code couleur :\n#{int(rouge)}{int(bleu)}{int(vert)}"), fg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
    else:
        pass

#widgets
code = Label(fen, text=(f"code couleur :\n#{int(rouge)}{int(bleu)}{int(vert)}"), font=16, bg="#000", fg=(f"#{int(rouge)}{int(bleu)}{int(vert)}"))
Rplus = Button(fen, text="+", command=rougeplus, bg="Red", font=16)
Rmoins = Button(fen, text="-", command=rougemoins, bg="Red", font=16)
Bplus = Button(fen, text="+", command=bleuplus, bg="Blue", font=16)
Bmoins = Button(fen, text="-", command=bleumoins, bg="Blue", font=16)
Vplus = Button(fen, text="+", command=vertplus, bg="Green", font=16)
Vmoins = Button(fen, text="-", command=vertmoins, bg="Green", font=16)

#place widgets
code.pack()
Rplus.place(relx=0.4, rely=0.3)
Rmoins.place(relx=0.4, rely=0.4)
Bplus.place(relx=0.5, rely=0.3)
Bmoins.place(relx=0.5, rely=0.4)
Vplus.place(relx=0.6, rely=0.3)
Vmoins.place(relx=0.6, rely=0.4)

#boucle fen
fen.mainloop()