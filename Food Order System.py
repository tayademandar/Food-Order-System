from tkinter import*
import time
import datetime

root = Tk()
################################################
#             Window Resolution                #
################################################
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}')
root.configure(background='#f7E7CE')
################################################
#         Window Title                         #
################################################
root.title("restaurant")


################################################
#                FRAMES                        #
################################################
Tops = Frame(root, width=1350, height=70, bd=12, relief="raise")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=("arial", 50, 'bold'), text="             Restaurant          ")
lblTitle.grid(row=0, column=0)

################################################
#                Date and Time                 #
################################################
localtime = time.asctime(time.localtime(time.time()))
lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, bd=10, anchor='w')
lblInfo.grid(row=1, column=0)
#################################################

BottomMainFrame = Frame(root, width=1300, height=800, bd=12, relief=SUNKEN)
BottomMainFrame.place(x=100,y=280)

f1left = Frame(BottomMainFrame, width=433, height=550, bd=4, relief='raise')
f1left.pack(side=LEFT)

f1middle= Frame(BottomMainFrame,width=433,height=550,bd=4,relief='raise')
f1middle.pack(side=LEFT)

f1right=Frame(BottomMainFrame,width=433,height=550,bd=4,relief='raise')
f1right.pack(side=LEFT)

################################################
#                Variables                      #
################################################


################################################
#     Left Frame(Starters/MainCourse)          #
################################################
varPannerTikka = StringVar()
varCheeseBalls = StringVar()
varAlooTikki = StringVar()
varCaesarSalad = StringVar()
varPannerMasala = StringVar()
varButterChicken = StringVar()
varBhendiFry = StringVar()
varPaneerMussalum = StringVar()

varPannerTikka.set(0)
varCheeseBalls.set(0)
varAlooTikki.set(0)
varCaesarSalad.set(0)
varPannerMasala.set(0)
varButterChicken.set(0)
varBhendiFry.set(0)
varPaneerMussalum.set(0)

################################################
#      Middle Frame(Breads/Desert)            #
################################################
varChapati = StringVar()
varGarlicNaan = StringVar()
varTandooriRoti = StringVar()
varButterNaan = StringVar()
varChocoLavaCake = StringVar()
varGulabJamun = StringVar()
varRasmalai = StringVar()
varJalebi = StringVar()

varChapati.set(0)
varGarlicNaan.set(0)
varTandooriRoti.set(0)
varButterNaan.set(0)
varChocoLavaCake.set(0)
varGulabJamun.set(0)
varRasmalai.set(0)
varJalebi.set(0)

################################################
#                  Total                       #
################################################
def total():
    if (varPannerTikka.get() == ""):
        cp1 = 0
    else:
        cp1 = float(varPannerTikka.get())

    if (varCheeseBalls.get() == ""):
        cp2 = 0
    else:
        cp2 = float(varCheeseBalls.get())

    if (varAlooTikki.get() == ""):
        cp3 = 0
    else:
        cp3 = float(varAlooTikki.get())

    if (varCaesarSalad.get() == ""):
        cp4 = 0
    else:
        cp4 = float(varCaesarSalad.get())

    if (varPannerMasala.get() == ""):
        cp5 = 0
    else:
        cp5 = float(varPannerMasala.get())

    if (varButterChicken.get() == ""):
        cp6 = 0
    else:
        cp6 = float(varButterChicken.get())

    if (varBhendiFry.get() == ""):
        cp7 = 0
    else:
        cp7 = float(varBhendiFry.get())

    if (varPaneerMussalum.get() == ""):
        cp8 = 0
    else:
        cp8 = float(varPaneerMussalum.get())

    if (varChapati.get() == ""):
        cp9 = 0
    else:
        cp9 = float(varChapati.get())

    if (varGarlicNaan.get() == ""):
        cp10 = 0
    else:
        cp10 = float(varGarlicNaan.get())

    if (varTandooriRoti.get() == ""):
        cp11 = 0
    else:
        cp11 = float(varTandooriRoti.get())

    if (varButterNaan.get() == ""):
        cp12 = 0
    else:
        cp12 = float(varButterNaan.get())

    if (varChocoLavaCake.get() == ""):
        cp13 = 0
    else:
        cp13 = float(varChocoLavaCake.get())

    if (varGulabJamun.get() == ""):
        cp14 = 0
    else:
        cp14 = float(varGulabJamun.get())

    if (varRasmalai.get() == ""):
        cp15 = 0
    else:
        cp15 = float(varRasmalai.get())

    if (varJalebi.get() == ""):
        cp16 = 0
    else:
        cp16 = float(varJalebi.get())



    cop1 = cp1 * 150
    cop2 = cp2 * 120
    cop3 = cp3 * 100
    cop4 = cp4 * 170

    cop5 = cp5 * 220
    cop6 = cp6 * 350
    cop7 = cp7 * 180
    cop8 = cp8 * 250

    cop9 = cp9 * 12
    cop10 = cp10 * 30
    cop11 = cp11 * 20
    cop12 = cp12 * 25

    cop13 = cp13 * 100
    cop14 = cp14 * 40
    cop15 = cp15 * 55
    cop16 = cp16 * 45



    subtotal = (cop1 +cop2 + cop3 + cop4 + cop5  +cop6 + cop7 + cop8 + cop9 + cop10 + cop11 + cop12 +cop13 +cop14+ cop15 +cop16)

    sercharge = ((cop1 + cop2 + cop3 + cop4 + cop5 +cop6 + cop7 + cop8 + cop9 + cop10 + cop11 + cop12 +cop13 +cop14+ cop15 +cop16) / 99)

    Total = (subtotal)+(sercharge)

    varsubtotal.set(subtotal)
    varTotal.set(Total)
    varsercharhge.set(sercharge)
varsubtotal = StringVar()
varTotal = StringVar()
varsercharhge = StringVar()


################################################
#                   Reset                      #
################################################
def reset():
    varPannerTikka.set(0)
    varCheeseBalls.set(0)
    varAlooTikki.set(0)
    varCaesarSalad.set(0)
    varPannerMasala.set(0)
    varButterChicken.set(0)
    varBhendiFry.set(0)
    varPaneerMussalum.set(0)
    varChapati.set(0)
    varGarlicNaan.set(0)
    varTandooriRoti.set(0)
    varButterNaan.set(0)
    varChocoLavaCake.set(0)
    varGulabJamun.set(0)
    varRasmalai.set(0)
    varJalebi.set(0)
    varsercharhge.set(0)
    varTotal.set(0)
    varsubtotal.set(0)


################################################
#                 Exit                         #
################################################
def qexit():
    root.destroy()
################################################
#              Food items entry                #
################################################
starterscat= Label(f1left,text='        Starters',font=('arial',30,'bold'))
starterscat.grid()
lblPaneerTikka= Label(f1left, font=('arial', 16, 'bold'),text="Paneer Tikka....(Rs.150)",bd=5,anchor="w")
lblPaneerTikka.grid(row=1, column=0)
txtPaneerTikka=Entry(f1left, font=('arial',16,'bold'),textvariable=varPannerTikka,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtPaneerTikka.grid(row=1,column=1)

lblCheeseBalls= Label(f1left, font=('arial', 16, 'bold'),text="CheeseBalls....(Rs.120)",bd=5,anchor="w")
lblCheeseBalls.grid(row=2, column=0)
txtCheeseBalls=Entry(f1left, font=('arial',16,'bold'),textvariable=varCheeseBalls,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtCheeseBalls.grid(row=2,column=1)

lblAlooTikki= Label(f1left, font=('arial', 16, 'bold'),text="AlooTikki....(Rs.100)    ",bd=5,anchor="w")
lblAlooTikki.grid(row=3, column=0)
txtAlooTikki=Entry(f1left, font=('arial',16,'bold'),textvariable=varAlooTikki,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtAlooTikki.grid(row=3,column=1)

lblCaesarSalad= Label(f1left, font=('arial', 16, 'bold'),text="Caesar Salad....(Rs.170)    ",bd=5,anchor="w")
lblCaesarSalad.grid(row=4, column=0)
txtCaesarSalad=Entry(f1left, font=('arial',16,'bold'),textvariable=varCaesarSalad,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtCaesarSalad.grid(row=4,column=1)

maincoursecat= Label(f1left,text='       Main Course',font=('arial',30,'bold'))
maincoursecat.grid()

lblPaneerMasala= Label(f1left, font=('arial', 16, 'bold'),text="Paneer Masala....(Rs.220)",bd=5,anchor="w")
lblPaneerMasala.grid(row=6, column=0)
txtPaneerMasala=Entry(f1left, font=('arial',16,'bold'),textvariable=varPannerMasala,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtPaneerMasala.grid(row=6,column=1)

lblButterChicken= Label(f1left, font=('arial', 16, 'bold'),text="ButterChicken....(Rs.350)",bd=5,anchor="w")
lblButterChicken.grid(row=7, column=0)
txtButterChicken=Entry(f1left, font=('arial',16,'bold'),textvariable=varButterChicken,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtButterChicken.grid(row=7,column=1)

lblBhendiFry= Label(f1left, font=('arial', 16, 'bold'),text="Bhendi Fry....(Rs.180)",bd=5,anchor="w")
lblBhendiFry.grid(row=8, column=0)
txtBhendiFry=Entry(f1left, font=('arial',16,'bold'),textvariable=varBhendiFry,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtBhendiFry.grid(row=8,column=1)

lblPaneerMussalum= Label(f1left, font=('arial', 16, 'bold'),text="Paneer Mussalum....(Rs.250)",bd=5,anchor="w")
lblPaneerMussalum.grid(row=9, column=0)
txtPaneerMussalum=Entry(f1left, font=('arial',16,'bold'),textvariable=varPaneerMussalum,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtPaneerMussalum.grid(row=9,column=1)

Breadscat= Label(f1middle,text='     Breads',font=('arial',30,'bold'))
Breadscat.grid()

lblChapati= Label(f1middle, font=('arial', 16, 'bold'),text="Chapati....(Rs.12)",bd=5,anchor="w")
lblChapati.grid(row=1, column=0)
txtChapati=Entry(f1middle, font=('arial',16,'bold'),textvariable=varChapati,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtChapati.grid(row=1,column=1)

lblGarlicNaan= Label(f1middle, font=('arial', 16, 'bold'),text="Garlic Naan....(Rs.30)",bd=5,anchor="w")
lblGarlicNaan.grid(row=2, column=0)
txtGarlicNaan=Entry(f1middle, font=('arial',16,'bold'),textvariable=varGarlicNaan,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtGarlicNaan.grid(row=2,column=1)

lblTandooriRoti= Label(f1middle, font=('arial', 16, 'bold'),text="Tandoori Roti....(Rs.20)    ",bd=5,anchor="w")
lblTandooriRoti.grid(row=3, column=0)
txtTandooriRoti=Entry(f1middle, font=('arial',16,'bold'),textvariable=varTandooriRoti,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtTandooriRoti.grid(row=3,column=1)

lblButterNaan= Label(f1middle, font=('arial', 16, 'bold'),text="ButterNaan....(Rs.25)    ",bd=5,anchor="w")
lblButterNaan.grid(row=4, column=0)
txtButterNaan=Entry(f1middle, font=('arial',16,'bold'),textvariable=varButterNaan,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtButterNaan.grid(row=4,column=1)

desertcat= Label(f1middle,text='     Desert',font=('arial',30,'bold'))
desertcat.grid()

lblChocoLavaCake= Label(f1middle, font=('arial', 16, 'bold'),text="Choco Lava Cake....(Rs.100)",bd=5,anchor="w")
lblChocoLavaCake.grid(row=6, column=0)
txtChocoLavaCake=Entry(f1middle, font=('arial',16,'bold'),textvariable=varChocoLavaCake,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtChocoLavaCake.grid(row=6,column=1)

lblGulabJamun= Label(f1middle, font=('arial', 16, 'bold'),text="Gulab Jamun....(Rs.40)",bd=5,anchor="w")
lblGulabJamun.grid(row=7, column=0)
txtGulabJamun=Entry(f1middle, font=('arial',16,'bold'),textvariable=varGulabJamun,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtGulabJamun.grid(row=7,column=1)

lblRasmalai= Label(f1middle, font=('arial', 16, 'bold'),text="Rasmalai....(Rs.50)",bd=5,anchor="w")
lblRasmalai.grid(row=8, column=0)
txtRasmalai=Entry(f1middle, font=('arial',16,'bold'),textvariable=varRasmalai,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtRasmalai.grid(row=8,column=1)

lblJalebi= Label(f1middle, font=('arial', 16, 'bold'),text="Jalebi....(Rs.45)",bd=5,anchor="w")
lblJalebi.grid(row=9, column=0)
txtJalebi=Entry(f1middle, font=('arial',16,'bold'),textvariable=varJalebi,bd=5,insertwidth=5,bg="white",justify='right',width=4)
txtJalebi.grid(row=9,column=1)


################################################
#         Total/Subtotal/surcharge             #
################################################
totalcat= Label(f1right,text='           Bill',font=('arial',30,'bold'))
totalcat.grid()

lblsubtotal= Label(f1right, font=('arial', 16, 'bold'),text="Subtotal",bd=5,anchor="w")
lblsubtotal.grid(row=1, column=0)
txtsubtotal=Entry(f1right, font=('arial',16,'bold'),textvariable=varsubtotal,bd=5,insertwidth=5,bg="white",justify='right',width=12)
txtsubtotal.grid(row=1,column=1)

lblsercharge= Label(f1right, font=('arial', 16, 'bold'),text="Ser Charge",bd=5,anchor="w")
lblsercharge.grid(row=2, column=0)
txtsercharge=Entry(f1right, font=('arial',16,'bold'),textvariable=varsercharhge,bd=5,insertwidth=5,bg="white",justify='right',width=12)
txtsercharge.grid(row=2,column=1)

lblTotal= Label(f1right, font=('arial', 16, 'bold'),text="Total",bd=5,anchor="w")
lblTotal.grid(row=3, column=0)
txtTotal=Entry(f1right, font=('arial',16,'bold'),textvariable=varTotal,bd=5,insertwidth=5,bg="white",justify='right',width=12)
txtTotal.grid(row=3,column=1)

################################################
#         Total/Reset/Exit Buttons             #
################################################
btnTotal=Button(f1right,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=total).grid(row=4,column=0)
btnReset=Button(f1right,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="aquamarine",command=reset).grid(row=5,column=0)
btnExit=Button(f1right,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="red",command=qexit).grid(row=6,column=0)
root.mainloop()



