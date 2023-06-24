import random
import tkinter as tk

elephant = [
    "將","士","士","象","象","車","車","馬",
    "馬","包","包","卒","卒","卒","卒","卒",
    "帥","仕","仕","相","相","俥","俥","傌",
    "傌","炮","炮","兵","兵","兵","兵","兵"
]
boss = []
user = []
desk = []

# 洗牌
def shuffle(array):
    random.shuffle(array)
    #print(array)
# 發牌
def dealingCard():
    print("== 發牌 ==")
    shuffle(elephant)
    print("elephant length= ",len(elephant))
    for i in range(4):
        boss.append(elephant[0])
        elephant.pop(0)
        user.append(elephant[0])
        elephant.pop(0)
    print("elephant = ",elephant)
    print("boss = ",boss)
    print("user = ",user)
    bossbox.insert(tk.END, boss)
    userbox.insert(tk.END, user)
    Flag = "boss"
    print("輪到", Flag)

# 莊家隨機出牌
def bossPlayingCard():
    print("== 莊家出牌 ==")
    shuffle(boss)
    desk.append(boss[0])
    boss.pop(0)
    print("elephant = ",elephant)
    print("desk = ",desk)
    print("boss = ",boss)
    bossbox.delete(1.0, tk.END) #清空
    deskbox.delete(1.0, tk.END) #清空
    bossbox.insert(tk.END, boss)
    deskbox.insert(tk.END, desk)
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
        bossbox.insert(tk.END, boss)
    if judge(whose) == "user":
        userbox.delete(1.0, tk.END) #清空
        userbox.insert(tk.END, user)
    deskbox.delete(1.0, tk.END) #清空
    deskbox.insert(tk.END, desk)
    Flag = judge(whose)
    print(Flag, whose, " = ", who)

# 抽牌
def drawingCard(who, whose):
    print("==", whose,"抽牌 ==")
    """
    if judge(whose) == "boss":
        bossbox.insert(tk.END, elephant[0])
    if judge(whose) == "user":
        userbox.insert(tk.END, elephant[0])
    """
    who.append(elephant[0])
    elephant.pop(0)
    if judge(whose) == "boss":
        bossbox.delete(1.0, tk.END) #清空
        bossbox.insert(tk.END, boss)
    if judge(whose) == "user":
        userbox.delete(1.0, tk.END) #清空
        userbox.insert(tk.END, user)
    Flag = judge(whose)
    print(Flag, whose, " = ", who)
# 出牌
def playingCard(who, whose):
    print("==", whose,"出牌 ==")
    n = int(editbox1.get())
    print(n)
    print(who[n])
    desk.append(who[n])
    who.pop(n)
    print("desk = ",desk)
    print(whose, " = ", who)
    if judge(whose) == "boss":
        bossbox.delete(1.0, tk.END) #清空
        bossbox.insert(tk.END, boss)
    if judge(whose) == "user":
        userbox.delete(1.0, tk.END) #清空
        userbox.insert(tk.END, user)
    deskbox.delete(1.0, tk.END) #清空
    deskbox.insert(tk.END, desk)
    Flag = "boss"
    print("輪到", Flag)
# 判定
def judge(whose):
    if whose == "莊家":
        return "boss"
    if whose == "玩家":
        return "user"

global Flag

win = tk.Tk() #產生視窗
win.title("象棋麻將") #視窗標題
win.geometry("600x500") #調整視窗大小



button1 = tk.Button(win, text = "發牌", command = dealingCard)
button1.place(x=20+250, y=40)
button2 = tk.Button(win, text = "莊家抽牌", command = lambda:drawingCard(boss, "莊家"))
button2.place(x=20+250, y=80)
button5 = tk.Button(win, text = "莊家撿牌", command = lambda:pickingupCard(boss, "莊家"))
button5.place(x=80+250, y=80)
button3 = tk.Button(win, text = "莊家出牌", command = bossPlayingCard)
button3.place(x=140+250, y=80)
button4 = tk.Button(win, text = "玩家抽牌", command = lambda:drawingCard(user, "玩家"))
button4.place(x=20+250, y=120)
button6 = tk.Button(win, text = "玩家撿牌", command = lambda:pickingupCard(user, "玩家"))
button6.place(x=80+250, y=120)

editbox1 = tk.Entry(width = 4, font = ("微軟正黑體", 12))
editbox1.place(x=200+250, y=120)
#menu = tk.OptionMenu(win, tk.StringVar().set(''), user)
#menu.place(x=200+250, y=160)
button7 = tk.Button(win, text = "玩家出牌", command = lambda:playingCard(user, "玩家"))
button7.place(x=140+250, y=120)


bossbox = tk.Text(win, font = ("微軟正黑體", 12))
bossbox.place(x=20, y=50, width=200, height=100)
deskbox = tk.Text(win, font = ("微軟正黑體", 12))
deskbox.place(x=20, y=200, width=200, height=100)
userbox = tk.Text(win, font = ("微軟正黑體", 12))
userbox.place(x=20, y=350, width=200, height=100)

win.mainloop() #持續顯示視窗

