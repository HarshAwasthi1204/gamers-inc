#Importing Required Modules
import tkinter as tek
import threading
import imageio
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from winsound import *
import time
from functools import partial
from tkinter import messagebox
import ast
import re
import random
import datetime

#Asking for the user's mysql password in order to connect to it
mysqlpass=input("Please Enter your MySQL Password: ")

#Intro
Window0 = tek.Tk()
#Page dimensions
Window0.title("Gamers' Inc.")
MonitorHeight0 = Window0.winfo_screenheight()
MonitorWidth0 = Window0.winfo_screenwidth()

if MonitorHeight0 == 768 and MonitorWidth0 == 1366:
    Geometry0 = Window0.geometry("%sx%s" % (MonitorWidth0,MonitorHeight0))
    Window0.state('zoomed')
    Window0.attributes('-fullscreen',True)
else:
    Geometry0 = Window0.geometry("1366x768")
    Window0.attributes('-fullscreen',False)

Window0.configure(bg = "Sky Blue")

BGimgpath02 = "Media/ProjectBG2.jpg"
BGimg02 = Image.open(BGimgpath02)
if MonitorHeight0 == 768 and MonitorWidth0 == 1366:
    BGimg02 = BGimg02.resize((MonitorWidth0,MonitorHeight0))
else:
    BGimg02 = BGimg02.resize((1366,768))
BGimg02 = ImageTk.PhotoImage(BGimg02)

#Disclaimer Canvas
if MonitorHeight0 == 768 and MonitorWidth0 == 1366:
    canvas0=tek.Canvas(Window0,width="%s" % (MonitorWidth0),height="%s" % (MonitorHeight0))
else:
    canvas0=tek.Canvas(Window0,width="1366",height="768")
canvas0.pack(side=tek.TOP,fill=tek.BOTH,expand=True)

#Disclaimer Text
img0=canvas0.create_image(0,0,anchor="nw",image=BGimg02)
text0=canvas0.create_text(327,15,anchor="nw",text="DISCLAIMER",font=('Battleground',160,'bold'),fill='Yellow')
text1=canvas0.create_text(348,215,anchor="nw",text="WAZZUP TESTER?",font=('Battleground',100,'bold'),fill='Blue')
disctext="""THIS APPLICATION HAS BEEN MADE FOR A SCHOOL PROJECT
ONLY. ALL THE IMAGES,VIDEOS AND AUDIOS USED BELONG
TO THEIR RESPECTIVE OWNERS. YOU CAN'T ACTUALLY BUY
OR PLAY ANY OF THE GAMES. I DON'T HOLD ANY RIGHTS
FOR SELLING OR PROMOTING THE TITLES. ALL THE RIGHTS
TO THE SOURCE CODE BELONG TO ME. HAPPY TESTING!
I'D APPRECIATE IF YOU'D REPORT ANY BUGS YOU FIND..."""
text2=canvas0.create_text(675,500,anchor=tek.CENTER,text=disctext,font=('Comic Sans MS',25,'bold'),fill='#8B0000',justify=tek.CENTER)
disccredits="CREDITS : HARSH AWASTHI"
text3=canvas0.create_text(670,720,text=disccredits,font=('Apple And Pear',25,'bold'),fill='Gold')
Window0.attributes("-alpha",0.0)
def fade_in():
    alpha = Window0.attributes("-alpha")
    if alpha < 1.0:
        alpha += 0.05
        Window0.attributes("-alpha", alpha)
        Window0.after(100, fade_in)
def fade_away():
    alpha = Window0.attributes("-alpha")
    if alpha > 0:
        alpha -= 0.1
        Window0.attributes("-alpha", alpha)
        Window0.after(100, fade_away)
    else:
        Window0.destroy()
fade_in()
Window0.after(10000,fade_away)
Window0.mainloop()

#Connecting to & working with MySQL
import mysql.connector as sql
try:
    conn=sql.connect(host="localhost",user="root",passwd=mysqlpass)
except:
    messagebox.showerror("ERROR!","INVALID MySQL PASSWORD!!")

#Creating Database
cursor=conn.cursor()
cursor.execute("CREATE database IF NOT EXISTS Project_Gamers_Inc")
conn.commit()
conn.close()

#Creating Accounts table
conn=sql.connect(host="localhost", user="root",passwd=mysqlpass,database="Project_Gamers_Inc")
cursor=conn.cursor()
cursor.execute ("CREATE table IF NOT EXISTS Accounts ( Acct_ID int primary key , Full_Name varchar(50) , Age int, Gender varchar(7), Date_Of_Birth date, Email_ID varchar(30), Username varchar(50), Password varchar(50), Location varchar(20), Balance numeric, Status varchar(50), Profile_Picture  varchar(1000), Date_Time_Joined datetime)")
#Initial data for demonstration
cursor.execute("SHOW TABLES LIKE 'Accounts'")
data0=cursor.fetchall()
count0= cursor.rowcount
cursor.execute("SELECT * FROM Accounts")
data1=cursor.fetchall()
count1=cursor.rowcount


initial_data_query="INSERT INTO Accounts(Acct_ID,Full_Name,Age,Gender,Date_Of_Birth,Email_ID,Username,Password,Location,Balance,Status,Profile_Picture,Date_Time_Joined) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
if count0 == 1 and count1 == 0:
    dt01 = datetime.datetime(2020,12,9,12,34,48)
    dt1 = dt01.strftime('%Y-%m-%d %H:%M:%S')
    dt02 = datetime.datetime(2020,12,10,16,44,12)
    dt2 = dt02.strftime('%Y-%m-%d %H:%M:%S')
    dt03 = datetime.datetime(2020,12,12,22,54,22)
    dt3 = dt03.strftime('%Y-%m-%d %H:%M:%S')
    dt04 = datetime.datetime(2020,12,26,2,10,55)
    dt4 = dt04.strftime('%Y-%m-%d %H:%M:%S')
    initial_data=[(1, 'Hank Stark', 17, 'Male', '2003-04-12', 'hankstark1204@gmail.com', 'HankStark1204','code&chill1204','India',10000,"In this era of CAPTCHAs, prove you're humane!","Media/images (9).jpg",dt1),
                  (2, 'Tony Williamson', 16, 'Male', '2004-07-05', 'tony2004@gmail.com', 'TonyW24','ilovegaming2004','USA',3000,"Plannin' a Video Game Party Night, Wanna join??","Media/images (8).jpg",dt2),
                  (3, 'Anne Dorrance', 17, 'Female', '2003-05-15', 'anned15@gmail.com', 'AnneDorr15','gameon?15','Australia',5000,"Be the reason someone smiles today!","Media/images.jpg",dt3),
                  (4, 'Caroline Starr', 16, 'Female', '2004-10-22', 'carols2204@gmail.com', 'CarolStarr2204','gamingislife22','Germany',4000,"Gamer 4 Life!","Media/image.jpg",dt4)]
    cursor.executemany(initial_data_query,initial_data)


conn.commit()
cursor=conn.cursor()
#Pre-Owned Games for existing users
pog1=str([{'Assassins Creed:@Valhalla':'Media/acvposter.jpg'},
         {'Cyberpunk 2077':'Media/cybpposter.jpg'},
         {'Halo: Infinite':'Media/hiposter.jpg'},
         {'Marvels Avengers':'Media/masposter.jpg'},
         {'Among Us':'Media/auposter.jpg'},
         {'Call Of Duty :@Back Ops Cold War':'Media/codbocwposter.jpg'},
         {'Horizon : Zero Dawn':'Media/hzdposter.jpg'},
         {'The Amazing@Spider-Man':'Media/tasmposter.jpg'},
         {'The Amazing@Spider-Man 2':'Media/tasm2poster.png'},
         {'Minecraft':'Media/mcposter.jpg'},
         {'Fall Guys':'Media/fgposter.jpg'},
         {'Rocket League':'Media/rlposter.jpg'},
         {'Call Of Duty:@Modern Warfare':'Media/codmwposter.jpg'},
         {'CONTROL':'Media/cntrlposter.jpg'},
         {'World War Z':'Media/wwzposter.jpg'},
         {'Assassins Creed:@Directors Cut':'Media/ac1poster.jpg'},
         {'Assassins Creed 2':'Media/ac2poster.jpg'},
         {'Assassins Creed:@Brotherhood':'Media/acbhposter.jpg'},
         {'Assassins Creed:@Revelations':'Media/acrvsposter.jpg'},
         {'Assassins Creed 3':'Media/ac3poster.jpg'},
         {'Assassins Creed 4:@Black Flag':'Media/ac4bfposter.jpg'},
         {'Assassins Creed:@Rogue':'Media/acrgposter.jpg'},
         {'Assassins Creed:@Unity':'Media/acuposter.jpg'},
         {'Assassins Creed:@Syndicate':'Media/acsposter.jpg'},
         {'Assassins Creed:@Origins':'Media/acorposter.jpg'},
         {'Assassins Creed:@Odyssey':'Media/acodposter.jpg'},
         {'Batman:@Arkham Asylum':'Media/baaposter.jpg'},
         {'Batman:@Arkham City':'Media/bacposter.jpg'},
         {'Batman:@Arkham Origins':'Media/baoposter.jpg'},
         {'Batman:@Arkham Knight':'Media/bakposter.jpg'},
         {'Dishonored':'Media/dhd1poster.png'},
         {'Dishonored 2':'Media/dhd2poster.jpg'},
         {'Dishonored: Death@Of The Outsider':'Media/dhddotoposter.jpg'},
         {'Resident Evil 7':'Media/re7poster.jpg'},
         {'Resident Evil 2@Remake':'Media/re2rposter.jpg'},
         {'Resident Evil 3@Remake':'Media/re3rposter.jpg'},
         {'Borderlands: Game@Of The Year':'Media/brdrl1poster.jpg'},
         {'Borderlands 2: Game@Of The Year':'Media/brdrl2poster.png'},
         {'Borderlands:@The Pre-Sequel':'Media/brdrltpsposter.jpg'},
         {'Borderlands 3':'Media/brdrl3poster.jpg'},
         {'Watch_Dogs':'Media/wd1poster.jpg'},
         {'Watch_Dogs 2':'Media/wd2poster.jpg'},
         {'Watch Dogs:@Legion':'Media/wdlposter.jpg'},
         {'Spider-Man:@Web Of Shadows':'Media/smwosposter.jpg'},
         {'X-Men Origins:@Wolverine':'Media/xmowposter.jpg'},
         {'Alan Wake':'Media/awposter.jpg'},
         {'Alan Wakes@American Nightmare':'Media/awanposter.jpg'},
         {'Deadpool':'Media/dplposter.jpg'},
         {'Need For Speed:@Rivals':'Media/nfsrposter.jpg'},
         {'Need For Speed:@Payback':'Media/nfspposter.jpg'}])

pog2=str([{'Among Us':'Media/auposter.jpg'},
         {'Cyberpunk 2077':'Media/cybpposter.jpg'},
         {'Halo: Infinite':'Media/hiposter.jpg'},
         {'Call Of Duty :@Back Ops Cold War':'Media/codbocwposter.jpg'},
         {'Fall Guys':'Media/fgposter.jpg'},
         {'CONTROL':'Media/cntrlposter.jpg'},
         {'Rocket League':'Media/rlposter.jpg'},
         {'Horizon@Zero Dawn':'Media/hzdposter.jpg'},
         {'Minecraft':'Media/mcposter.jpg'},
         {'Call Of Duty:@Modern Warfare':'Media/codmwposter.jpg'},
         {'World War Z':'Media/wwzposter.jpg'},
         {'Dishonored':'Media/dhd1poster.png'},
         {'Dishonored 2':'Media/dhd2poster.jpg'},
         {'Dishonored: Death@Of The Outsider':'Media/dhddotoposter.jpg'},
         {'Resident Evil 7':'Media/re7poster.jpg'},
         {'Resident Evil 2@Remake':'Media/re2rposter.jpg'},
         {'Resident Evil 3@Remake':'Media/re3rposter.jpg'},
         {'Borderlands: Game@Of The Year':'Media/brdrl1poster.jpg'},
         {'Borderlands 2: Game@Of The Year':'Media/brdrl2poster.png'},
         {'Borderlands:@The Pre-Sequel':'Media/brdrltpsposter.jpg'},
         {'Borderlands 3':'Media/brdrl3poster.jpg'},
         {'Need For Speed:@Rivals':'Media/nfsrposter.jpg'},
         {'Need For Speed:@Payback':'Media/nfspposter.jpg'},
         {'Alan Wake':'Media/awposter.jpg'},
         {'Alan Wakes@American Nightmare':'Media/awanposter.jpg'}])

pog3=str([{'Cyberpunk 2077':'Media/cybpposter.jpg'},
         {'Halo: Infinite':'Media/hiposter.jpg'},
         {'Call Of Duty :@Back Ops Cold War':'Media/codbocwposter.jpg'},
         {'Fall Guys':'Media/fgposter.jpg'},
         {'CONTROL':'Media/cntrlposter.jpg'},
         {'Rocket League':'Media/rlposter.jpg'},
         {'Deadpool':'Media/dplposter.jpg'},
         {'Assassins Creed:@Directors Cut':'Media/ac1poster.jpg'},
         {'Assassins Creed 2':'Media/ac2poster.jpg'},
         {'Assassins Creed:@Brotherhood':'Media/acbhposter.jpg'},
         {'Assassins Creed:@Revelations':'Media/acrvsposter.jpg'},
         {'Assassins Creed 3':'Media/ac3poster.jpg'},
         {'Assassins Creed 4:@Black Flag':'Media/ac4bfposter.jpg'},
         {'Assassins Creed:@Rogue':'Media/acrgposter.jpg'},
         {'Assassins Creed:@Unity':'Media/acuposter.jpg'},
         {'Assassins Creed:@Syndicate':'Media/acsposter.jpg'},
         {'Assassins Creed:@Origins':'Media/acorposter.jpg'},
         {'Assassins Creed:@Odyssey':'Media/acodposter.jpg'},
         {'Watch_Dogs':'Media/wd1poster.jpg'},
         {'Watch_Dogs 2':'Media/wd2poster.jpg'},
         {'Assassins Creed:@Valhalla':'Media/acvposter.jpg'},
         {'Marvels Avengers':'Media/masposter.jpg'},
         {'Among Us':'Media/auposter.jpg'},
         {'Watch Dogs:@Legion':'Media/wdlposter.jpg'},
         {'Horizon : Zero Dawn':'Media/hzdposter.jpg'},
         {'The Amazing@Spider-Man':'Media/tasmposter.jpg'},
         {'The Amazing@Spider-Man 2':'Media/tasm2poster.png'},
         {'Minecraft':'Media/mcposter.jpg'},
         {'Call Of Duty:@Modern Warfare':'Media/codmwposter.jpg'},
         {'World War Z':'Media/wwzposter.jpg'},
         {'Dishonored':'Media/dhd1poster.png'},
         {'Dishonored 2':'Media/dhd2poster.jpg'},
         {'Dishonored: Death@Of The Outsider':'Media/dhddotoposter.jpg'},
         {'Resident Evil 7':'Media/re7poster.jpg'},
         {'Resident Evil 2@Remake':'Media/re2rposter.jpg'},
         {'Resident Evil 3@Remake':'Media/re3rposter.jpg'},
         {'Need For Speed:@Rivals':'Media/nfsrposter.jpg'},
         {'Need For Speed:@Payback':'Media/nfspposter.jpg'},
         {'Spider-Man:@Web Of Shadows':'Media/smwosposter.jpg'},
         {'X-Men Origins:@Wolverine':'Media/xmowposter.jpg'},
         {'Alan Wake':'Media/awposter.jpg'},
         {'Alan Wakes0American Nightmare':'Media/awanposter.jpg'}])

pog4=str([{'Marvels Avengers':'Media/masposter.jpg'},
         {'Among Us':'Media/auposter.jpg'},
         {'Cyberpunk 2077':'Media/cybpposter.jpg'},
         {'Halo: Infinite':'Media/hiposter.jpg'},
         {'Fall Guys':'Media/fgposter.jpg'},
         {'CONTROL':'Media/cntrlposter.jpg'},
         {'Rocket League':'Media/rlposter.jpg'},
         {'Deadpool':'Media/dplposter.jpg'},
         {'Watch_Dogs':'Media/wd1poster.jpg'},
         {'Watch_Dogs 2':'Media/wd2poster.jpg'},
         {'Watch Dogs:@Legion':'Media/wdlposter.jpg'},
         {'Horizon : Zero Dawn':'Media/hzdposter.jpg'},
         {'The Amazing@Spider-Man':'Media/tasmposter.jpg'},
         {'The Amazing@Spider-Man 2':'Media/tasm2poster.png'},
         {'Minecraft':'Media/mcposter.jpg'},
         {'Batman:@Arkham Asylum':'Media/baaposter.jpg'},
         {'Batman:@Arkham City':'Media/bacposter.jpg'},
         {'Batman:@Arkham Origins':'Media/baoposter.jpg'},
         {'Batman:@Arkham Knight':'Media/bakposter.jpg'},
         {'Resident Evil 7':'Media/re7poster.jpg'},
         {'Resident Evil 2@Remake':'Media/re2rposter.jpg'},
         {'Resident Evil 3@Remake':'Media/re3rposter.jpg'},
         {'Spider-Man:@Web Of Shadows':'Media/smwosposter.jpg'},
         {'X-Men Origins:@Wolverine':'Media/xmowposter.jpg'},
         {'Alan Wake':'Media/awposter.jpg'},
         {'Alan Wakes@American Nightmare':'Media/awanposter.jpg'}])

#Creating Inventory table
cursor.execute("CREATE table IF NOT EXISTS Inventory ( Acct_ID int PRIMARY KEY, Full_Name varchar(50), Email_ID varchar(30), Username varchar(50), Balance numeric, Games_Owned varchar(10000))")
#Initial data for demonstration
cursor.execute("SHOW TABLES LIKE 'Inventory'")
data2=cursor.fetchall()
count2= cursor.rowcount
cursor.execute("SELECT * FROM Inventory")
data3=cursor.fetchall()
count3=cursor.rowcount


initial_data_query1="INSERT INTO Inventory(Acct_ID,Full_Name,Email_ID,Username,Balance,Games_Owned) VALUES(%s,%s,%s,%s,%s,%s)"
if count2 == 1 and count3 == 0:
    initial_data1=[(1, 'Hank Stark', 'hankstark1204@gmail.com', 'HankStark1204', 10000, pog1),
                   (2, 'Tony Williamson', 'tony2004@gmail.com', 'TonyW24', 3000, pog2),
                   (3, 'Anne Dorrance', 'anned15@gmail.com', 'AnneDorr15', 5000, pog3),
                   (4, 'Caroline Starr', 'carols2204@gmail.com', 'CarolStarr2204', 4000, pog4)]
    cursor.executemany(initial_data_query1,initial_data1)

conn.commit()
cursor=conn.cursor()




#Creating Avail_Games table
cursor.execute ("CREATE table IF NOT EXISTS Avail_Games (Available varchar(10000))")
#Storing List Of Games In The Database
cursor.execute("SHOW TABLES LIKE 'Avail_Games'")
data4=cursor.fetchall()
count4= cursor.rowcount
cursor.execute("SELECT * FROM Avail_Games")
data5=cursor.fetchall()
count5=cursor.rowcount

av_g=str([{'Assassins Creed -@Valhalla':'Media/acvposter.jpg'},
         {'Cyberpunk 2077':'Media/cybpposter.jpg'},
         {'Halo - Infinite':'Media/hiposter.jpg'},
         {'Marvels Avengers':'Media/masposter.jpg'},
         {'Among Us':'Media/auposter.jpg'},
         {'Call Of Duty -@Back Ops Cold War':'Media/codbocwposter.jpg'},
         {'Horizon - Zero Dawn':'Media/hzdposter.jpg'},
         {'The Amazing@Spider-Man':'Media/tasmposter.jpg'},
         {'The Amazing@Spider-Man 2':'Media/tasm2poster.png'},
         {'Minecraft':'Media/mcposter.jpg'},
         {'Fall Guys':'Media/fgposter.jpg'},
         {'Rocket League':'Media/rlposter.jpg'},
         {'Call Of Duty -@Modern Warfare':'Media/codmwposter.jpg'},
         {'CONTROL':'Media/cntrlposter.jpg'},
         {'World War Z':'Media/wwzposter.jpg'},
         {'Assassins Creed -@Directors Cut':'Media/ac1poster.jpg'},
         {'Assassins Creed 2':'Media/ac2poster.jpg'},
         {'Assassins Creed -@Brotherhood':'Media/acbhposter.jpg'},
         {'Assassins Creed -@Revelations':'Media/acrvsposter.jpg'},
         {'Assassins Creed 3':'Media/ac3poster.jpg'},
         {'Assassins Creed 4 -@Black Flag':'Media/ac4bfposter.jpg'},
         {'Assassins Creed -@Rogue':'Media/acrgposter.jpg'},
         {'Assassins Creed -@Unity':'Media/acuposter.jpg'},
         {'Assassins Creed -@Syndicate':'Media/acsposter.jpg'},
         {'Assassins Creed -@Origins':'Media/acorposter.jpg'},
         {'Assassins Creed -@Odyssey':'Media/acodposter.jpg'},
         {'Batman -@Arkham Asylum':'Media/baaposter.jpg'},
         {'Batman -@Arkham City':'Media/bacposter.jpg'},
         {'Batman -@Arkham Origins':'Media/baoposter.jpg'},
         {'Batman -@Arkham Knight':'Media/bakposter.jpg'},
         {'Dishonored':'Media/dhd1poster.png'},
         {'Dishonored 2':'Media/dhd2poster.jpg'},
         {'Dishonored - Death@Of The Outsider':'Media/dhddotoposter.jpg'},
         {'Resident Evil 7':'Media/re7poster.jpg'},
         {'Resident Evil 2@Remake':'Media/re2rposter.jpg'},
         {'Resident Evil 3@Remake':'Media/re3rposter.jpg'},
         {'Borderlands - Game@Of The Year':'Media/brdrl1poster.jpg'},
         {'Borderlands 2 - Game@Of The Year':'Media/brdrl2poster.png'},
         {'Borderlands -@The Pre-Sequel':'Media/brdrltpsposter.jpg'},
         {'Borderlands 3':'Media/brdrl3poster.jpg'},
         {'Watch_Dogs':'Media/wd1poster.jpg'},
         {'Watch_Dogs 2':'Media/wd2poster.jpg'},
         {'Watch Dogs -@Legion':'Media/wdlposter.jpg'},
         {'Spider-Man -@Web Of Shadows':'Media/smwosposter.jpg'},
         {'X-Men Origins -@Wolverine':'Media/xmowposter.jpg'},
         {'Alan Wake':'Media/awposter.jpg'},
         {'Alan Wakes@American Nightmare':'Media/awanposter.jpg'},
         {'Deadpool':'Media/dplposter.jpg'},
         {'Need For Speed -@Rivals':'Media/nfsrposter.jpg'},
         {'Need For Speed -@Payback':'Media/nfspposter.jpg'}])


initial_data_query2 = "INSERT INTO Avail_Games (Available) Values(%s)"
if count0 == 1 and count1 == 0:
    initial_data2= [av_g]
    cursor.execute(initial_data_query2,initial_data2)

conn.commit()
cursor=conn.cursor()

#Main Content
#Page Layout
Window = tek.Tk()
Window.title("Gamers' Inc.")
MonitorHeight = Window.winfo_screenheight()
MonitorWidth = Window.winfo_screenwidth()

if MonitorHeight == 768 and MonitorWidth == 1366:
    Geometry = Window.geometry("%sx%s" % (MonitorWidth,MonitorHeight))
    Window.state('zoomed')
    Window.attributes('-fullscreen',True)
else:
    Geometry = Window.geometry("1366x768")
    Window.attributes('-fullscreen',False)

Window.configure(bg = "Sky Blue")
#Background
frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
BGimgpath = "Media/ProjectBG.jpg"
BGimg = Image.open(BGimgpath)
if MonitorHeight == 768 and MonitorWidth == 1366:
    BGimg = BGimg.resize((MonitorWidth,MonitorHeight))
else:
    BGimg = BGimg.resize((1366,768))
BGimg = ImageTk.PhotoImage(BGimg)
panel = tek.Label(frame0, image = BGimg)
panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
frame0.destroy()
panel.destroy()

#Canvas
if MonitorHeight == 768 and MonitorWidth == 1366:
    canvas=tek.Canvas(Window,width="%s" % (MonitorWidth),height="%s" % (MonitorHeight))
else:
    canvas=tek.Canvas(Window,width="1366",height="768")
canvas.pack(side=tek.TOP,fill=tek.BOTH,expand=True)
canvas.destroy()

#misc variable declaration
j=0
e=0
h=1
a=False
d=False
username=""
dobyear=None
stopvid=False
change=""
payname=""
paycost=""
payimg=""
#Status
status="Logged Out"
if MonitorHeight == 768 and MonitorWidth == 1366:
    windowfullscreen=True
else:
    windowfullscreen=False
windowzoomed=False
audioplay=False

#misc image conversions
BGimgpath = "Media/ProjectBG.jpg"
BGimg = Image.open(BGimgpath)
if MonitorHeight == 768 and MonitorWidth == 1366:
    BGimg = BGimg.resize((MonitorWidth,MonitorHeight))
else:
    BGimg = BGimg.resize((1366,768))
BGimg = ImageTk.PhotoImage(BGimg)

BGimgpath2 = "Media/ProjectBG2.jpg"
BGimg2 = Image.open(BGimgpath2)
if MonitorHeight == 768 and MonitorWidth == 1366:
    BGimg2 = BGimg2.resize((MonitorWidth,MonitorHeight))
else:
    BGimg2 = BGimg2.resize((1366,768))
BGimg2 = ImageTk.PhotoImage(BGimg2)

BGimgpath3 = "Media/ProjectBG3.jpg"
BGimg3 = Image.open(BGimgpath3)
if MonitorHeight == 768 and MonitorWidth == 1366:
    BGimg3 = BGimg3.resize((MonitorWidth,MonitorHeight))
else:
    BGimg3 = BGimg3.resize((1366,768))
BGimg3 = ImageTk.PhotoImage(BGimg3)

BGimgpath4 = "Media/ProjectBG4.png"
BGimg4 = Image.open(BGimgpath4)
if MonitorHeight == 768 and MonitorWidth == 1366:
    BGimg4 = BGimg4.resize((MonitorWidth,MonitorHeight))
else:
    BGimg4 = BGimg4.resize((1366,768))
BGimg4 = ImageTk.PhotoImage(BGimg4)

BGimgpath5 = "Media/ProjectBG5.jpg"
BGimg5 = Image.open(BGimgpath5)
if MonitorHeight == 768 and MonitorWidth == 1366:
    BGimg5 = BGimg5.resize((MonitorWidth,MonitorHeight))
else:
    BGimg5 = BGimg5.resize((1366,768))
BGimg5 = ImageTk.PhotoImage(BGimg5)

BGimgpath6 = "Media/ProjectBG6.jpg"
BGimg6 = Image.open(BGimgpath6)
if MonitorHeight == 768 and MonitorWidth == 1366:
    BGimg6 = BGimg6.resize((MonitorWidth,MonitorHeight))
else:
    BGimg6 = BGimg6.resize((1366,768))
BGimg6 = ImageTk.PhotoImage(BGimg6)

BGimgpath7 = "Media/ProjectBG7.jpg"
BGimg7 = Image.open(BGimgpath7)
if MonitorHeight == 768 and MonitorWidth == 1366:
    BGimg7 = BGimg7.resize((MonitorWidth,MonitorHeight))
else:
    BGimg7 = BGimg7.resize((1366,768))
BGimg7 = ImageTk.PhotoImage(BGimg7)

img = "Media/Creed Valhalla title1.jpg"
imgl = Image.open(img)
imgl = imgl.resize((370,120))
imgl = ImageTk.PhotoImage(imgl)
btnimg=Image.open("Media/download2.jpg")
btnimg=ImageTk.PhotoImage(btnimg)

Img = "Media/images.png"
Img1 = Image.open(Img)
Img1 = Img1.resize((50,50))
Img1 = ImageTk.PhotoImage(Img1)


def close():
    global stopvid
    if messagebox.askyesno("Quit", "Do You Really Wanna Exit The App Now?"):
        if messagebox.showinfo(title="Thanks A Bunch!", message="Thank You For Using My App! Hope You Had A Good Time! Your Feedback Is Always Welcome! Have A Great Day!"):
            stopvid=True
            PlaySound(None, SND_PURGE)
            Window.after(16,lambda:Window.destroy())

Window.protocol("WM_DELETE_WINDOW",close)

def escape(event):
    global windowfullscreen
    global windowzoomed
    if windowfullscreen == True:
        Window.attributes('-fullscreen',False)
        Window.state('zoomed')
        windowfullscreen = False
        windowzoomed = True
    elif windowzoomed == True:
        close()
    else:
        close()
Window.bind("<Escape>",escape)

def antierror0(thrd,chng):
    global stopvid
    global change
    if thrd.is_alive():
        stopvid=True
        change=chng
    else:
        stopvid=True
        change=chng
        antierror1(thrd)
def antierror1(thrd):
    global stopvid
    global change
    stopvid=True
    if thrd.is_alive():
        thrd.join()
    if change == "Home":
        Window.after(11,lambda:antierror2(thrd,show_home_page))
    elif change == "Browse":
        Window.after(11,lambda:antierror2(thrd,show_browse_pages))
    elif change == "Search":
        Window.after(11,lambda:antierror2(thrd,show_search_page))
    elif change == "NewsAndUpdates":
        Window.after(11,lambda:antierror2(thrd,show_news_and_updates_page))
    elif change == "About":
        Window.after(11,lambda:antierror2(thrd,show_about_page))
    elif change == "Login":
        Window.after(11,lambda:antierror2(thrd,show_login_page))
    elif change == "Profile":
        Window.after(11,lambda:antierror2(thrd,show_profile_page))
    elif change == "ACV":
        Window.after(11,lambda:antierror2(thrd,acv))
    elif change == "Pay":
        Window.after(11,lambda:antierrorpay1(thrd))
def antierror2(thrd,page):
    global stopvid
    stopvid=True
    if thrd.is_alive():
        thrd.join()
    Window.after(12,lambda:page())
def antierrorpay0(thrd,paytitle,payprice,payposter):
    global stopvid
    global change
    global payname
    global paycost
    global payimg
    if thrd.is_alive():
        stopvid=True
        PlaySound(None, SND_PURGE)
        change="Pay"
        payname=paytitle
        paycost=payprice
        payimg=payposter
    else:
        stopvid=True
        PlaySound(None, SND_PURGE)
        change="Pay"
        payname=paytitle
        paycost=payprice
        payimg=payposter
        antierrorpay1(thrd)
def antierrorpay1(thrd):
    global stopvid
    global payname
    global paycost
    global payimg
    stopvid=True
    PlaySound(None, SND_PURGE)
    if thrd.is_alive():
        thrd.join()
    Window.after(12,lambda:show_payment_page(payname,paycost,payimg))

def global_dp():
    global acct_dp_final
    global acct_dp_final1
    #Fetching Profile Info
    cursor.execute('SELECT * FROM Accounts WHERE Username = "%s"'% username)
    result=cursor.fetchall()
    e=1
    for column in result:
        for value in column:
            globals()["profval" + str(e)] = value
            e += 1

    acct_dp=profval12
    acct_dp_final=Image.open(acct_dp)
    acct_dp_final=acct_dp_final.resize((180,250))
    acct_dp_final=ImageTk.PhotoImage(acct_dp_final)
    acct_dp1=profval12
    acct_dp_final1=Image.open(acct_dp1)
    acct_dp_final1=acct_dp_final1.resize((50,50))
    acct_dp_final1=ImageTk.PhotoImage(acct_dp_final1)

def audioplayback():
    global audioplay
    audios = ["Media/audio1.wav","Media/audio2.wav","Media/audio3.wav","Media/audio4.wav"]
    audio=random.choice(audios)
    def play(audiop):
        return PlaySound(audiop, SND_FILENAME | SND_ASYNC | SND_LOOP)
    if audioplay == False:
        Window.after(0,lambda:play(audio))
        audioplay = True

#Welcome Page
def Welcome_Page():
    global Window
    global panel
    global canvas
    Window.update()

    #Canvas
    if MonitorHeight == 768 and MonitorWidth == 1366:
        canvas=tek.Canvas(Window,width="%s" % (MonitorWidth),height="%s" % (MonitorHeight))
    else:
        canvas=tek.Canvas(Window,width="1366",height="768")
    canvas.pack(side=tek.TOP,fill=tek.BOTH,expand=True)

    #Welcome Text
    img=canvas.create_image(0,0,anchor="nw",image=BGimg6)
    text=canvas.create_text(255,50,anchor="nw",text="WELCOME TO",font=('Battlelines',150,'bold'),fill='Gold')
    text1=canvas.create_text(255,250,anchor="nw",text="GAMERS' INC.",font=('Battlelines',150,'bold'),fill='Gold')
    text2=canvas.create_text(1350,750,anchor="se",text="v2.0",font=('Battlelines',50,'bold'),fill='Gold')

    #Get started button
    def btinte(e):
        e.widget.config(bg='Cyan',fg='Lime')
        return
    def btintl(e):
        e.widget.config(bg='Orange',fg='Blue')
        return

    startbtn=tek.Button(master=canvas,text="GET STARTED",bg="Orange",fg="Blue",font=('Avellana Pro',50,'bold'),cursor="hand2",bd=0,activebackground='Cyan',activeforeground='Yellow',command=show_home_page)
    startbtn.place(x=450,y=520,width=450,height=150)
    
    startbtn.bind("<Enter>",btinte)
    startbtn.bind("<Leave>",btintl)
    #music
    panel.after(0,audioplayback)
    Window.update()


#Home Page
def Home_Page():
    global Window
    global panel
    global stopvid
    global change
    Window.update()
    change=""
    stopvid=False
    
    #Background
    frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
    frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    panel = tek.Label(frame0, image = BGimg)
    panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    #Ft Gif
    video_name = "Media/NaiveRightFulmar5.mp4" #This is your video file path
    video = imageio.get_reader(video_name)

    def stream(label):
        global stopvid
        global change
        while True:
            for image in video.iter_data():
                frame_image = ImageTk.PhotoImage(Image.fromarray(image))
                label.config(image=frame_image)
                label.image = frame_image
                if stopvid == True:
                    break
            if stopvid == True:
                break
        Window.after(10,lambda:antierror1(thread))

    my_label = tek.Label(panel,bd=0)
    my_label.place(x=45,y=50)
    global thread
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()

    #ft highlight shortcut
    frame=tek.Frame(master=frame0,relief=tek.RIDGE, bd=0)
    frame.grid(row=0,column=0)
    Panel = tek.Label(image = imgl)
    Panel.place(x = 915, y = 80)
    pre_order=tek.Button(master=frame0,text="Pre Order Now",command=lambda:antierror0(thread,"ACV"),image=btnimg,bg="black",fg="white",height=60,width=270,cursor="hand2")
    pre_order.place(x=980,y=250)

    #Top Bar
    panel.rowconfigure(0,weight=1)
    panel.columnconfigure(0,weight=1)
    frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
    frame1.grid(row=0,column=0,sticky="new")
    label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
    label1.pack(fill=tek.X, expand=True)
    #Top bar buttons
    def btinte(e):
        e.widget.config(bg='red')
        return
    def btintl(e):
        e.widget.config(bg='Sky Blue')
        return

    Panel1 = tek.Label(frame1, image = Img1)
    Panel1.place(x = 0, y = 0)

    Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
    Name.place(x=54,y=0,width=300,height=52)

    home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',state=tek.ACTIVE)
    home.place(x=354,y=0,width=120,height=52)

    nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=lambda:antierror0(thread,"NewsAndUpdates"))
    nu.place(x=474,y=0,width=120,height=52)

    browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=lambda:antierror0(thread,"Browse"))
    browse.place(x=594,y=0,width=120,height=52)

    search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=lambda:antierror0(thread,"Search"))
    search.place(x=714,y=0,width=120,height=52)
    
    abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=lambda:antierror0(thread,"About"))
    abt.place(x=834,y=0,width=120,height=52)

    if status == "Logged In":
        login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=lambda:antierror0(thread,"Profile"))
        login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
        pp=tek.Label(frame1,image=acct_dp_final1)
        pp.place(relx=1.0,y=0,anchor="ne")
    else:
        login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=lambda:antierror0(thread,"Login"))
        login_btn.place(x=1246,y=0,width=120,height=52)

    for btn in [home,nu,browse,search,abt,login_btn]:
        btn.bind("<Enter>",btinte)
        btn.bind("<Leave>",btintl)
        
    #Ft. Games
    frame2=tek.Frame(master=frame0, width=550, height=309.38, relief=tek.RIDGE, bd=1)
    frame2.place(x=380,y=370)
    label2=tek.Label(master=frame2, bg="Green", fg="yellow",height=20,width=78)
    label2.place(x=0,y=0)

    images=['Media/ft1.jpg','Media/ft2.jpg','Media/ft3.jpg','Media/ft4.jpg','Media/ft5.jpg','Media/ft6.jpg','Media/ft7.jpg']

    i=1
    for image in images:
        FTimgpath = image
        FTimg = Image.open(FTimgpath)
        FTimg = FTimg.resize((550,309))
        FTimg = ImageTk.PhotoImage(FTimg)
        globals()["image" + str(i)] = FTimg
        i += 1

    #buttons for ft images
    def btinte1(e):
        e.widget.config(bg='orange')
        return
    def btintl1(e):
        e.widget.config(bg='green')
        return
    
    global j
    j=0
    def imager():
        global j
        if j in range(0,7):
            j+=1
            Panel2["image"]= globals()["image"+str(j)]
        else:
            j=0
            j+=1
            Panel2["image"]= globals()["image"+str(j)]
    def imagel():
        global j
        if j in range(2,8):
            j-=1
            Panel2["image"]= globals()["image"+str(j)]
        else:
            j=8
            j-=1
            Panel2["image"]= globals()["image"+str(j)]

    Panel2 = tek.Label(frame2, image = image1,bd=0)
    Panel2.place(x = -1, y = -1)

    nextr=tek.Button(master=frame0,text="->",bg="Green",fg="Yellow",font=('Bacon',15,'bold'),cursor="hand2",command=imager,bd=0,activebackground='blue',activeforeground='gold')
    nextr.place(x=950,y=500)

    nextl=tek.Button(master=frame0,text="<-",bg="Green",fg="Yellow",font=('Bacon',15,'bold'),cursor="hand2",command=imagel,bd=0,activebackground='blue',activeforeground='gold')
    nextl.place(x=317,y=500)

    for b in [nextr,nextl]:
        b.bind("<Enter>",btinte1)
        b.bind("<Leave>",btintl1)

    #ft images slideshow
    def slides():
        global j
        if j in range(0,7):
            j+=1
            Panel2["image"]= globals()["image"+str(j)]
        else:
            j=0
            j+=1
            Panel2["image"]= globals()["image"+str(j)]
        nextr.after(2000,slides)

    thread1=threading.Thread(target=slides)
    thread1.daemon = 1
    thread1.start()


    #ft label
    FT=tek.Label(master=frame0,text="FEAT",bg='yellow',fg='red',font=('Battleground',120,'bold'))
    FT.place(x=35,y=450)

    FT1=tek.Label(master=frame0,text="URED",bg='yellow',fg='red',font=('Battleground',120,'bold'))
    FT1.place(x=1100,y=450)
    def flash():
        FT["bg"]= "Lime"
        FT["fg"]= "Orange"
        FT1["bg"]= "Lime"
        FT1["fg"]= "Orange"
        panel.after(2000,deflash)
    def deflash():
        FT["bg"]= "Yellow"
        FT["fg"]= "Red"
        FT1["bg"]= "Yellow"
        FT1["fg"]= "Red"
        panel.after(2000,flash)

    thread2=threading.Thread(target=flash)
    thread2.start()

    thread3=threading.Thread(target=deflash)
    thread3.start()

    #music
    global audioplay
    if audioplay == False:
        audioplayback()
    
    Window.update()

#News & Updates Page
def News_And_Updates_Page():
    global frame0
    global panel
    Window.update()
    #Background
    frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
    frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    panel = tek.Label(frame0, image = BGimg5)
    panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    #Top Bar
    panel.rowconfigure(0,weight=1)
    panel.columnconfigure(0,weight=1)
    frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
    frame1.grid(row=0,column=0,sticky="new")
    label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
    label1.pack(fill=tek.X, expand=True)
    #Top bar buttons
    def btinte(e):
        e.widget.config(bg='red')
        return
    def btintl(e):
        e.widget.config(bg='Sky Blue')
        return

    Panel1 = tek.Label(frame1, image = Img1)
    Panel1.place(x = 0, y = 0)

    Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
    Name.place(x=54,y=0,width=300,height=52)

    home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
    home.place(x=354,y=0,width=120,height=52)

    nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',state=tek.ACTIVE)
    nu.place(x=474,y=0,width=120,height=52)

    browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
    browse.place(x=594,y=0,width=120,height=52)

    search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
    search.place(x=714,y=0,width=120,height=52)

    if status == "Logged In":
        login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=lambda:antierror0(thread,"Profile"))
        login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
        pp=tek.Label(frame1,image=acct_dp_final1)
        pp.place(relx=1.0,y=0,anchor="ne")
    else:
        login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=lambda:antierror0(thread,"Login"))
        login_btn.place(x=1246,y=0,width=120,height=52)

    abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
    abt.place(x=834,y=0,width=120,height=52)

    for btn in [home,nu,browse,search,abt,login_btn]:
        btn.bind("<Enter>",btinte)
        btn.bind("<Leave>",btintl)

    #Nu. Games
    frame2=tek.Frame(master=frame0, width=1040, height=585, relief=tek.RIDGE, bd=1)
    frame2.place(x=150,y=100)
    label2=tek.Label(master=frame2, bg="Green", fg="yellow",height=20,width=78)
    label2.place(x=0,y=0)

    nuimages=['Media/acvnu.jpg','Media/aunu.jpg','Media/brdrl3nu.jpg','Media/cybpnu.jpeg','Media/fgnu.jpg','Media/hinu.jpg','Media/hzdnu.jpeg','Media/masnu.jpg','Media/rlnu.jpg','Media/wdlnu.jpeg']

    i=1
    for nuimage in nuimages:
        NUimgpath = nuimage
        NUimg = Image.open(NUimgpath)
        NUimg = NUimg.resize((1040,585))
        NUimg = ImageTk.PhotoImage(NUimg)
        globals()["nuimage" + str(i)] = NUimg
        i += 1

    #buttons for nu images
    def btinte1(e):
        e.widget.config(bg='orange')
        return
    def btintl1(e):
        e.widget.config(bg='green')
        return
    global e   
    e=0  
    def imager():
        global e
        if e in range(0,10):
            e+=1
            Panel2["image"]= globals()["nuimage"+str(e)]
        else:
            e=0
            e+=1
            Panel2["image"]= globals()["nuimage"+str(e)]
    def imagel():
        global e
        if e in range(2,11):
            e-=1
            Panel2["image"]= globals()["nuimage"+str(e)]
        else:
            e=11
            e-=1
            Panel2["image"]= globals()["nuimage"+str(e)]

    Panel2 = tek.Label(frame2, image = image1,bd=0)
    Panel2.place(x = -1, y = -1)

    nextr=tek.Button(master=frame0,text="->",bg="Green",fg="Yellow",font=('Bacon',15,'bold'),cursor="hand2",command=imager,bd=0,activebackground='blue',activeforeground='gold')
    nextr.place(x=1245,y=370)

    nextl=tek.Button(master=frame0,text="<-",bg="Green",fg="Yellow",font=('Bacon',15,'bold'),cursor="hand2",command=imagel,bd=0,activebackground='blue',activeforeground='gold')
    nextl.place(x=50,y=370)

    for b in [nextr,nextl]:
        b.bind("<Enter>",btinte1)
        b.bind("<Leave>",btintl1)

    #nu images slideshow
    def slides1():
        global e
        if e in range(0,10):
            e+=1
            Panel2["image"]= globals()["nuimage"+str(e)]
        else:
            e=0
            e+=1
            Panel2["image"]= globals()["nuimage"+str(e)]
        nextr.after(2000,slides1)

    thread2=threading.Thread(target=slides1)
    thread2.daemon = 1
    thread2.start()
    #music
    global audioplay
    if audioplay == False:
        audioplayback()
    Window.update()

#Login Page
def Login_Page():
    global frame0
    global panel
    Window.update()
    #Background
    frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
    frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    panel = tek.Label(frame0, image = BGimg4)
    panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    def btinte(e):
        e.widget.config(bg='blue')
        return
    def btintl(e):
        e.widget.config(bg='red')
        return

    #Top Bar
    panel.rowconfigure(0,weight=1)
    panel.columnconfigure(0,weight=1)
    frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
    frame1.grid(row=0,column=0,sticky="new")
    label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
    label1.pack(fill=tek.X, expand=True)
    #Top bar buttons
    def btinte1(e):
        e.widget.config(bg='red')
        return
    def btintl1(e):
        e.widget.config(bg='Sky Blue')
        return

    Panel1 = tek.Label(frame1, image = Img1)
    Panel1.place(x = 0, y = 0)

    Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
    Name.place(x=54,y=0,width=300,height=52)

    home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
    home.place(x=354,y=0,width=120,height=52)

    nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
    nu.place(x=474,y=0,width=120,height=52)

    browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
    browse.place(x=594,y=0,width=120,height=52)

    search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
    search.place(x=714,y=0,width=120,height=52)
    
    abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
    abt.place(x=834,y=0,width=120,height=52)

    login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',state=tek.ACTIVE)
    login_btn.place(x=1246,y=0,width=120,height=52)

    for btn in [home,nu,browse,search,abt,login_btn]:
        btn.bind("<Enter>",btinte1)
        btn.bind("<Leave>",btintl1)
        
    #Login Panel
    login_panel=tek.Label(panel,bg='#2c2f33',height=25,width=105)
    login_panel.place(x=304,y=170)

    login_label_error_usrnm=tek.Label(login_panel,bg='#2c2f33',fg='#2c2f33',font=('Avellana Pro',12,'bold'),text="-- ERROR! INCORRECT USERNAME!")
    login_label_error_usrnm.place(x=180,y=90)
    login_label_error_pswd=tek.Label(login_panel,bg='#2c2f33',fg='#2c2f33',font=('Avellana Pro',12,'bold'),text="-- ERROR! INCORRECT PASSWORD!")
    login_label_error_pswd.place(x=180,y=200)

    login_label1=tek.Label(login_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='WELCOME USER!')
    login_label1.place(x=230,y=2)
    login_label2=tek.Label(login_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="LOGIN TO UNLOCK THE FULL FUNCTIONALITY OF THE APP!")
    login_label2.place(x=180,y=50)

    usrnm_label=tek.Label(login_panel,bg='#2c2f33',fg='Gold',font=('Beway',30,'bold'),text='USERNAME')
    usrnm_label.place(x=10,y=90)
    usrnm= tek.Entry(master=login_panel,bg='Orange',fg='Yellow',font=('Agency FB',30,'bold'))
    usrnm.place(x=10,y=130)

    pswd_label=tek.Label(login_panel,bg='#2c2f33',fg='Gold',font=('Beway',30,'bold'),text='PASSWORD')
    pswd_label.place(x=10,y=200)
    pswd= tek.Entry(master=login_panel,bg='Orange',fg='Yellow',font=('Agency FB',30,'bold'))
    pswd.place(x=10,y=240)

    #Loading Visual
    def loading():
        panel.after(10,lambda:login.config(fg='Gold',text='PLEASE WAIT'))
        panel.after(1010,lambda:login.config(fg='Gold',text='PLEASE WAIT.'))
        panel.after(2010,lambda:login.config(fg='Gold',text='PLEASE WAIT..'))
        panel.after(3010,lambda:login.config(fg='Gold',text='PLEASE WAIT...'))
        panel.after(4010,lambda:login.config(fg='Gold',text='PLEASE WAIT....'))
        panel.after(5010,lambda:login.config(fg='Gold',text='PLEASE WAIT.....'))
    #Logging In  
    def login():
        global status
        global username
        global password
        i=1
        cursor=conn.cursor()
        username = usrnm.get()
        password=pswd.get()
        cursor.execute('SELECT EXISTS(SELECT Username, Password FROM Accounts WHERE Username = "%s")' % username)
        result=cursor.fetchall()
        for output in result:
            for value in output:
                val0 = value
        if val0 == 1:
            cursor.execute('SELECT Username, Password FROM Accounts WHERE Username = "%s"'% username)
            result=cursor.fetchall()
            for column in result:
                for value in column:
                    globals()["val" + str(i)] = value
                    i += 1
            conn.commit()
            if username == val1 and password == val2:
                status="Logged In"
                login_label_error_usrnm.config(fg='#2c2f33')
                login_label_error_pswd.config(fg='#2c2f33')
                usrnm_label.config(fg='Gold')
                pswd_label.config(fg='Gold')
                #Fetching Profile Info
                cursor.execute('SELECT * FROM Accounts WHERE Username = "%s"'% username)
                result=cursor.fetchall()
                p=1
                for column in result:
                    for value in column:
                        globals()["profval" + str(p)] = value
                        p += 1
                loading()
                global_dp()
                panel.after(6010,lambda:login.config(fg='Lime',text='LOGGED IN!'))
                panel.after(8010,show_home_page)
                
            else:
                status="Logged Out"
                login_label_error_pswd.config(fg='Red')
                pswd_label.config(fg='Red')
                panel.after(5000,lambda:login_label_error_pswd.config(fg='#2c2f33'))
                panel.after(5000,lambda:pswd_label.config(fg='Gold'))
                usrnm_label.config(fg='Gold')
                login_label_error_usrnm.config(fg='#2c2f33')
                
        else:
            login_label_error_usrnm.config(fg='Red')
            usrnm_label.config(fg='Red')
            panel.after(5000,lambda:login_label_error_usrnm.config(fg='#2c2f33'))
            panel.after(5000,lambda:usrnm_label.config(fg='Gold'))
            pswd_label.config(fg='Gold')
            login_label_error_pswd.config(fg='#2c2f33')
            

    login=tek.Button(master=login_panel,text="LOGIN",font=('Battlelines',15,'bold'),bg="Red",fg="Yellow",cursor="hand2",bd=0,activebackground='lime',activeforeground='blue',command=login)
    login.place(x=85,y=310,width=250,height=55)

    login.bind("<Enter>",btinte)
    login.bind("<Leave>",btintl)


    part_label=tek.Label(login_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',15,'bold'),text="""    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |""")
    part_label.place(x=440,y=81)

    def btnundere(e):
        e.widget.config(font=('Apple And Pear',20,'bold','underline'))
        return
    def btnunderl(e):
        e.widget.config(font=('Apple And Pear',20,'bold'))
        return

    login_label3=tek.Label(login_panel,bg='#2c2f33',fg='Gold',font=('Avellana Pro',15,'bold'),text="DON'T HAVE AN ACCOUNT?")
    login_label3.place(x=470,y=90)

    #music
    global audioplay
    if audioplay == False:
        audioplayback()

    #Create Account page
    def create_account_page():
        global Window
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg3)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        def btinte(e):
            e.widget.config(bg='blue')
            return
        def btintl(e):
            e.widget.config(bg='red')
            return

        #Create Account Panel
        crta_panel=tek.Label(panel,bg='#2c2f33',height=45,width=130)
        crta_panel.place(x=220,y=10)

        crta_label1=tek.Label(crta_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='CREATE ACCOUNT')
        crta_label1.place(x=290,y=2)
        crta_label2=tek.Label(crta_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="CREATE AN ACCOUNT TO UNLOCK THE FULL FUNCTIONALITY OF THE APP!")
        crta_label2.place(x=200,y=50)

        back_btn=tek.Button(master=crta_panel,text="< Back",font=('Avellana Pro',18,'bold'),bg="Orange",fg="Blue",cursor="hand2",bd=0,activebackground='lime',activeforeground='blue',command=show_login_page)
        back_btn.place(relx=0.0,rely=0.0,width=100,height=35)
        

        crta_name1_label=tek.Label(crta_panel,bg='#2c2f33',fg='Gold',font=('Beway',25,'bold'),text='FIRST NAME')
        crta_name1_label.place(x=42,y=100)
        crta_name1= tek.Entry(master=crta_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        crta_name1.place(x=42,y=140)

        crta_name2_label=tek.Label(crta_panel,bg='#2c2f33',fg='Gold',font=('Beway',25,'bold'),text='MIDDLE NAME')
        crta_name2_label.place(x=332,y=100)
        crta_name2= tek.Entry(master=crta_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        crta_name2.place(x=332,y=140)

        crta_name3_label=tek.Label(crta_panel,bg='#2c2f33',fg='Gold',font=('Beway',25,'bold'),text='LAST NAME')
        crta_name3_label.place(x=622,y=100)
        crta_name3= tek.Entry(master=crta_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        crta_name3.place(x=622,y=140)

        crta_age_label=tek.Label(crta_panel,bg='#2c2f33',fg='Gold',font=('Beway',25,'bold'),text='AGE')
        crta_age_label.place(x=42,y=200)
        crta_age= tek.Entry(master=crta_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        crta_age.place(x=42,y=240)
        #Handling Errors with age Entry
        def age_check():
            global age_error
            global ageval
            ageval=int(crta_age.get())
            dobval0=crta_dob.get()
            cursor.execute('SELECT TIMESTAMPDIFF(YEAR,"%s", CURDATE()) AS difference'%dobval0)
            result=cursor.fetchall()
            for output in result:
                for value in output:
                    agevalcheck = value
            if agevalcheck == ageval:
                age_error=False
                crta_age_label.config(fg='Gold')
                crta_age.config(bg='Orange')        
            else:
                age_error=True
                crta_age_label.config(fg='Red')
                crta_age.config(bg='Red')

        crta_dob_label=tek.Label(crta_panel,bg='#2c2f33',fg='Gold',font=('Beway',25,'bold'),text='DOB(YYYY-MM-DD)')
        crta_dob_label.place(x=332,y=200)
        crta_dob= tek.Entry(master=crta_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        crta_dob.place(x=332,y=240)
        #Handling Errors with DOB Entry
        def dob_check():
            global dob_error
            global dobval
            dobval=crta_dob.get()
            ageval0=int(crta_age.get())
            cursor.execute('SELECT DATE("%s") AS valid;'%dobval)
            result=cursor.fetchall()
            for output in result:
                for value in output:
                    dobvalcheck = value
            if dobvalcheck is None:
                dob_error=True
                crta_dob_label.config(fg='Red')
                crta_dob.config(bg='Red')
            else:
                cursor.execute('SELECT TIMESTAMPDIFF(YEAR,"%s", CURDATE()) AS difference'%dobval)
                result=cursor.fetchall()
                for output in result:
                   for value in output:
                        dobvalcheck1 = value
                if dobvalcheck1 == ageval0:
                    dob_error=False
                    crta_dob_label.config(fg='Gold')
                    crta_dob.config(bg='Orange')
                else:
                    dob_error=True
                    crta_dob_label.config(fg='Red')
                    crta_dob.config(bg='Red')
                

        crta_gender_label=tek.Label(crta_panel,bg='#2c2f33',fg='Gold',font=('Beway',25,'bold'),text='GENDER')
        crta_gender_label.place(x=622,y=200)
        crta_gender= tek.Entry(master=crta_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        crta_gender.place(x=622,y=240)

        crta_emailid_label=tek.Label(crta_panel,bg='#2c2f33',fg='Gold',font=('Beway',25,'bold'),text='EMAIL ID')
        crta_emailid_label.place(x=42,y=300)
        crta_emailid= tek.Entry(master=crta_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        crta_emailid.place(x=42,y=340)

        crta_emailid1_label=tek.Label(crta_panel,bg='#2c2f33',fg='Gold',font=('Beway',25,'bold'),text='CONFIRM EMAIL ID')
        crta_emailid1_label.place(x=332,y=300)
        crta_emailid1= tek.Entry(master=crta_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        crta_emailid1.place(x=332,y=340)
        #Handling Errors with Email ID Entries
        def emailid_check():
            global emailid_error
            global emailidval
            global emailid1val
            emailidval=crta_emailid.get()
            emailid1val=crta_emailid1.get()
            if emailidval != emailid1val:
                emailid_error=True
                crta_emailid_label.config(fg='Red')
                crta_emailid.config(bg='Red')
                crta_emailid1_label.config(fg='Red')
                crta_emailid1.config(bg='Red')
            else:
                emailid_error=False
                crta_emailid_label.config(fg='Gold')
                crta_emailid.config(bg='Orange')
                crta_emailid1_label.config(fg='Gold')
                crta_emailid1.config(bg='Orange')

        crta_location_label=tek.Label(crta_panel,bg='#2c2f33',fg='Gold',font=('Beway',25,'bold'),text='LOCATION')
        crta_location_label.place(x=622,y=300)
        crta_location = tek.Entry(master=crta_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        crta_location.place(x=622,y=340)

        crta_usrnm_label=tek.Label(crta_panel,bg='#2c2f33',fg='Gold',font=('Beway',25,'bold'),text='USERNAME')
        crta_usrnm_label.place(x=42,y=400)
        crta_usrnm= tek.Entry(master=crta_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        crta_usrnm.place(x=42,y=440)
        #Handling Errors with Username Entry
        def username_check():
            global usrnm_error
            global usrnmval
            usrnmval=crta_usrnm.get()
            cursor.execute('SELECT EXISTS(SELECT Username FROM Accounts WHERE Username = "%s")' % usrnmval)
            result=cursor.fetchall()
            for output in result:
                for value in output:
                    usrnmvalcheck = value
            if usrnmvalcheck == 1:
                usrnm_error=True
                crta_usrnm_label.config(fg='Red')
                crta_usrnm.config(bg='Red')
            else:
                usrnm_error=False
                crta_usrnm_label.config(fg='Gold')
                crta_usrnm.config(bg='Orange')
                
            

        crta_pswd_label=tek.Label(crta_panel,bg='#2c2f33',fg='Gold',font=('Beway',25,'bold'),text='PASSWORD')
        crta_pswd_label.place(x=332,y=400)
        crta_pswd= tek.Entry(master=crta_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        crta_pswd.place(x=332,y=440)

        crta_pswd1_label=tek.Label(crta_panel,bg='#2c2f33',fg='Gold',font=('Beway',25,'bold'),text='CONFIRM PASSWORD')
        crta_pswd1_label.place(x=622,y=400)
        crta_pswd1= tek.Entry(master=crta_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        crta_pswd1.place(x=622,y=440)
        #Handling Errors with Password Entries
        def password_check():
            global pswd_error
            global pswdval
            global pswd1val
            pswdval=crta_pswd.get()
            pswdval1=crta_pswd1.get()
            if pswdval != pswdval1:
                pswd_error=True
                crta_pswd_label.config(fg='Red')
                crta_pswd.config(bg='Red')
                crta_pswd1_label.config(fg='Red')
                crta_pswd1.config(bg='Red')
            else:
                pswd_error=False
                crta_pswd_label.config(fg='Gold')
                crta_pswd.config(bg='Orange')
                crta_pswd1_label.config(fg='Gold')
                crta_pswd1.config(bg='Orange')

                
        readtcs_btn=tek.Button(master=crta_panel,text="VIEW T&Cs",bg="#2c2f33",fg="Sky Blue",font=('Apple And Pear',15,'bold'),cursor="hand2",bd=0,activebackground='#2c2f33',activeforeground='Gold',command=show_terms_of_service_page)
        readtcs_btn.place(x=42,y=540)
        def btnunderle(e):
            e.widget.config(font=('Apple And Pear',15,'bold','underline'))
            return
        def btnunderll(e):
            e.widget.config(font=('Apple And Pear',15,'bold'))
            return
        readtcs_btn.bind("<Enter>",btnunderle)
        readtcs_btn.bind("<Leave>",btnunderll)

        checktcs=tek.IntVar()
        tcsdone=tek.Checkbutton(master=crta_panel,text="I'VE READ AND AGREE TO ALL THE TERMS & CONDITIONS",bg="#2c2f33",fg="Green",font=('Apple And Pear',15,'bold'),cursor="hand2",activebackground='#2c2f33',activeforeground='Green',variable=checktcs)
        tcsdone.place(x=42,y=570)
        tcsdone_error=tek.Label(crta_panel,bg='#2c2f33',fg='#2c2f33',font=('Avellana Pro',12,'bold'),text="< PLEASE AGREE TO OUR TERMS & CONDITIONS\nIN ORDER TO CREATE AN ACCOUNT")
        tcsdone_error.place(x=522,y=570)
        #Handling Errors with situation where user doesn't agree to the T&Cs
        def tcs_check():
            global checktcsval
            checktcsval=checktcs.get()
            if checktcsval == 0:
                tcsdone_error.config(fg="Red")
            else:
                tcsdone_error.config(fg="#2c2f33")
                

        #loading visual
        def loading1():
            panel.after(10,lambda:crtacc.config(fg='Gold',text='PLEASE WAIT'))
            panel.after(1010,lambda:crtacc.config(fg='Gold',text='PLEASE WAIT.'))
            panel.after(2010,lambda:crtacc.config(fg='Gold',text='PLEASE WAIT..'))
            panel.after(3010,lambda:crtacc.config(fg='Gold',text='PLEASE WAIT...'))
            panel.after(4010,lambda:crtacc.config(fg='Gold',text='PLEASE WAIT....'))
            panel.after(5010,lambda:crtacc.config(fg='Gold',text='PLEASE WAIT.....'))
            

        #Creating Account
        def create_account():
            global status
            global acct_id
            global initial_data_query
            global bal
            global stat
            global dp_file
            global go
            global dtf
            bal=0
            stat="-"
            dp_file="Media/defaultdp.png"
            go=[]
            go=str(go)
            dt = datetime.datetime.now()
            dtf = dt.strftime('%Y-%m-%d %H:%M:%S')
            dob_check()
            age_check()
            emailid_check()
            username_check()
            password_check()
            tcs_check()
            cursor.execute('SELECT Acct_ID FROM Accounts ORDER BY Acct_ID DESC LIMIT 1')
            result=cursor.fetchall()
            for output in result:
                for value in output:
                    acct_id=value
            acct_id=acct_id+1
            first_name=crta_name1.get()
            middle_name=crta_name2.get()
            last_name=crta_name3.get()
            full_name=first_name+" "+middle_name+" "+last_name
            gender=crta_gender.get()
            location=crta_location.get()
            if age_error ==  False and dob_error == False and emailid_error == False and usrnm_error == False and pswd_error == False and checktcsval == 1:
                crta_label_error.config(fg="#2c2f33")
                details=(acct_id,full_name,ageval,gender,dobval,emailidval,usrnmval,pswdval,location,bal,stat,dp_file,dtf)
                cursor.execute(initial_data_query,details)
                details1=(acct_id,full_name,emailidval,usrnmval,bal,go)
                cursor.execute(initial_data_query1,details1)
                loading1()
                conn.commit()
                panel.after(6010,lambda:crtacc.config(fg='Lime',text='ACCOUNT CREATED!'))
                panel.after(8010,show_login_page)
            else:
                status="Logged Out"
                crta_label_error.config(fg="Red")
            
            
        crtacc=tek.Button(master=crta_panel,text="CREATE ACCOUNT",font=('Battlelines',15,'bold'),bg="Red",fg="Yellow",cursor="hand2",bd=0,activebackground='lime',activeforeground='blue',command=create_account)
        crtacc.place(x=330,y=610,width=250,height=55)
        def btinte(e):
            e.widget.config(bg='blue')
            return
        def btintl(e):
            e.widget.config(bg='red')
            return
        crtacc.bind("<Enter>",btinte)
        crtacc.bind("<Leave>",btintl)

        crta_label_error=tek.Label(crta_panel,bg='#2c2f33',fg='#2c2f33',font=('Avellana Pro',12,'bold'),text="AN ERROR OCURRED! PLEASE RE-CHECK THE ENTRIES HIGHLIGHTED IN RED COLOR & CORRECT THEM")
        crta_label_error.place(x=102,y=500)

    #showing crtacc page
    def show_create_account_page():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        create_account_page()
        
    create_acct_btn=tek.Button(master=login_panel,text="Create Account",bg="#2c2f33",fg="Sky Blue",font=('Apple And Pear',20,'bold'),cursor="hand2",bd=0,activebackground='#2c2f33',activeforeground='Gold',command=show_create_account_page)
    create_acct_btn.place(x=500,y=130)


    login_label4=tek.Label(login_panel,bg='#2c2f33',fg='Gold',font=('Avellana Pro',15,'bold'),text="FORGOT YOUR PASSWORD?")
    login_label4.place(x=470,y=200)

    def password_reset_page():
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        #Reset Password Panel
        resetp_panel=tek.Label(panel,bg='#2c2f33',height=25,width=105)
        resetp_panel.place(x=304,y=170)

        resetp_label1=tek.Label(resetp_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='OOPS! FORGOT YOUR PASSWORD?')
        resetp_label1.place(x=65,y=2)
        resetp_label2=tek.Label(resetp_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="DON'T PANIC! FOLLOW THESE SIMPLE INSTRUCTIONS TO RESET IT!")
        resetp_label2.place(x=130,y=50)

        back_btn=tek.Button(master=resetp_panel,text="<",font=('Avellana Pro',18,'bold'),bg="Orange",fg="Blue",cursor="hand2",bd=0,activebackground='lime',activeforeground='blue',command=show_login_page)
        back_btn.place(relx=0.0,rely=0.0,width=50,height=35)

        resetp_usrnm_label=tek.Label(resetp_panel,bg='#2c2f33',fg='Gold',font=('Beway',20,'bold'),text='USERNAME')
        resetp_usrnm_label.place(x=60,y=90)
        resetp_usrnm= tek.Entry(master=resetp_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'))
        resetp_usrnm.place(x=60,y=130)

        resetp_label_inst0_emailid=tek.Label(resetp_panel,bg='#2c2f33',fg='#2c2f33',font=('Avellana Pro',12,'bold'),text="PLEASE TYPE IN THE\n<<< MENTIONED LINKED\nEMAIL ID TO VERIFY\nYOUR IDENTITY")
        resetp_label_inst0_emailid.place(x=500,y=290)

        resetp_emailid_label=tek.Label(resetp_panel,bg='#2c2f33',fg='Gold',font=('Beway',20,'bold'),text='EMAIL ID',state=tek.DISABLED)
        resetp_emailid_label.place(x=420,y=90)
        resetp_emailid= tek.Entry(master=resetp_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'),state=tek.DISABLED)
        resetp_emailid.place(x=420,y=130)

        resetp_pswd_label=tek.Label(resetp_panel,bg='#2c2f33',fg='Gold',font=('Beway',20,'bold'),text='NEW PASSWORD',state=tek.DISABLED)
        resetp_pswd_label.place(x=60,y=200)
        resetp_pswd= tek.Entry(master=resetp_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'),state=tek.DISABLED)
        resetp_pswd.place(x=60,y=240)

        resetp_pswd1_label=tek.Label(resetp_panel,bg='#2c2f33',fg='Gold',font=('Beway',20,'bold'),text='CONFIRM NEW PASSWORD',state=tek.DISABLED)
        resetp_pswd1_label.place(x=420,y=200)
        resetp_pswd1= tek.Entry(master=resetp_panel,bg='Orange',fg='Yellow',font=('Agency FB',20,'bold'),state=tek.DISABLED)
        resetp_pswd1.place(x=420,y=240)

        def loading2():
                panel.after(10,lambda:reset_pass.config(fg='Blue',text='PLEASE WAIT'))
                panel.after(1010,lambda:reset_pass.config(fg='Blue',text='PLEASE WAIT.'))
                panel.after(2010,lambda:reset_pass.config(fg='Blue',text='PLEASE WAIT..'))
                panel.after(3010,lambda:reset_pass.config(fg='Blue',text='PLEASE WAIT...'))
                panel.after(4010,lambda:reset_pass.config(fg='Blue',text='PLEASE WAIT....'))
                panel.after(5010,lambda:reset_pass.config(fg='Blue',text='PLEASE WAIT.....'))

        def reset_password():
            global resetp_email
            global resetp_username
            global resetp_password
            global resetp_password1
            a=1
            resetp_username = resetp_usrnm.get()
            cursor.execute('SELECT EXISTS(SELECT Username FROM Accounts WHERE Username = "%s")' % resetp_username)
            result=cursor.fetchall()
            for output in result:
                for value in output:
                    val0 = value
            if val0 == 1:
                loading2()
                panel.after(6010,lambda:reset_pass.config(text='SUCCESS',fg='Green',font=('Battlelines',15,'bold')))
                panel.after(11010,lambda:reset_pass.config(text="CHECK",font=('Battlelines',15,'bold'),fg='Blue'))
                panel.after(6010,lambda:resetp_usrnm_label.config(fg='Gold'))
                cursor.execute('SELECT Email_ID, Username FROM Accounts WHERE Username = "%s"'% resetp_username)
                result=cursor.fetchall()
                for column in result:
                    for value in column:
                        globals()["rstval" + str(a)] = value
                        a += 1
                conn.commit()
                length=len(rstval1)
                emailid_slice=rstval1[:4]
                emailid_hint=emailid_slice.ljust(length,"*")
                panel.after(11010,lambda:resetp_label_inst0_emailid.config(fg="Yellow"))
                panel.after(11010,lambda:reset_pass.config(text=emailid_hint))
                panel.after(16010,lambda:reset_pass.config(text="CHECK"))
                panel.after(6010,lambda:resetp_emailid.config(state=tek.NORMAL))
                panel.after(6010,lambda:resetp_emailid_label.config(state=tek.NORMAL))
                def check2():
                    resetp_email=resetp_emailid.get()
                    if resetp_email == rstval1 and resetp_username == rstval2:
                        panel.after(6010,lambda:resetp_label_inst0_emailid.config(fg="#2c2f33"))
                        loading2()
                        panel.after(6010,lambda:reset_pass.config(text='SUCCESS',fg='Green',font=('Battlelines',15,'bold')))
                        panel.after(11010,lambda:reset_pass.config(text="RESET PASSWORD",font=('Battlelines',15,'bold'),fg='Blue'))
                        panel.after(6010,lambda:resetp_pswd.config(state=tek.NORMAL))
                        panel.after(6010,lambda:resetp_pswd1.config(state=tek.NORMAL))
                        panel.after(6010,lambda:resetp_pswd_label.config(state=tek.NORMAL))
                        panel.after(6010,lambda:resetp_pswd1_label.config(state=tek.NORMAL))
                        panel.after(6010,lambda:resetp_emailid_label.config(fg='Gold'))
                        def check3():
                            resetp_password=resetp_pswd.get()
                            resetp_password1=resetp_pswd1.get()
                            if resetp_email == rstval1 and resetp_username == rstval2 and resetp_password == resetp_password1:
                                loading2()
                                panel.after(6010,lambda:resetp_pswd_label.config(fg='Gold'))
                                panel.after(6010,lambda:resetp_pswd1_label.config(fg='Gold'))
                                resetp_details=(resetp_password,resetp_username,resetp_email)
                                cursor.execute('UPDATE Accounts SET Password = "%s" Where Username = "%s" AND Email_ID = "%s"' % resetp_details)
                                conn.commit()
                                panel.after(6010,lambda:reset_pass.config(text="PASSWORD RESET SUCCESSFUL!",font=('Battlelines',15,'bold'),fg='Green'))
                                panel.after(8010,show_login_page)
                            else:
                                loading2()
                                panel.after(6010,lambda:reset_pass.config(text="PASSWORDS DON'T MATCH",fg='Red',font=('Battlelines',15,'bold')))
                                panel.after(6010,lambda:resetp_pswd_label.config(fg='Red'))
                                panel.after(6010,lambda:resetp_pswd1_label.config(fg='Red'))
                                panel.after(11010,lambda:reset_pass.config(text="RESET PASSWORD",font=('Battlelines',15,'bold'),fg='Blue'))
                        
                        reset_pass.config(command=check3)
                    else:
                        loading2()
                        panel.after(6010,lambda:resetp_pswd.config(state=tek.DISABLED))
                        panel.after(6010,lambda:resetp_pswd1.config(state=tek.DISABLED))
                        panel.after(6010,lambda:resetp_pswd_label.config(state=tek.DISABLED))
                        panel.after(6010,lambda:resetp_pswd1_label.config(state=tek.DISABLED))
                        panel.after(6010,lambda:reset_pass.config(text='INVALID EMAIL ID',fg='Red',font=('Battlelines',15,'bold')))
                        panel.after(6010,lambda:resetp_emailid_label.config(fg='Red'))
                        panel.after(11010,lambda:reset_pass.config(text="CHECK",font=('Battlelines',15,'bold'),fg='Blue'))
                    
                reset_pass.config(command=check2)        
            else:
                loading2()
                panel.after(6010,lambda:resetp_emailid.config(state=tek.DISABLED))
                panel.after(6010,lambda:resetp_emailid_label.config(state=tek.DISABLED))
                panel.after(6010,lambda:reset_pass.config(text='USERNAME NOT FOUND',fg='Red',font=('Battlelines',15,'bold')))
                panel.after(6010,lambda:resetp_usrnm_label.config(fg='Red'))
                panel.after(11010,lambda:reset_pass.config(text="CHECK",font=('Battlelines',15,'bold'),fg='Blue'))
                
        def btinte(e):
            e.widget.config(bg='yellow')
            return
        def btintl(e):
            e.widget.config(bg='orange')
            return

        reset_pass=tek.Button(master=resetp_panel,text="CHECK",font=('Battlelines',15,'bold'),bg="Orange",fg="Blue",cursor="hand2",bd=0,activebackground='lime',activeforeground='blue',command=reset_password)
        reset_pass.place(x=230,y=310,width=250,height=55)

        reset_pass.bind("<Enter>",btinte)
        reset_pass.bind("<Leave>",btintl)

    #showing rstpswd page
    def show_password_reset_page():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        password_reset_page()

    pswdreset_btn=tek.Button(master=login_panel,text="Reset Password",bg="#2c2f33",fg="Sky Blue",font=('Apple And Pear',20,'bold'),cursor="hand2",bd=0,activebackground='#2c2f33',activeforeground='Gold',command=show_password_reset_page)
    pswdreset_btn.place(x=500,y=240)
    for bt in [create_acct_btn,pswdreset_btn]:
        bt.bind("<Enter>",btnundere)
        bt.bind("<Leave>",btnunderl)
    Window.update()

def Profile_Page():
    global frame0
    global panel
    Window.update()
    #Background
    frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
    frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    panel = tek.Label(frame0, image = BGimg5)
    panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    def btinte1(e):
        e.widget.config(bg='blue')
        return
    def btintl1(e):
        e.widget.config(bg='red')
        return
    #Top Bar
    panel.rowconfigure(0,weight=1)
    panel.columnconfigure(0,weight=1)
    frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
    frame1.grid(row=0,column=0,sticky="new")
    label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
    label1.pack(fill=tek.X, expand=True)
    #Top bar buttons
    def btinte(e):
        e.widget.config(bg='red')
        return
    def btintl(e):
        e.widget.config(bg='Sky Blue')
        return

    Panel1 = tek.Label(frame1, image = Img1)
    Panel1.place(x = 0, y = 0)

    Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
    Name.place(x=54,y=0,width=300,height=52)

    home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
    home.place(x=354,y=0,width=120,height=52)

    nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
    nu.place(x=474,y=0,width=120,height=52)

    browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
    browse.place(x=594,y=0,width=120,height=52)

    search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
    search.place(x=714,y=0,width=120,height=52)

    abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
    abt.place(x=834,y=0,width=120,height=52)

    login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange')
    login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
    pp=tek.Label(frame1,image=acct_dp_final1)
    pp.place(relx=1.0,y=0,anchor="ne")

    for btn in [home,nu,browse,search,abt,login_btn]:
        btn.bind("<Enter>",btinte)
        btn.bind("<Leave>",btintl)

    #Profile Panel
    profile_panel=tek.Label(panel,bg='#2c2f33',height=42,width=191)
    profile_panel.place(x=9,y=58)

    profile_label1=tek.Label(profile_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='YOUR PROFILE')
    profile_label1.place(x=540,y=2)
    profile_label2=tek.Label(profile_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="LOOKIN' COOL EH?")
    profile_label2.place(x=602,y=50)

    prof_panel=tek.Label(profile_panel,bg='#23272a',height=16,width=191,relief=tek.RIDGE)
    prof_panel.place(x=-2,y=70)

    dp_panel=tek.Label(prof_panel)
    dp_panel.place(x = 0, y = 0)

    cursor.execute('SELECT * FROM Accounts WHERE Username = "%s"'% username)
    result=cursor.fetchall()
    i=1
    for column in result:
        for value in column:
            globals()["profval" + str(i)] = value
            i += 1
    dp_panel.config(image=acct_dp_final)

    usrnm_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',20,'bold'),text='USERNAME:')
    usrnm_profile_label.place(x=200,y=5)
    usrnm_profile_label1=tek.Label(prof_panel,bg='#2c2f33',fg='Gold',font=('Apple and Pear',20,'bold'),text=profval7)
    usrnm_profile_label1.place(x=350,y=5)

    fullname_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',20,'bold'),text='FULL NAME:')
    fullname_profile_label.place(x=200,y=50)
    fullname_profile_label1=tek.Label(prof_panel,bg='#2c2f33',fg='Gold',font=('Apple and Pear',20,'bold'),text=profval2)
    fullname_profile_label1.place(x=350,y=50)

    location_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',20,'bold'),text='LOCATION:')
    location_profile_label.place(x=200,y=95)
    location_profile_label1=tek.Label(prof_panel,bg='#2c2f33',fg='Gold',font=('Apple and Pear',20,'bold'),text=profval9)
    location_profile_label1.place(x=350,y=95)

    status_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',20,'bold'),text='STATUS:')
    status_profile_label.place(x=200,y=140)
    status_profile_label1=tek.Label(prof_panel,bg='#2c2f33',fg='Gold',font=('Apple and Pear',20,'bold'),text=profval11)
    status_profile_label1.place(x=350,y=140)

    gender_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',20,'bold'),text='GENDER:')
    gender_profile_label.place(x=200,y=185)
    gender_profile_label1=tek.Label(prof_panel,bg='#2c2f33',fg='Gold',font=('Apple and Pear',20,'bold'),text=profval4)
    gender_profile_label1.place(x=350,y=185)

    age_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',20,'bold'),text='AGE:')
    age_profile_label.place(x=600,y=5)
    age_profile_label1=tek.Label(prof_panel,bg='#2c2f33',fg='Gold',font=('Apple and Pear',20,'bold'),text=profval3)
    age_profile_label1.place(x=750,y=5)

    emailid_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',20,'bold'),text='EMAIL ID:')
    emailid_profile_label.place(x=600,y=50)
    emailid_profile_label1=tek.Label(prof_panel,bg='#2c2f33',fg='Gold',font=('Apple and Pear',20,'bold'),text=profval6)
    emailid_profile_label1.place(x=750,y=50)

    bal_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',20,'bold'),text='BALANCE:')
    bal_profile_label.place(x=600,y=95)
    bal_profile_label1=tek.Label(prof_panel,bg='#2c2f33',fg='Gold',font=('Apple and Pear',20,'bold'),text=(profval10,"G-Coins"))
    bal_profile_label1.place(x=750,y=95)

    cursor.execute('SELECT TIMESTAMPDIFF(DAY,"%s", NOW()) AS difference'%profval13)
    resultl=cursor.fetchall()
    for outputl in resultl:
        for lvlvalue in outputl:
            lvlcheck = lvlvalue
    lvlcheckfinal = lvlcheck//3

    level_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',20,'bold'),text='LEVEL:')
    level_profile_label.place(x=600,y=185)
    level_profile_label1=tek.Label(prof_panel,bg='#2c2f33',fg='Gold',font=('Apple and Pear',20,'bold'),text=lvlcheckfinal)
    level_profile_label1.place(x=750,y=185)

    #music
    global audioplay
    if audioplay == False:
        audioplayback()

    def Add_Balance_Page():
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg7)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        #Add Balance Panel
        addb_panel=tek.Label(panel,bg='#2c2f33',height=25,width=105)
        addb_panel.place(x=304,y=170)

        addb_label1=tek.Label(addb_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='RAN OUT OF G-COINS?')
        addb_label1.place(x=175,y=2)
        addb_label2=tek.Label(addb_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="TIME TO REPLENISH YOUR WALLET!")
        addb_label2.place(x=240,y=50)

        back_btn=tek.Button(master=addb_panel,text="< Back",font=('Avellana Pro',18,'bold'),bg="Orange",fg="Blue",cursor="hand2",bd=0,activebackground='lime',activeforeground='blue',command=show_profile_page)
        back_btn.place(relx=0.0,rely=0.0,width=100,height=35)

        cursor.execute('SELECT Balance FROM Accounts WHERE Username = "%s"'% username)
        result=cursor.fetchall()
        for output in result:
            for value in output:
                balance=value

        balance_label=tek.Label(addb_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',25,'bold'),text='CURRENT BALANCE:')
        balance_label.place(x=125,y=100)
        balance_label1=tek.Label(addb_panel,bg='#2c2f33',fg='Gold',font=('Apple and Pear',25,'bold'),text=(balance,"G-Coins"))
        balance_label1.place(x=415,y=100)

        addbal_label=tek.Label(addb_panel,bg='#2c2f33',fg='Gold',font=('Avellana Pro',23,'bold'),text='ENTER AMOUNT TO ADD:')
        addbal_label.place(x=50,y=200)
        addbal= tek.Entry(master=addb_panel,bg='Orange',fg='Yellow',font=('Agency FB',25,'bold'))
        addbal.place(x=395,y=200)

        balance_label2=tek.Label(addb_panel,bg='#2c2f33',fg='#2c2f33',font=('Apple and Pear',15,'bold'),text="PLEASE REFRESH THE PAGE TO VIEW UPDATED BALANCE..")
        balance_label2.place(x=135,y=270)

        def loading2():
            panel.after(10,lambda:addb.config(fg='Gold',text='PLEASE WAIT'))
            panel.after(1010,lambda:addb.config(fg='Gold',text='PLEASE WAIT.'))
            panel.after(2010,lambda:addb.config(fg='Gold',text='PLEASE WAIT..'))
            panel.after(3010,lambda:addb.config(fg='Gold',text='PLEASE WAIT...'))
            panel.after(4010,lambda:addb.config(fg='Gold',text='PLEASE WAIT....'))
            panel.after(5010,lambda:addb.config(fg='Gold',text='PLEASE WAIT.....'))

        def add_balance():
            loading2()
            baladd=int(addbal.get())
            cursor.execute('UPDATE Accounts SET Balance = Balance + %s Where Username = "%s"' % (baladd,username) )
            cursor.execute('UPDATE Inventory SET Balance = Balance + %s Where Username = "%s"' % (baladd,username) )
            conn.commit()
            panel.after(6010,lambda:addb.config(text="BALANCE UPDATED!",font=('Battlelines',15,'bold'),fg='Lime'))
            panel.after(11010,lambda:addb.config(text="ADD BALANCE",font=('Battlelines',15,'bold'),fg='Yellow'))
            panel.after(6010,lambda:balance_label2.config(fg="Lime"))

        addb=tek.Button(master=addb_panel,text="ADD BALANCE",font=('Battlelines',15,'bold'),bg="Red",fg="Yellow",cursor="hand2",bd=0,activebackground='lime',activeforeground='blue',command=add_balance)
        addb.place(x=230,y=310,width=250,height=55)
        Window.update()

    def show_add_balance_page():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Add_Balance_Page()

    edit_bal_btn=tek.Button(master=prof_panel,text="ADD BALANCE",font=('Avellana Pro',15,'bold'),bg="Orange",fg="Blue",cursor="hand2",bd=0,activebackground='lime',activeforeground='blue',command=show_add_balance_page)
    edit_bal_btn.place(x=925,y=95,width=150,height=35)

    def Edit_Profile_Page():
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg4)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        def btinte(e):
            e.widget.config(bg='blue')
            return
        def btintl(e):
            e.widget.config(bg='red')
            return
        #Edit Profile panel
        profile_panel=tek.Label(panel,bg='#2c2f33',height=42,width=140)
        profile_panel.place(x=180,y=50)

        profile_label1=tek.Label(profile_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='EDIT PROFILE')
        profile_label1.place(x=348,y=2)
        profile_label2=tek.Label(profile_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="WANNA CHANGE DETAILS?")
        profile_label2.place(x=375,y=50)

        prof_panel=tek.Label(profile_panel,bg='#23272a',height=42,width=140,relief=tek.RIDGE)
        prof_panel.place(x=-2,y=70)

        back_btn=tek.Button(master=profile_panel,text="< Back",font=('Avellana Pro',18,'bold'),bg="Orange",fg="Blue",cursor="hand2",bd=0,activebackground='lime',activeforeground='blue',command=show_profile_page)
        back_btn.place(relx=0.0,rely=0.0,width=100,height=35)

        dp_panel=tek.Label(prof_panel)
        dp_panel.place(x = 0, y = 0)

        cursor.execute('SELECT * FROM Accounts WHERE Username = "%s"'% username)
        result=cursor.fetchall()
        i=1
        for column in result:
            for value in column:
                globals()["profval" + str(i)] = value
                i += 1

        dp_panel.config(image=acct_dp_final)
        def edit_dp():
            global acct_dp
            global acct_dp1
            global acct_dp_final
            global acct_dp_final1
            global cursor
            filepath = askopenfilename(filetypes=[("Image Files", "*.jpg"),("Image Files", "*.png"), ("Image Files", "*.jpeg"), ("All Files", "*.*")])
            if not filepath:
                return
            
            Imgdp= Image.open(filepath)
            Imgdp1= Imgdp.resize((180,250))
            Imgdp1 = ImageTk.PhotoImage(Imgdp1)
            dp_panel.config(image=Imgdp1)
            dp_panel.image=Imgdp1
            cursor.execute('UPDATE Accounts SET Profile_Picture= "%s" WHERE Username="%s"'%(filepath,username))
            conn.commit()
            acct_dp=filepath
            acct_dp_final=Image.open(acct_dp)
            acct_dp_final=acct_dp_final.resize((180,250))
            acct_dp_final=ImageTk.PhotoImage(acct_dp_final)
            acct_dp1=filepath
            acct_dp_final1=Image.open(acct_dp1)
            acct_dp_final1=acct_dp_final1.resize((50,50))
            acct_dp_final1=ImageTk.PhotoImage(acct_dp_final1)
            cursor=conn.cursor()
        dp_edit_btn=tek.Button(prof_panel,bg='Gold',fg='Blue',bd=0,font=('Avellana Pro',13,'bold'),text='EDIT PROFILE PICTURE',activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=edit_dp)
        dp_edit_btn.place(x=0,y=400)
        usrnm_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',25,'bold'),text='USERNAME:')
        usrnm_profile_label.place(x=190,y=20)
        edit_usrnm= tek.Entry(master=prof_panel,bg='Orange',fg='Blue',font=('Agency FB',15,'bold'))
        edit_usrnm.place(x=370,y=20)
        #Handling Errors with Username Entry
        def username_check():
            global usrnm_error
            global usrnmval
            usrnmval=edit_usrnm.get()
            cursor.execute('SELECT EXISTS(SELECT Username FROM Accounts WHERE Username = "%s")' % usrnmval)
            result=cursor.fetchall()
            for output in result:
                for value in output:
                    usrnmvalcheck = value
            if usrnmvalcheck == 1:
                usrnm_error=True
                usrnm_profile_label.config(fg='Red')
                edit_usrnm.config(bg='Red')
            else:
                usrnm_error=False
                usrnm_profile_label.config(fg='Lime')
                edit_usrnm.config(bg='Orange')
        def editusrnm():
            global username
            username_check()
            username = usrnmval
            details1=(usrnmval,profval1)
            if usrnm_error==False:
                edit_usrnm_error.config(fg="#23272a")
                cursor.execute('UPDATE Accounts SET Username = "%s" WHERE Acct_ID = %s'%details1)
                cursor.execute('UPDATE Inventory SET Username = "%s" WHERE Acct_ID = %s'%details1)
                edit_usrnm_done.config(fg="Green")
                conn.commit()
            else:
                edit_usrnm_error.config(fg="Red")
        edit_usrnm_btn=tek.Button(prof_panel,bg='Gold',fg='Blue',bd=0,font=('Avellana Pro',15,'bold'),text='EDIT USERNAME',activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=editusrnm)
        edit_usrnm_btn.place(x=600,y=20)
        edit_usrnm_error=tek.Label(prof_panel,bg='#23272a',fg='#23272a',font=('Avellana Pro',12,'bold'),text="USERNAME ALREADY TAKEN")
        edit_usrnm_error.place(x=750,y=20)
        edit_usrnm_done=tek.Label(prof_panel,bg='#23272a',fg='#23272a',font=('Avellana Pro',12,'bold'),text="DONE!")
        edit_usrnm_done.place(x=750,y=40)

        fullname_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',25,'bold'),text='FULL NAME:')
        fullname_profile_label.place(x=190,y=100)
        edit_fullname= tek.Entry(master=prof_panel,bg='Orange',fg='Blue',font=('Agency FB',15,'bold'))
        edit_fullname.place(x=370,y=100)
        def editfullname():
            global fullnameval
            fullnameval=edit_fullname.get()
            details2=(fullnameval,profval1)
            cursor.execute('UPDATE Accounts SET Full_Name = "%s" WHERE Acct_ID = %s'%details2)
            cursor.execute('UPDATE Inventory SET Full_Name = "%s" WHERE Acct_ID = %s'%details2)
            edit_fullname_done.config(fg="Green")
            conn.commit()
        edit_fullname_btn=tek.Button(prof_panel,bg='Gold',fg='Blue',bd=0,font=('Avellana Pro',15,'bold'),text='EDIT FULL NAME',activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=editfullname)
        edit_fullname_btn.place(x=600,y=100)
        edit_fullname_done=tek.Label(prof_panel,bg='#23272a',fg='#23272a',font=('Avellana Pro',12,'bold'),text="DONE!")
        edit_fullname_done.place(x=750,y=125)

        location_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',25,'bold'),text='LOCATION:')
        location_profile_label.place(x=190,y=180)
        edit_location= tek.Entry(master=prof_panel,bg='Orange',fg='Blue',font=('Agency FB',15,'bold'))
        edit_location.place(x=370,y=180)
        def editlocation():
            global locationval
            locationval=edit_location.get()
            details3=(locationval,profval1)
            cursor.execute('UPDATE Accounts SET Location = "%s" WHERE Acct_ID = %s'%details3)
            edit_location_done.config(fg="Green")
            conn.commit()
        edit_location_btn=tek.Button(prof_panel,bg='Gold',fg='Blue',bd=0,font=('Avellana Pro',15,'bold'),text='EDIT LOCATION',activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=editlocation)
        edit_location_btn.place(x=600,y=180)
        edit_location_done=tek.Label(prof_panel,bg='#23272a',fg='#23272a',font=('Avellana Pro',12,'bold'),text="DONE!")
        edit_location_done.place(x=750,y=205)

        status_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',25,'bold'),text='STATUS:')
        status_profile_label.place(x=190,y=260)
        edit_status= tek.Entry(master=prof_panel,bg='Orange',fg='Blue',font=('Agency FB',15,'bold'))
        edit_status.place(x=370,y=260)
        def editstatus():
            global statusval
            statusval=edit_status.get()
            details4=(statusval,profval1)
            cursor.execute('UPDATE Accounts SET Status = "%s" WHERE Acct_ID = %s'%details4)
            edit_status_done.config(fg="Green")
            conn.commit()
        edit_status_btn=tek.Button(prof_panel,bg='Gold',fg='Blue',bd=0,font=('Avellana Pro',15,'bold'),text='EDIT STATUS',activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=editstatus)
        edit_status_btn.place(x=600,y=260)
        edit_status_done=tek.Label(prof_panel,bg='#23272a',fg='#23272a',font=('Avellana Pro',12,'bold'),text="DONE!")
        edit_status_done.place(x=750,y=285)

        emailid_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',25,'bold'),text='EMAIL ID:')
        emailid_profile_label.place(x=190,y=340)
        edit_emailid= tek.Entry(master=prof_panel,bg='Orange',fg='Blue',font=('Agency FB',15,'bold'))
        edit_emailid.place(x=370,y=340)
        def editemailid():
            global emailidval
            emailidval=edit_emailid.get()
            details5=(emailidval,profval1)
            cursor.execute('UPDATE Accounts SET Email_ID = "%s" WHERE Acct_ID = %s'%details5)
            cursor.execute('UPDATE Inventory SET Email_ID = "%s" WHERE Acct_ID = %s'%details5)
            edit_emailid_done.config(fg="Green")
            conn.commit()
        edit_emailid_btn=tek.Button(prof_panel,bg='Gold',fg='Blue',bd=0,font=('Avellana Pro',15,'bold'),text='EDIT EMAIL ID',activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=editemailid)
        edit_emailid_btn.place(x=600,y=340)
        edit_emailid_done=tek.Label(prof_panel,bg='#23272a',fg='#23272a',font=('Avellana Pro',12,'bold'),text="DONE!")
        edit_emailid_done.place(x=750,y=365)

        age_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',25,'bold'),text='AGE:')
        age_profile_label.place(x=190,y=420)
        edit_age= tek.Entry(master=prof_panel,bg='Orange',fg='Blue',font=('Agency FB',15,'bold'))
        edit_age.place(x=370,y=420)
        def editage():
            global cursor
            global dobyear
            global ageval1
            ageval1=int(edit_age.get())
            details6=(ageval1,profval1)
            cursor.execute('UPDATE Accounts SET Age = %s WHERE Acct_ID = %s'%details6)
            conn.commit()
            cursor=conn.cursor()
            cursor.execute('SELECT YEAR(CURDATE()) FROM Accounts WHERE username = "%s"' % username)
            result=cursor.fetchall()
            for output in result:
                for value in output:
                    dobyear = int(value)
            dobyear = dobyear - ageval1
            cursor.execute('UPDATE Accounts SET Date_Of_Birth = Date_Format(Date_Of_Birth,"{}-%m-%d")WHERE Username = "{}"'.format(dobyear,username))
            conn.commit()
            cursor=conn.cursor()
            edit_age_done.config(fg="Green")
        edit_age_btn=tek.Button(prof_panel,bg='Gold',fg='Blue',bd=0,font=('Avellana Pro',15,'bold'),text='EDIT AGE',activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=editage)
        edit_age_btn.place(x=600,y=420)
        edit_age_done=tek.Label(prof_panel,bg='#23272a',fg='#23272a',font=('Avellana Pro',12,'bold'),text="DONE!")
        edit_age_done.place(x=750,y=445)

        pswd_profile_label=tek.Label(prof_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',25,'bold'),text='PASSWORD:')
        pswd_profile_label.place(x=190,y=500)
        edit_pswd= tek.Entry(master=prof_panel,bg='Orange',fg='Blue',font=('Agency FB',15,'bold'))
        edit_pswd.place(x=370,y=500)
        def editpswd():
            global pswdval
            pswdval=edit_pswd.get()
            details7=(pswdval,profval1)
            cursor.execute('UPDATE Accounts SET Password = "%s" WHERE Acct_ID = %s'%details7)
            edit_pswd_done.config(fg="Green")
            conn.commit()
        edit_pswd_btn=tek.Button(prof_panel,bg='Gold',fg='Blue',bd=0,font=('Avellana Pro',15,'bold'),text='EDIT PASSWORD',activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=editpswd)
        edit_pswd_btn.place(x=600,y=500)
        edit_pswd_done=tek.Label(prof_panel,bg='#23272a',fg='#23272a',font=('Avellana Pro',12,'bold'),text="DONE!")
        edit_pswd_done.place(x=800,y=525)

    def show_edit_profile_page():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Edit_Profile_Page()

    edit_profile_btn=tek.Button(prof_panel,bg='Gold',fg='Blue',bd=0,font=('Avellana Pro',20,'bold'),text='EDIT PROFILE',activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_edit_profile_page)
    edit_profile_btn.place(relx=1.0,y=0,anchor="ne")

    def loading4():
            panel.after(10,lambda:logout_btn.config(fg='Black',text='PLEASE WAIT'))
            panel.after(1010,lambda:logout_btn.config(fg='Black',text='PLEASE WAIT.'))
            panel.after(2010,lambda:logout_btn.config(fg='Black',text='PLEASE WAIT..'))
            panel.after(3010,lambda:logout_btn.config(fg='Black',text='PLEASE WAIT...'))
            panel.after(4010,lambda:logout_btn.config(fg='Black',text='PLEASE WAIT....'))
            panel.after(5010,lambda:logout_btn.config(fg='Black',text='PLEASE WAIT.....'))
    def logout():
        global status
        loading4()
        status="Logged Out"
        panel.after(6010,show_home_page)
    logout_btn=tek.Button(prof_panel,bg='Red',fg='Brown',bd=0,font=('Avellana Pro',20,'bold'),text='Log Out',activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=logout)
    logout_btn.place(relx=1.0,rely=1.0,anchor="se",width=170)

    m=1
    for img in ["Media/C1.jpg","Media/C2.jpg","Media/C3.png"]:
        Cimgpath = img
        Cimg = Image.open(Cimgpath)
        Cimg = Cimg.resize((218,150))
        Cimg = ImageTk.PhotoImage(Cimg)
        globals()["cimg" + str(m)] = Cimg
        m += 1

    def btinte1(e):
        e.widget.config(bg='yellow')
        return
    def btintl1(e):
        e.widget.config(bg='#23272a')
        return

    viewinv_profile_label=tek.Label(profile_panel,bg='#23272a',fg='Blue',bd=0,height=150,width=218,image=cimg1,anchor="n")
    viewinv_profile_label.place(x=100,y=375)
    viewinv_profile_btn=tek.Button(profile_panel,bg='#23272a',fg='Orange',bd=0,text='VIEW INVENTORY',font=('Avellana Pro',20,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_inventory_pages)
    viewinv_profile_btn.place(x=100,y=525)

    browse_profile_label=tek.Label(profile_panel,bg='#23272a',fg='Blue',bd=0,height=150,width=218,image=cimg3,anchor="n")
    browse_profile_label.place(x=550,y=375)
    browse_profile_btn=tek.Button(profile_panel,bg='#23272a',fg='Orange',bd=0,text=' BROWSE GAMES ',font=('Avellana Pro',20,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_browse_pages)
    browse_profile_btn.place(x=550,y=525)

    def Delete_Account_Page():
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        #Delete Account Panel
        delacc_panel=tek.Label(panel,bg='#2c2f33',height=25,width=105)
        delacc_panel.place(x=304,y=170)

        delacc_label1=tek.Label(delacc_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='WANNA DELETE YOUR ACCOUNT?')
        delacc_label1.place(x=80,y=2)
        delacc_label2=tek.Label(delacc_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',15,'bold'),text="WHY!? JUST WHY!? THINK AGAIN! : (")
        delacc_label2.place(x=220,y=50)

        delacc_label=tek.Label(delacc_panel,bg='#2c2f33',fg='Gold',font=('Avellana Pro',25,'bold'),text='ARE YOU REALLY DAMN SURE\nYOU WANNA DELETE YOUR ACCOUNT??')
        delacc_label.place(x=92,y=130)

        def loading3():
            panel.after(10,lambda:yes_btn.config(fg='Black',text='PLEASE WAIT'))
            panel.after(1010,lambda:yes_btn.config(fg='Black',text='PLEASE WAIT.'))
            panel.after(2010,lambda:yes_btn.config(fg='Black',text='PLEASE WAIT..'))
            panel.after(3010,lambda:yes_btn.config(fg='Black',text='PLEASE WAIT...'))
            panel.after(4010,lambda:yes_btn.config(fg='Black',text='PLEASE WAIT....'))
            panel.after(5010,lambda:yes_btn.config(fg='Black',text='PLEASE WAIT.....'))

        def Delete_Account():
            global status
            loading3()
            cursor.execute('DELETE FROM Accounts Where Username = "%s"' % username)
            cursor.execute('DELETE FROM Inventory Where Username = "%s"' % username)
            conn.commit()
            panel.after(6010,lambda:yes_btn.config(text="ACCOUNT DELETED!",font=('Battlelines',15,'bold'),fg='Black'))
            status="Logged Out"
            panel.after(8010,show_home_page)

        yes_btn=tek.Button(master=delacc_panel,text="YES",font=('Battlelines',15,'bold'),bg="Red",fg="Black",cursor="hand2",bd=0,activebackground='Red',activeforeground='Brown',command=Delete_Account)
        yes_btn.place(x=420,y=310,width=210,height=55)
        no_btn=tek.Button(master=delacc_panel,text="NO",font=('Battlelines',15,'bold'),bg="Lime",fg="Yellow",cursor="hand2",bd=0,activebackground='lime',activeforeground='blue',command=show_profile_page)
        no_btn.place(x=100,y=310,width=210,height=55)
        Window.update()

    def show_delete_account_page():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Delete_Account_Page()

    delacc_profile_label=tek.Label(profile_panel,bg='#23272a',fg='Blue',bd=0,height=150,width=218,image=cimg2,anchor="n")
    delacc_profile_label.place(x=1015,y=375)
    delacc_profile_btn=tek.Button(profile_panel,bg='#23272a',fg='Orange',bd=0,text='DELETE ACCOUNT',font=('Avellana Pro',20,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_delete_account_page)
    delacc_profile_btn.place(x=1015,y=525)

    for btn in [viewinv_profile_btn,browse_profile_btn,delacc_profile_btn]:
        btn.bind("<Enter>",btinte1)
        btn.bind("<Leave>",btintl1)
    Window.update()

def Browse_Pages():
    #Background
    frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
    frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    panel = tek.Label(frame0, image = BGimg2)
    panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    #music
    global audioplay
    if audioplay == False:
        audioplayback()
    
    def Browse_Page_1():
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg2)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        def btinte(e):
            e.widget.config(bg='blue')
            return
        def btintl(e):
            e.widget.config(bg='red')
            return

        images=['Media/ft1.jpg','Media/ft2.jpg','Media/ft3.jpg','Media/ft3(1).jpg','Media/ft4.jpg','Media/ft5.jpg','Media/ft5(1).jpg','Media/ft6.jpg','Media/ft7.jpg','Media/ft7(1).jpg','Media/ft8.jpg','Media/ft9.jpg','Media/ft10.jpg','Media/ft11.jpg','Media/ft12.jpg','Media/ft13.jpg','Media/ft14.jpg','Media/ft15.jpg']

        b=1
        for image in images:
            FTimgpath = image
            FTimg = Image.open(FTimgpath)
            FTimg = FTimg.resize((194,120))
            FTimg = ImageTk.PhotoImage(FTimg)
            globals()["bimage" + str(b)] = FTimg
            b += 1
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',state=tek.ACTIVE)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)
        
        if status == "Logged In":
            login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
            login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
            pp=tek.Label(frame1,image=acct_dp_final1)
            pp.place(relx=1.0,y=0,anchor="ne")
        else:
            login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_login_page)
            login_btn.place(x=1246,y=0,width=120,height=52)

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Browse Panel
        browse_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        browse_panel.place(x=50,y=58)
        browse_label1=tek.Label(browse_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='BROWSE GAMES')
        browse_label1.place(x=485,y=2)
        browse_label2=tek.Label(browse_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="GRAB YOUR CONTROLLERS, LONG GAMING SESSIONS INCOMING!")
        browse_label2.place(x=407,y=50)

        browse_game_label0=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage4,anchor="n")
        browse_game_label0.place(x=22,y=85)
        browse_game_btn0=tek.Button(browse_panel,command=acv,bg='#23272a',fg='Orange',bd=0,text="Assassin's Creed\nValhalla",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn0.place(x=22,y=195,height=48,width=194)

        browse_game_label1=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage2,anchor="n")
        browse_game_label1.place(x=22,y=255)
        browse_game_btn1=tek.Button(browse_panel,command=cybp,bg='#23272a',fg='Orange',bd=0,text='CyberPunk 2077',font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn1.place(x=22,y=365,height=48,width=194)

        browse_game_label2=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage7,anchor="n")
        browse_game_label2.place(x=22,y=425)
        browse_game_btn2=tek.Button(browse_panel,command=hi,bg='#23272a',fg='Orange',bd=0,text='Halo Infinite',font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn2.place(x=22,y=535,height=48,width=194)

        browse_game_label3=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage1,anchor="n")
        browse_game_label3.place(x=277,y=85)
        browse_game_btn3=tek.Button(browse_panel,command=mas,bg='#23272a',fg='Orange',bd=0,text="Marvel's Avengers",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn3.place(x=277,y=195,height=48,width=194)

        browse_game_label4=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage5,anchor="n")
        browse_game_label4.place(x=277,y=255)
        browse_game_btn4=tek.Button(browse_panel,command=au,bg='#23272a',fg='Orange',bd=0,text='Among Us',font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn4.place(x=277,y=365,height=48,width=194)

        browse_game_label5=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage8,anchor="n")
        browse_game_label5.place(x=277,y=425)
        browse_game_btn5=tek.Button(browse_panel,command=codbocw,bg='#23272a',fg='Orange',bd=0,text='Call Of Duty: Black Ops\nCold War',font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn5.place(x=277,y=535,height=48,width=194)

        browse_game_label6=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage10,anchor="n")
        browse_game_label6.place(x=533,y=85)
        browse_game_btn6=tek.Button(browse_panel,command=hzd,bg='#23272a',fg='Orange',bd=0,text='Horizon: Zero Dawn',font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn6.place(x=533,y=195,height=48,width=194)

        browse_game_label7=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage11,anchor="n")
        browse_game_label7.place(x=533,y=255)
        browse_game_btn7=tek.Button(browse_panel,command=tasm,bg='#23272a',fg='Orange',bd=0,text='The Amazing\nSpider-Man',font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn7.place(x=533,y=365,height=48,width=194)

        browse_game_label8=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage12,anchor="n")
        browse_game_label8.place(x=533,y=425)
        browse_game_btn8=tek.Button(browse_panel,command=tasm2,bg='#23272a',fg='Orange',bd=0,text='The Amazing\nSpider-Man 2',font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn8.place(x=533,y=535,height=48,width=194)

        browse_game_label9=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage13,anchor="n")
        browse_game_label9.place(x=789,y=85)
        browse_game_btn9=tek.Button(browse_panel,command=mc,bg='#23272a',fg='Orange',bd=0,text='Minecraft',font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn9.place(x=789,y=195,height=48,width=194)

        browse_game_label10=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage14,anchor="n")
        browse_game_label10.place(x=789,y=255)
        browse_game_btn10=tek.Button(browse_panel,command=fg,bg='#23272a',fg='Orange',bd=0,text='Fall Guys',font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn10.place(x=789,y=365,height=48,width=194)

        browse_game_label11=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage15,anchor="n")
        browse_game_label11.place(x=789,y=425)
        browse_game_btn11=tek.Button(browse_panel,command=rl,bg='#23272a',fg='Orange',bd=0,text='Rocket League',font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn11.place(x=789,y=535,height=48,width=194)

        browse_game_label12=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage16,anchor="n")
        browse_game_label12.place(x=1044,y=85)
        browse_game_btn12=tek.Button(browse_panel,command=codmw,bg='#23272a',fg='Orange',bd=0,text='Call Of Duty:\nModern Warfare',font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn12.place(x=1044,y=195,height=48,width=194)

        browse_game_label13=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage17,anchor="n")
        browse_game_label13.place(x=1044,y=255)
        browse_game_btn13=tek.Button(browse_panel,command=cntrl,bg='#23272a',fg='Orange',bd=0,text='CONTROL',font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn13.place(x=1044,y=365,height=48,width=194)

        browse_game_label14=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage18,anchor="n")
        browse_game_label14.place(x=1044,y=425)
        browse_game_btn14=tek.Button(browse_panel,command=wwz,bg='#23272a',fg='Orange',bd=0,text='World War Z',font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn14.place(x=1044,y=535,height=48,width=194)

        browse_back_btn=tek.Button(browse_panel,bg='Grey',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
        browse_back_btn.place(x=330,y=590,width=80)
        browse_btn1=tek.Button(browse_panel,bg='Grey',fg='Cyan',bd=0,text='1',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
        browse_btn1.place(x=430,y=590,width=80)
        browse_btn2=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b2)
        browse_btn2.place(x=530,y=590,width=80)
        browse_btn3=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b3)
        browse_btn3.place(x=630,y=590,width=80)
        browse_btn4=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b4)
        browse_btn4.place(x=730,y=590,width=80)
        browse_next_btn=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b2)
        browse_next_btn.place(x=830,y=590,width=80)
        Window.update()

    def Browse_Page_2():
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg3)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        def btinte(e):
            e.widget.config(bg='blue')
            return
        def btintl(e):
            e.widget.config(bg='red')
            return

        images=['Media/ft16.jpg','Media/ft17.jpg','Media/ft18.jpg','Media/ft19.jpg','Media/ft20.jpg','Media/ft21.jpg','Media/ft22.jpg','Media/ft23.jpg','Media/ft24.jpg','Media/ft25.jpg','Media/ft26.jpg','Media/ft27.jpg','Media/ft28.jpg','Media/ft29.jpg','Media/ft30.jpg']

        b=1
        for image in images:
            FTimgpath = image
            FTimg = Image.open(FTimgpath)
            FTimg = FTimg.resize((194,120))
            FTimg = ImageTk.PhotoImage(FTimg)
            globals()["bimage" + str(b)] = FTimg
            b += 1
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',state=tek.ACTIVE)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        if status == "Logged In":
            login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
            login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
            pp=tek.Label(frame1,image=acct_dp_final1)
            pp.place(relx=1.0,y=0,anchor="ne")
        else:
            login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_login_page)
            login_btn.place(x=1246,y=0,width=120,height=52)

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Browse Panel
        browse_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        browse_panel.place(x=50,y=58)
        browse_label1=tek.Label(browse_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='BROWSE GAMES')
        browse_label1.place(x=485,y=2)
        browse_label2=tek.Label(browse_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="GRAB YOUR CONTROLLERS, LONG GAMING SESSIONS INCOMING!")
        browse_label2.place(x=407,y=50)

        browse_game_label0=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage1,anchor="n")
        browse_game_label0.place(x=22,y=85)
        browse_game_btn0=tek.Button(browse_panel,command=ac1,bg='#23272a',fg='Orange',bd=0,text="Assassin's Creed",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn0.place(x=22,y=195,height=48,width=194)

        browse_game_label1=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage2,anchor="n")
        browse_game_label1.place(x=22,y=255)
        browse_game_btn1=tek.Button(browse_panel,command=ac2,bg='#23272a',fg='Orange',bd=0,text="Assassin's Creed 2",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn1.place(x=22,y=365,height=48,width=194)

        browse_game_label2=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage3,anchor="n")
        browse_game_label2.place(x=22,y=425)
        browse_game_btn2=tek.Button(browse_panel,command=acbh,bg='#23272a',fg='Orange',bd=0,text="Assassin's Creed\nBrotherhood",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn2.place(x=22,y=535,height=48,width=194)

        browse_game_label3=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage4,anchor="n")
        browse_game_label3.place(x=277,y=85)
        browse_game_btn3=tek.Button(browse_panel,command=acrvs,bg='#23272a',fg='Orange',bd=0,text="Assassin's Creed\nRevelations",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn3.place(x=277,y=195,height=48,width=194)

        browse_game_label4=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage5,anchor="n")
        browse_game_label4.place(x=277,y=255)
        browse_game_btn4=tek.Button(browse_panel,command=ac3,bg='#23272a',fg='Orange',bd=0,text="Assassin's Creed 3",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn4.place(x=277,y=365,height=48,width=194)

        browse_game_label5=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage6,anchor="n")
        browse_game_label5.place(x=277,y=425)
        browse_game_btn5=tek.Button(browse_panel,command=ac4bf,bg='#23272a',fg='Orange',bd=0,text="Assassin's Creed 4\nBlack Flag",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn5.place(x=277,y=535,height=48,width=194)

        browse_game_label6=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage7,anchor="n")
        browse_game_label6.place(x=533,y=85)
        browse_game_btn6=tek.Button(browse_panel,command=acrg,bg='#23272a',fg='Orange',bd=0,text="Assassin's Creed\nRogue",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn6.place(x=533,y=195,height=48,width=194)

        browse_game_label7=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage8,anchor="n")
        browse_game_label7.place(x=533,y=255)
        browse_game_btn7=tek.Button(browse_panel,command=acu,bg='#23272a',fg='Orange',bd=0,text="Assassin's Creed\nUnity",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn7.place(x=533,y=365,height=48,width=194)

        browse_game_label8=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage9,anchor="n")
        browse_game_label8.place(x=533,y=425)
        browse_game_btn8=tek.Button(browse_panel,command=acs,bg='#23272a',fg='Orange',bd=0,text="Assassin's Creed\nSyndicate",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn8.place(x=533,y=535,height=48,width=194)

        browse_game_label9=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage10,anchor="n")
        browse_game_label9.place(x=789,y=85)
        browse_game_btn9=tek.Button(browse_panel,command=acor,bg='#23272a',fg='Orange',bd=0,text="Assassin's Creed\nOrigins",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn9.place(x=789,y=195,height=48,width=194)

        browse_game_label10=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage11,anchor="n")
        browse_game_label10.place(x=789,y=255)
        browse_game_btn10=tek.Button(browse_panel,command=acod,bg='#23272a',fg='Orange',bd=0,text="Assassin's Creed\nOdyssey",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn10.place(x=789,y=365,height=48,width=194)

        browse_game_label11=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage12,anchor="n")
        browse_game_label11.place(x=789,y=425)
        browse_game_btn11=tek.Button(browse_panel,command=baa,bg='#23272a',fg='Orange',bd=0,text="Batman Arkham\nAsylum",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn11.place(x=789,y=535,height=48,width=194)

        browse_game_label12=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage13,anchor="n")
        browse_game_label12.place(x=1044,y=85)
        browse_game_btn12=tek.Button(browse_panel,command=bac,bg='#23272a',fg='Orange',bd=0,text='Batman Arkham City',font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn12.place(x=1044,y=195,height=48,width=194)

        browse_game_label13=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage14,anchor="n")
        browse_game_label13.place(x=1044,y=255)
        browse_game_btn13=tek.Button(browse_panel,command=bao,bg='#23272a',fg='Orange',bd=0,text='Batman Arkham\nOrigins',font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn13.place(x=1044,y=365,height=48,width=194)

        browse_game_label14=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage15,anchor="n")
        browse_game_label14.place(x=1044,y=425)
        browse_game_btn14=tek.Button(browse_panel,command=bak,bg='#23272a',fg='Orange',bd=0,text='Batman Arkham Knight',font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn14.place(x=1044,y=535,height=48,width=194)

        browse_back_btn=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b1)
        browse_back_btn.place(x=330,y=590,width=80)
        browse_btn1=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b1)
        browse_btn1.place(x=430,y=590,width=80)
        browse_btn2=tek.Button(browse_panel,bg='Grey',fg='Cyan',bd=0,text='2',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
        browse_btn2.place(x=530,y=590,width=80)
        browse_btn3=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b3)
        browse_btn3.place(x=630,y=590,width=80)
        browse_btn4=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b4)
        browse_btn4.place(x=730,y=590,width=80)
        browse_next_btn=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b3)
        browse_next_btn.place(x=830,y=590,width=80)
        Window.update()

    def Browse_Page_3():
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg4)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        def btinte(e):
            e.widget.config(bg='blue')
            return
        def btintl(e):
            e.widget.config(bg='red')
            return

        images=['Media/ft31.jpg','Media/ft32.jpg','Media/ft33.jpeg','Media/ft34.jpg','Media/ft35.jpg','Media/ft36.jpeg','Media/ft37.jpg','Media/ft38.jpg','Media/ft39.jpg','Media/ft40.jpg','Media/ft41.jpg','Media/ft42.png','Media/ft43.jpg','Media/ft44.png','Media/ft45.jpg']

        b=1
        for image in images:
            FTimgpath = image
            FTimg = Image.open(FTimgpath)
            FTimg = FTimg.resize((194,120))
            FTimg = ImageTk.PhotoImage(FTimg)
            globals()["bimage" + str(b)] = FTimg
            b += 1
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',state=tek.ACTIVE)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        if status == "Logged In":
            login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
            login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
            pp=tek.Label(frame1,image=acct_dp_final1)
            pp.place(relx=1.0,y=0,anchor="ne")
        else:
            login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_login_page)
            login_btn.place(x=1246,y=0,width=120,height=52)

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Browse Panel
        browse_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        browse_panel.place(x=50,y=58)
        browse_label1=tek.Label(browse_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='BROWSE GAMES')
        browse_label1.place(x=485,y=2)
        browse_label2=tek.Label(browse_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="GRAB YOUR CONTROLLERS, LONG GAMING SESSIONS INCOMING!")
        browse_label2.place(x=407,y=50)

        browse_game_label0=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage1,anchor="n")
        browse_game_label0.place(x=22,y=85)
        browse_game_btn0=tek.Button(browse_panel,command=dhd1,bg='#23272a',fg='Orange',bd=0,text="Dishonored",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn0.place(x=22,y=195,height=48,width=194)

        browse_game_label1=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage2,anchor="n")
        browse_game_label1.place(x=22,y=255)
        browse_game_btn1=tek.Button(browse_panel,command=dhd2,bg='#23272a',fg='Orange',bd=0,text="Dishonored 2",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn1.place(x=22,y=365,height=48,width=194)

        browse_game_label2=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage3,anchor="n")
        browse_game_label2.place(x=22,y=425)
        browse_game_btn2=tek.Button(browse_panel,command=dhddoto,bg='#23272a',fg='Orange',bd=0,text="Dishonored: Death Of\nthe Outsider",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn2.place(x=22,y=535,height=48,width=194)

        browse_game_label3=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage4,anchor="n")
        browse_game_label3.place(x=277,y=85)
        browse_game_btn3=tek.Button(browse_panel,command=re7,bg='#23272a',fg='Orange',bd=0,text="Resident Evil 7",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn3.place(x=277,y=195,height=48,width=194)

        browse_game_label4=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage5,anchor="n")
        browse_game_label4.place(x=277,y=255)
        browse_game_btn4=tek.Button(browse_panel,command=re2r,bg='#23272a',fg='Orange',bd=0,text="Resident Evil 2\nRemake",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn4.place(x=277,y=365,height=48,width=194)

        browse_game_label5=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage6,anchor="n")
        browse_game_label5.place(x=277,y=425)
        browse_game_btn5=tek.Button(browse_panel,command=re3r,bg='#23272a',fg='Orange',bd=0,text="Resident Evil 3\nRemake",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn5.place(x=277,y=535,height=48,width=194)

        browse_game_label6=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage7,anchor="n")
        browse_game_label6.place(x=533,y=85)
        browse_game_btn6=tek.Button(browse_panel,command=brdrl1,bg='#23272a',fg='Orange',bd=0,text="Borderlands",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn6.place(x=533,y=195,height=48,width=194)

        browse_game_label7=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage8,anchor="n")
        browse_game_label7.place(x=533,y=255)
        browse_game_btn7=tek.Button(browse_panel,command=brdrl2,bg='#23272a',fg='Orange',bd=0,text="Borderlands 2",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn7.place(x=533,y=365,height=48,width=194)

        browse_game_label8=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage9,anchor="n")
        browse_game_label8.place(x=533,y=425)
        browse_game_btn8=tek.Button(browse_panel,command=brdrltps,bg='#23272a',fg='Orange',bd=0,text="Borderlands:\nThe Pre-Sequel",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn8.place(x=533,y=535,height=48,width=194)

        browse_game_label9=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage10,anchor="n")
        browse_game_label9.place(x=789,y=85)
        browse_game_btn9=tek.Button(browse_panel,command=brdrl3,bg='#23272a',fg='Orange',bd=0,text="Borderlands 3",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn9.place(x=789,y=195,height=48,width=194)

        browse_game_label10=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage11,anchor="n")
        browse_game_label10.place(x=789,y=255)
        browse_game_btn10=tek.Button(browse_panel,command=wd1,bg='#23272a',fg='Orange',bd=0,text="Watch Dogs",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn10.place(x=789,y=365,height=48,width=194)

        browse_game_label11=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage12,anchor="n")
        browse_game_label11.place(x=789,y=425)
        browse_game_btn11=tek.Button(browse_panel,command=wd2,bg='#23272a',fg='Orange',bd=0,text="Watch Dogs 2",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn11.place(x=789,y=535,height=48,width=194)

        browse_game_label12=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage13,anchor="n")
        browse_game_label12.place(x=1044,y=85)
        browse_game_btn12=tek.Button(browse_panel,command=wdl,bg='#23272a',fg='Orange',bd=0,text='Watch Dogs Legion',font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn12.place(x=1044,y=195,height=48,width=194)

        browse_game_label13=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage14,anchor="n")
        browse_game_label13.place(x=1044,y=255)
        browse_game_btn13=tek.Button(browse_panel,command=smwos,bg='#23272a',fg='Orange',bd=0,text='Spider-Man:\nWeb Of Shadows',font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn13.place(x=1044,y=365,height=48,width=194)

        browse_game_label14=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage15,anchor="n")
        browse_game_label14.place(x=1044,y=425)
        browse_game_btn14=tek.Button(browse_panel,command=xmow,bg='#23272a',fg='Orange',bd=0,text='X-Men Origins:\nWolverine',font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn14.place(x=1044,y=535,height=48,width=194)

        browse_back_btn=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b2)
        browse_back_btn.place(x=330,y=590,width=80)
        browse_btn1=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b1)
        browse_btn1.place(x=430,y=590,width=80)
        browse_btn2=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b2)
        browse_btn2.place(x=530,y=590,width=80)
        browse_btn3=tek.Button(browse_panel,bg='Grey',fg='Cyan',bd=0,text='3',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
        browse_btn3.place(x=630,y=590,width=80)
        browse_btn4=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b4)
        browse_btn4.place(x=730,y=590,width=80)
        browse_next_btn=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b4)
        browse_next_btn.place(x=830,y=590,width=80)
        Window.update()

    def Browse_Page_4():
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg7)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        def btinte(e):
            e.widget.config(bg='blue')
            return
        def btintl(e):
            e.widget.config(bg='red')
            return

        images=['Media/ft46.jpg','Media/ft47.jpg','Media/ft48.jpg','Media/ft49.jpg','Media/ft50.jpg']

        b=1
        for image in images:
            FTimgpath = image
            FTimg = Image.open(FTimgpath)
            FTimg = FTimg.resize((194,120))
            FTimg = ImageTk.PhotoImage(FTimg)
            globals()["bimage" + str(b)] = FTimg
            b += 1
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',state=tek.ACTIVE)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        if status == "Logged In":
            login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
            login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
            pp=tek.Label(frame1,image=acct_dp_final1)
            pp.place(relx=1.0,y=0,anchor="ne")
        else:
            login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_login_page)
            login_btn.place(x=1246,y=0,width=120,height=52)

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Browse Panel
        browse_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        browse_panel.place(x=50,y=58)
        browse_label1=tek.Label(browse_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='BROWSE GAMES')
        browse_label1.place(x=485,y=2)
        browse_label2=tek.Label(browse_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="GRAB YOUR CONTROLLERS, LONG GAMING SESSIONS INCOMING!")
        browse_label2.place(x=407,y=50)

        browse_game_label0=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage1,anchor="n")
        browse_game_label0.place(x=22,y=85)
        browse_game_btn0=tek.Button(browse_panel,command=aw,bg='#23272a',fg='Orange',bd=0,text="Alan Wake",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn0.place(x=22,y=195,height=48,width=194)

        browse_game_label1=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage2,anchor="n")
        browse_game_label1.place(x=22,y=255)
        browse_game_btn1=tek.Button(browse_panel,command=awan,bg='#23272a',fg='Orange',bd=0,text="Alan Wake's\nAmerican Nightmare",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn1.place(x=22,y=365,height=48,width=194)

        browse_game_label2=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage3,anchor="n")
        browse_game_label2.place(x=22,y=425)
        browse_game_btn2=tek.Button(browse_panel,command=dpl,bg='#23272a',fg='Orange',bd=0,text="Deadpool",font=('Avellana Pro',18,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn2.place(x=22,y=535,height=48,width=194)

        browse_game_label3=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage4,anchor="n")
        browse_game_label3.place(x=277,y=85)
        browse_game_btn3=tek.Button(browse_panel,command=nfsr,bg='#23272a',fg='Orange',bd=0,text="Need For Speed\nRivals",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn3.place(x=277,y=195,height=48,width=194)

        browse_game_label4=tek.Label(browse_panel,bg='#23272a',fg='Blue',bd=0,height=120,width=194,image=bimage5,anchor="n")
        browse_game_label4.place(x=277,y=255)
        browse_game_btn4=tek.Button(browse_panel,command=nfsp,bg='#23272a',fg='Orange',bd=0,text="Need For Speed\nPayback",font=('Avellana Pro',16,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
        browse_game_btn4.place(x=277,y=365,height=48,width=194)

        browse_back_btn=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b3)
        browse_back_btn.place(x=330,y=590,width=80)
        browse_btn1=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b1)
        browse_btn1.place(x=430,y=590,width=80)
        browse_btn2=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b2)
        browse_btn2.place(x=530,y=590,width=80)
        browse_btn3=tek.Button(browse_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show_b3)
        browse_btn3.place(x=630,y=590,width=80)
        browse_btn4=tek.Button(browse_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
        browse_btn4.place(x=730,y=590,width=80)
        browse_next_btn=tek.Button(browse_panel,bg='Grey',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',15,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
        browse_next_btn.place(x=830,y=590,width=80)
        Window.update()

    def show_b1():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Browse_Page_1()

    def show_b2():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Browse_Page_2()

    def show_b3():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Browse_Page_3()

    def show_b4():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Browse_Page_4()
    Browse_Page_1()
    Window.update()

#Details For Each Game To Be Shown In The Details Page
def acv():
    title="ASSASSIN'S CREED: VALHALLA"
    x1=450
    y1=0
    gimg1='Media/acv1.jpg'
    gimg2='Media/acv2.jpg'
    gimg3='Media/acv3.jpg'
    gimg4='Media/acv4.jpg'
    gimg5='Media/acv5.jpg'
    tsoundpath='Media/acvta.wav'
    description = """In Assassin's Creed® Valhalla, become Eivor, a legendary Viking warrior on a quest for glory. Explore England's Dark Ages as you raid your enemies, grow your\nsettlement, and build your political power.
•Lead epic Viking raids against Saxon troops and fortresses.\n
•Dual-wield powerful weapons and relive the visceral fighting style of the Vikings.\n
•Challenge yourself with the most varied collection of enemies ever in Assassin's Creed.\n
•Shape the growth of your character with each choice and carve a path to glory.\n
•Explore a Dark Age open world, from the shores of Norway to the kingdoms of England.\n
•Personalize your experience by growing your clan's settlement."""
    descfont=11
    descfg='Sky Blue'
    tpath='Media/acvt.mp4'
    fpss=0.035
    price=3270
    btnbg='Aqua'
    btnfg='White'
    btntxt='Buy Now'
    developer='Ubisoft Montreal'
    publisher='Ubisoft'
    genre='Action-Adventure\nRPG'
    rating='-'
    poster='Media/acvposter.jpg'
    title1='Assassins Creed:@Valhalla'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def cybp():
    title="CYBERPUNK 2077"
    x1=520
    y1=0
    gimg1='Media/cybp1.jpg'
    gimg2='Media/cybp2.jpg'
    gimg3='Media/cybp3.jpg'
    gimg4='Media/cybp4.jpg'
    gimg5='Media/cybp5.jpg'
    tsoundpath='Media/cybpta.wav'
    description = """Cyberpunk 2077 is an open-world, action-adventure story set in Night City, a megalopolis obsessed with power, glamour and body modification.\n
You play as V, a mercenary outlaw going after a one-of-a-kind implant that is the key to immortality.\n
You can customize your character’s cyberware, skillset and playstyle,
and explore a vast city where the choices you make shape the story and the world around you.\n
Become a cyberpunk, an urban mercenary equipped with cybernetic enhancements and build your legend on the streets of Night City.\n
Enter the massive open world of Night City, a place that sets new standards in terms of visuals, complexity and depth.\n
Take the riskiest job of your life and go after a prototype implant that is the key to immortality."""
    descfont=13
    descfg='Gold'
    tpath='Media/cybpt.mp4'
    fpss=0.027
    price=3000
    btnbg='Yellow'
    btnfg='Black'
    btntxt='Pre-Order Now'
    developer='CD Projekt Red'
    publisher='CD Projekt Red'
    genre='Action RPG'
    rating='-'
    poster='Media/cybpposter.jpg'
    title1='Cyberpunk 2077'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def hi():
    title="HALO: INFINITE"
    x1=530
    y1=0
    gimg1='Media/hi1.jpg'
    gimg2='Media/hi2.jpg'
    gimg3='Media/hi3.jpg'
    gimg4='Media/hi4.jpg'
    gimg5='Media/hi5.jpg'
    tsoundpath='Media/hita.wav'
    description = """The legendary Halo series returns with the most expansive Master Chief story yet.

Campaign: When all hope is lost and humanity’s fate hangs in the balance,
the Master Chief is ready to confront the most ruthless foe he’s ever faced.
Begin anew and step inside the armor of humanity’s greatest hero to experience an epic adventure
and finally explore the scale of the Halo ring itself.

Multiplayer: Halo’s celebrated multiplayer returns!
More information coming later this year (requires Xbox Live Gold on console, membership sold separately).

Forge: Halo’s epic content creation tool is back and more powerful than ever. More information coming later this year."""
    descfont=14
    descfg='Green'
    tpath='Media/hit.mp4'
    fpss=0.011
    price=2500
    btnbg='Green'
    btnfg='Gold'
    btntxt='Pre-Order Now'
    developer='343 Industries'
    publisher='Xbox Game Studios'
    genre='Action'
    rating='-'
    poster='Media/hiposter.jpg'
    title1='Halo: Infinite'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)
    
def mas():
    title="MARVEL'S AVENGERS"
    x1=480
    y1=0
    gimg1='Media/mas1.jpg'
    gimg2='Media/mas2.jpg'
    gimg3='Media/mas3.jpg'
    gimg4='Media/mas4.jpg'
    gimg5='Media/mas5.jpg'
    tsoundpath='Media/masta.wav'
    description = """Assemble your team of Earth’s Mightiest Heroes, embrace your powers, and live your Super Hero dreams. Marvel’s Avengers is an epic, third-person,
action-adventure game that combines an original, cinematic story with single-player and co-operative gameplay*.

Assemble into a team of up to four players online, master extraordinary abilities, customize a growing roster of Heroes, and defend
the Earth from escalating threats. Marvel’s Avengers begins at A-Day, where Captain America, Iron Man, the Hulk, Black Widow, and Thor
are unveiling a new, hi-tech Avengers Headquarters in San Francisco. The celebration turns deadly when a mysterious enemy causes
a catastrophic accident which results in massive devastation.

Blamed for the tragedy, the Avengers disband. Five years later, with all Super Heroes outlawed and the world in peril,
a sprawling adventure ignites when a determined young woman named Kamala Khan sets out to reassemble and rebuild
the Avengers to stop the unchecked power of the secretive new force known as AIM.

Marvel’s Avengers continues the epic journey with new Heroes and new narrative delivered on an ongoing basis, for the definitive Avengers gaming experience."""
    descfont=11
    descfg='Red'
    tpath='Media/mast.mp4'
    fpss=0.027
    price=3000
    btnbg='Red'
    btnfg='Sky Blue'
    btntxt='Buy Now'
    developer='Crystal Dynamics,\nEidos-Montréal,\nNixxes'
    publisher='Square Enix'
    genre='Action-Adventure\nRPG'
    rating="6/10"
    poster='Media/masposter.jpg'
    title1='Marvels Avengers'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def au():
    title="AMONG US"
    x1=540
    y1=0
    gimg1='Media/au1.jpg'
    gimg2='Media/au2.jpg'
    gimg3='Media/au3.jpg'
    gimg4='Media/au4.jpg'
    gimg5='Media/au5.jpg'
    tsoundpath='Media/auta.wav'
    description = """Play with 4-10 player online or via local WiFi as you attempt to prepare your spaceship for departure, but beware as one or more
random players among the Crew are Impostors bent on killing everyone! Originally created as a party game, we recommend
playing with friends at a LAN party or online using voice chat. Enjoy cross-platform play between Android, iOS and PC.

Features
• Customization: Pick your color and hat.
• Lots of game options: Add more impostors, more tasks, and so much more!
• Quickly find a game online from the host list.
• In-game text chat.
• Rich discord integration.
• Cross-platform play between PC, Android, and iOS!"""
    descfont=14
    descfg='Orange'
    tpath='Media/aut.mp4'
    fpss=0.025
    price=200
    btnbg='Lime'
    btnfg='Blue'
    btntxt='Buy Now'
    developer='Innersloth'
    publisher='Innersloth'
    genre='Casual'
    rating="10/10"
    poster='Media/auposter.jpg'
    title1='Among Us'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def codbocw():
    title="CALL OF DUTY : BLACK OPS COLD WAR"
    x1=350
    y1=0
    gimg1='Media/codbocw1.jpg'
    gimg2='Media/codbocw2.jpg'
    gimg3='Media/codbocw3.jpg'
    gimg4='Media/codbocw4.jpg'
    gimg5='Media/codbocw5.jpg'
    tsoundpath='Media/codbocwta.wav'
    description = """Campaign
Black Ops Cold War will drop fans into the depths of the Cold War’s volatile geopolitical battle of the early 1980s.
Nothing is ever as it seems in a gripping single-player Campaign, where players will come face-to-face with historical
figures and hard truths, as they battle around the globe through iconic locales
like East Berlin, Vietnam, Turkey, Soviet KGB headquarters and more.

Multiplayer
Bring a Cold War arsenal of weapons and equipment into the next generation of Multiplayer in Call of Duty®: Black Ops Cold War.
Engage in deniable operations as an elite operative using state of the art tools of the tradecraft across a variety of experiences
from small skirmishes to all out, vehicle-fueled warfare.

Zombies
Uncover dark Cold War experiments that unleash a new Zombie threat
to take on in frightening and intense co-operative gameplay with friends."""
    descfont=12
    descfg='Orange'
    tpath='Media/codbocwt.mp4'
    fpss=0.027
    price=4437
    btnbg='Orange'
    btnfg='Black'
    btntxt='Buy Now'
    developer='Treyarch,\nRaven Software,\nBeenox'
    publisher='Activision'
    genre='First-Person\nShooter'
    rating="8.5/10"
    poster='Media/codbocwposter.jpg'
    title1='Call Of Duty :@Back Ops Cold War'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def hzd():
    title="HORIZON: ZERO DAWN"
    x1=480
    y1=0
    gimg1='Media/hzd1.jpg'
    gimg2='Media/hzd2.jpg'
    gimg3='Media/hzd3.jpg'
    gimg4='Media/hzd4.jpg'
    gimg5='Media/hzd5.jpg'
    tsoundpath='Media/hzdta.wav'
    description = """EARTH IS OURS NO MORE
Experience Aloy’s entire legendary quest to unravel the mysteries of a world ruled by deadly Machines.
An outcast from her tribe, the young hunter fights to uncover her past, discover her destiny… and stop a catastrophic threat to the future.
Unleash devastating, tactical attacks against unique Machines and rival tribes as you explore an open world teeming with wildlife and danger.
Horizon Zero Dawn™ is a multi-award-winning action role-playing game – and this Complete Edition for PC includes the huge expansion The Frozen Wilds,
featuring new lands, skills, weapons and Machines.

INCLUDES:
• Horizon Zero Dawn
• The Frozen Wilds expansion
• Carja Storm Ranger Outfit and Carja Mighty Bow
• Carja Trader Pack
• Banuk Trailblazer Outfit and Banuk Culling Bow
• Banuk Traveller Pack
• Nora Keeper Pack
• Digital art book"""
    descfont=10
    descfg='Lime'
    tpath='Media/hzdt.mp4'
    fpss=0.027
    price=1099
    btnbg='Lime'
    btnfg='Yellow'
    btntxt='Buy Now'
    developer='Guerrilla'
    publisher='PlayStation\nMobile, Inc.'
    genre='Action, Adventure,\nRPG'
    rating="7/10"
    poster='Media/hzdposter.jpg'
    title1='Horizon : Zero Dawn'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def tasm():
    title="THE AMAZING SPIDER-MAN"
    x1=440
    y1=0
    gimg1='Media/tasm1.jpg'
    gimg2='Media/tasm2.jpg'
    gimg3='Media/tasm3.jpg'
    gimg4='Media/tasm4.jpeg'
    gimg5='Media/tasm5.jpg'
    tsoundpath='Media/tasmta.wav'
    description = """The huge metropolis suffocates from the power of criminals. On the streets of the city begins a real war,
and only Spider-Man is able to purify his native New York from robbers, thieves and murderers.
Peter Parker again puts on his legendary costume and goes to the warpath. But from the shadows that thicken over
Manhattan, the flight of the web is followed by something ominous ... and it craves blood.

This incredibly spectacular action based on the Hollywood blockbuster will allow you to apply the most impressive
fighting techniques from the arsenal of Spider-Man. You will fly above the city, jump over skyscrapers,
descend to the ground and fight with the legendary villains from the classic comics Marvel.
The plot of the game begins where the events of the film end.
Find out what awaits the hero after the final credits are played!"""
    descfont=15
    descfg='Sky Blue'
    tpath='Media/tasmt.mp4'
    fpss=0.027
    price=850
    btnbg='Blue'
    btnfg='Red'
    btntxt='Buy Now'
    developer='Beenox'
    publisher='Activision'
    genre='Action, Adventure'
    rating="7/10"
    poster='Media/tasmposter.jpg'
    title1='The Amazing@Spider-Man'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def tasm2():
    title="THE AMAZING SPIDER-MAN 2"
    x1=440
    y1=0
    gimg1='Media/tasm21.jpg'
    gimg2='Media/tasm22.jpg'
    gimg3='Media/tasm23.jpg'
    gimg4='Media/tasm24.jpg'
    gimg5='Media/tasm25.jpg'
    tsoundpath='Media/tasm2ta.wav'
    description = """For the first time in the history of the Amazing Spider-Man series, play for Peter Parker.
Fight with new villains from the movie and the Spider-Man universe.

New mechanics of flight on the web, improved capabilities of throwers of the web and its chemical components,
allowing to freeze and explode objects with cobwebs. Explore Manhattan,
which surpasses the size of the city from the previous game.

The new system "Hero or threat to society" awards you for the actions of Spider-Man helping residents and fighting crime.
New abilities and a large selection of fast acrobatic techniques."""
    descfont=15
    descfg='Lime'
    tpath='Media/tasm2t.mp4'
    fpss=0.026
    price=1000
    btnbg='Blue'
    btnfg='Red'
    btntxt='Buy Now'
    developer='Beenox'
    publisher='Activision'
    genre='Action, Adventure'
    rating="6.5/10"
    poster='Media/tasm2poster.png'
    title1='The Amazing@Spider-Man 2'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def mc():
    title="MINECRAFT"
    x1=520
    y1=0
    gimg1='Media/mc1.png'
    gimg2='Media/mc2.png'
    gimg3='Media/mc3.png'
    gimg4='Media/mc4.png'
    gimg5='Media/mc5.png'
    tsoundpath='Media/mcta.wav'
    description = """The original version of Minecraft!
Java Edition has cross-platform play between Windows,
Linux and macOS, and also supports user-created skins and mods.
Includes a decade’s worth of updates, with much more to come!"""
    descfont=30
    descfg='Lime'
    tpath='Media/mct.mp4'
    fpss=0.026
    price=1994
    btnbg='Lime'
    btnfg='Navy Blue'
    btntxt='Buy Now'
    developer='Mojang'
    publisher='Mojang, Microsoft\nStudios'
    genre='Sandbox, Survivial'
    rating="10/10"
    poster='Media/mcposter.jpg'
    title1='Minecraft'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def fg():
    title="FALL GUYS : ULTIMATE KNOCKOUT"
    x1=380
    y1=0
    gimg1='Media/fg1.jpg'
    gimg2='Media/fg2.jpg'
    gimg3='Media/fg3.jpg'
    gimg4='Media/fg4.jpg'
    gimg5='Media/fg5.jpg'
    tsoundpath='Media/fgta.wav'
    description = """Fall Guys: Ultimate Knockout flings hordes of contestants together online in a mad dash through round after round of escalating chaos until one victor remains!
Battle bizarre obstacles, shove through unruly competitors, and overcome the unbending laws of physics as you stumble towards greatness.
Leave your dignity at the door and prepare for hilarious failure in your quest to claim the crown!

Massive Online Pandemonium: Dive into a series of ridiculous challenges and wild obstacle courses with masses of other competitors online,
all with the hopes of making the cut and advancing to the next round of mayhem.

Competitive & Cooperative: Shift between competitive free-for-alls and cooperative challenges where the losing team all get eliminated!

Comically Physical: Watch in delight as your fellow competitors bend, bounce, and bash their way to hilarious, physics-based failure!

Delightfully Customizable: Fail in style with everything from fashionable pineapple couture to the latest in bunny hats available to customize your
look in Fall Guys."""
    descfont=11
    descfg='Magenta'
    tpath='Media/fgt.mp4'
    fpss=0.026
    price=560
    btnbg='Magenta'
    btnfg='Sky Blue'
    btntxt='Buy Now'
    developer='Mediatonic'
    publisher='Devolver Digital'
    genre='Action, Casual,\nIndie, Multiplayer,\nSports'
    rating="9/10"
    poster='Media/fgposter.jpg'
    title1='Fall Guys'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def rl():
    title="ROCKET LEAGUE"
    x1=500
    y1=0
    gimg1='Media/rl1.jpg'
    gimg2='Media/rl2.jpg'
    gimg3='Media/rl3.jpg'
    gimg4='Media/rl4.jpg'
    gimg5='Media/rl5.jpg'
    tsoundpath='Media/rlta.wav'
    description = """PLAY ROCKET LEAGUE FOR FREE!


Download and compete in the high-octane hybrid of arcade-style soccer and vehicular mayhem! customize your car,
hit the field, and compete in one of the most critically acclaimed sports games of all time!
Download and take your shot! Hit the field by yourself or with friends in 1v1, 2v2, and 3v3 Online Modes,
or enjoy Extra Modes like Rumble, Snow Day, or Hoops. Unlock items in Rocket Pass, climb the Competitive Ranks,
compete in Competitive Tournaments, complete Challenges, enjoy cross-platform progression and more!
The field is waiting. Take your shot!"""
    descfont=15
    descfg='Cyan'
    tpath='Media/rlt.mp4'
    fpss=0.026
    price=0
    btnbg='Cyan'
    btnfg='Orange'
    btntxt='Buy Now'
    developer='Psyonix LLC'
    publisher='Psyonix LLC'
    genre='Sports,\nMultiplayer'
    rating="9.3/10"
    poster='Media/rlposter.jpg'
    title1='Rocket League'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def codmw():
    title="CALL OF DUTY : MODERN WARFARE"
    x1=380
    y1=0
    gimg1='Media/codmw1.png'
    gimg2='Media/codmw2.jpg'
    gimg3='Media/codmw3.png'
    gimg4='Media/codmw4.jpg'
    gimg5='Media/codmw5.jpg'
    tsoundpath='Media/codmwta.wav'
    description = """Welcome to Warzone
The new massive combat arena from Call of Duty® - completely free for players across all platforms.

Campaign
In the visceral and dramatic single-player story campaign, Call of Duty: Modern Warfare
pushes boundaries and breaks rules the way only Modern Warfare can.

Multiplayer
Experience the ultimate online playground with classic multiplayer.

Special Operations - Co-op
Assemble into strike-teams of 4 players to execute multi-phased objectives against a new and encroaching terror threat."""
    descfont=13
    descfg='Yellow'
    tpath='Media/codmwt.mp4'
    fpss=0.026
    price=4439
    btnbg='Black'
    btnfg='Yellow'
    btntxt='Buy Now'
    developer=' Infinity Ward,\nSledgehammer\nGames'
    publisher='Activision'
    genre='First-Person\nShooter'
    rating="8/10"
    poster='Media/codmwposter.jpg'
    title1='Call Of Duty:@Modern Warfare'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def cntrl():
    title="CONTROL"
    x1=550
    y1=0
    gimg1='Media/cntrl1.jpg'
    gimg2='Media/cntrl2.jpg'
    gimg3='Media/cntrl3.jpg'
    gimg4='Media/cntrl4.jpg'
    gimg5='Media/cntrl5.jpg'
    tsoundpath='Media/cntrlta.wav'
    description = """Control Ultimate Edition

A corruptive presence has invaded the Federal Bureau of Control…Only you have the power to stop it.
The world is now your weapon in an epic fight to annihilate an ominous enemy through deep and unpredictable environments.
Containment has failed, humanity is at stake. Will you regain control?

Winner of over 80 awards, Control is a visually stunning third-person action-adventure that will keep you on the edge
of your seat. Blending open-ended environments with the signature world-building and storytelling of renowned developer,
Remedy Entertainment, Control presents an expansive and intensely gratifying gameplay experience."""
    descfont=15
    descfg='Red'
    tpath='Media/cntrlt.mp4'
    fpss=0.026
    price=1499
    btnbg='Red'
    btnfg='Black'
    btntxt='Buy Now'
    developer='Remedy\nEntertainment'
    publisher='505 Games'
    genre='Action, Adventure'
    rating="8.8/10"
    poster='Media/cntrlposter.jpg'
    title1='CONTROL'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def wwz():
    title="WORLD WAR Z"
    x1=530
    y1=0
    gimg1='Media/wwz1.jpg'
    gimg2='Media/wwz2.png'
    gimg3='Media/wwz3.jpg'
    gimg4='Media/wwz4.png'
    gimg5='Media/wwz5.jpg'
    tsoundpath='Media/wwzta.wav'
    description = """Outlive the dead

Humanity is on the brink of extinction. From New York to Moscow, through Jerusalem, Tokyo and Marseille,
the undead apocalypse continues to spread. As the end looms, a hardened few band together to defeat
the horde and outlive the dead. World War Z is a heart-pounding coop third-person shooter
for up to 4 players featuring swarms of hundreds of zombies. Based on the Paramount Pictures film,
World War Z focuses on fast-paced gameplay while exploring new storylines from around the world."""
    descfont=17
    descfg='Red'
    tpath='Media/wwzt.mp4'
    fpss=0.026
    price=1266
    btnbg='Black'
    btnfg='Red'
    btntxt='Buy Now'
    developer='Saber\nInteractive'
    publisher='Mad Dog Games'
    genre='Third-Person\nShooter'
    rating="7.4/10"
    poster='Media/wwzposter.jpg'
    title1='World War Z'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def ac1():
    title="ASSASSIN'S CREED: DIRECTOR'S CUT"
    x1=370
    y1=0
    gimg1='Media/ac11.jpg'
    gimg2='Media/ac12.jpg'
    gimg3='Media/ac13.jpg'
    gimg4='Media/ac14.jpg'
    gimg5='Media/ac15.jpg'
    tsoundpath='Media/ac1ta.wav'
    description = """Assassin's Creed™ is the next-gen game developed by Ubisoft Montreal that redefines the action genre.


While other games claim to be next-gen with impressive graphics and physics, Assassin's Creed merges technology,
game design, theme and emotions into a world where you instigate chaos and become a vulnerable, yet powerful,
agent of change. The setting is 1191 AD. The Third Crusade is tearing the Holy Land apart. You, Altair,
intend to stop the hostilities by suppressing both sides of the conflict. You are an Assassin,
a warrior shrouded in secrecy and feared for your ruthlessness. Your actions can throw your immediate environment
into chaos, and your existence will shape events during this pivotal moment in history."""
    descfont=15
    descfg='White'
    tpath='Media/ac1t.mp4'
    fpss=0.027
    price=499
    btnbg='White'
    btnfg='Red'
    btntxt='Buy Now'
    developer='Ubisoft Montreal'
    publisher='Ubisoft'
    genre='Action, Adventure'
    rating="7.9/10"
    poster='Media/ac1poster.jpg'
    title1='Assassins Creed:@Directors Cut'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def ac2():
    title="ASSASSIN'S CREED 2"
    x1=500
    y1=0
    gimg1='Media/ac21.jpg'
    gimg2='Media/ac22.jpg'
    gimg3='Media/ac23.jpg'
    gimg4='Media/ac24.jpg'
    gimg5='Media/ac25.jpg'
    tsoundpath='Media/ac2ta.wav'
    description = """Assassin’s Creed® 2 is the follow-up to the title that became the fastest-selling new IP in video game history.


The highly anticipated title features a new hero, Ezio Auditore da Firenze, a young Italian noble, and a new era,
the Renaissance. Assassin’s Creed 2 retains the core gameplay experience that made the first opus a resounding
success and features new experiences that will surprise and challenge players. Assassin’s Creed 2 is an epic story
of family, vengeance and conspiracy set in the pristine, yet brutal, backdrop of a Renaissance Italy.
Ezio befriends Leonardo da Vinci, takes on Florence’s most powerful families and ventures throughout the canals of
Venice where he learns to become a master assassin."""
    descfont=15
    descfg='Silver'
    tpath='Media/ac2t.mp4'
    fpss=0.028
    price=499
    btnbg='White'
    btnfg='Maroon'
    btntxt='Buy Now'
    developer='Ubisoft Montreal'
    publisher='Ubisoft'
    genre='Action, Adventure'
    rating="8.6/10"
    poster='Media/ac2poster.jpg'
    title1='Assassins Creed 2'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def acbh():
    title="ASSASSIN'S CREED: BROTHERHOOD"
    x1=480
    y1=0
    gimg1='Media/acbh1.jpg'
    gimg2='Media/acbh2.jpg'
    gimg3='Media/acbh3.jpg'
    gimg4='Media/acbh4.jpg'
    gimg5='Media/acbh5.jpg'
    tsoundpath='Media/acbhta.wav'
    description = """Live and breathe as Ezio, a legendary Master Assassin, in his enduring struggle against the powerful
Templar Order. He must journey into Italy’s greatest city, Rome, center of power, greed and corruption to strike
at the heart of the enemy.

Defeating the corrupt tyrants entrenched there will require not only strength, but leadership, as Ezio commands an entire
Brotherhood who will rally to his side. Only by working together can the Assassins defeat their mortal enemies.

And for the first time, introducing an award-winning multiplayer layer that allows you to choose from a wide range of
unique characters, each with their own signature weapons and assassination techniques, and match your skills against
other players from around the world. It’s time to join the Brotherhood."""
    descfont=15
    descfg='Grey'
    tpath='Media/acbht.mp4'
    fpss=0.028
    price=749
    btnbg='White'
    btnfg='Silver'
    btntxt='Buy Now'
    developer='Ubisoft Montreal'
    publisher='Ubisoft'
    genre='Action, Adventure'
    rating="8.8/10"
    poster='Media/acbhposter.jpg'
    title1='Assassins Creed:@Brotherhood'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def acrvs():
    title="ASSASSIN'S CREED: REVELATIONS"
    x1=400
    y1=0
    gimg1='Media/acrvs1.jpg'
    gimg2='Media/acrvs2.jpg'
    gimg3='Media/acrvs3.jpg'
    gimg4='Media/acrvs4.jpg'
    gimg5='Media/acrvs5.jpg'
    tsoundpath='Media/acrvsta.wav'
    description = """When a man has won all his battles and defeated his enemies; what is left for him to achieve?
Ezio Auditore must leave his life behind in search of answers, In search of the truth.

In Assassin’s Creed® Revelations, master assassin Ezio Auditore walks in the footsteps of the legendary mentor Altair,
on a journey of discovery and revelation. It is a perilous path – one that will take Ezio to Constantinople,
the heart of the Ottoman Empire, where a growing army of Templars threatens to destabilize the region.

In addition to Ezio’s award-winning story, a refined and expanded online multiplayer experience returns with more modes,
more maps and more characters, allowing you to test your assassin skills against others from around the world."""
    descfont=15
    descfg='Blue'
    tpath='Media/acrvst.mp4'
    fpss=0.027
    price=749
    btnbg='Navy Blue'
    btnfg='Grey'
    btntxt='Buy Now'
    developer='Ubisoft Montreal'
    publisher='Ubisoft'
    genre='Action, Adventure'
    rating="8.0/10"
    poster='Media/acrvsposter.jpg'
    title1='Assassins Creed:@Revelations'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def ac3():
    title="ASSASSIN'S CREED 3"
    x1=500
    y1=0
    gimg1='Media/ac31.jpg'
    gimg2='Media/ac32.jpg'
    gimg3='Media/ac33.jpg'
    gimg4='Media/ac34.jpg'
    gimg5='Media/ac35.jpg'
    tsoundpath='Media/ac3ta.wav'
    description = """The American Colonies, 1775. It’s a time of civil unrest and political upheaval in the Americas. As a Native American assassin fights
to protect his land and his people, he will ignite the flames of a young nation’s revolution. Assassin’s Creed® III takes you back to the
American Revolutionary War, but not the one you’ve read about in history books...
Key Features:
As a Native American assassin, eliminate your enemies with guns, bows, tomahawks, and more!

From bustling city streets to chaotic battlefields, play a critical role in the most legendary events of the American Revolution
including the Battle of Bunker Hill and Great Fire of New York.

Experience the truth behind the most gruesome war in history: the American Revolution.

Introducing the Ubisoft-AnvilNext game engine, stunning new technology that will revolutionize gaming with powerful graphics, lifelike animations,
immersive combat,and advanced physics."""
    descfont=11
    descfg='Sky Blue'
    tpath='Media/ac3t.mp4'
    fpss=0.027
    price=749
    btnbg='Yellow'
    btnfg='Blue'
    btntxt='Buy Now'
    developer='Ubisoft Montreal'
    publisher='Ubisoft'
    genre='Action, Adventure'
    rating="8.0/10"
    poster='Media/ac3poster.jpg'
    title1='Assassins Creed 3'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def ac4bf():
    title="ASSASSIN'S CREED 4: BLACK FLAG"
    x1=380
    y1=0
    gimg1='Media/ac4bf1.jpg'
    gimg2='Media/ac4bf2.jpg'
    gimg3='Media/ac4bf3.jpg'
    gimg4='Media/ac4bf4.jpg'
    gimg5='Media/ac4bf5.jpg'
    tsoundpath='Media/ac4bfta.wav'
    description = """The year is 1715. Pirates rule the Caribbean and have established their
own lawless Republic where corruption, greediness and cruelty are commonplace.

Among these outlaws is a brash young captain named Edward Kenway. His fight for glory has earned him
the respect of legends like Blackbeard, but also drawn him into the ancient war between
Assassins and Templars, a war that may destroy everything the pirates have built.

Welcome to the Golden Age of Piracy."""
    descfont=17
    descfg='Blue'
    tpath='Media/ac4bft.mp4'
    fpss=0.027
    price=999
    btnbg='Sky Blue'
    btnfg='White'
    btntxt='Buy Now'
    developer='Ubisoft Montreal'
    publisher='Ubisoft'
    genre='Action, Adventure'
    rating="9/10"
    poster='Media/ac4bfposter.jpg'
    title1='Assassins Creed 4:@Black Flag'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def acrg():
    title="ASSASSIN'S CREED : ROGUE"
    x1=400
    y1=0
    gimg1='Media/acrg1.jpg'
    gimg2='Media/acrg2.jpg'
    gimg3='Media/acrg3.jpg'
    gimg4='Media/acrg4.jpg'
    gimg5='Media/acrg5.jpg'
    tsoundpath='Media/acrgta.wav'
    description = """18th century, North America. Amidst the chaos and violence of the French and Indian War,
Shay Patrick Cormac, a fearless young member of the Brotherhood of Assassin’s, undergoes a dark transformation
that will forever shape the future of the American colonies. After a dangerous mission gone tragically wrong,
Shay turns his back on the Assassins who, in response, attempt to end his life. Cast aside by those he once called brothers,
Shay sets out on a mission to wipe out all who turned against him and ultimately become the most feared
Assassin hunter in history.

Introducing Assassin’s Creed® Rogue, the darkest chapter in the Assassin’s Creed franchise yet.
As Shay, you will experience the slow transformation from Assassin to Assassin Hunter. Follow your own creed and set off
on an extraordinary journey through New York City, the wild river valley, and far away to the icy cold waters of the
North Atlantic in pursuit of your ultimate goal - bringing down the Assassins for good."""
    descfont=14
    descfg='Red'
    tpath='Media/acrgt.mp4'
    fpss=0.027
    price=999
    btnbg='White'
    btnfg='Sky Blue'
    btntxt='Buy Now'
    developer='Ubisoft Sofia,\nUbisoft Kiev'
    publisher='Ubisoft'
    genre='Action, Adventure'
    rating="7.4/10"
    poster='Media/acrgposter.jpg'
    title1='Assassins Creed:@Rogue'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def acu():
    title="ASSASSIN'S CREED : UNITY"
    x1=400
    y1=0
    gimg1='Media/acu1.jpg'
    gimg2='Media/acu2.jpg'
    gimg3='Media/acu3.jpg'
    gimg4='Media/acu4.jpg'
    gimg5='Media/acu5.jpg'
    tsoundpath='Media/acuta.wav'
    description = """Assassin’s Creed® Unity is an action/adventure game set in the city of Paris during one of its
darkest hours, the French Revolution.

Take ownership of the story by customising Arno's equipement to make the experience unique to you,
both visually and mechanically.

In addition to an epic single-player experience, Assassin’s Creed Unity delivers the excitement
of playing with up to three friends through online cooperative gameplay in specific missions.

Throughout the game, take part in one of the most pivotal moments of French history in a compelling
storyline and a breath-taking playground that brought you the city of lights of today."""
    descfont=14
    descfg='Blue'
    tpath='Media/acut.mp4'
    fpss=0.027
    price=1499
    btnbg='Red'
    btnfg='White'
    btntxt='Buy Now'
    developer='Ubisoft'
    publisher='Ubisoft'
    genre='Action, Adventure'
    rating="6/10"
    poster='Media/acuposter.jpg'
    title1='Assassins Creed:@Unity'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def acs():
    title="ASSASSIN'S CREED : SYNDICATE"
    x1=380
    y1=0
    gimg1='Media/acs1.jpg'
    gimg2='Media/acs2.jpg'
    gimg3='Media/acs3.jpg'
    gimg4='Media/acs4.jpg'
    gimg5='Media/acs5.jpg'
    tsoundpath='Media/acsta.wav'
    description = """London, 1868. In the heart of the Industrial Revolution, lead your underworld organization and grow your influence to fight those who exploit the less privileged in the name of progress:
Champion justice
As Jacob Frye, a young and reckless Assassin, use your skills to help those trampled by the march of progress. From freeing exploited children used as slave labour in factories, to stealing precious assets from enemy boats, you will stop at nothing
to bring justice back to London’s streets.

Command London’s underworld
To reclaim London for the people, you will need an army. As a gang leader, strengthen your stronghold and rally rival gang members to your cause, in order to take back the capital from the Templars’ hold.

A new dynamic fighting system
In Assassin’s Creed Syndicate, action is fast-paced and brutal. As a master of combat, combine powerful multi-kills and countermoves to strike your enemies down.

A whole new arsenal
Choose your own way to fight enemies. Take advantage of the Rope Launcher technology to be as stealthy as ever and strike with your Hidden Blade. Or choose the kukri knife and the brass knuckles to get the drop on your enemies.

A new age of transportation
In London, the systemic vehicles offer an ever-changing environment. Drive carriages to chase your target, use your parkour skills to engage in epic fights atop high-speed trains, or make your own way amongst the boats of the River Thames.

A vast open world
Travel the city at the height of the Industrial Revolution and meet iconic historical figures. From Westminster to Whitechapel, you will come across Darwin, Dickens, Queen Victoria… and many more.

A sharper focus
Take aim, engage in combat or launch a grappling hook by keeping your target in sight with Tobii Eye Tracking. The Clean UI lets you focus on the matter at hand while the Extended View and Dynamic Light features increase your immersion,
making you dive even deeper into the thrilling adventure in the streets of London. Compatible with all Tobii Eye Tracking gaming devices."""
    descfont=7
    descfg='Silver'
    tpath='Media/acst.mp4'
    fpss=0.027
    price=1999
    btnbg='Black'
    btnfg='Red'
    btntxt='Buy Now'
    developer='Ubisoft,\nToronto studios'
    publisher='Ubisoft'
    genre='Action, Adventure'
    rating="7.4/10"
    poster='Media/acsposter.jpg'
    title1='Assassins Creed:@Syndicate'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def acor():
    title="ASSASSIN'S CREED : ORIGINS"
    x1=380
    y1=0
    gimg1='Media/acor1.jpg'
    gimg2='Media/acor2.jpg'
    gimg3='Media/acor3.jpg'
    gimg4='Media/acor4.jpg'
    gimg5='Media/acor5.jpg'
    tsoundpath='Media/acorta.wav'
    description = """ASSASSIN’S CREED® ORIGINS IS A NEW BEGINNING
*The Discovery Tour by Assassin’s Creed®: Ancient Egypt is available now as a free update!*

Ancient Egypt, a land of majesty and intrigue, is disappearing in a ruthless fight for power. Unveil dark secrets and forgotten myths as you go back to the one founding moment:
The Origins of the Assassin’s Brotherhood.

A COUNTRY TO DISCOVER
Sail down the Nile, uncover the mysteries of the pyramids or fight your way against dangerous ancient factions and wild beasts as you explore this gigantic and unpredictable land.

A NEW STORY EVERY TIME YOU PLAY
Engage into multiple quests and gripping stories as you cross paths with strong and memorable characters, from the wealthiest high-born to the most desperate outcasts.

EMBRACE ACTION-RPG
Experience a completely new way to fight. Loot and use dozens of weapons with different characteristics and rarities.
Explore deep progression mechanics and challenge your skills against unique and powerful bosses."""
    descfont=10
    descfg='Gold'
    tpath='Media/acort.mp4'
    fpss=0.023
    price=2999
    btnbg='Gold'
    btnfg='Silver'
    btntxt='Buy Now'
    developer='Ubisoft Montreal'
    publisher='Ubisoft'
    genre='Action, Adventure,\nRPG'
    rating="9/10"
    poster='Media/acorposter.jpg'
    title1='Assassins Creed:@Origins'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def acod():
    title="ASSASSIN'S CREED : ODYSSEY"
    x1=380
    y1=0
    gimg1='Media/acod1.jpg'
    gimg2='Media/acod2.jpg'
    gimg3='Media/acod3.jpg'
    gimg4='Media/acod4.jpg'
    gimg5='Media/acod5.jpg'
    tsoundpath='Media/acodta.wav'
    description = """Choose your fate in Assassin's Creed® Odyssey.
From outcast to living legend, embark on an odyssey to uncover the secrets of your past and change the fate of Ancient Greece.

TRAVEL TO ANCIENT GREECE
From lush vibrant forests to volcanic islands and bustling cities, start a journey of exploration and encounters in a war torn world shaped by gods and men.

FORGE YOUR LEGEND
Your decisions will impact how your odyssey unfolds. Play through multiple endings thanks to the new dialogue system and the choices you make.
Customize your gear, ship, and special abilities to become a legend.

FIGHT ON A NEW SCALE
Demonstrate your warrior's abilities in large scale epic battles between Athens and Sparta featuring hundreds of soldiers, or ram and cleave your way through
entire fleets in naval battles across the Aegean Sea.

GAZE IN WONDER
Experience the action in a whole new light with Tobii Eye Tracking. The Extended View feature gives you a broader perspective of the environment,
and the Dynamic Light and Sun Effects immerse you in the sandy dunes according to where you set your sights. Tagging, aiming and locking on your targets becomes a lot
more natural when you can do it by looking at them. Let your vision lead the way and enhance your gameplay. Visit the Tobii website to check the list of compatible devices."""
    descfont=8
    descfg='Sky Blue'
    tpath='Media/acodt.mp4'
    fpss=0.0245
    price=2999
    btnbg='Blue'
    btnfg='Gold'
    btntxt='Buy Now'
    developer='Ubisoft'
    publisher='Ubisoft'
    genre='Action, Adventure,\nRPG'
    rating="9.2/10"
    poster='Media/acodposter.jpg'
    title1='Assassins Creed:@Odyssey'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def baa():
    title="BATMAN : ARKHAM ASYLUM"
    x1=400
    y1=0
    gimg1='Media/baa1.jpg'
    gimg2='Media/baa2.jpg'
    gimg3='Media/baa3.jpg'
    gimg4='Media/baa4.jpg'
    gimg5='Media/baa5.jpg'
    tsoundpath='Media/baata.wav'
    description = """Critically acclaimed Batman: Arkham Asylum returns with a remastered Game of the Year Edition, featuring 4 extra Challenge Maps. The additional Challenge Maps are Crime Alley;
Scarecrow Nightmare;Totally Insane and Nocturnal Hunter (both from the Insane Night Map Pack).
Utilize the unique FreeFlow™ combat system to chain together unlimited combos seamlessly and battle with huge groups of The Joker’s henchmen in brutal melee brawls

Investigate as Batman, the WORLD’S GREATEST DETECTIVE, by solving intricate puzzles with the help of cutting edge forensic tools including x-ray scanning, fingerprint scans,
‘Amido Black’ spray and a pheromone tracker

Face off against Gotham’s greatest villains including The Joker, HARLEY QUINN, POISON IVY and KILLER CROC

Become the Invisible Predator™ with Batman’s fear takedowns and unique vantage point system to move without being seen and hunt enemies

Choose multiple takedown methods, including swooping from the sky and smashing through walls.

Explore every inch of Arkham Asylum and roam freely on the infamous island, presented for the first time ever in its gritty and realistic entirety

Experience what it’s like to be BATMAN using BATARANGS, explosive gel aerosol, The Batclaw, sonar resonator and the line launcher

Unlock more secrets by completing hidden challenges in the world and develop and customize equipment by earning experience points Enjoy complete superhero freedom in the environment with
the use of Batman’s grapnel gun to get to any place you can see, jump from any height and glide in any direction"""
    descfont=8
    descfg='Grey'
    tpath='Media/baat.mp4'
    fpss=0.024
    price=565
    btnbg='Black'
    btnfg='Grey'
    btntxt='Buy Now'
    developer='RockSteady\nStudios'
    publisher='Warner Bros.\nInteractive\nEntertainment'
    genre='Action, Adventure'
    rating="9.1/10"
    poster='Media/baaposter.jpg'
    title1='Batman:@Arkham Asylum'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def bac():
    title="BATMAN : ARKHAM CITY"
    x1=400
    y1=0
    gimg1='Media/bac1.jpg'
    gimg2='Media/bac2.jpg'
    gimg3='Media/bac3.jpg'
    gimg4='Media/bac4.jpg'
    gimg5='Media/bac5.jpg'
    tsoundpath='Media/bacta.wav'
    description = """Batman: Arkham City builds upon the intense, atmospheric foundation of
Batman: Arkham Asylum, sending players flying through the expansive Arkham City -
five times larger than the game world in Batman: Arkham Asylum - the new maximum security "home"
for all of Gotham City's thugs, gangsters and insane criminal masterminds.

Featuring an incredible Rogues Gallery of Gotham City's most dangerous criminals including Catwoman,
The Joker, The Riddler, Two-Face, Harley Quinn, The Penguin, Mr. Freeze and many others,
the game allows players to genuinely experience what it feels like to be The Dark Knight
delivering justice on the streets of Gotham City."""
    descfont=17
    descfg='Grey'
    tpath='Media/bact.mp4'
    fpss=0.0265
    price=565
    btnbg='Black'
    btnfg='Grey'
    btntxt='Buy Now'
    developer='RockSteady\nStudios'
    publisher='Warner Bros.\nInteractive\nEntertainment'
    genre='Action, Adventure'
    rating="9.1/10"
    poster='Media/bacposter.jpg'
    title1='Batman:@Arkham City'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def bao():
    title="BATMAN : ARKHAM ORIGINS"
    x1=390
    y1=0
    gimg1='Media/bao1.jpg'
    gimg2='Media/bao2.jpg'
    gimg3='Media/bao3.jpg'
    gimg4='Media/bao4.jpg'
    gimg5='Media/bao5.jpg'
    tsoundpath='Media/baota.wav'
    description = """Batman™: Arkham Origins is the next installment in the blockbuster Batman: Arkham
videogame franchise.

Developed by WB Games Montréal, the game features an expanded Gotham City and introduces an original
prequel storyline set several years before the events of Batman: Arkham Asylum and Batman: Arkham City,
the first two critically acclaimed games of the franchise.
Taking place before the rise of Gotham City’s most dangerous criminals, the game showcases a young and
unrefined Batman as he faces a defining moment in his early career as a crime fighter that sets his path
to becoming the Dark Knight."""
    descfont=17
    descfg='Grey'
    tpath='Media/baot.mp4'
    fpss=0.026
    price=565
    btnbg='Black'
    btnfg='Grey'
    btntxt='Buy Now'
    developer='WB Games\nMontreal,\nSplash Damage'
    publisher='Warner Bros.\nInteractive\nEntertainment'
    genre='Action, Adventure'
    rating="7.4/10"
    poster='Media/baoposter.jpg'
    title1='Batman:@Arkham Origins'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def bak():
    title="BATMAN : ARKHAM KNIGHT"
    x1=390
    y1=0
    gimg1='Media/bak1.jpg'
    gimg2='Media/bak2.jpg'
    gimg3='Media/bak3.jpg'
    gimg4='Media/bak4.jpg'
    gimg5='Media/bak5.jpg'
    tsoundpath='Media/bakta.wav'
    description = """Batman™: Arkham Knight brings the award-winning Arkham trilogy from Rocksteady Studios to its
epic conclusion. Developed exclusively for New-Gen platforms, Batman: Arkham Knight introduces
Rocksteady's uniquely designed version of the Batmobile. The highly anticipated addition of this
legendary vehicle, combined with the acclaimed gameplay of the Arkham series, offers gamers the
ultimate and complete Batman experience as they tear through the streets and soar across the skyline
of the entirety of Gotham City.

In this explosive finale, Batman faces the ultimate threat against the city that he is sworn to protect,
as Scarecrow returns to unite the super criminals of Gotham and destroy the Batman forever."""
    descfont=17
    descfg='Grey'
    tpath='Media/bakt.mp4'
    fpss=0.026
    price=1899
    btnbg='Black'
    btnfg='Grey'
    btntxt='Buy Now'
    developer='RockSteady\nStudios'
    publisher='Warner Bros.\nInteractive\nEntertainment'
    genre='Action, Adventure'
    rating="9/10"
    poster='Media/bakposter.jpg'
    title1='Batman:@Arkham Knight'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def dhd1():
    title="DISHONORED"
    x1=520
    y1=0
    gimg1='Media/dhd11.jpg'
    gimg2='Media/dhd12.jpg'
    gimg3='Media/dhd13.jpg'
    gimg4='Media/dhd14.jpg'
    gimg5='Media/dhd15.jpg'
    tsoundpath='Media/dhd1ta.wav'
    description = """Dishonored is an immersive first-person action game that casts you as a supernatural assassin driven by revenge.
With Dishonored’s flexible combat system, creatively eliminate your targets as you combine the supernatural abilities,weapons
and unusual gadgets at your disposal. Pursue your enemies under the cover of darkness or ruthlessly attack them head on with
weapons drawn. The outcome of each mission plays out based on the choices you make.

Story:
Dishonored is set in Dunwall, an industrial whaling city where strange steampunk- inspired technology and otherworldly forces
coexist in the shadows. You are the once-trusted bodyguard of the beloved Empress. Framed for her murder, you become an infamous
assassin, known only by the disturbing mask that has become your calling card. In a time of uncertainty, when the city is besieged
by plague and ruled by a corrupt government armed with industrial technologies, dark forces conspire to bestow upon you abilities
beyond those of any common man – but at what cost?
The truth behind your betrayal is as murky as the waters surrounding the city, and the life you once had is gone forever."""
    descfont=13
    descfg='Silver'
    tpath='Media/dhd1t.mp4'
    fpss=0.0255
    price=670
    btnbg='Silver'
    btnfg='Black'
    btntxt='Buy Now'
    developer='Arkane Studios'
    publisher='Bethesda\nSoftworks'
    genre='Action, Adventure'
    rating="9.1/10"
    poster='Media/dhd1poster.png'
    title1='Dishonored'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def dhd2():
    title="DISHONORED 2"
    x1=520
    y1=0
    gimg1='Media/dhd21.jpg'
    gimg2='Media/dhd22.jpg'
    gimg3='Media/dhd23.jpg'
    gimg4='Media/dhd24.jpg'
    gimg5='Media/dhd25.jpg'
    tsoundpath='Media/dhd2ta.wav'
    description = """Reprise your role as a supernatural assassin in Dishonored 2.

Praised by PC Gamer as “brilliant”, IGN as “amazing” and “a super sequel, IGN as “amazing” and “a superb sequel”, declared a “masterpiece”
by Eurogamer, and hailed “a must-play revenge tale among the best in its class” by Game Informer, Dishonored 2 is the follow up to
Arkane Studio's first-person action blockbuster and winner of more than 100 'Game of the Year' awards, Dishonored.

Play your way in a world where mysticism and industry collide. Will you choose to play as Empress Emily Kaldwin or the royal protector,
Corvo Attano? Will you make your way through the game unseen, make full use of its brutal combat system, or use a blend of both?

How will you combine your character's unique set of powers, weapons and gadgets to eliminate your enemies? The story responds to your choices,
leading to intriguing outcomes, as you play through each of the game's hand-crafted missions."""
    descfont=13
    descfg='Silver'
    tpath='Media/dhd2t.mp4'
    fpss=0.024
    price=2670
    btnbg='Silver'
    btnfg='Red'
    btntxt='Buy Now'
    developer='Arkane Studios'
    publisher='Bethesda\nSoftworks'
    genre='Action'
    rating="8.6/10"
    poster='Media/dhd2poster.jpg'
    title1='Dishonored 2'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def dhddoto():
    title="DISHONORED : DEATH OF THE OUTSIDER"
    x1=340
    y1=0
    gimg1='Media/dhddoto1.jpg'
    gimg2='Media/dhddoto2.jpg'
    gimg3='Media/dhddoto3.jpg'
    gimg4='Media/dhddoto4.jpg'
    gimg5='Media/dhddoto5.jpg'
    tsoundpath='Media/dhddotota.wav'
    description = """From the award-winning developers at Arkane® Studios comes Dishonored®: Death of the Outsider, the next standalone
adventure in the critically-acclaimed Dishonored® series. Be a badass supernatural assassin and take on the role of notorious Billie Lurk
as she reunites with her mentor Daud in order to pull off the greatest assassination ever conceived. Building upon Dishonored® 2’s signature
gameplay and art style, Death of the Outsider features all the series hallmarks, including brutal combat systems, unique level design, and
immersive storytelling that responds to your every choice. With compelling characters and exhilarating action, Death of the Outsider is the
perfect entry point for those new to the Dishonored series, while delivering a significant expansion of the gameplay and world for longtime fans.
STORY:
Take on the role of Billie Lurk (aka Megan Foster), once one of Dunwall's most notorious killers-for-hire. Reunited with your old mentor, the
legendary assassin Daud, you undertake the greatest assassination ever conceived: killing the Outsider, a god-like figure whom Billie and Daud
see as instrumental to some of the Empire's most dishonorable moments. As you venture deep into the grimiest corners of Karnaca to uncover
the mystery of the Outsider and his origins, you will face deadly opposition, ancient powers, and difficult decisions that will forever
change the world around you."""
    descfont=13
    descfg='Silver'
    tpath='Media/dhddotot.mp4'
    fpss=0.024
    price=2000
    btnbg='Red'
    btnfg='Maroon'
    btntxt='Buy Now'
    developer='Arkane Studios'
    publisher='Bethesda\nSoftworks'
    genre='Action'
    rating="8.1/10"
    poster='Media/dhddotoposter.jpg'
    title1='Dishonored: Death@Of The Outsider'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def re7():
    title="RESIDENT EVIL 7 : BIOHAZARD"
    x1=370
    y1=0
    gimg1='Media/re71.jpg'
    gimg2='Media/re72.jpg'
    gimg3='Media/re73.jpg'
    gimg4='Media/re74.jpg'
    gimg5='Media/re75.jpg'
    tsoundpath='Media/re7ta.wav'
    description = """Resident Evil 7 biohazard is the next major entry in the renowned Resident Evil series and sets a new course
for the franchise as it leverages its roots and opens the door to a truly terrifying horror experience. A dramatic
new shift for the series to first person view in a photorealistic style powered by Capcom’s new RE Engine,
Resident Evil 7 delivers an unprecedented level of immersion that brings the thrilling horror
up close and personal.

Set in modern day rural America and taking place after the dramatic events of Resident Evil® 6, players experience
the terror directly from the first person perspective. Resident Evil 7 embodies the series’ signature gameplay elements
of exploration and tense atmosphere that first coined “survival horror” some twenty years ago; meanwhile, a complete
refresh of gameplay systems simultaneously propels the survival horror experience to the next level."""
    descfont=15
    descfg='Orange'
    tpath='Media/re7t.mp4'
    fpss=0.0255
    price=1999
    btnbg='Black'
    btnfg='Orange'
    btntxt='Buy Now'
    developer='CAPCOM Co.,\nLtd.'
    publisher='CAPCOM Co.,\nLtd.'
    genre='Action, Adventure'
    rating="8.3/10"
    poster='Media/re7poster.jpg'
    title1='Resident Evil 7'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def re2r():
    title="RESIDENT EVIL 2 REMAKE"
    x1=400
    y1=0
    gimg1='Media/re2r1.jpg'
    gimg2='Media/re2r2.jpg'
    gimg3='Media/re2r3.jpg'
    gimg4='Media/re2r4.jpg'
    gimg5='Media/re2r5.jpg'
    tsoundpath='Media/re2rta.wav'
    description = """The genre-defining masterpiece Resident Evil 2 returns, completely rebuilt from the ground up for a deeper narrative experience.
Using Capcom’s proprietary RE Engine, Resident Evil 2 offers a fresh take on the classic survival horror saga with breathtakingly realistic
visuals, heart-pounding immersive audio, a new over-the-shoulder camera, and modernized controls on top of gameplay modes from the original
game.

In Resident Evil 2, the classic action, tense exploration, and puzzle solving gameplay that defined the Resident Evil series returns.
Players join rookie police officer Leon Kennedy and college student Claire Redfield, who are thrust together by a disastrous outbreak
in Raccoon City that transformed its population into deadly zombies. Both Leon and Claire have their own separate playable campaigns,
allowing players to see the story from both characters’ perspectives. The fate of these two fan favorite characters is in players hands
as they work together to survive and get to the bottom of what is behind the terrifying attack on the city. Will they make it out alive?"""
    descfont=13
    descfg='Red'
    tpath='Media/re2rt.mp4'
    fpss=0.0255
    price=1999
    btnbg='Blue'
    btnfg='Red'
    btntxt='Buy Now'
    developer='CAPCOM Co.,\nLtd.'
    publisher='CAPCOM Co.,\nLtd.'
    genre='Action'
    rating="8.9/10"
    poster='Media/re2rposter.jpg'
    title1='Resident Evil 2@Remake'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def re3r():
    title="RESIDENT EVIL 3 REMAKE"
    x1=400
    y1=0
    gimg1='Media/re3r1.jpg'
    gimg2='Media/re3r2.jpg'
    gimg3='Media/re3r3.jpg'
    gimg4='Media/re3r4.jpg'
    gimg5='Media/re3r5.jpg'
    tsoundpath='Media/re3rta.wav'
    description = """Jill Valentine is one of the last remaining people in Raccoon City to witness the atrocities
Umbrella performed. To stop her, Umbrella unleashes their ultimate secret weapon; Nemesis!

Also includes Resident Evil Resistance, a new 1 vs 4 online multiplayer game set in the
Resident Evil universe where four survivors face-off against a sinister Mastermind."""
    descfont=20
    descfg='Blue'
    tpath='Media/re3rt.mp4'
    fpss=0.0265
    price=3499
    btnbg='Black'
    btnfg='Blue'
    btntxt='Buy Now'
    developer='CAPCOM Co.,\nLtd.'
    publisher='CAPCOM Co.,\nLtd.'
    genre='Action'
    rating="7.7/10"
    poster='Media/re3rposter.jpg'
    title1='Resident Evil 3@Remake'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def brdrl1():
    title="BORDERLANDS : GAME OF THE YEAR"
    x1=350
    y1=0
    gimg1='Media/brdrl11.jpg'
    gimg2='Media/brdrl12.jpg'
    gimg3='Media/brdrl13.jpg'
    gimg4='Media/brdrl14.jpg'
    gimg5='Media/brdrl15.jpg'
    tsoundpath='Media/brdrl1ta.wav'
    description = """Lock, Load, & Face the Madness
Get ready for the mind blowing insanity! Play as one of four trigger-happy mercenaries and take out everything that stands in your way!
With its addictive action, frantic first-person shooter combat, massive arsenal of weaponry, RPG elements and four-player co-op*,
Borderlands is a breakthrough experience that challenges all the conventions of modern shooters. Borderlands places you in the role of a
mercenary on the lawless and desolate planet of Pandora, hell-bent on finding a legendary stockpile of powerful alien technology known as The Vault.

Role Playing Shooter (RPS) - Combines frantic first-person shooting action with accessible role-playing character progression
Co-Op Frenzy - Fly solo in single player or drop in and out with up to 4 Player Co-Op online for a maniacal multiplayer experience
Bazillions of Guns - Gun lust fulfilled with rocket-launching shotguns, enemy-torching revolvers, SMGs that fire lightning rounds, and tons more
Radical Art Style - New visual style combines traditional rendering techniques with hand-drawn textures to create a unique and eye-catching spin
on the First Person genre Intense Vehicular Combat - Get behind the wheel and engage in intense vehicle-to-vehicle combat."""
    descfont=12
    descfg='Yellow'
    tpath='Media/brdrl1t.mp4'
    fpss=0.0265
    price=1599
    btnbg='Yellow'
    btnfg='Orange'
    btntxt='Buy Now'
    developer='Gearbox Software'
    publisher='2K'
    genre='Action, RPG'
    rating="8.1/10"
    poster='Media/brdrl1poster.jpg'
    title1='Borderlands: Game@Of The Year'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def brdrl2():
    title="BORDERLANDS 2 : GAME OF THE YEAR"
    x1=350
    y1=0
    gimg1='Media/brdrl21.jpg'
    gimg2='Media/brdrl22.jpg'
    gimg3='Media/brdrl23.jpg'
    gimg4='Media/brdrl24.jpg'
    gimg5='Media/brdrl25.jpg'
    tsoundpath='Media/brdrl2ta.wav'
    description = """A new era of shoot and loot is about to begin. Play as one of four new vault hunters facing
off against a massive new world of creatures, psychos and the evil mastermind,
Handsome Jack.

Make new friends, arm them with a bazillion weapons and fight
alongside them in 4 player co-op on a relentless quest for revenge and redemption
across the undiscovered and unpredictable living planet."""
    descfont=20
    descfg='Orange'
    tpath='Media/brdrl2t.mp4'
    fpss=0.0265
    price=1999
    btnbg='Yellow'
    btnfg='Blue'
    btntxt='Buy Now'
    developer='Gearbox Software'
    publisher='2K'
    genre='Action, RPG'
    rating="8.9/10"
    poster='Media/brdrl2poster.png'
    title1='Borderlands 2: Game@Of The Year'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def brdrltps():
    title="BORDERLANDS : THE PRE-SEQUEL"
    x1=370
    y1=0
    gimg1='Media/brdrltps1.jpg'
    gimg2='Media/brdrltps2.jpg'
    gimg3='Media/brdrltps3.jpg'
    gimg4='Media/brdrltps4.jpg'
    gimg5='Media/brdrltps5.jpg'
    tsoundpath='Media/brdrltpsta.wav'
    description = """LAUNCH INTO THE BORDERLANDS UNIVERSE AND SHOOT ‘N’ LOOT YOUR WAY THROUGH A BRAND NEW ADVENTURE THAT
ROCKETS YOU ONTO PANDORA’S MOON IN BORDERLANDS: THE PRE-SEQUEL!

Discover the story behind Borderlands 2 villain, Handsome Jack, and his rise to power. Taking place between the
original Borderlands and Borderlands 2, the Pre-Sequel gives you a whole lotta new gameplay featuring the genre
blending fusion of shooter and RPG mechanics that players have come to love.

Float through the air with each low gravity jump while taking enemies down from above using new ice and laser weapons.
Catch-a-ride and explore the lunar landscape with new vehicles allowing for more levels of destructive mayhem."""
    descfont=15
    descfg='Blue'
    tpath='Media/brdrltpst.mp4'
    fpss=0.0265
    price=1999
    btnbg='Blue'
    btnfg='Orange'
    btntxt='Buy Now'
    developer='2K Australia,\nGearbox Software'
    publisher='2K'
    genre='Action, RPG'
    rating="7.5/10"
    poster='Media/brdrltpsposter.jpg'
    title1='Borderlands:@The Pre-Sequel'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def brdrl3():
    title="BORDERLANDS 3"
    x1=520
    y1=0
    gimg1='Media/brdrl31.jpg'
    gimg2='Media/brdrl32.jpg'
    gimg3='Media/brdrl33.jpg'
    gimg4='Media/brdrl34.jpg'
    gimg5='Media/brdrl35.jpg'
    tsoundpath='Media/brdrl3ta.wav'
    description = """The original shooter-looter returns, packing bazillions of guns and an all-new mayhem-fueled adventure!

Blast through new worlds and enemies as one of four brand new Vault Hunters – the ultimate
treasure-seeking badasses of the Borderlands, each with deep skill trees, abilities, and customization.

Play solo or join
with friends to take on insane enemies, score loads of loot and save your home from the most ruthless cult
leaders in the galaxy."""
    descfont=18
    descfg='Lime'
    tpath='Media/brdrl3t.mp4'
    fpss=0.0265
    price=2990
    btnbg='Blue'
    btnfg='Yellow'
    btntxt='Buy Now'
    developer='Gearbox Software'
    publisher='2K'
    genre='Action, RPG'
    rating="8.1/10"
    poster='Media/brdrl3poster.jpg'
    title1='Borderlands 3'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def wd1():
    title="WATCH_DOGS"
    x1=520
    y1=0
    gimg1='Media/wd11.jpg'
    gimg2='Media/wd12.jpg'
    gimg3='Media/wd13.jpg'
    gimg4='Media/wd14.jpg'
    gimg5='Media/wd15.jpg'
    tsoundpath='Media/wd1ta.wav'
    description = """All it takes is the swipe of a finger. We connect with friends. We buy the latest gadgets and gear. We find out what’s happening in the world.
But with that same simple swipe, we cast an increasingly expansive shadow. With each connection, we leave a digital trail that tracks our every move
and milestone, our every like and dislike. And it’s not just people. Today, all major cities are networked. Urban infrastructures are monitored and
controlled by complex operating systems.

In Watch_Dogs, this system is called the Central Operating System (CTOS) – and it controls almost every piece of the city’s technology and holds key
information on all of the city’s residents.

You play as Aiden Pearce, a brilliant hacker and former thug, whose criminal past led to a violent family tragedy. Now on the hunt for those who hurt
your family, you'll be able to monitor and hack all who surround you by manipulating everything connected to the city’s network. Access omnipresent
security cameras, download personal information to locate a target, control traffic lights and public transportation to stop the enemy…and more.

Use the city of Chicago as your ultimate weapon and exact your own style of revenge."""
    descfont=11
    descfg='Silver'
    tpath='Media/wd1t.mp4'
    fpss=0.0265
    price=1499
    btnbg='Blue'
    btnfg='Grey'
    btntxt='Buy Now'
    developer='Ubisoft'
    publisher='Ubisoft'
    genre='Action, Adventure'
    rating="7.7/10"
    poster='Media/wd1poster.jpg'
    title1='Watch_Dogs'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def wd2():
    title="WATCH_DOGS 2"
    x1=520
    y1=0
    gimg1='Media/wd21.jpg'
    gimg2='Media/wd22.jpg'
    gimg3='Media/wd23.jpg'
    gimg4='Media/wd24.jpg'
    gimg5='Media/wd25.jpg'
    tsoundpath='Media/wd2ta.wav'
    description = """Play as Marcus Holloway, a brilliant young hacker living in the birthplace of the tech revolution, the San Francisco Bay Area.
Team up with Dedsec, a notorious group of hackers, to execute the biggest hack in history; take down ctOS 2.0, an invasive
operating system being used by criminal masterminds to monitor and manipulate citizens on a massive scale.

Explore the dynamic open-world, full of gameplay possibilities
Hack into every connected device and take control of the city infrastructure.
Develop different skills to suit your playstyle, and upgrade your hacker tools – RC cars, Quadcopter drone, 3D printed
weapons and much more. Stay seamlessly connected to your friends with a brand new co-op and adversarial multiplayer
Watch Dogs experience."""
    descfont=15
    descfg='Yellow'
    tpath='Media/wd2t.mp4'
    fpss=0.0265
    price=2999
    btnbg='Grey'
    btnfg='Blue'
    btntxt='Buy Now'
    developer='Ubisoft'
    publisher='Ubisoft'
    genre='Action, Adventure'
    rating="9/10"
    poster='Media/wd2poster.jpg'
    title1='Watch_Dogs 2'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def wdl():
    title="WATCH DOGS : LEGION"
    x1=510
    y1=0
    gimg1='Media/wdl1.jpg'
    gimg2='Media/wdl2.jpg'
    gimg3='Media/wdl3.jpg'
    gimg4='Media/wdl4.jpg'
    gimg5='Media/wdl5.jpg'
    tsoundpath='Media/wdlta.wav'
    description = """Build a resistance from virtually anyone you see as you hack, infiltrate, and fight to take back a near-future London
that is facing its downfall. Welcome to the Resistance.

Recruit and play as anyone in the city. Everyone you see has a unique backstory, personality, and skill set.

Hack armed drones, deploy spider-bots, and take down enemies using an Augmented Reality Cloak.

Explore a massive urban open world featuring London’s many iconic landmarks and fun side activities.

Take your recruits online and team up with your friends as you complete missions and challenging endgame content."""
    descfont=15
    descfg='Red'
    tpath='Media/wdlt.mp4'
    fpss=0.0265
    price=2999
    btnbg='Maroon'
    btnfg='Blue'
    btntxt='Buy Now'
    developer='Ubisoft Toronto'
    publisher='Ubisoft'
    genre='Action, Adventure'
    rating="8/10"
    poster='Media/wdlposter.jpg'
    title1='Watch Dogs:@Legion'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def smwos():
    title="SPIDER-MAN : WEB OF SHADOWS"
    x1=380
    y1=0
    gimg1='Media/smwos1.jpg'
    gimg2='Media/smwos2.jpg'
    gimg3='Media/smwos3.jpg'
    gimg4='Media/smwos4.jpg'
    gimg5='Media/smwos5.jpg'
    tsoundpath='Media/smwosta.wav'
    description = """A deadly symbiote invasion brings devastation to New York City. In Spider-Man: Web of Shadows, the game is set in an
apocalyptic vision of the city. You'll have complete control over New York City's salvation and the fate of Spider-man.
It also features an all-new combat system that allows for three-dimensional battles that can start on the street and end
up on rooftops. You can also switch between the red and black Spider-Man suits, choose to ally with Marvel's heroes or
villains and decide what missions to undertake to save Manhattan from destruction.

Extra Credit - As you progress, you earn experience in multiple combat disciplines so you can custom-design your ideal
Spider-Man Instant Replay - dozens of story choices and character customization options"""
    descfont=15
    descfg='Blue'
    tpath='Media/smwost.mp4'
    fpss=0.0265
    price=699
    btnbg='Red'
    btnfg='Black'
    btntxt='Buy Now'
    developer='Treyarch, Shaba\nGames, Aspyr'
    publisher='Activision'
    genre='Action, Adventure'
    rating="5.3/10"
    poster='Media/smwosposter.jpg'
    title1='Spider-Man:@Web Of Shadows'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def xmow():
    title="X-MEN ORIGINS : WOLVERINE"
    x1=380
    y1=0
    gimg1='Media/xmow1.jpg'
    gimg2='Media/xmow2.jpg'
    gimg3='Media/xmow3.jpg'
    gimg4='Media/xmow4.jpg'
    gimg5='Media/xmow5.jpg'
    tsoundpath='Media/xmowta.wav'
    description = """Uncage Wolverine's tragic past and discover how the ultimate weapon was created.


Unleash the razor sharp adamantium claws, feral instincts and mutant regeneration
power of the world's fiercest hero. Visceral combat. Pure rage. Epic battles.
Take on the impossible in your hunt to uncover the secrets of
Weapon X then exact your revenge."""
    descfont=20
    descfg='Silver'
    tpath='Media/xmowt.mp4'
    fpss=0.0265
    price=899
    btnbg='Gold'
    btnfg='Orange'
    btntxt='Buy Now'
    developer='Raven Software'
    publisher='Activision'
    genre='Action, Adventure\nHack and Slash'
    rating="7.8/10"
    poster='Media/xmowposter.jpg'
    title1='X-Men Origins:@Wolverine'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def aw():
    title="ALAN WAKE"
    x1=520
    y1=0
    gimg1='Media/aw1.jpg'
    gimg2='Media/aw2.jpg'
    gimg3='Media/aw3.jpg'
    gimg4='Media/aw4.jpg'
    gimg5='Media/aw5.jpg'
    tsoundpath='Media/awta.wav'
    description = """When the wife of the best-selling writer Alan Wake disappears on their vacation, his search turns up pages from a
thriller he doesn’t even remember writing. A Dark Presence stalks the small town of Bright Falls, pushing Wake to the brink of sanity in
his fight to unravel the mystery and save his love.

Presented in the style of a TV series, Alan Wake features the trademark Remedy storytelling and pulse-pounding action sequences. As players
dive deeper and deeper into the mystery, they’ll face overwhelming odds, plot twists, and cliffhangers. It’s only by mastering the Fight With
Light combat mechanic that they can stay one step ahead of the darkness that spreads across Bright Falls.

With the body of an action game and the mind of a psychological thriller, Alan Wake’s intense atmosphere, deep and multilayered story, and
exceptionally tense combat sequences provide players with an entertaining and original gaming experience."""
    descfont=13
    descfg='Blue'
    tpath='Media/awt.mp4'
    fpss=0.0265
    price=459
    btnbg='Blue'
    btnfg='Silver'
    btntxt='Buy Now'
    developer='Remedy\nEntertainment'
    publisher='Remedy\nEntertainment'
    genre='Action, Adventure'
    rating="8.3/10"
    poster='Media/awposter.jpg'
    title1='Alan Wake'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def awan():
    title="ALAN WAKE'S AMERICAN NIGHTMARE"
    x1=380
    y1=0
    gimg1='Media/awan1.jpg'
    gimg2='Media/awan2.jpg'
    gimg3='Media/awan3.jpg'
    gimg4='Media/awan4.jpg'
    gimg5='Media/awan5.jpg'
    tsoundpath='Media/awanta.wav'
    description = """In this brand new standalone experience, Alan Wake fights the herald of darkness,
the evil Mr. Scratch!

A thrilling new storyline, hordes of creepy enemies, serious firepower and beautiful Arizona locations, combined with a fun
and challenging new game mode make this a must for Alan Wake veterans, and the perfect jumping on point for new players!"""
    descfont=15
    descfg='Silver'
    tpath='Media/awant.mp4'
    fpss=0.0265
    price=329
    btnbg='Orange'
    btnfg='Blue'
    btntxt='Buy Now'
    developer='Remedy\nEntertainment'
    publisher='Remedy\nEntertainment'
    genre='Action, Adventure'
    rating="7.3/10"
    poster='Media/awanposter.jpg'
    title1='Alan Wakes@American Nightmare'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

def dpl():
    title="DEADPOOL"
    x1=550
    y1=0
    gimg1='Media/dpl1.jpg'
    gimg2='Media/dpl2.jpg'
    gimg3='Media/dpl3.jpg'
    gimg4='Media/dpl4.jpg'
    gimg5='Media/dpl5.jpg'
    tsoundpath='Media/dplta.wav'
    description = """There are a few important things I need to say before you crack into my insanely sweet game. I'm a mercenary
with an accelerated healing factor. I've been described as unstable, which is just plain coo-coo. I'm gonna battle
for the safety of humans and mutants. Be prepared for just about anything.

Incredible Action: I made sure to capture all my good sides, so I made my game a third-person action-shooter.
X-Men Fans: Keep a look out because some of my X-Men pals are making an appearance.
Insane Battle: I'm really good at killing, so I made it a blast stringing together combos, and totally eviscerating
my enemies.
Weapons Galore: I brought my skills and a buttload of my favorite things. Katanas, guns, explosives, duct tape
and of course, yours truly - ME!"""
    descfont=15
    descfg='Red'
    tpath='Media/dplt.mp4'
    fpss=0.0265
    price=1499
    btnbg='Red'
    btnfg='Black'
    btntxt='Buy Now'
    developer='High Moon\nStudios, Mercenary\nTechnology'
    publisher='Activision'
    genre='Action, Adventure'
    rating="6/10"
    poster='Media/dplposter.jpg'
    title1='Deadpool'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def nfsr():
    title="NEED FOR SPEED : RIVALS"
    x1=400
    y1=0
    gimg1='Media/nfsr1.jpg'
    gimg2='Media/nfsr2.jpg'
    gimg3='Media/nfsr3.jpg'
    gimg4='Media/nfsr4.jpg'
    gimg5='Media/nfsr5.jpg'
    tsoundpath='Media/nfsrta.wav'
    description = """Own the complete Need for Speed Rivals experience. Get the full game, plus all six downloadable content packs with the Complete Edition.

Key features

6 additional packs — Get the Simply Jaguar Complete Pack, the Ferrari Edizioni Speciali Complete Pack, the Concept Lamborghini Complete Pack, the Koenigsegg Agera One, the Complete Movie Pack,
and the Loaded Garage Pack.

Race with friends — Imagine your race and your friend’s pursuit colliding, creating a world where no 2 events feel the same. Don’t want to play with others? Simply choose to make Redview County
yours alone and dominate the advanced Racer and Cop AI.

High-stakes rivalry — Racers are lone wolves out for glory, driving agile cars built for high-speed racing and epic chases. Cops work in teams to hunt down and bust racers using the full power
of the police force. Switch roles whenever you like, and watch the stakes grow through a new scoring system that puts your speed points on the line.

Your car, your identity — Personalize your cars with performance and style modifications. Power up your car with the latest upgrades in pursuit technology and personalize your bodywork with
fresh paint jobs, liveries, custom license plates, rims, and decals to show off your car to the world.

Pursuit and evasion tech — Use the latest pursuit tech and modifications to change your pursuit or escape strategy on the fly. Racers evade Cops using turbo bursts, jammers, and
electromagnetic pulses. Cops will be armed for aggressive busts, deploying shockwaves, spike strips, and calling in police roadblocks or helicopter support."""
    descfont=8
    descfg='Blue'
    tpath='Media/nfsrt.mp4'
    fpss=0.0265
    price=999
    btnbg='Black'
    btnfg='Blue'
    btntxt='Buy Now'
    developer='Criterion\nSoftware'
    publisher='Electronic Arts'
    genre='Action, Adventure,\nRacing'
    rating="7.6/10"
    poster='Media/nfsrposter.jpg'
    title1='Need For Speed:@Rivals'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)


def nfsp():
    title="NEED FOR SPEED : PAYBACK"
    x1=400
    y1=0
    gimg1='Media/nfsp1.jpg'
    gimg2='Media/nfsp2.jpg'
    gimg3='Media/nfsp3.jpg'
    gimg4='Media/nfsp4.jpg'
    gimg5='Media/nfsp5.jpg'
    tsoundpath='Media/nfspta.wav'
    description = """Set in the underworld of Fortune Valley, you and your crew were divided by betrayal and reunited by revenge to take down The House, a nefarious cartel that rules the city’s casinos, criminals and cops.
In this corrupt gambler’s paradise, the stakes are high and The House always wins.

Craft unique rides with deeper performance and visual customization than ever before. Push them to the limit when you narrowly escape the heat in epic cop battles. From insane heist missions to
devastating car battles to jaw-dropping set piece moments, Need for Speed Payback delivers an edge-of-your-seat, adrenaline-fueled action-driving fantasy.

Key Features:
Scrap to stock to supercar. Your car is at the center of everything you do in Need for Speed Payback. Endlessly fine-tune your performance with each of the five distinct car classes
(Race, Drift, Off-Road, Drag and Runner) to turn the tables on the competition in any race, mission or challenge. Live out an action-driving fantasy. Play as three distinct characters
united by one common goal: revenge. Tyler, Mac and Jess team up to even the score against all odds, and enter the ultimate race to take down The House. Battle cops with ever-increasing
intensity, race against rivals across the city and drive on and off-road through mountains, canyons and deserts. High stakes competition. Win big with all-new Risk vs Reward gameplay.
Intense cop chases mean the stakes have never been higher. Challenge your friends or potential rivals via Autolog recommendations throughout the events or go head-to-head in classic
online leaderboards.

The Need for Speed™ Payback - Deluxe Edition gives you an edge over the competition. Stand out from the crowd with exclusive customization items and receive in-game discounts, Rep bonuses
and five shipments to get your adventure started.

Also includes the upcoming Story Mission Pack and the Need for Speed™ Payback Platinum Car Pack with exclusive† Platinum Blue Underglow."""
    descfont=8
    descfg='Red'
    tpath='Media/nfspt.mp4'
    fpss=0.0265
    price=1499
    btnbg='Sky Blue'
    btnfg='Yellow'
    btntxt='Buy Now'
    developer='Ghost Games'
    publisher='Electronic Arts'
    genre='Action, Adventure,\nSports, Racing,\nStrategy'
    rating="6.2/10"
    poster='Media/nfspposter.jpg'
    title1='Need For Speed:@Payback'
    show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)

    
#Game Details Page
def Game_Details_Page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1):
    global frame0
    global panel
    global stopvid
    global thread1
    global h
    global change
    global audioplay
    Window.update()
    stopvid=False
    change=""
    PlaySound(None, SND_PURGE)
    audioplay=False
    h=1
    #Background
    frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
    frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    panel = tek.Label(frame0, image = BGimg6)
    panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    #Top Bar
    panel.rowconfigure(0,weight=1)
    panel.columnconfigure(0,weight=1)
    frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
    frame1.grid(row=0,column=0,sticky="new")
    label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
    label1.pack(fill=tek.X, expand=True)

    #Top bar buttons
    def btinte(e):
        e.widget.config(bg='red')
        return
    def btintl(e):
        e.widget.config(bg='Sky Blue')
        return

    Panel1 = tek.Label(frame1, image = Img1)
    Panel1.place(x = 0, y = 0)

    Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
    Name.place(x=54,y=0,width=300,height=52)

    home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=lambda:antierror0(thread1,"Home"))
    home.place(x=354,y=0,width=120,height=52)

    nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
    nu.place(x=474,y=0,width=120,height=52)

    browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=lambda:antierror0(thread1,"Browse"))
    browse.place(x=594,y=0,width=120,height=52)

    search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
    search.place(x=714,y=0,width=120,height=52)

    abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=lambda:antierror0(thread1,"About"))
    abt.place(x=834,y=0,width=120,height=52)

    if status == "Logged In":
        login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=lambda:antierror0(thread1,"Profile"))
        login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
        pp=tek.Label(frame1,image=acct_dp_final1)
        pp.place(relx=1.0,y=0,anchor="ne")
    else:
        login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=lambda:antierror0(thread1,"Login"))
        login_btn.place(x=1246,y=0,width=120,height=52)

    for btn in [home,nu,browse,search,abt,login_btn]:
        btn.bind("<Enter>",btinte)
        btn.bind("<Leave>",btintl)

    #Game Details Panel 
    gamed_panel=tek.Label(panel,bg='#2c2f33',height=42,width=191)
    gamed_panel.place(x=9,y=58)

    gamed_label1=tek.Label(gamed_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text=title)
    gamed_label1.place(x=x1,y=y1)
    gamed_label2=tek.Label(gamed_panel,bg='#2c2f33',fg='Cyan',text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    gamed_label2.place(x=0,y=50)

    back_btn=tek.Button(master=gamed_panel,text="< Back",font=('Avellana Pro',18,'bold'),bg="Orange",fg="Blue",cursor="hand2",bd=0,activebackground='lime',activeforeground='blue',command=lambda:antierror0(thread1,"Browse"))
    back_btn.place(relx=0.0,rely=0.0,width=100,height=35)
    #Sneak Peek Box
    frame2=tek.Frame(master=gamed_panel, width=550, height=309.38, relief=tek.RIDGE, bd=1,bg='#23272a')
    frame2.place(x=250,y=70)

    gimages=[gimg1,gimg2,gimg3,gimg4,gimg5]

    g=2
    for gimage in gimages:
        gimgpath = gimage
        gimg = Image.open(gimgpath)
        gimg = gimg.resize((550,309))
        gimg = ImageTk.PhotoImage(gimg)
        globals()["gimage" + str(g)] = gimg
        g += 1
    def imager():
        global stopvid
        global thread1
        global h
        global a
        global d
        global change
        change=""
        stopvid = True
        d = False
        a = True
        PlaySound(None, SND_PURGE)
        if h in range(1,6):
            h+=1
            Panel2["image"]= globals()["gimage"+str(h)]
        else:
            h=1
            stopvid=False
            thread1 = threading.Thread(target=stream1, args=(Panel2,))
            thread1.daemon = True
            thread1.start()
            PlaySound(tsoundpath, SND_FILENAME | SND_ASYNC | SND_LOOP)

    def imagel():
        global stopvid
        global thread1
        global h
        global a
        global d
        global change
        change=""
        stopvid=True
        a = False
        d = True
        PlaySound(None, SND_PURGE)
        if h in range(3,7):
            h-=1
            Panel2["image"]= globals()["gimage"+str(h)]
        elif h == 2:
            h-=1
            stopvid=False
            thread1 = threading.Thread(target=stream1, args=(Panel2,))
            thread1.daemon = True
            thread1.start()
            PlaySound(tsoundpath, SND_FILENAME | SND_ASYNC | SND_LOOP)
        else:
            h=6
            stopvid=True
            
            
    Panel2 = tek.Label(frame2,bd=0)
    Panel2.place(x = -1, y = -1)

    nextr=tek.Button(master=frame0,text="->",bg="Green",fg="Yellow",font=('Bacon',15,'bold'),cursor="hand2",bd=0,command=imager,activebackground='blue',activeforeground='gold')
    nextr.place(x=840,y=260)

    nextl=tek.Button(master=frame0,text="<-",bg="Green",fg="Yellow",font=('Bacon',15,'bold'),cursor="hand2",bd=0,command=imagel,activebackground='blue',activeforeground='gold')
    nextl.place(x=194,y=260)

    gamed_panel1=tek.Label(gamed_panel,bg='#23272a',height=16,width=150,relief=tek.RIDGE)
    gamed_panel1.place(x=0,y=385)

    gamedesc=tek.Label(gamed_panel1,text=description,font=('Apple And Pear',descfont,'bold'),fg=descfg,bg='#23272a',justify='left')
    gamedesc.place(x=0,y=0)


    gamed_panel2=tek.Label(gamed_panel,bg='#23272a',height=37,width=39,relief=tek.RIDGE)
    gamed_panel2.place(relx=1.0,y=70,anchor="ne")

    #Ft Gif
    video_name = tpath #This is your video file path
    video = imageio.get_reader(video_name)

    def stream1(label):
        global stopvid
        global a
        global d
        global change
        PlaySound(tsoundpath, SND_FILENAME | SND_ASYNC | SND_LOOP)
        while True:
            for image in video.iter_data():
                frame_image = ImageTk.PhotoImage(Image.fromarray(image))
                label.config(image=frame_image)
                label.image = frame_image
                if stopvid == True:
                    break
                else:
                    time.sleep(fpss)
            if stopvid == True:
                break
        Window.after(10,lambda:antierror1(thread1))
        if a == True:
            Panel2.config(image=gimage2)
        elif d == True:
            Panel2.config(image=gimage6)
    global thread1
    thread1 = threading.Thread(target=stream1, args=(Panel2,))
    thread1.daemon = True
    thread1.start()

    price_label=tek.Label(gamed_panel2,bg='#23272a',fg='Green',text=(price," G-Coins"),font=('Avellana Pro',22,'bold'),height=3,width=15)
    price_label.place(x=28,y=2)
    buy_btn=tek.Button(gamed_panel2,bg=btnbg,fg=btnfg,height=2,width=25,activebackground='Orange',activeforeground='Yellow',text=btntxt,bd=0,font=('Battlelines',15,'bold'),cursor="hand2",command=lambda:antierrorpay0(thread1,title1,price,poster))
    buy_btn.place(x=21,y=120)

    developer_label=tek.Label(gamed_panel2,bg='#23272a',fg='Orange',font=('Battlelines',15,'bold'),text='Developer:')
    developer_label.place(x=15,y=220)
    developer_label1=tek.Label(gamed_panel2,bg='#23272a',fg='Gold',font=('Battlelines',15,'bold'),text=developer)
    developer_label1.place(x=110,y=220)

    publisher_label=tek.Label(gamed_panel2,bg='#23272a',fg='Orange',font=('Battlelines',15,'bold'),text='Publisher:')
    publisher_label.place(x=15,y=300)
    publisher_label1=tek.Label(gamed_panel2,bg='#23272a',fg='Gold',font=('Battlelines',15,'bold'),text=publisher)
    publisher_label1.place(x=110,y=300)

    genre_label=tek.Label(gamed_panel2,bg='#23272a',fg='Orange',font=('Battlelines',15,'bold'),text='Genre:')
    genre_label.place(x=15,y=380)
    genre_label1=tek.Label(gamed_panel2,bg='#23272a',fg='Gold',font=('Battlelines',15,'bold'),text=genre)
    genre_label1.place(x=110,y=380)

    rating_label=tek.Label(gamed_panel2,bg='#23272a',fg='Orange',font=('Battlelines',15,'bold'),text='Rating:')
    rating_label.place(x=15,y=460)
    rating_label1=tek.Label(gamed_panel2,bg='#23272a',fg='Gold',font=('Battlelines',15,'bold'),text=rating)
    rating_label1.place(x=110,y=460)
 
    insuff_curr_error=tek.Label(gamed_panel2,bg='#23272a',fg='#23272a',font=('Apple And Pear',10,'bold'),text="You don't have enough G-Coins to buy\nthis game! Go refill your wallet\nat the Profile Editing Page!")
    insuff_curr_error.place(x=26,y=500)

    if status == "Logged In":
        tempdict={title1:poster}
        cursor.execute('SELECT Games_Owned FROM Inventory WHERE Username = "%s"' % username)
        result=cursor.fetchall()
        for output in result:
            for value in output:
                Lcheck = value
        Lcheck1=ast.literal_eval(Lcheck)
        if tempdict in Lcheck1:
            buy_btn.config(text="Owned",fg="Black",state=tek.DISABLED)
        else:
            if profval10 < price:
                insuff_curr_error.config(fg="red")
                buy_btn.config(text="Insufficient Balance",bg="Grey",state=tek.DISABLED)
                price_label.config(fg="Red")
    else:
        buy_btn.config(text="LOGIN TO BUY THIS GAME",bg="Grey",state=tek.DISABLED)

#Payment Page
def Payment_Page(title2,price2,poster2):
    global frame0
    global panel
    Window.update()
    #Background
    frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
    frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    panel = tek.Label(frame0, image = BGimg3)
    panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    #Top Bar
    panel.rowconfigure(0,weight=1)
    panel.columnconfigure(0,weight=1)
    frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
    frame1.grid(row=0,column=0,sticky="new")
    label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
    label1.pack(fill=tek.X, expand=True)
    #Top bar buttons
    def btinte(e):
        e.widget.config(bg='red')
        return
    def btintl(e):
        e.widget.config(bg='Sky Blue')
        return

    Panel1 = tek.Label(frame1, image = Img1)
    Panel1.place(x = 0, y = 0)

    Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
    Name.place(x=54,y=0,width=300,height=52)

    home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
    home.place(x=354,y=0,width=120,height=52)

    nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
    nu.place(x=474,y=0,width=120,height=52)

    browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
    browse.place(x=594,y=0,width=120,height=52)

    search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
    search.place(x=714,y=0,width=120,height=52)

    abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
    abt.place(x=834,y=0,width=120,height=52)

    login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
    login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
    pp=tek.Label(frame1,image=acct_dp_final1)
    pp.place(relx=1.0,y=0,anchor="ne")

    for btn in [home,nu,browse,search,abt,login_btn]:
        btn.bind("<Enter>",btinte)
        btn.bind("<Leave>",btintl)

    #Payment Panel
    payment_panel=tek.Label(panel,bg='#2c2f33',height=42,width=130)
    payment_panel.place(x=220,y=58)

    payment_label1=tek.Label(payment_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='PAYMENT SECTION')
    payment_label1.place(x=290,y=2)
    payment_label2=tek.Label(payment_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="ONE STEP AWAY FROM YOUR GAME!")
    payment_label2.place(x=328,y=50)

    pimages=[poster2]
    for pimage in pimages:
        pimgpath = pimage
        pimg = Image.open(pimgpath)
        pimg = pimg.resize((200,270))
        pimg = ImageTk.PhotoImage(pimg)
        globals()["pimage" + str(1)] = pimg
    
    payment_game_label0=tek.Label(payment_panel,bg='#23272a',fg='Blue',bd=0,height=284,width=214,image=pimage1)
    payment_game_label0.place(x=360,y=80)

    checkout_panel=tek.Label(payment_panel,bg='#23272a',height=12,width=130,relief=tek.RIDGE)
    checkout_panel.place(x=-2,y=375)

    title11=list(title2)
    t=0
    while t < len(title11):
        if title11[t] == '@':
            title11[t] = '\n'
        t+=1
    title111=''.join(title11)
    
    name_label=tek.Label(checkout_panel,bg='#23272a',fg='Cyan',font=('Avellana Pro',30,'bold'),text='TITLE:')
    name_label.place(x=70,y=20)
    name_label1=tek.Label(checkout_panel,bg='#2c2f33',fg='Gold',font=('Apple and Pear',20,'bold'),text=title111)
    name_label1.place(x=350,y=20)
    price_label=tek.Label(checkout_panel,bg='#23272a',fg='Cyan',font=('Avellana Pro',30,'bold'),text='PRICE:')
    price_label.place(x=70,y=80)
    price_label1=tek.Label(checkout_panel,bg='#2c2f33',fg='Gold',font=('Apple and Pear',20,'bold'),text=(price2,"G-COINS"))
    price_label1.place(x=350,y=80)

    checktcs1=tek.IntVar()
    tcsdone1=tek.Checkbutton(master=checkout_panel,text="I'VE READ AND AGREE TO ALL THE TERMS & CONDITIONS",bg="#23272a",fg="Green",font=('Apple And Pear',15,'bold'),cursor="hand2",activebackground='#2c2f33',activeforeground='Green',variable=checktcs1)
    tcsdone1.place(x=70,y=140)
    tcsdone1_error=tek.Label(checkout_panel,bg='#23272a',fg='#23272a',font=('Avellana Pro',11,'bold'),text="< PLEASE AGREE TO OUR TERMS & CONDITIONS\nIN ORDER TO BUY YOUR GAME")
    tcsdone1_error.place(x=570,y=138)

    #Handling Errors with situation where user doesn't agree to the T&Cs
    def tcs_check1():
        global checktcsval1
        checktcsval1=checktcs1.get()
        if checktcsval1 == 0:
            tcsdone1_error.config(fg="Red")
        else:
            tcsdone1_error.config(fg="#23272a")
    def loading3():
        panel.after(10,lambda:pay.config(fg='Gold',text='PLEASE WAIT'))
        panel.after(1010,lambda:pay.config(fg='Gold',text='PLEASE WAIT.'))
        panel.after(2010,lambda:pay.config(fg='Gold',text='PLEASE WAIT..'))
        panel.after(3010,lambda:pay.config(fg='Gold',text='PLEASE WAIT...'))
        panel.after(4010,lambda:pay.config(fg='Gold',text='PLEASE WAIT....'))
        panel.after(5010,lambda:pay.config(fg='Gold',text='PLEASE WAIT.....'))
    def pay_and_buy():
        tcs_check1()
        if checktcsval1 == 1:
            loading3()
            cursor.execute('UPDATE Accounts SET Balance = Balance - %s Where Username = "%s"' % (price2,username) )
            cursor.execute('UPDATE Inventory SET Balance = Balance - %s Where Username = "%s"' % (price2,username) )
            cursor.execute('SELECT BALANCE FROM Accounts WHERE Username = "%s"' % (username))
            result0=cursor.fetchall()
            for output0 in result0:
                for value0 in output0:
                    bal00 = value0
            if bal00 <= 0:
                cursor.execute('UPDATE Inventory SET Balance = 0 Where Username = "%s"' % (username) )
            cursor.execute('SELECT Games_Owned FROM Inventory WHERE Username = "%s"' % username)
            result=cursor.fetchall()
            for output in result:
                for value in output:
                    L0 = value
            L1=ast.literal_eval(L0)
            L1.append({title2:poster2})
            L2=str(L1)
            cursor.execute('UPDATE Inventory SET Games_Owned = "%s" WHERE Username = "%s"'% (L2,username))
            conn.commit()
            panel.after(6010,lambda:pay.config(text="BOUGHT!",font=('Battlelines',15,'bold'),fg='Lime'))
            panel.after(11010,lambda:pay.config(text="PAY & BUY NOW",font=('Battlelines',15,'bold'),fg='Yellow'))
            panel.after(11010,show_browse_pages)

    pay=tek.Button(master=payment_panel,text="PAY & BUY NOW",font=('Battlelines',15,'bold'),bg="Red",fg="Yellow",cursor="hand2",bd=0,activebackground='lime',activeforeground='blue',command=pay_and_buy)
    pay.place(x=330,y=570,width=250,height=55)
    def btinte(e):
        e.widget.config(bg='blue')
        return
    def btintl(e):
        e.widget.config(bg='red')
        return
    pay.bind("<Enter>",btinte)
    pay.bind("<Leave>",btintl)
    #music
    global audioplay
    if audioplay == False:
        audioplayback()
    Window.update()

#Inventory Pages
def Inventory_Pages():
    global frame0
    global panel
    Window.update()
    #Background
    frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
    frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    panel = tek.Label(frame0, image = BGimg)
    panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    #misc conversions
    cursor.execute('SELECT Games_Owned FROM Inventory WHERE Username = "%s"' % username)
    result=cursor.fetchall()
    for output in result:
        for value in output:
            L0 = value
        L00=list(L0)
    f=0
    while f < len(L00):
        if L00[f] == '@':
            L00[f] = '\n'
        f+=1
    L000=''.join(L00)
    L1=ast.literal_eval(L000.replace('\n','\\n'))

    #music
    global audioplay
    if audioplay == False:
        audioplayback()

    def Inventory_Page_1():
        global i
        global j
        global k
        global x1
        global y1
        global x2
        global y2
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
        login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
        pp=tek.Label(frame1,image=acct_dp_final1)
        pp.place(relx=1.0,y=0,anchor="ne")

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Inventory Panel
        inventory_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        inventory_panel.place(x=50,y=58)
        inventory_label1=tek.Label(inventory_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='YOUR INVENTORY')
        inventory_label1.place(x=480,y=2)
        inventory_label2=tek.Label(inventory_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="HEY! NOICE COLLECTION YOU'VE GOT THERE BUD!")
        inventory_label2.place(x=462,y=50)
        x1=62
        y1=85
        x2=62
        y2=285
        i=1
        j=0
        k=10
        if len(L1) <= 10:
            browse_back_btn=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L1) > 10 and len(L1) <= 20:
            browse_back_btn=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L1) > 20 and len(L1) <= 30:
            browse_back_btn=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L1) > 30 and len(L1) <= 40:
            browse_back_btn=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L1) > 40 and len(L1) <= 50:
            browse_back_btn=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show5)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_next_btn.place(x=890,y=597,width=80)
        def install(btn,txt):
                panel.after(10,lambda:btn.config(fg='Gold',text='INSTALLING'))
                panel.after(1010,lambda:btn.config(fg='Gold',text='INSTALLING.'))
                panel.after(2010,lambda:btn.config(fg='Gold',text='INSTALLING..'))
                panel.after(3010,lambda:btn.config(fg='Gold',text='INSTALLING...'))
                panel.after(4010,lambda:btn.config(fg='Gold',text='INSTALLING....'))
                panel.after(5010,lambda:btn.config(fg='Gold',text='INSTALLING.....'))
                panel.after(6010,lambda:btn.config(fg='Gold',text='INSTALLED'))
                panel.after(9010,lambda:btn.config(fg='Gold',text=txt))
                panel.after(9015,lambda:btn.config(command=play(btn,txt)))
                    
        def play(btn,txt):
            def playe(e):
                e.widget.config(text="PLAY",bg="Green")
                return
            def playl(e):
                e.widget.config(text=txt,bg="#23272a")
                return
            for bt in [btn]:
                bt.bind("<Enter>",playe)
                bt.bind("<Leave>",playl)
                bt.config(command=msgbox)
        def msgbox():
            messagebox.showinfo("Heads UP!","This application is just a demo to demonstrate how a digital video game distribution service works. You obviously can't actually install or play games via this facility! I don't have the rights to sell those titles anyway :/")

        for dicts in L1[j:k]:
            for key,value in dicts.items():
                globals()["img" + str(i)] = value
                globals()["img" + str(i+1)] = Image.open(globals()["img" + str(i)])
                globals()["img" + str(i+1)] = globals()["img" + str(i+1)].resize((180,200))
                globals()["img" + str(i+1)] = ImageTk.PhotoImage(globals()["img" + str(i+1)])
                globals()["inv_game_label" + str(i)] = tek.Label(inventory_panel,bg='#23272a',fg='Blue',bd=0,height=200,width=180,image=globals()["img" + str(i+1)],anchor="n")
                globals()["inv_game_label" + str(i)].place(x=x1,y=y1)
                globals()["inv_game_btn" + str(i)] = tek.Button(inventory_panel,bg='#23272a',fg='Orange',bd=0,text=key,font=('Avellana Pro',13,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
                globals()["inv_game_btn" + str(i)].place(x=x2,y=y2,height=48,width=180)
                globals()["inv_game_btn" + str(i)].config(command=partial(install,globals()["inv_game_btn" + str(i)],key))
                globals()["inv_game_label" + str(i)].image= globals()["img" + str(i+1)]
                if y1 == 85 and y2 == 285:
                    y1 = 345
                    y2 = 545
                elif y1 == 345 and y2 == 545:
                    y1 = 85
                    y2 = 285
                    x1+=239
                    x2+=239
                i+=1
        Window.update()

    def Inventory_Page_2():
        global i
        global j
        global k
        global x1
        global y1
        global x2
        global y2
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg3)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
        login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
        pp=tek.Label(frame1,image=acct_dp_final1)
        pp.place(relx=1.0,y=0,anchor="ne")

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Inventory Panel
        inventory_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        inventory_panel.place(x=50,y=58)
        inventory_label1=tek.Label(inventory_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='YOUR INVENTORY')
        inventory_label1.place(x=480,y=2)
        inventory_label2=tek.Label(inventory_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="HEY! NOICE COLLECTION YOU'VE GOT THERE BUD!")
        inventory_label2.place(x=462,y=50)
        x1=62
        y1=85
        x2=62
        y2=285
        i=11
        j=10
        k=20
        if len(L1) > 10 and len(L1) <= 20:
            browse_back_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L1) > 20 and len(L1) <= 30:
            browse_back_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L1) > 30 and len(L1) <= 40:
            browse_back_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L1) > 40 and len(L1) <= 50:
            browse_back_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show5)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_next_btn.place(x=890,y=597,width=80)
        def install(btn,txt):
                panel.after(10,lambda:btn.config(fg='Gold',text='INSTALLING'))
                panel.after(1010,lambda:btn.config(fg='Gold',text='INSTALLING.'))
                panel.after(2010,lambda:btn.config(fg='Gold',text='INSTALLING..'))
                panel.after(3010,lambda:btn.config(fg='Gold',text='INSTALLING...'))
                panel.after(4010,lambda:btn.config(fg='Gold',text='INSTALLING....'))
                panel.after(5010,lambda:btn.config(fg='Gold',text='INSTALLING.....'))
                panel.after(6010,lambda:btn.config(fg='Gold',text='INSTALLED'))
                panel.after(9010,lambda:btn.config(fg='Gold',text=txt))
                panel.after(9015,lambda:btn.config(command=play(btn,txt)))
                    
        def play(btn,txt):
            def playe(e):
                e.widget.config(text="PLAY",bg="Green")
                return
            def playl(e):
                e.widget.config(text=txt,bg="#23272a")
                return
            for bt in [btn]:
                bt.bind("<Enter>",playe)
                bt.bind("<Leave>",playl)
                bt.config(command=msgbox)
        def msgbox():
            messagebox.showinfo("Heads UP!","This application is just a demo to demonstrate how a digital video game distribution service works. You obviously can't actually install or play games via this facility! I don't have the rights to sell those titles anyway :/")

        for dicts in L1[j:k]:
            for key,value in dicts.items():
                globals()["img" + str(i)] = value
                globals()["img" + str(i+1)] = Image.open(globals()["img" + str(i)])
                globals()["img" + str(i+1)] = globals()["img" + str(i+1)].resize((180,200))
                globals()["img" + str(i+1)] = ImageTk.PhotoImage(globals()["img" + str(i+1)])
                globals()["inv_game_label" + str(i)] = tek.Label(inventory_panel,bg='#23272a',fg='Blue',bd=0,height=200,width=180,image=globals()["img" + str(i+1)],anchor="n")
                globals()["inv_game_label" + str(i)].place(x=x1,y=y1)
                globals()["inv_game_btn" + str(i)] = tek.Button(inventory_panel,bg='#23272a',fg='Orange',bd=0,text=key,font=('Avellana Pro',13,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
                globals()["inv_game_btn" + str(i)].place(x=x2,y=y2,height=48,width=180)
                globals()["inv_game_btn" + str(i)].config(command=partial(install,globals()["inv_game_btn" + str(i)],key))
                globals()["inv_game_label" + str(i)].image= globals()["img" + str(i+1)]
                if y1 == 85 and y2 == 285:
                    y1 = 345
                    y2 = 545
                elif y1 == 345 and y2 == 545:
                    y1 = 85
                    y2 = 285
                    x1+=239
                    x2+=239
                i+=1
        Window.update()

    def Inventory_Page_3():
        global i
        global j
        global k
        global x1
        global y1
        global x2
        global y2
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg5)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
        login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
        pp=tek.Label(frame1,image=acct_dp_final1)
        pp.place(relx=1.0,y=0,anchor="ne")

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Inventory Panel
        inventory_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        inventory_panel.place(x=50,y=58)
        inventory_label1=tek.Label(inventory_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='YOUR INVENTORY')
        inventory_label1.place(x=480,y=2)
        inventory_label2=tek.Label(inventory_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="HEY! NOICE COLLECTION YOU'VE GOT THERE BUD!")
        inventory_label2.place(x=462,y=50)
        x1=62
        y1=85
        x2=62
        y2=285
        i=21
        j=20
        k=30
        if len(L1) > 20 and len(L1) <= 30:
            browse_back_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L1) > 30 and len(L1) <= 40:
            browse_back_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show4)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L1) > 40 and len(L1) <= 50:
            browse_back_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show5)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show4)
            browse_next_btn.place(x=890,y=597,width=80)
        def install(btn,txt):
                panel.after(10,lambda:btn.config(fg='Gold',text='INSTALLING'))
                panel.after(1010,lambda:btn.config(fg='Gold',text='INSTALLING.'))
                panel.after(2010,lambda:btn.config(fg='Gold',text='INSTALLING..'))
                panel.after(3010,lambda:btn.config(fg='Gold',text='INSTALLING...'))
                panel.after(4010,lambda:btn.config(fg='Gold',text='INSTALLING....'))
                panel.after(5010,lambda:btn.config(fg='Gold',text='INSTALLING.....'))
                panel.after(6010,lambda:btn.config(fg='Gold',text='INSTALLED'))
                panel.after(9010,lambda:btn.config(fg='Gold',text=txt))
                panel.after(9015,lambda:btn.config(command=play(btn,txt)))
                    
        def play(btn,txt):
            def playe(e):
                e.widget.config(text="PLAY",bg="Green")
                return
            def playl(e):
                e.widget.config(text=txt,bg="#23272a")
                return
            for bt in [btn]:
                bt.bind("<Enter>",playe)
                bt.bind("<Leave>",playl)
                bt.config(command=msgbox)
        def msgbox():
            messagebox.showinfo("Heads UP!","This application is just a demo to demonstrate how a digital video game distribution service works. You obviously can't actually install or play games via this facility! I don't have the rights to sell those titles anyway :/")

        for dicts in L1[j:k]:
            for key,value in dicts.items():
                globals()["img" + str(i)] = value
                globals()["img" + str(i+1)] = Image.open(globals()["img" + str(i)])
                globals()["img" + str(i+1)] = globals()["img" + str(i+1)].resize((180,200))
                globals()["img" + str(i+1)] = ImageTk.PhotoImage(globals()["img" + str(i+1)])
                globals()["inv_game_label" + str(i)] = tek.Label(inventory_panel,bg='#23272a',fg='Blue',bd=0,height=200,width=180,image=globals()["img" + str(i+1)],anchor="n")
                globals()["inv_game_label" + str(i)].place(x=x1,y=y1)
                globals()["inv_game_btn" + str(i)] = tek.Button(inventory_panel,bg='#23272a',fg='Orange',bd=0,text=key,font=('Avellana Pro',13,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
                globals()["inv_game_btn" + str(i)].place(x=x2,y=y2,height=48,width=180)
                globals()["inv_game_btn" + str(i)].config(command=partial(install,globals()["inv_game_btn" + str(i)],key))
                globals()["inv_game_label" + str(i)].image= globals()["img" + str(i+1)]
                if y1 == 85 and y2 == 285:
                    y1 = 345
                    y2 = 545
                elif y1 == 345 and y2 == 545:
                    y1 = 85
                    y2 = 285
                    x1+=239
                    x2+=239
                i+=1
        Window.update()

    def Inventory_Page_4():
        global i
        global j
        global k
        global x1
        global y1
        global x2
        global y2
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg7)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
        login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
        pp=tek.Label(frame1,image=acct_dp_final1)
        pp.place(relx=1.0,y=0,anchor="ne")

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Inventory Panel
        inventory_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        inventory_panel.place(x=50,y=58)
        inventory_label1=tek.Label(inventory_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='YOUR INVENTORY')
        inventory_label1.place(x=480,y=2)
        inventory_label2=tek.Label(inventory_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="HEY! NOICE COLLECTION YOU'VE GOT THERE BUD!")
        inventory_label2.place(x=462,y=50)
        x1=62
        y1=85
        x2=62
        y2=285
        i=31
        j=30
        k=40
        if len(L1) > 30 and len(L1) <= 40:
            browse_back_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L1) > 40 and len(L1) <= 50:
            browse_back_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show5)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show5)
            browse_next_btn.place(x=890,y=597,width=80)
        def install(btn,txt):
                panel.after(10,lambda:btn.config(fg='Gold',text='INSTALLING'))
                panel.after(1010,lambda:btn.config(fg='Gold',text='INSTALLING.'))
                panel.after(2010,lambda:btn.config(fg='Gold',text='INSTALLING..'))
                panel.after(3010,lambda:btn.config(fg='Gold',text='INSTALLING...'))
                panel.after(4010,lambda:btn.config(fg='Gold',text='INSTALLING....'))
                panel.after(5010,lambda:btn.config(fg='Gold',text='INSTALLING.....'))
                panel.after(6010,lambda:btn.config(fg='Gold',text='INSTALLED'))
                panel.after(9010,lambda:btn.config(fg='Gold',text=txt))
                panel.after(9015,lambda:btn.config(command=play(btn,txt)))
                    
        def play(btn,txt):
            def playe(e):
                e.widget.config(text="PLAY",bg="Green")
                return
            def playl(e):
                e.widget.config(text=txt,bg="#23272a")
                return
            for bt in [btn]:
                bt.bind("<Enter>",playe)
                bt.bind("<Leave>",playl)
                bt.config(command=msgbox)
        def msgbox():
            messagebox.showinfo("Heads UP!","This application is just a demo to demonstrate how a digital video game distribution service works. You obviously can't actually install or play games via this facility! I don't have the rights to sell those titles anyway :/")

        for dicts in L1[j:k]:
            for key,value in dicts.items():
                globals()["img" + str(i)] = value
                globals()["img" + str(i+1)] = Image.open(globals()["img" + str(i)])
                globals()["img" + str(i+1)] = globals()["img" + str(i+1)].resize((180,200))
                globals()["img" + str(i+1)] = ImageTk.PhotoImage(globals()["img" + str(i+1)])
                globals()["inv_game_label" + str(i)] = tek.Label(inventory_panel,bg='#23272a',fg='Blue',bd=0,height=200,width=180,image=globals()["img" + str(i+1)],anchor="n")
                globals()["inv_game_label" + str(i)].place(x=x1,y=y1)
                globals()["inv_game_btn" + str(i)] = tek.Button(inventory_panel,bg='#23272a',fg='Orange',bd=0,text=key,font=('Avellana Pro',13,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
                globals()["inv_game_btn" + str(i)].place(x=x2,y=y2,height=48,width=180)
                globals()["inv_game_btn" + str(i)].config(command=partial(install,globals()["inv_game_btn" + str(i)],key))
                globals()["inv_game_label" + str(i)].image= globals()["img" + str(i+1)]
                if y1 == 85 and y2 == 285:
                    y1 = 345
                    y2 = 545
                elif y1 == 345 and y2 == 545:
                    y1 = 85
                    y2 = 285
                    x1+=239
                    x2+=239
                i+=1
        Window.update()

    def Inventory_Page_5():
        global i
        global j
        global k
        global x1
        global y1
        global x2
        global y2
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg6)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
        login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
        pp=tek.Label(frame1,image=acct_dp_final1)
        pp.place(relx=1.0,y=0,anchor="ne")

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Inventory Panel
        inventory_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        inventory_panel.place(x=50,y=58)
        inventory_label1=tek.Label(inventory_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='YOUR INVENTORY')
        inventory_label1.place(x=480,y=2)
        inventory_label2=tek.Label(inventory_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="HEY! NOICE COLLECTION YOU'VE GOT THERE BUD!")
        inventory_label2.place(x=462,y=50)
        x1=62
        y1=85
        x2=62
        y2=285
        i=41
        j=40
        k=50
        if len(L1) > 40 and len(L1) <= 50:
            browse_back_btn=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show4)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=show4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(inventory_panel,bg='Orange',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(inventory_panel,bg='Grey',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_next_btn.place(x=890,y=597,width=80)
        def install(btn,txt):
                panel.after(10,lambda:btn.config(fg='Gold',text='INSTALLING'))
                panel.after(1010,lambda:btn.config(fg='Gold',text='INSTALLING.'))
                panel.after(2010,lambda:btn.config(fg='Gold',text='INSTALLING..'))
                panel.after(3010,lambda:btn.config(fg='Gold',text='INSTALLING...'))
                panel.after(4010,lambda:btn.config(fg='Gold',text='INSTALLING....'))
                panel.after(5010,lambda:btn.config(fg='Gold',text='INSTALLING.....'))
                panel.after(6010,lambda:btn.config(fg='Gold',text='INSTALLED'))
                panel.after(9010,lambda:btn.config(fg='Gold',text=txt))
                panel.after(9015,lambda:btn.config(command=play(btn,txt)))
                    
        def play(btn,txt):
            def playe(e):
                e.widget.config(text="PLAY",bg="Green")
                return
            def playl(e):
                e.widget.config(text=txt,bg="#23272a")
                return
            for bt in [btn]:
                bt.bind("<Enter>",playe)
                bt.bind("<Leave>",playl)
                bt.config(command=msgbox)
        def msgbox():
            messagebox.showinfo("Heads UP!","This application is just a demo to demonstrate how a digital video game distribution service works. You obviously can't actually install or play games via this facility! I don't have the rights to sell those titles anyway :/")

        for dicts in L1[j:k]:
            for key,value in dicts.items():
                globals()["img" + str(i)] = value
                globals()["img" + str(i+1)] = Image.open(globals()["img" + str(i)])
                globals()["img" + str(i+1)] = globals()["img" + str(i+1)].resize((180,200))
                globals()["img" + str(i+1)] = ImageTk.PhotoImage(globals()["img" + str(i+1)])
                globals()["inv_game_label" + str(i)] = tek.Label(inventory_panel,bg='#23272a',fg='Blue',bd=0,height=200,width=180,image=globals()["img" + str(i+1)],anchor="n")
                globals()["inv_game_label" + str(i)].place(x=x1,y=y1)
                globals()["inv_game_btn" + str(i)] = tek.Button(inventory_panel,bg='#23272a',fg='Orange',bd=0,text=key,font=('Avellana Pro',13,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
                globals()["inv_game_btn" + str(i)].place(x=x2,y=y2,height=48,width=180)
                globals()["inv_game_btn" + str(i)].config(command=partial(install,globals()["inv_game_btn" + str(i)],key))
                globals()["inv_game_label" + str(i)].image= globals()["img" + str(i+1)]
                if y1 == 85 and y2 == 285:
                    y1 = 345
                    y2 = 545
                elif y1 == 345 and y2 == 545:
                    y1 = 85
                    y2 = 285
                    x1+=239
                    x2+=239
                i+=1
        
        Window.update()

    def show1():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Inventory_Page_1()
    def show2():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Inventory_Page_2()
    def show3():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Inventory_Page_3()
    def show4():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Inventory_Page_4()
    def show5():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Inventory_Page_5()
    Inventory_Page_1()
    Window.update()

#Search Page
def Search_Page():
    global frame0
    global panel
    Window.update()
    #Background
    frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
    frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    panel = tek.Label(frame0, image = BGimg)
    panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    #misc conversions
    cursor.execute('SELECT * FROM Avail_Games')
    result=cursor.fetchall()
    for output in result:
        for value in output:
            L10 = value
        L100=list(L10)
    L1000=''.join(L100)
    L11=ast.literal_eval(L1000)
    #music
    global audioplay
    if audioplay == False:
        audioplayback()

    def btinte(e):
        e.widget.config(bg='blue')
        return
    def btintl(e):
        e.widget.config(bg='red')
        return

    #Top Bar
    panel.rowconfigure(0,weight=1)
    panel.columnconfigure(0,weight=1)
    frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
    frame1.grid(row=0,column=0,sticky="new")
    label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
    label1.pack(fill=tek.X, expand=True)
    #Top bar buttons
    def btinte(e):
        e.widget.config(bg='red')
        return
    def btintl(e):
        e.widget.config(bg='Sky Blue')
        return

    Panel1 = tek.Label(frame1, image = Img1,cursor="hand2")
    Panel1.place(x = 0, y = 0)

    Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold",cursor="hand2")
    Name.place(x=54,y=0,width=300,height=52)

    home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
    home.place(x=354,y=0,width=120,height=52)

    nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
    nu.place(x=474,y=0,width=120,height=52)

    browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
    browse.place(x=594,y=0,width=120,height=52)

    search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',state=tek.ACTIVE)
    search.place(x=714,y=0,width=120,height=52)

    abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
    abt.place(x=834,y=0,width=120,height=52)

    if status == "Logged In":
        login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
        login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
        pp=tek.Label(frame1,image=acct_dp_final1)
        pp.place(relx=1.0,y=0,anchor="ne")
    else:
        login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_login_page)
        login_btn.place(x=1246,y=0,width=120,height=52)

    for btn in [home,nu,browse,search,abt,login_btn]:
        btn.bind("<Enter>",btinte)
        btn.bind("<Leave>",btintl)
        
    #Search Panel
    search_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
    search_panel.place(x=50,y=58)

    search_label1=tek.Label(search_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='SEARCH GAMES')
    search_label1.place(x=490,y=2)
    search_label2=tek.Label(search_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="LOOKING FOR A SPECIFIC FAV GAME EH?")
    search_label2.place(x=484,y=50)

    search_label=tek.Label(search_panel,bg='Blue',fg='Gold',font=('Beway',65,'bold'),text='SEARCH')
    search_label.place(x=510,y=150)
    search_entry= tek.Entry(search_panel,bg='Orange',fg='Yellow',font=('Avellana Pro',48,'bold'))
    search_entry.place(x=250,y=275)

    search_label_error=tek.Label(search_panel,bg='#2c2f33',fg='#2c2f33',font=('Avellana Pro',15,'bold'),text="ERROR! NO MATCHES FOUND! PLEASE CHECK YOUR ENTRY!")
    search_label_error.place(x=385,y=570)
    
    L2 = []
    #loading visual
    def loading6():
        panel.after(10,lambda:search_btn.config(fg='Sky Blue',text='PLEASE WAIT'))
        panel.after(1010,lambda:search_btn.config(fg='Sky Blue',text='PLEASE WAIT.'))
        panel.after(2010,lambda:search_btn.config(fg='Sky Blue',text='PLEASE WAIT..'))
        panel.after(3010,lambda:search_btn.config(fg='Sky Blue',text='PLEASE WAIT...'))
        panel.after(4010,lambda:search_btn.config(fg='Sky Blue',text='PLEASE WAIT....'))
        panel.after(5010,lambda:search_btn.config(fg='Sky Blue',text='PLEASE WAIT.....'))
    def search():
        global L6
        search_criterion = search_entry.get()
        if search_criterion != '':
            loading6()
            regex = """
                    ^({0}+)
                    |
                    .
                    *({0})
                    .
                    *(g)$
                    """.format(search_criterion)
            compiled = re.compile(regex,re.VERBOSE|re.IGNORECASE)
            for element in L11:
                for key,value in element.items():
                    string = (key+":"+value)
                    reg = compiled.fullmatch(string)
                    if reg != None:
                        matchedstr = string.split(":",1)
                        k = matchedstr[0]
                        v = matchedstr[1]
                        matcheddict = {k:v}
                        L2.append(matcheddict)

                    L3 = str(L2)
                    L4=list(L3)
                    f1=0
                    while f1 < len(L4):
                        if L4[f1] == '@':
                            L4[f1] = '\n'
                        f1+=1
                    L5=''.join(L4)
                    L6=ast.literal_eval(L5.replace('\n','\\n'))
                    search_label_error.config(fg='#2c2f33')
                    search_entry.config(bg='Orange')
                    panel.after(6010,lambda:search_btn.config(fg='Sky Blue',text='FOUND!!'))
                    panel.after(7010,lambda:search_btn.config(fg='Sky Blue',text='SEARCH'))
                    panel.after(8010,show_search_results_pages)
        else:
            search_entry.config(bg='Red')
            search_label_error.config(fg='Red')
    search_btn=tek.Button(master=search_panel,text="Search",bg="Orange",fg="Sky Blue",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=search)
    search_btn.place(x=510,y=470,width=250,height=55)

    Window.update()
#Search Results
def Search_Results_Pages():
    global frame0
    global panel
    global L6
    Window.update()
    #Background
    frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
    frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    panel = tek.Label(frame0, image = BGimg)
    panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    #music
    global audioplay
    if audioplay == False:
        audioplayback()
    def Search_Results_Page1():
        global a1
        global b1
        global k1
        global p1
        global q1
        global p2
        global q2
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        def btinte(e):
            e.widget.config(bg='blue')
            return
        def btintl(e):
            e.widget.config(bg='red')
            return

        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1,cursor="hand2")
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold",cursor="hand2")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        if status == "Logged In":
            login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
            login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
            pp=tek.Label(frame1,image=acct_dp_final1)
            pp.place(relx=1.0,y=0,anchor="ne")
        else:
            login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_login_page)
            login_btn.place(x=1246,y=0,width=120,height=52)

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Search Results Panel
        sr_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        sr_panel.place(x=50,y=58)
        sr_label1=tek.Label(sr_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='SEARCH RESULTS')
        sr_label1.place(x=480,y=2)
        sr_label2=tek.Label(sr_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="HERE'S WHAT MATCHED YOUR ENTRY!")
        sr_label2.place(x=462,y=50)
        p1=62
        q1=85
        p2=62
        q2=285
        a1=1
        b1=0
        k1=10

        if len(L6) <= 10:
            browse_back_btn=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L6) > 10 and len(L6) <= 20:
            browse_back_btn=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L6) > 20 and len(L6) <= 30:
            browse_back_btn=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L6) > 30 and len(L6) <= 40:
            browse_back_btn=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L6) > 40 and len(L6) <= 50:
            browse_back_btn=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr5)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_next_btn.place(x=890,y=597,width=80)

        def GoToDetails(btn,txt):
            if txt == "Assassins Creed -\nValhalla":
                acv()
            elif txt == "Cyberpunk 2077":
                cybp()
            elif txt == "Halo - Infinite":
                hi()
            elif txt == "Marvels Avengers":
                mas()
            elif txt == "Among Us":
                au()
            elif txt == "Call Of Duty -\nBack Ops Cold War":
                codbocw()
            elif txt == "Horizon - Zero Dawn":
                hzd()
            elif txt == "The Amazing\nSpider-Man":
                tasm()
            elif txt == "The Amazing\nSpider-Man 2":
                tasm2()
            elif txt == "Minecraft":
                mc()
            elif txt == "Fall Guys":
                fg()
            elif txt == "Rocket League":
                rl()
            elif txt == "Call Of Duty -\nModern Warfare":
                codmw()
            elif txt == "CONTROL":
                cntrl()
            elif txt == "World War Z":
                wwz()
            elif txt == "Assassins Creed -\nDirectors Cut":
                ac1()
            elif txt == "Assassins Creed 2":
                ac2()
            elif txt == "Assassins Creed -\nBrotherhood":
                acbh()
            elif txt == "Assassins Creed -\nRevelations":
                acrvs()
            elif txt == "Assassins Creed 3":
                ac3()
            elif txt == "Assassins Creed 4 -\nBlack Flag":
                ac4bf()
            elif txt == "Assassins Creed -\nRogue":
                acrg()
            elif txt == "Assassins Creed -\nUnity":
                acu()
            elif txt == "Assassins Creed -\nSyndicate":
                acs()
            elif txt == "Assassins Creed -\nOrigins":
                acor()
            elif txt == "Assassins Creed -\nOdyssey":
                acod()
            elif txt == "Batman -\nArkham Asylum":
                baa()
            elif txt == "Batman -\nArkham City":
                bac()
            elif txt == "Batman -\nArkham Origins":
                bao()
            elif txt == "Batman -\nArkham Knight":
                bak()
            elif txt == "Dishonored":
                dhd1()
            elif txt == "Dishonored 2":
                dhd2()
            elif txt == "Dishonored - Death\nOf The Outsider":
                dhddoto()
            elif txt == "Resident Evil 7":
                re7()
            elif txt == "Resident Evil 2\nRemake":
                re2r()
            elif txt == "Resident Evil 3\nRemake":
                re3r()
            elif txt == "Borderlands - Game\nOf The Year":
                brdrl1()
            elif txt == "Borderlands 2 - Game\nOf The Year":
                brdrl2()
            elif txt == "Borderlands -\nThe Pre-Sequel":
                brdrltps()
            elif txt == "Borderlands 3":
                brdrl3()
            elif txt == "Watch_Dogs":
                wd1()
            elif txt == "Watch_Dogs 2":
                wd2()
            elif txt == "Watch Dogs -\nLegion":
                wdl()
            elif txt == "Spider-Man -\nWeb Of Shadows":
                smwos()
            elif txt == "X-Men Origins -\nWolverine":
                xmow()
            elif txt == "Alan Wake":
                aw()
            elif txt == "Alan Wakes\nAmerican Nightmare":
                awan()
            elif txt == "Deadpool":
                dpl()
            elif txt == "Need For Speed -\nRivals":
                nfsr()
            elif txt == "Need For Speed -\nPayback":
                nfsp()
                
        for dicts in L6[b1:k1]:
            for key,value in dicts.items():
                globals()["img" + str(a1)] = value
                globals()["img" + str(a1+1)] = Image.open(globals()["img" + str(a1)])
                globals()["img" + str(a1+1)] = globals()["img" + str(a1+1)].resize((180,200))
                globals()["img" + str(a1+1)] = ImageTk.PhotoImage(globals()["img" + str(a1+1)])
                globals()["sr_game_label" + str(a1)] = tek.Label(sr_panel,bg='#23272a',fg='Blue',bd=0,height=200,width=180,image=globals()["img" + str(a1+1)],anchor="n")
                globals()["sr_game_label" + str(a1)].place(x=p1,y=q1)
                globals()["sr_game_btn" + str(a1)] = tek.Button(sr_panel,bg='#23272a',fg='Orange',bd=0,text=key,font=('Avellana Pro',13,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
                globals()["sr_game_btn" + str(a1)].place(x=p2,y=q2,height=48,width=180)
                globals()["sr_game_btn" + str(a1)].config(command=partial(GoToDetails,globals()["sr_game_btn" + str(a1)],key))
                globals()["sr_game_label" + str(a1)].image= globals()["img" + str(a1+1)]
                if q1 == 85 and q2 == 285:
                    q1 = 345
                    q2 = 545
                elif q1 == 345 and q2 == 545:
                    q1 = 85
                    q2 = 285
                    p1+=239
                    p2+=239
                a1+=1
        Window.update()
    def Search_Results_Page2():
        global a1
        global b1
        global k1
        global p1
        global q1
        global p2
        global q2
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg3)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        if status == "Logged In":
            login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
            login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
            pp=tek.Label(frame1,image=acct_dp_final1)
            pp.place(relx=1.0,y=0,anchor="ne")
        else:
            login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_login_page)
            login_btn.place(x=1246,y=0,width=120,height=52)

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Search Results Panel
        sr_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        sr_panel.place(x=50,y=58)
        sr_label1=tek.Label(sr_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='YOUR INVENTORY')
        sr_label1.place(x=480,y=2)
        sr_label2=tek.Label(sr_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="HEY! NOICE COLLECTION YOU'VE GOT THERE BUD!")
        sr_label2.place(x=462,y=50)
        p1=62
        q1=85
        p2=62
        q2=285
        a1=11
        b1=10
        k1=20
        if len(L6) > 10 and len(L6) <= 20:
            browse_back_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L6) > 20 and len(L6) <= 30:
            browse_back_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L6) > 30 and len(L6) <= 40:
            browse_back_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L6) > 40 and len(L6) <= 50:
            browse_back_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr5)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_next_btn.place(x=890,y=597,width=80)


        def GoToDetails(btn,txt):
            if txt == "Assassins Creed -\nValhalla":
                acv()
            elif txt == "Cyberpunk 2077":
                cybp()
            elif txt == "Halo - Infinite":
                hi()
            elif txt == "Marvels Avengers":
                mas()
            elif txt == "Among Us":
                au()
            elif txt == "Call Of Duty -\nBack Ops Cold War":
                codbocw()
            elif txt == "Horizon - Zero Dawn":
                hzd()
            elif txt == "The Amazing\nSpider-Man":
                tasm()
            elif txt == "The Amazing\nSpider-Man 2":
                tasm2()
            elif txt == "Minecraft":
                mc()
            elif txt == "Fall Guys":
                fg()
            elif txt == "Rocket League":
                rl()
            elif txt == "Call Of Duty -\nModern Warfare":
                codmw()
            elif txt == "CONTROL":
                cntrl()
            elif txt == "World War Z":
                wwz()
            elif txt == "Assassins Creed -\nDirectors Cut":
                ac1()
            elif txt == "Assassins Creed 2":
                ac2()
            elif txt == "Assassins Creed -\nBrotherhood":
                acbh()
            elif txt == "Assassins Creed -\nRevelations":
                acrvs()
            elif txt == "Assassins Creed 3":
                ac3()
            elif txt == "Assassins Creed 4 -\nBlack Flag":
                ac4bf()
            elif txt == "Assassins Creed -\nRogue":
                acrg()
            elif txt == "Assassins Creed -\nUnity":
                acu()
            elif txt == "Assassins Creed -\nSyndicate":
                acs()
            elif txt == "Assassins Creed -\nOrigins":
                acor()
            elif txt == "Assassins Creed -\nOdyssey":
                acod()
            elif txt == "Batman -\nArkham Asylum":
                baa()
            elif txt == "Batman -\nArkham City":
                bac()
            elif txt == "Batman -\nArkham Origins":
                bao()
            elif txt == "Batman -\nArkham Knight":
                bak()
            elif txt == "Dishonored":
                dhd1()
            elif txt == "Dishonored 2":
                dhd2()
            elif txt == "Dishonored - Death\nOf The Outsider":
                dhddoto()
            elif txt == "Resident Evil 7":
                re7()
            elif txt == "Resident Evil 2\nRemake":
                re2r()
            elif txt == "Resident Evil 3\nRemake":
                re3r()
            elif txt == "Borderlands - Game\nOf The Year":
                brdrl1()
            elif txt == "Borderlands 2 - Game\nOf The Year":
                brdrl2()
            elif txt == "Borderlands -\nThe Pre-Sequel":
                brdrltps()
            elif txt == "Borderlands 3":
                brdrl3()
            elif txt == "Watch_Dogs":
                wd1()
            elif txt == "Watch_Dogs 2":
                wd2()
            elif txt == "Watch Dogs -\nLegion":
                wdl()
            elif txt == "Spider-Man -\nWeb Of Shadows":
                smwos()
            elif txt == "X-Men Origins -\nWolverine":
                xmow()
            elif txt == "Alan Wake":
                aw()
            elif txt == "Alan Wakes\nAmerican Nightmare":
                awan()
            elif txt == "Deadpool":
                dpl()
            elif txt == "Need For Speed -\nRivals":
                nfsr()
            elif txt == "Need For Speed -\nPayback":
                nfsp()
        for dicts in L6[b1:k1]:
            for key,value in dicts.items():
                globals()["img" + str(a1)] = value
                globals()["img" + str(a1+1)] = Image.open(globals()["img" + str(a1)])
                globals()["img" + str(a1+1)] = globals()["img" + str(a1+1)].resize((180,200))
                globals()["img" + str(a1+1)] = ImageTk.PhotoImage(globals()["img" + str(a1+1)])
                globals()["sr_game_label" + str(a1)] = tek.Label(sr_panel,bg='#23272a',fg='Blue',bd=0,height=200,width=180,image=globals()["img" + str(a1+1)],anchor="n")
                globals()["sr_game_label" + str(a1)].place(x=p1,y=q1)
                globals()["sr_game_btn" + str(a1)] = tek.Button(sr_panel,bg='#23272a',fg='Orange',bd=0,text=key,font=('Avellana Pro',13,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
                globals()["sr_game_btn" + str(a1)].place(x=p2,y=q2,height=48,width=180)
                globals()["sr_game_btn" + str(a1)].config(command=partial(GoToDetails,globals()["sr_game_btn" + str(a1)],key))
                globals()["sr_game_label" + str(a1)].image= globals()["img" + str(a1+1)]
                if q1 == 85 and q2 == 285:
                    q1 = 345
                    q2 = 545
                elif q1 == 345 and q2 == 545:
                    q1 = 85
                    q2 = 285
                    p1+=239
                    p2+=239
                a1+=1
        Window.update()

    def Search_Results_Page3():
        global a1
        global b1
        global k1
        global p1
        global q1
        global p2
        global q2
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg5)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        if status == "Logged In":
            login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
            login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
            pp=tek.Label(frame1,image=acct_dp_final1)
            pp.place(relx=1.0,y=0,anchor="ne")
        else:
            login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_login_page)
            login_btn.place(x=1246,y=0,width=120,height=52)

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Search Results Panel
        sr_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        sr_panel.place(x=50,y=58)
        sr_label1=tek.Label(sr_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='YOUR INVENTORY')
        sr_label1.place(x=480,y=2)
        sr_label2=tek.Label(sr_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="HEY! NOICE COLLECTION YOU'VE GOT THERE BUD!")
        sr_label2.place(x=462,y=50)
        p1=62
        q1=85
        p2=62
        q2=285
        a1=21
        b1=20
        k1=30
        if len(L6) > 20 and len(L6) <= 30:
            browse_back_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L6) > 30 and len(L6) <= 40:
            browse_back_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr4)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L6) > 40 and len(L6) <= 50:
            browse_back_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr5)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr4)
            browse_next_btn.place(x=890,y=597,width=80)


        def GoToDetails(btn,txt):
            if txt == "Assassins Creed -\nValhalla":
                acv()
            elif txt == "Cyberpunk 2077":
                cybp()
            elif txt == "Halo - Infinite":
                hi()
            elif txt == "Marvels Avengers":
                mas()
            elif txt == "Among Us":
                au()
            elif txt == "Call Of Duty -\nBack Ops Cold War":
                codbocw()
            elif txt == "Horizon - Zero Dawn":
                hzd()
            elif txt == "The Amazing\nSpider-Man":
                tasm()
            elif txt == "The Amazing\nSpider-Man 2":
                tasm2()
            elif txt == "Minecraft":
                mc()
            elif txt == "Fall Guys":
                fg()
            elif txt == "Rocket League":
                rl()
            elif txt == "Call Of Duty -\nModern Warfare":
                codmw()
            elif txt == "CONTROL":
                cntrl()
            elif txt == "World War Z":
                wwz()
            elif txt == "Assassins Creed -\nDirectors Cut":
                ac1()
            elif txt == "Assassins Creed 2":
                ac2()
            elif txt == "Assassins Creed -\nBrotherhood":
                acbh()
            elif txt == "Assassins Creed -\nRevelations":
                acrvs()
            elif txt == "Assassins Creed 3":
                ac3()
            elif txt == "Assassins Creed 4 -\nBlack Flag":
                ac4bf()
            elif txt == "Assassins Creed -\nRogue":
                acrg()
            elif txt == "Assassins Creed -\nUnity":
                acu()
            elif txt == "Assassins Creed -\nSyndicate":
                acs()
            elif txt == "Assassins Creed -\nOrigins":
                acor()
            elif txt == "Assassins Creed -\nOdyssey":
                acod()
            elif txt == "Batman -\nArkham Asylum":
                baa()
            elif txt == "Batman -\nArkham City":
                bac()
            elif txt == "Batman -\nArkham Origins":
                bao()
            elif txt == "Batman -\nArkham Knight":
                bak()
            elif txt == "Dishonored":
                dhd1()
            elif txt == "Dishonored 2":
                dhd2()
            elif txt == "Dishonored - Death\nOf The Outsider":
                dhddoto()
            elif txt == "Resident Evil 7":
                re7()
            elif txt == "Resident Evil 2\nRemake":
                re2r()
            elif txt == "Resident Evil 3\nRemake":
                re3r()
            elif txt == "Borderlands - Game\nOf The Year":
                brdrl1()
            elif txt == "Borderlands 2 - Game\nOf The Year":
                brdrl2()
            elif txt == "Borderlands -\nThe Pre-Sequel":
                brdrltps()
            elif txt == "Borderlands 3":
                brdrl3()
            elif txt == "Watch_Dogs":
                wd1()
            elif txt == "Watch_Dogs 2":
                wd2()
            elif txt == "Watch Dogs -\nLegion":
                wdl()
            elif txt == "Spider-Man -\nWeb Of Shadows":
                smwos()
            elif txt == "X-Men Origins -\nWolverine":
                xmow()
            elif txt == "Alan Wake":
                aw()
            elif txt == "Alan Wakes\nAmerican Nightmare":
                awan()
            elif txt == "Deadpool":
                dpl()
            elif txt == "Need For Speed -\nRivals":
                nfsr()
            elif txt == "Need For Speed -\nPayback":
                nfsp()
        for dicts in L6[b1:k1]:
            for key,value in dicts.items():
                globals()["img" + str(a1)] = value
                globals()["img" + str(a1+1)] = Image.open(globals()["img" + str(a1)])
                globals()["img" + str(a1+1)] = globals()["img" + str(a1+1)].resize((180,200))
                globals()["img" + str(a1+1)] = ImageTk.PhotoImage(globals()["img" + str(a1+1)])
                globals()["sr_game_label" + str(a1)] = tek.Label(sr_panel,bg='#23272a',fg='Blue',bd=0,height=200,width=180,image=globals()["img" + str(a1+1)],anchor="n")
                globals()["sr_game_label" + str(a1)].place(x=p1,y=q1)
                globals()["sr_game_btn" + str(a1)] = tek.Button(sr_panel,bg='#23272a',fg='Orange',bd=0,text=key,font=('Avellana Pro',13,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
                globals()["sr_game_btn" + str(a1)].place(x=p2,y=q2,height=48,width=180)
                globals()["sr_game_btn" + str(a1)].config(command=partial(GoToDetails,globals()["sr_game_btn" + str(a1)],key))
                globals()["sr_game_label" + str(a1)].image= globals()["img" + str(a1+1)]
                if q1 == 85 and q2 == 285:
                    q1 = 345
                    q2 = 545
                elif q1 == 345 and q2 == 545:
                    q1 = 85
                    q2 = 285
                    p1+=239
                    p2+=239
                a1+=1
        Window.update()

    def Search_Results_Page4():
        global a1
        global b1
        global k1
        global p1
        global q1
        global p2
        global q2
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg7)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        if status == "Logged In":
            login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
            login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
            pp=tek.Label(frame1,image=acct_dp_final1)
            pp.place(relx=1.0,y=0,anchor="ne")
        else:
            login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_login_page)
            login_btn.place(x=1246,y=0,width=120,height=52)

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Search Results Panel
        sr_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        sr_panel.place(x=50,y=58)
        sr_label1=tek.Label(sr_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='YOUR INVENTORY')
        sr_label1.place(x=480,y=2)
        sr_label2=tek.Label(sr_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="HEY! NOICE COLLECTION YOU'VE GOT THERE BUD!")
        sr_label2.place(x=462,y=50)
        p1=62
        q1=85
        p2=62
        q2=285
        a1=31
        b1=30
        k1=40
        if len(L6) > 30 and len(L6) <= 40:
            browse_back_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_next_btn.place(x=890,y=597,width=80)
        elif len(L6) > 40 and len(L6) <= 50:
            browse_back_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr5)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr5)
            browse_next_btn.place(x=890,y=597,width=80)


        def GoToDetails(btn,txt):
            if txt == "Assassins Creed -\nValhalla":
                acv()
            elif txt == "Cyberpunk 2077":
                cybp()
            elif txt == "Halo - Infinite":
                hi()
            elif txt == "Marvels Avengers":
                mas()
            elif txt == "Among Us":
                au()
            elif txt == "Call Of Duty -\nBack Ops Cold War":
                codbocw()
            elif txt == "Horizon - Zero Dawn":
                hzd()
            elif txt == "The Amazing\nSpider-Man":
                tasm()
            elif txt == "The Amazing\nSpider-Man 2":
                tasm2()
            elif txt == "Minecraft":
                mc()
            elif txt == "Fall Guys":
                fg()
            elif txt == "Rocket League":
                rl()
            elif txt == "Call Of Duty -\nModern Warfare":
                codmw()
            elif txt == "CONTROL":
                cntrl()
            elif txt == "World War Z":
                wwz()
            elif txt == "Assassins Creed -\nDirectors Cut":
                ac1()
            elif txt == "Assassins Creed 2":
                ac2()
            elif txt == "Assassins Creed -\nBrotherhood":
                acbh()
            elif txt == "Assassins Creed -\nRevelations":
                acrvs()
            elif txt == "Assassins Creed 3":
                ac3()
            elif txt == "Assassins Creed 4 -\nBlack Flag":
                ac4bf()
            elif txt == "Assassins Creed -\nRogue":
                acrg()
            elif txt == "Assassins Creed -\nUnity":
                acu()
            elif txt == "Assassins Creed -\nSyndicate":
                acs()
            elif txt == "Assassins Creed -\nOrigins":
                acor()
            elif txt == "Assassins Creed -\nOdyssey":
                acod()
            elif txt == "Batman -\nArkham Asylum":
                baa()
            elif txt == "Batman -\nArkham City":
                bac()
            elif txt == "Batman -\nArkham Origins":
                bao()
            elif txt == "Batman -\nArkham Knight":
                bak()
            elif txt == "Dishonored":
                dhd1()
            elif txt == "Dishonored 2":
                dhd2()
            elif txt == "Dishonored - Death\nOf The Outsider":
                dhddoto()
            elif txt == "Resident Evil 7":
                re7()
            elif txt == "Resident Evil 2\nRemake":
                re2r()
            elif txt == "Resident Evil 3\nRemake":
                re3r()
            elif txt == "Borderlands - Game\nOf The Year":
                brdrl1()
            elif txt == "Borderlands 2 - Game\nOf The Year":
                brdrl2()
            elif txt == "Borderlands -\nThe Pre-Sequel":
                brdrltps()
            elif txt == "Borderlands 3":
                brdrl3()
            elif txt == "Watch_Dogs":
                wd1()
            elif txt == "Watch_Dogs 2":
                wd2()
            elif txt == "Watch Dogs -\nLegion":
                wdl()
            elif txt == "Spider-Man -\nWeb Of Shadows":
                smwos()
            elif txt == "X-Men Origins -\nWolverine":
                xmow()
            elif txt == "Alan Wake":
                aw()
            elif txt == "Alan Wakes\nAmerican Nightmare":
                awan()
            elif txt == "Deadpool":
                dpl()
            elif txt == "Need For Speed -\nRivals":
                nfsr()
            elif txt == "Need For Speed -\nPayback":
                nfsp()
        for dicts in L6[b1:k1]:
            for key,value in dicts.items():
                globals()["img" + str(a1)] = value
                globals()["img" + str(a1+1)] = Image.open(globals()["img" + str(a1)])
                globals()["img" + str(a1+1)] = globals()["img" + str(a1+1)].resize((180,200))
                globals()["img" + str(a1+1)] = ImageTk.PhotoImage(globals()["img" + str(a1+1)])
                globals()["sr_game_label" + str(a1)] = tek.Label(sr_panel,bg='#23272a',fg='Blue',bd=0,height=200,width=180,image=globals()["img" + str(a1+1)],anchor="n")
                globals()["sr_game_label" + str(a1)].place(x=p1,y=q1)
                globals()["sr_game_btn" + str(a1)] = tek.Button(sr_panel,bg='#23272a',fg='Orange',bd=0,text=key,font=('Avellana Pro',13,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
                globals()["sr_game_btn" + str(a1)].place(x=p2,y=q2,height=48,width=180)
                globals()["sr_game_btn" + str(a1)].config(command=partial(GoToDetails,globals()["sr_game_btn" + str(a1)],key))
                globals()["sr_game_label" + str(a1)].image= globals()["img" + str(a1+1)]
                if q1 == 85 and q2 == 285:
                    q1 = 345
                    q2 = 545
                elif q1 == 345 and q2 == 545:
                    q1 = 85
                    q2 = 285
                    p1+=239
                    p2+=239
                a1+=1
        Window.update()

    def Search_Results_Page5():
        global a1
        global b1
        global k1
        global p1
        global q1
        global p2
        global q2
        global frame0
        global panel
        Window.update()
        #Background
        frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
        frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        panel = tek.Label(frame0, image = BGimg6)
        panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #Top Bar
        panel.rowconfigure(0,weight=1)
        panel.columnconfigure(0,weight=1)
        frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
        frame1.grid(row=0,column=0,sticky="new")
        label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
        label1.pack(fill=tek.X, expand=True)
        #Top bar buttons
        def btinte(e):
            e.widget.config(bg='red')
            return
        def btintl(e):
            e.widget.config(bg='Sky Blue')
            return

        Panel1 = tek.Label(frame1, image = Img1)
        Panel1.place(x = 0, y = 0)

        Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
        Name.place(x=54,y=0,width=300,height=52)

        home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
        home.place(x=354,y=0,width=120,height=52)

        nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
        nu.place(x=474,y=0,width=120,height=52)

        browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
        browse.place(x=594,y=0,width=120,height=52)

        search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
        search.place(x=714,y=0,width=120,height=52)

        abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_about_page)
        abt.place(x=834,y=0,width=120,height=52)

        if status == "Logged In":
            login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
            login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
            pp=tek.Label(frame1,image=acct_dp_final1)
            pp.place(relx=1.0,y=0,anchor="ne")
        else:
            login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_login_page)
            login_btn.place(x=1246,y=0,width=120,height=52)

        for btn in [home,nu,browse,search,abt,login_btn]:
            btn.bind("<Enter>",btinte)
            btn.bind("<Leave>",btintl)

        #Search Results Panel
        sr_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
        sr_panel.place(x=50,y=58)
        sr_label1=tek.Label(sr_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='YOUR INVENTORY')
        sr_label1.place(x=480,y=2)
        sr_label2=tek.Label(sr_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="HEY! NOICE COLLECTION YOU'VE GOT THERE BUD!")
        sr_label2.place(x=462,y=50)
        p1=62
        q1=85
        p2=62
        q2=285
        a1=41
        b1=40
        k1=50
        if len(L6) > 40 and len(L6) <= 50:
            browse_back_btn=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='BACK',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr4)
            browse_back_btn.place(x=290,y=597,width=80)
            browse_btn1=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='1',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr1)
            browse_btn1.place(x=390,y=597,width=80)
            browse_btn2=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='2',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr2)
            browse_btn2.place(x=490,y=597,width=80)
            browse_btn3=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='3',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr3)
            browse_btn3.place(x=597,y=597,width=80)
            browse_btn4=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='4',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",command=showsr4)
            browse_btn4.place(x=690,y=597,width=80)
            browse_btn5=tek.Button(sr_panel,bg='Orange',fg='Cyan',bd=0,text='5',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_btn5.place(x=790,y=597,width=80)
            browse_next_btn=tek.Button(sr_panel,bg='Grey',fg='Cyan',bd=0,text='NEXT',font=('Avellana Pro',12,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2",state=tek.DISABLED)
            browse_next_btn.place(x=890,y=597,width=80)


        def GoToDetails(btn,txt):
            if txt == "Assassins Creed -\nValhalla":
                acv()
            elif txt == "Cyberpunk 2077":
                cybp()
            elif txt == "Halo - Infinite":
                hi()
            elif txt == "Marvels Avengers":
                mas()
            elif txt == "Among Us":
                au()
            elif txt == "Call Of Duty -\nBack Ops Cold War":
                codbocw()
            elif txt == "Horizon - Zero Dawn":
                hzd()
            elif txt == "The Amazing\nSpider-Man":
                tasm()
            elif txt == "The Amazing\nSpider-Man 2":
                tasm2()
            elif txt == "Minecraft":
                mc()
            elif txt == "Fall Guys":
                fg()
            elif txt == "Rocket League":
                rl()
            elif txt == "Call Of Duty -\nModern Warfare":
                codmw()
            elif txt == "CONTROL":
                cntrl()
            elif txt == "World War Z":
                wwz()
            elif txt == "Assassins Creed -\nDirectors Cut":
                ac1()
            elif txt == "Assassins Creed 2":
                ac2()
            elif txt == "Assassins Creed -\nBrotherhood":
                acbh()
            elif txt == "Assassins Creed -\nRevelations":
                acrvs()
            elif txt == "Assassins Creed 3":
                ac3()
            elif txt == "Assassins Creed 4 -\nBlack Flag":
                ac4bf()
            elif txt == "Assassins Creed -\nRogue":
                acrg()
            elif txt == "Assassins Creed -\nUnity":
                acu()
            elif txt == "Assassins Creed -\nSyndicate":
                acs()
            elif txt == "Assassins Creed -\nOrigins":
                acor()
            elif txt == "Assassins Creed -\nOdyssey":
                acod()
            elif txt == "Batman -\nArkham Asylum":
                baa()
            elif txt == "Batman -\nArkham City":
                bac()
            elif txt == "Batman -\nArkham Origins":
                bao()
            elif txt == "Batman -\nArkham Knight":
                bak()
            elif txt == "Dishonored":
                dhd1()
            elif txt == "Dishonored 2":
                dhd2()
            elif txt == "Dishonored - Death\nOf The Outsider":
                dhddoto()
            elif txt == "Resident Evil 7":
                re7()
            elif txt == "Resident Evil 2\nRemake":
                re2r()
            elif txt == "Resident Evil 3\nRemake":
                re3r()
            elif txt == "Borderlands - Game\nOf The Year":
                brdrl1()
            elif txt == "Borderlands 2 - Game\nOf The Year":
                brdrl2()
            elif txt == "Borderlands -\nThe Pre-Sequel":
                brdrltps()
            elif txt == "Borderlands 3":
                brdrl3()
            elif txt == "Watch_Dogs":
                wd1()
            elif txt == "Watch_Dogs 2":
                wd2()
            elif txt == "Watch Dogs -\nLegion":
                wdl()
            elif txt == "Spider-Man -\nWeb Of Shadows":
                smwos()
            elif txt == "X-Men Origins -\nWolverine":
                xmow()
            elif txt == "Alan Wake":
                aw()
            elif txt == "Alan Wakes\nAmerican Nightmare":
                awan()
            elif txt == "Deadpool":
                dpl()
            elif txt == "Need For Speed -\nRivals":
                nfsr()
            elif txt == "Need For Speed -\nPayback":
                nfsp()
        for dicts in L6[b1:k1]:
            for key,value in dicts.items():
                globals()["img" + str(a1)] = value
                globals()["img" + str(a1+1)] = Image.open(globals()["img" + str(a1)])
                globals()["img" + str(a1+1)] = globals()["img" + str(a1+1)].resize((180,200))
                globals()["img" + str(a1+1)] = ImageTk.PhotoImage(globals()["img" + str(a1+1)])
                globals()["sr_game_label" + str(a1)] = tek.Label(sr_panel,bg='#23272a',fg='Blue',bd=0,height=200,width=180,image=globals()["img" + str(a1+1)],anchor="n")
                globals()["sr_game_label" + str(a1)].place(x=p1,y=q1)
                globals()["sr_game_btn" + str(a1)] = tek.Button(sr_panel,bg='#23272a',fg='Orange',bd=0,text=key,font=('Avellana Pro',13,'bold'),activebackground = 'Yellow', activeforeground='Blue',cursor="hand2")
                globals()["sr_game_btn" + str(a1)].place(x=p2,y=q2,height=48,width=180)
                globals()["sr_game_btn" + str(a1)].config(command=partial(GoToDetails,globals()["sr_game_btn" + str(a1)],key))
                globals()["sr_game_label" + str(a1)].image= globals()["img" + str(i+1)]
                if q1 == 85 and q2 == 285:
                    q1 = 345
                    q = 545
                elif q1 == 345 and q2 == 545:
                    q1 = 85
                    q2 = 285
                    p1+=239
                    p2+=239
                a1+=1
            
        Window.update()
    def showsr1():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Search_Results_Page1()
    def showsr2():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Search_Results_Page2()
    def showsr3():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Search_Results_Page3()
    def showsr4():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Search_Results_Page4()
    def showsr5():
        global frame0
        global panel
        frame0.destroy()
        panel.destroy()
        Window.update()
        Search_Results_Page5()
    Search_Results_Page1()
    Window.update()  
#About Page
def About_Page():
    global frame0
    global panel
    Window.update()
    #Background
    frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
    frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    panel = tek.Label(frame0, image = BGimg)
    panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    #Top Bar
    panel.rowconfigure(0,weight=1)
    panel.columnconfigure(0,weight=1)
    frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
    frame1.grid(row=0,column=0,sticky="new")
    label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
    label1.pack(fill=tek.X, expand=True)
    #Top bar buttons
    def btinte(e):
        e.widget.config(bg='red')
        return
    def btintl(e):
        e.widget.config(bg='Sky Blue')
        return

    Panel1 = tek.Label(frame1, image = Img1)
    Panel1.place(x = 0, y = 0)

    Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
    Name.place(x=54,y=0,width=300,height=52)

    home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
    home.place(x=354,y=0,width=120,height=52)

    nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
    nu.place(x=474,y=0,width=120,height=52)

    browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
    browse.place(x=594,y=0,width=120,height=52)

    search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
    search.place(x=714,y=0,width=120,height=52)

    abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',state=tek.ACTIVE)
    abt.place(x=834,y=0,width=120,height=52)

    if status == "Logged In":
        login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
        login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
        pp=tek.Label(frame1,image=acct_dp_final1)
        pp.place(relx=1.0,y=0,anchor="ne")
    else:
        login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_login_page)
        login_btn.place(x=1246,y=0,width=120,height=52)

    for btn in [home,nu,browse,search,abt,login_btn]:
        btn.bind("<Enter>",btinte)
        btn.bind("<Leave>",btintl)

    #About Panel
    about_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
    about_panel.place(x=50,y=58)
    about_label1=tek.Label(about_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='ABOUT US (ME.. ACTUALLY)')
    about_label1.place(x=395,y=2)
    about_label2=tek.Label(about_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="I'M ONE SINGLE GUY. NO GROUP. BUT NEVERMIND...")
    about_label2.place(x=450,y=50)
    about_panel1=tek.Label(about_panel,bg='#23272a',height=36,width=180)
    about_panel1.place(x=-2,y=89)

    abttxt="""the morning... outta nowhere... Well basically it's a demonstration of how digital video game
distribution services work. To be honest, I couldn't find a suitable topic for my project so
I randomly picked this one up since I was already planning to work on GUI based programs.
You obviously can't actually buy real games or install/play them using my application, I
don't even have the rights to sell 'em! But yeah you can enjoy all the efforts I put into it.
Been a nice experience for me. Greatly levelled up my debugging skills as well lol.

Oh and by the way, since you're here to read about the application & the guy behind it,
lemme introduce you to myself.."""

    abttxt1="""I love coding as you can tell by looking at the source code (if you were lucky enough to get
a look!). Oh and while you're at it, why not give the terms of service a read? You can
find them by clicking the button down below."""

    about_titletxt=tek.Label(about_panel1,bg='#23272a',fg='Yellow',font=('Allenatore Regular',50,'bold'),text="GAMERS' INC")
    about_titletxt.place(x=20,y=0)
    about_text0=tek.Label(about_panel1,bg='#23272a',fg='Gold',font=('Baby Boston',15,'bold'),text='is an idea that was born out of a random thought... At 5 in')
    about_text0.place(x=390,y=30)
    about_text=tek.Label(about_panel1,bg='#23272a',fg='Gold',font=('Baby Boston',15,'bold'),text=abttxt,justify=tek.LEFT)
    about_text.place(x=20,y=70)
    about_text1=tek.Label(about_panel1,bg='#23272a',fg='Lime',font=('Baby Boston',15,'bold'),text="Hey! I'm Harsh, a teen aspiring to be a full stack developer.")
    about_text1.place(x=430,y=348)
    about_text2=tek.Label(about_panel1,bg='#23272a',fg='Lime',font=('Baby Boston',15,'bold'),text=abttxt1,justify=tek.LEFT)
    about_text2.place(x=20,y=388)
    tos_btn=tek.Button(about_panel1,bg='Gold',fg='Blue',bd=0,font=('Avellana Pro',15,'bold'),text='TERMS OF SERVICE',activebackground = 'Orange', activeforeground='Blue',cursor="hand2",command=show_terms_of_service_page)
    tos_btn.place(x=530,y=500)

    #music
    global audioplay
    if audioplay == False:
        audioplayback()
    Window.update()

#Terms Of Service Page
def Terms_Of_Service_Page():
    global frame0
    global panel
    Window.update()
    #Background
    frame0=tek.Frame(master=Window,relief=tek.RIDGE, bd=0)
    frame0.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    panel = tek.Label(frame0, image = BGimg4)
    panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    #Top Bar
    panel.rowconfigure(0,weight=1)
    panel.columnconfigure(0,weight=1)
    frame1=tek.Frame(master=panel, width=3, height=3, relief=tek.RIDGE, bd=0)
    frame1.grid(row=0,column=0,sticky="new")
    label1=tek.Label(master=frame1, text="", bg="Navy Blue",height=3,width=3)
    label1.pack(fill=tek.X, expand=True)
    #Top bar buttons
    def btinte(e):
        e.widget.config(bg='red')
        return
    def btintl(e):
        e.widget.config(bg='Sky Blue')
        return

    Panel1 = tek.Label(frame1, image = Img1)
    Panel1.place(x = 0, y = 0)

    Name=tek.Label(master=frame1,font=("Bacon",20,"bold"),text="Gamers' Inc.", bg="Navy Blue",fg="Gold")
    Name.place(x=54,y=0,width=300,height=52)

    home=tek.Button(master=frame1,text="Home",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_home_page)
    home.place(x=354,y=0,width=120,height=52)

    nu=tek.Button(master=frame1,text="News & Updates",bg="Sky Blue",fg="Yellow",font=('Battlelines',12,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_news_and_updates_page)
    nu.place(x=474,y=0,width=120,height=52)

    browse=tek.Button(master=frame1,text="Browse",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_browse_pages)
    browse.place(x=594,y=0,width=120,height=52)

    search=tek.Button(master=frame1,text="Search",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_search_page)
    search.place(x=714,y=0,width=120,height=52)

    abt=tek.Button(master=frame1,text="About",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',state=tek.ACTIVE)
    abt.place(x=834,y=0,width=120,height=52)

    if status == "Logged In":
        login_btn=tek.Button(master=frame1,text=username,bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',anchor="w",activeforeground='orange',command=show_profile_page)
        login_btn.place(relx=1.0,y=0,width=250,height=52,anchor="ne")
        pp=tek.Label(frame1,image=acct_dp_final1)
        pp.place(relx=1.0,y=0,anchor="ne")
    else:
        login_btn=tek.Button(master=frame1,text="Login",bg="Sky Blue",fg="Yellow",font=('Battlelines',15,'bold'),cursor="hand2",bd=0,activebackground='green',activeforeground='orange',command=show_login_page)
        login_btn.place(x=1246,y=0,width=120,height=52)

    for btn in [home,nu,browse,search,abt,login_btn]:
        btn.bind("<Enter>",btinte)
        btn.bind("<Leave>",btintl)

    #Terms Of Service Panel
    tos_panel=tek.Label(panel,bg='#2c2f33',height=42,width=180)
    tos_panel.place(x=50,y=58)
    tos_label1=tek.Label(tos_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',30,'bold'),text='TERMS OF SERVICE')
    tos_label1.place(x=482,y=2)
    tos_label2=tek.Label(tos_panel,bg='#2c2f33',fg='Cyan',font=('Avellana Pro',12,'bold'),text="GOTTA FOLLOW THE RULES EH? YOU DON'T WANNA END UP IN SANTA'S NAUGHTY LIST!")
    tos_label2.place(x=352,y=50)
    tos_panel1=tek.Label(tos_panel,bg='#23272a',height=16,width=180)
    tos_panel1.place(x=-2,y=85)
    tos_panel2=tek.Label(tos_panel,bg='#23272a',height=11,width=180)
    tos_panel2.place(x=-2,y=335)

    tcstxt="""Hey There! Great! I appreciate that you actually came here to give the T&Cs a read! Not a lot of people really do that right? But don't worry! I won't waste much of
your time! Primarily because there's nothing much to add here, and of course, I wouldn't want to waste time of such a law-conscious person. Since this is just a
demonstration (that too for a school project), there aren't any serious terms & conditions really, just don't break it, or... try to copy it since I really put
in a significant amount of effort while developing this application.
Oh and if you're among the few lucky people to get the source code aswell DO NOT TOUCH IT!! I REPEAT, DO.NOT.TOUCH.IT!! THIS IS A SERIOUS WARNING!!
YOU CAN RUIN THE CODE AND YOU WOULDN'T EVEN REALIZE! Oh and by the way, by agreeing to the T&Cs, you also agree to the Privacy Policy
mentioned below. That's it! Have fun using my application!""" 
    tcs_label1=tek.Label(tos_panel1,bg='#23272a',fg='Yellow',font=('Avellana Pro',20,'bold'),text='TERMS & CONDITIONS')
    tcs_label1.place(x=500,y=2)
    tcs_label2=tek.Label(tos_panel1,bg='#23272a',fg='Yellow',font=('Avellana Pro',15,'bold'),text=tcstxt,justify=tek.LEFT)
    tcs_label2.place(x=11,y=45)

    pptxt="""The Privacy Policy lets you know what information is collected while you use my application. Again, since this is only a demonstration, not much of your
information is collected. Only the information that you enter while creating an account is stored on the database for proper functionality of the application. But
that's it, you don't need to panic either! The information which is collected is stored on your device only, it isn't sent or shared with anyone else over the
internet. The database is created and stored on the localhost server, i.e. your own device. So that's all for the privacy policy as well!""" 
    pp_label1=tek.Label(tos_panel2,bg='#23272a',fg='Orange',font=('Avellana Pro',20,'bold'),text='PRIVACY POLICY')
    pp_label1.place(x=500,y=2)
    pp_label2=tek.Label(tos_panel2,bg='#23272a',fg='Orange',font=('Avellana Pro',15,'bold'),text=pptxt,justify=tek.LEFT)
    pp_label2.place(x=11,y=45)

    crctxt="""© 2020 Gamers' Inc. All rights reserved. All trademarks are property of their respective owners in India and other countries. Just kidding, I haven't really made any copyright
claims (At least not yet) But again, I put in significant amount of efforts so please don't try to copy or manipulate my code. Thanks!"""
    cttxt="""If you've got any queries or want to contact me, you can drop a mail on the following ID :
I'll respond at the earliest!"""
    crc_label=tek.Label(tos_panel,bg='#2c2f33',fg='Lime',font=('Avellana Pro',14,'bold'),text=crctxt,justify=tek.LEFT)
    crc_label.place(x=11,y=520)
    ct_label=tek.Label(tos_panel,bg='#2c2f33',fg='Sky Blue',font=('Avellana Pro',14,'bold'),text=cttxt,justify=tek.LEFT)
    ct_label.place(x=11,y=580)
    ct_id=tek.Label(tos_panel,bg='#2c2f33',fg='Gold',font=('Comic Sans MS',14,'bold'),text="hankstark1204@gmail.com")
    ct_id.place(x=650,y=576)
    Window.update()


#Functions to create/switch pages       
def show_welcome_page():
    global frame0
    global panel
    global canvas
    frame0.destroy()
    panel.destroy()
    canvas.destroy()
    Window.update()
    Welcome_Page()
def show_home_page():
    global frame0
    global canvas
    global panel
    frame0.destroy()
    canvas.destroy()
    panel.destroy()
    Window.update()
    Home_Page()
def show_news_and_updates_page():
    global frame0
    global panel
    frame0.destroy()
    panel.destroy()
    Window.update()
    News_And_Updates_Page()
def show_login_page():
    global frame0
    global panel
    frame0.destroy()
    panel.destroy()
    Window.update()
    Login_Page()
def show_profile_page():
    global frame0
    global panel
    frame0.destroy()
    panel.destroy()
    Window.update()
    Profile_Page()
def show_browse_pages():
    global frame0
    global panel
    frame0.destroy()
    panel.destroy()
    Window.update()
    Browse_Pages()
def show_game_details_page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1):
    global frame0
    global panel
    frame0.destroy()
    panel.destroy()
    Window.update()
    Game_Details_Page(title,x1,y1,gimg1,gimg2,gimg3,gimg4,gimg5,tsoundpath,description,descfont,descfg,tpath,fpss,price,btnbg,btnfg,btntxt,developer,publisher,genre,rating,poster,title1)
def show_payment_page(title2,price2,poster2):
    global frame0
    global panel
    frame0.destroy()
    panel.destroy()
    Window.update()
    Payment_Page(title2,price2,poster2)
def show_inventory_pages():
    global frame0
    global panel
    frame0.destroy()
    panel.destroy()
    Window.update()
    Inventory_Pages()
def show_search_page():
    global frame0
    global panel
    frame0.destroy()
    panel.destroy()
    Window.update()
    Search_Page()
def show_search_results_pages():
    global frame0
    global panel
    frame0.destroy()
    panel.destroy()
    Window.update()
    Search_Results_Pages()
def show_about_page():
    global frame0
    global panel
    frame0.destroy()
    panel.destroy()
    Window.update()
    About_Page()
def show_terms_of_service_page():
    global frame0
    global panel
    frame0.destroy()
    panel.destroy()
    Window.update()
    Terms_Of_Service_Page()
Welcome_Page()
Window.update()
Window.mainloop()
