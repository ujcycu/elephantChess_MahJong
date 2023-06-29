import random
import tkinter as tk
from tkinter import messagebox
from alg import transChi,classify,matchTwo,matchThree


# 洗牌
def shuffle(array):
    random.shuffle(array)
    #print(array)
# 發牌
def dealingCard():
    print("== 發牌 ==")
    #shuffle(elephant)
    shuffle(elephant_num)
    print("elephant_num length= ",len(elephant_num))
    for i in range(4):
        boss.append(elephant_num[0])
        elephant_num.pop(0)
        user.append(elephant_num[0])
        elephant_num.pop(0)
    """
    print(elephant_num)
    print("elephant = ",transChi(elephant_num))
    print("boss = ",transChi(boss))
    print("user = ",transChi(user))
    """
    printText()
    bossbox.insert(tk.END, transChi(boss))
    userbox.insert(tk.END, transChi(user))
    Flag = "boss"
    print("輪到", Flag)
    flag(Flag)

# 莊家隨機出牌
def bossPlayingCard():
    print("== 莊家出牌 ==")
    shuffle(boss)
    desk.append(boss[0])
    boss.pop(0)
    """
    print("elephant = ",transChi(elephant_num))
    print("desk = ",transChi(desk))
    print("boss = ",transChi(boss))
    """
    printText()
    bossbox.delete(1.0, tk.END) #清空
    deskbox.delete(1.0, tk.END) #清空
    bossbox.insert(tk.END, transChi(boss))
    deskbox.insert(tk.END, transChi(desk))
    if elephant_num == []:
        tk.messagebox.showinfo("本局", "和局!!!")
    Flag = "user"
    print("輪到", Flag)
    flag(Flag)

# 撿牌
def pickingupCard(who, whose):
    print("==", whose,"撿牌 ==")
    n = len(desk)-1
    #print(n)
    who.append(desk[n])
    #desk.pop(0)
    desk.pop(n)
    if judge(whose) == "boss":
        bossbox.delete(1.0, tk.END) #清空
        bossbox.insert(tk.END, transChi(boss))
    if judge(whose) == "user":
        userbox.delete(1.0, tk.END) #清空
        userbox.insert(tk.END, transChi(user))
    deskbox.delete(1.0, tk.END) #清空
    deskbox.insert(tk.END, transChi(desk))
    Flag = judge(whose)
    #print(Flag, whose, " = ", who)
    printText()
    if classify(who) != "KOG":
        print(whose, "win!!!")
        tk.messagebox.showinfo(whose, "胡了!!!")
        Flag = ""
    flag(Flag)

# 抽牌
def drawingCard(who, whose):
    print("==", whose,"抽牌 ==")
    who.append(elephant_num[0])
    elephant_num.pop(0)
    if judge(whose) == "boss":
        bossbox.delete(1.0, tk.END) #清空
        bossbox.insert(tk.END, transChi(boss))
    if judge(whose) == "user":
        userbox.delete(1.0, tk.END) #清空
        userbox.insert(tk.END, transChi(user))
    Flag = judge(whose)
    #print(Flag, whose, " = ", who)
    printText()
    if classify(who) != "KOG":
        print("you win")
        tk.messagebox.showinfo(whose, "胡了!!!")
        Flag = ""
    flag(Flag)
# 出牌
def playingCard(who, whose):
    print("==", whose,"出牌 ==")
    n = int(editbox1.get())
    print(n)
    print(who[n])
    desk.append(who[n])
    who.pop(n)
    """
    print("desk = ",transChi(desk))
    print(whose, " = ", who)
    """
    printText()
    if judge(whose) == "boss":
        bossbox.delete(1.0, tk.END) #清空
        bossbox.insert(tk.END, transChi(boss))
    if judge(whose) == "user":
        userbox.delete(1.0, tk.END) #清空
        userbox.insert(tk.END, transChi(user))
    deskbox.delete(1.0, tk.END) #清空
    deskbox.insert(tk.END, transChi(desk))
    if elephant_num == []:
        tk.messagebox.showinfo("本局", "和局!!!")
    Flag = "boss"
    print("輪到", Flag)
    flag(Flag)
# 判定
def judge(whose):
    if whose == "莊家":
        return "boss"
    if whose == "玩家":
        return "user"
def printText():
    print("elephant = ",transChi(elephant_num))
    print(elephant_num)
    print("boss = ",transChi(boss),boss)
    print("user = ",transChi(user),user)
    print("desk = ",transChi(desk),desk)

global Flag

# 象棋
elephant = [ 
    "將","士","士","象","象","車","車","馬", #0-7 
    "馬","包","包","卒","卒","卒","卒","卒", #8-15
    "帥","仕","仕","相","相","俥","俥","傌", #16-23 
    "傌","炮","炮","兵","兵","兵","兵","兵"  #24-31
]

def flag(Flag):
    if Flag == "":
        label['text'] = "請開始"
        button1.place(x=20+250, y=50)
        bossDrawing.place_forget()
        button5.place_forget()
        button3.place_forget()
        button4.place_forget()
        button6.place_forget()
        button7.place_forget()
        editbox1.place_forget()
        # 清空
        deskbox.delete(1.0, tk.END) #清空
        bossbox.delete(1.0, tk.END) #清空
        userbox.delete(1.0, tk.END) #清空
        desk.clear()
        boss.clear()
        user.clear()
        elephant_num.clear()
        for i in range(32):
            elephant_num.append(i)
    elif Flag == "boss":
        label['text'] = "輪到莊家"
        button1.place_forget()
        button4.place_forget()
        button6.place_forget()
        button7.place_forget()
        editbox1.place_forget()
        if len(boss) <= 4:
            #bossDrawing = tk.Button(win, text = "莊家抽牌", command = lambda:drawingCard(boss, "莊家"))
            bossDrawing.place(x=20+250, y=90)
        if len(desk) > 0:
            #button5 = tk.Button(win, text = "莊家撿牌", command = lambda:pickingupCard(boss, "莊家"))
            button5.place(x=90+250, y=90)
        if len(boss) > 4:
            #button3 = tk.Button(win, text = "莊家出牌", command = bossPlayingCard)
            button5.place_forget()
            bossDrawing.place_forget()
            button3.place(x=160+250, y=90)
    elif Flag == "user":
        label['text'] = "輪到玩家"
        button1.place_forget()
        bossDrawing.place_forget()
        button5.place_forget()
        button3.place_forget()
        if len(user) <= 4:
            button4.place(x=20+250, y=130)
        if len(desk) > 0:
            button6.place(x=90+250, y=130)
        if len(user) > 4:
            button4.place_forget()
            button6.place_forget()
            button7.place(x=160+250, y=130)
            editbox1.place(x=230+250, y=130)
        
        
    
# 象棋序號
elephant_num = []
for i in range(32):
    elephant_num.append(i)

boss = [] #莊家
user = [] #玩家
desk = [] #檯面

win = tk.Tk() #產生視窗
win.title("象棋麻將") #視窗標題
win.geometry("600x500") #調整視窗大小

Flag = ""
label = tk.Label(win, text=Flag, font = ("微軟正黑體", 12))
label.place(x=270, y=250)


button1 = tk.Button(win, text = "發牌", command = dealingCard)

#button2
bossDrawing = tk.Button(win, text = "莊家抽牌", command = lambda:drawingCard(boss, "莊家"))
button5 = tk.Button(win, text = "莊家撿牌", command = lambda:pickingupCard(boss, "莊家"))
button3 = tk.Button(win, text = "莊家出牌", command = bossPlayingCard)
button4 = tk.Button(win, text = "玩家抽牌", command = lambda:drawingCard(user, "玩家"))
button6 = tk.Button(win, text = "玩家撿牌", command = lambda:pickingupCard(user, "玩家"))
editbox1 = tk.Entry(width = 4, font = ("微軟正黑體", 12))
button7 = tk.Button(win, text = "玩家出牌", command = lambda:playingCard(user, "玩家"))
bossbox = tk.Text(win, font = ("微軟正黑體", 12))
bossbox.place(x=20, y=50, width=200, height=100)
deskbox = tk.Text(win, font = ("微軟正黑體", 12))
deskbox.place(x=20, y=200, width=200, height=100)
userbox = tk.Text(win, font = ("微軟正黑體", 12))
userbox.place(x=20, y=350, width=200, height=100)


flag(Flag)

win.mainloop() #持續顯示視窗

