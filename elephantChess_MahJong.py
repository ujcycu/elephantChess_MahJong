import random
import tkinter as tk
from tkinter import messagebox


# 序號轉中文
def transChi(array):
    arr = []
    for i in array:
        arr.append(elephant[i])
    return arr

# 判定胡了 #0,1-10,11-15 #16,17-26,27-31
def classify(array):
    chi = transChi(array)
    countB = chi.count('卒')
    countR = chi.count('兵')
    if countB == 5 or countR == 5:
        return "5win!!!"
    elif countB == 3 or countR == 3:
        if countB == 2 or countR == 2:
            return "3卒/兵+2卒/兵!!!"
        else:
            two = matchTwo(array) #找對子
            if two == True:
                return "3卒/兵+對子!!!"
            else:
                return "KOG"
    elif countB == 2 or countR == 2:
        three = matchThree(array) #找順子
        if three == True:
            return "2卒/兵+順子!!!"
        else:
            return "KOG"
    else:
        two = matchTwo(array)
        three = matchThree(array)
        if two == True and three == True:
            return "對子+順子"
        else:
            return "KOG"
# 判定對子
def matchTwo(array): #0, 1-10; 16, 17-26
    for i in array:
        if i == 0: #將
            for j in array:
                if j == 16:
                    return True #"將帥"
        elif i > 0 and i <= 10: #士象車馬包 1-10
            if i%2 == 0:
                for j in array:
                    if j == i-1:
                        return True #"兩支一樣的(黑)"
        elif i > 16 and i <= 26:
            if i%2 == 0:
                for j in array:
                    if j == i-1:
                        return True #"兩支一樣的(紅)"
# 判定順子 # 將士象/車馬包/帥仕相/俥傌炮
def matchThree(array): #0, 1-10; 16, 17-26
    for i in array:
        if i == 0:
            for j in array:
                if j == 1 or j == 2:
                    for k in array:
                        if k == 3 or k == 4:
                            return True #將士象
        elif i == 5 or i == 6:
            for j in array:
                if j == 7 or j == 8:
                    for k in array:
                        if k == 9 or k == 10:
                            return True #車馬包
        elif i == 16:
            for j in array:
                if j == 17 or j == 18:
                    for k in array:
                        if k == 19 or k == 20:
                            return True #帥仕相
        elif i == 21 or i == 22:
            for j in array:
                if j == 23 or j == 24:
                    for k in array:
                        if k == 25 or k == 26:
                            return True #俥傌炮


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
    print(elephant_num)
    print("elephant = ",transChi(elephant_num))
    print("boss = ",transChi(boss))
    print("user = ",transChi(user))
    bossbox.insert(tk.END, transChi(boss))
    userbox.insert(tk.END, transChi(user))
    Flag = "boss"
    print("輪到", Flag)

# 莊家隨機出牌
def bossPlayingCard():
    print("== 莊家出牌 ==")
    shuffle(boss)
    desk.append(boss[0])
    boss.pop(0)
    print("elephant = ",transChi(elephant_num))
    print("desk = ",transChi(desk))
    print("boss = ",transChi(boss))
    bossbox.delete(1.0, tk.END) #清空
    deskbox.delete(1.0, tk.END) #清空
    bossbox.insert(tk.END, transChi(boss))
    deskbox.insert(tk.END, transChi(desk))
    if elephant_num == []:
        tk.messagebox.showinfo("本局", "和局!!!")
    Flag = "user"
    print("輪到", Flag)

# 撿牌
def pickingupCard(who, whose):
    print("==", whose,"撿牌 ==")
    n = len(desk)-1
    print(n)
    who.append(desk[n])
    desk.pop(0)
    if judge(whose) == "boss":
        bossbox.delete(1.0, tk.END) #清空
        bossbox.insert(tk.END, transChi(boss))
    if judge(whose) == "user":
        userbox.delete(1.0, tk.END) #清空
        userbox.insert(tk.END, transChi(user))
    deskbox.delete(1.0, tk.END) #清空
    deskbox.insert(tk.END, transChi(desk))
    Flag = judge(whose)
    print(Flag, whose, " = ", who)
    if classify(who) != "KOG":
        print(whose, "win!!!")
        tk.messagebox.showinfo(whose, "胡了!!!")

# 抽牌
def drawingCard(who, whose):
    print("==", whose,"抽牌 ==")
    """
    if judge(whose) == "boss":
        bossbox.insert(tk.END, elephant[0])
    if judge(whose) == "user":
        userbox.insert(tk.END, elephant[0])
    """
    who.append(elephant_num[0])
    elephant_num.pop(0)
    if judge(whose) == "boss":
        bossbox.delete(1.0, tk.END) #清空
        bossbox.insert(tk.END, transChi(boss))
    if judge(whose) == "user":
        userbox.delete(1.0, tk.END) #清空
        userbox.insert(tk.END, transChi(user))
    Flag = judge(whose)
    print(Flag, whose, " = ", who)
    if classify(who) != "KOG":
        print("you win")
        tk.messagebox.showinfo(whose, "胡了!!!")
# 出牌
def playingCard(who, whose):
    print("==", whose,"出牌 ==")
    n = int(editbox1.get())
    print(n)
    print(who[n])
    desk.append(who[n])
    who.pop(n)
    print("desk = ",transChi(desk))
    print(whose, " = ", who)
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
# 判定
def judge(whose):
    if whose == "莊家":
        return "boss"
    if whose == "玩家":
        return "user"

global Flag

# 象棋
elephant = [ 
    "將","士","士","象","象","車","車","馬", #0-7 
    "馬","包","包","卒","卒","卒","卒","卒", #8-15
    "帥","仕","仕","相","相","俥","俥","傌", #16-23 
    "傌","炮","炮","兵","兵","兵","兵","兵"  #24-31
]
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

button1 = tk.Button(win, text = "發牌", command = dealingCard)
button1.place(x=20+250, y=50)
button2 = tk.Button(win, text = "莊家抽牌", command = lambda:drawingCard(boss, "莊家"))
button2.place(x=20+250, y=90)
button5 = tk.Button(win, text = "莊家撿牌", command = lambda:pickingupCard(boss, "莊家"))
button5.place(x=90+250, y=90)
button3 = tk.Button(win, text = "莊家出牌", command = bossPlayingCard)
button3.place(x=160+250, y=90)
button4 = tk.Button(win, text = "玩家抽牌", command = lambda:drawingCard(user, "玩家"))
button4.place(x=20+250, y=130)
button6 = tk.Button(win, text = "玩家撿牌", command = lambda:pickingupCard(user, "玩家"))
button6.place(x=90+250, y=130)

editbox1 = tk.Entry(width = 4, font = ("微軟正黑體", 12))
editbox1.place(x=230+250, y=130)
#menu = tk.OptionMenu(win, tk.StringVar().set(''), user)
#menu.place(x=200+250, y=160)
button7 = tk.Button(win, text = "玩家出牌", command = lambda:playingCard(user, "玩家"))
button7.place(x=160+250, y=130)

bossbox = tk.Text(win, font = ("微軟正黑體", 12))
bossbox.place(x=20, y=50, width=200, height=100)
deskbox = tk.Text(win, font = ("微軟正黑體", 12))
deskbox.place(x=20, y=200, width=200, height=100)
userbox = tk.Text(win, font = ("微軟正黑體", 12))
userbox.place(x=20, y=350, width=200, height=100)

Flag = "ready?"
label = tk.Label(win, text=Flag, font = ("微軟正黑體", 12))
label.place(x=270, y=250)

win.mainloop() #持續顯示視窗

