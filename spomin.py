from turtle import *
import time
import random

barve = ["tomato", "peru", "olive", "yellow", "seagreen", "maroon", "navy", "skyblue"]
barveVSpominu = {}
imaBarvo = False
karte = {}
izbranaKarta1 = None
izbranaSt1 = None
izbranaKarta2 = None
izbranaSt2 = None
stIzbranih = 0
stIger=0
rekord = 0


pravilnoUganjeni = 0
narobeUganjeni = 0

isSleep = False

i = 0
j = 0

screen = Screen()
screen.setup(900, 700)
screen.colormode(255)

#vsi napisi
naslov = Turtle()
naslov.speed(0)
naslov.penup()
naslov.hideturtle()
naslov.goto(0, 275)

loading = Turtle()
loading.speed(0)
loading.pu()
loading.ht()
loading.goto(0, 240)


napisLevo = Turtle()
napisLevo.speed(0)
napisLevo.pu()
napisLevo.ht()
napisLevo.goto(-360, 100)

napisDesno = Turtle()
napisDesno.speed(0)
napisDesno.pu()
napisDesno.ht()
napisDesno.goto(360, 100)

napisZmaga = Turtle()
napisZmaga.speed(0)
napisZmaga.pu()
napisZmaga.ht()
napisZmaga.goto(0, 0)

napisSpodaj = Turtle()
napisSpodaj.speed(0)
napisSpodaj.pu()
napisSpodaj.ht()

igrajZnova = Turtle()
igrajZnova.penup()
igrajZnova.speed(0)
igrajZnova.shape("triangle")
igrajZnova.color("green")
igrajZnova.shapesize(3)
igrajZnova.goto(0, -300)
igrajZnova.hideturtle()

napisIgrajZnova = Turtle()
napisIgrajZnova.penup()
napisIgrajZnova.speed(0)
napisIgrajZnova.goto(0, -250)
napisIgrajZnova.hideturtle()

rekordNapis = Turtle()
rekordNapis.hideturtle()
rekordNapis.penup()
rekordNapis.speed(0)
rekordNapis.goto(-445,200)
rekordNapis.write("Rekord: nedefiniran", font=("Arial", 14, "bold"))


novRekordNapis = Turtle()
novRekordNapis.hideturtle()
novRekordNapis.penup()
novRekordNapis.speed(0)
novRekordNapis.goto(0,-175)



#inicializacija originalne karte
kartaOriginal = Turtle()
kartaOriginal.speed(10)
kartaOriginal.penup()
kartaOriginal.goto(-187.5, -187.5)
kartaOriginal.shapesize(5)
kartaOriginal.shape("circle")
kartaOriginal.hideturtle()


def spomin(x, y):
    global stIzbranih 
    global pravilnoUganjeni 
    global narobeUganjeni
    global stIger
    global rekord
    if stIger==1:
        rekordNapis.write("Rekord: " + str(narobeUganjeni), font=("Ariel", 14, "bold"))
        rekord = narobeUganjeni
    elif stIger>1:
        rekordNapis.clear()
        if rekord>narobeUganjeni:
            rekordNapis.write("Rekord: " + str(narobeUganjeni), font=("Ariel", 14, "bold"))
            rekord = narobeUganjeni
        rekordNapis.write("Rekord: " + str(rekord), font=("Arial",14, "bold"))
    stIger+=1
    stIzbranih = 0
    pravilnoUganjeni = 0
    narobeUganjeni = 0
    igrajZnova.hideturtle()
    napisSpodaj.clear()
    napisSpodaj.goto(0, -300)
    napisSpodaj.write("Napačni ugibi: 0", align="center", font=('Helvetica', 16, "bold"))
    napisZmaga.clear()
    novRekordNapis.clear()
    napisIgrajZnova.clear()
    naslov.write("IGRA SPOMIN", align="center", font=("Verdana", 30, "bold"))
    loading.write("mešanje...", align="center", font=('Helvetica', 12))
    
    #ustvarjanje in zapisovanje klonov
    for i in range(0,4):
        kartaOriginal.goto(-187.5, -187.5+i*125)
        for j in range(0,4):
            karte[j + (4*i)] = {"clone": kartaOriginal.clone(), "barva":None, "odkrita": False}
            karte[j + (4*i)]["clone"].showturtle()
            kartaOriginal.forward(125)


    
#nastavljanje barv
    for i in range(0,8):
        barveVSpominu[i]={"barva": barve[i], "st": 0}
         

#vsaka karta dobi eno barvo, po dve imata isto
    for i in range(0, 16):
        imaBarvo = False
        while not imaBarvo:
            randInt = random.randint(0,7)
            if barveVSpominu[randInt]["st"]<2:
                karte[i]["barva"]=barveVSpominu[randInt]["barva"]
                barveVSpominu[randInt]["st"]+=1;
                imaBarvo = True
        karte[i]["clone"].fillcolor(str(karte[i]["barva"]))
    loading.clear()

    time.sleep(2)

    for i in range(0, 16):
        karte[15-i]["clone"].fillcolor("black")
    for i in range (0,16):
        karte[i]["clone"].onclick(identifyCard)

#nastavljanje onclick lastnosti
def kartaIzbrana(st):
    global stIzbranih
    global izbranaKarta1
    global izbranaKarta2
    global izbranaSt1
    global izbranaSt2
    global pravilnoUganjeni
    global isSleep
    global narobeUganjeni
    global rekord
    global stIger
    karte[st]["clone"].fillcolor(str(karte[st]["barva"]))
    karte[st]["odkrita"]=True
    if (stIzbranih==1):
        izbranaKarta1=karte[st]["barva"]
        izbranaSt1=st
    elif (stIzbranih==2):
        izbranaKarta2=karte[st]["barva"]
        izbranaSt2=st
    if stIzbranih == 2:
        if (izbranaKarta1==izbranaKarta2):
            napisDesno.write("BRAVO", align="center", font=('Helvetica', 16, "bold"))
            time.sleep(1)
            napisDesno.clear()
            pravilnoUganjeni+=1
        else:
            narobeUganjeni+=1
            napisLevo.write("Ni pravilno", align="center", font=('Helvetica', 16, "bold"))
            napisSpodaj.clear()
            napisSpodaj.write("Napačni ugibi: " + str(narobeUganjeni), align="center", font=('Helvetica', 16, "bold"))
            time.sleep(1)
            napisLevo.clear()
            karte[izbranaSt1]["clone"].fillcolor("black")
            karte[izbranaSt2]["clone"].fillcolor("black")
            karte[izbranaSt1]["odkrita"]=False
            karte[izbranaSt2]["odkrita"]=False
        stIzbranih=0
        isSleep=False
        if pravilnoUganjeni==8:
            for i in range(0, 16):
                karte[i]["clone"].hideturtle()
            napisZmaga.write("Bravo, dober spomin imaš", align="center", font=('Arial', 32, "bold"))
            naslov.clear()
            napisSpodaj.clear()
            napisSpodaj.goto(0, -100)
            napisSpodaj.write("Napačni ugibi: " + str(narobeUganjeni), align="center", font=('Helvetica', 20, "bold"))
            igrajZnova.showturtle()
            napisIgrajZnova.write("Igraj znova:", align="center", font=('Arial', 17, 'bold'))
            rekordNapis.clear()
            if narobeUganjeni<rekord and stIger>0:
                novRekordNapis.write("Postavil si nov rekord!", align="center", font=("Arial", 20, "bold"))
            
            
                
def identifyCard(x, y):
    global stIzbranih
    global isSleep
    global karte
    if not isSleep:
        g = 0;
        d = 0;
        if x >= -237.5 and x<=-137.5:
            d=0
        elif x >= -112.5 and x<= -12.5:
            d=1
        elif x>=12.5 and x<=112.5:
            d=2
        elif x >=137.5 and x<=237.5:
            d=3
        if y >= -237.5 and y<=-137.5:
            g=0
        elif y >= -112.5 and y<= -12.5:
            g=1
        elif y>=12.5 and y<=112.5:
            g=2
        elif y >=137.5 and y<=237.5:
            g=3
        if not karte[d+(4*g)]["odkrita"]:
            stIzbranih+=1
            if stIzbranih == 2:
                isSleep=True
            kartaIzbrana(d+(4*g))

igrajZnova.onclick(spomin)

spomin(0, 0)
        


done()

