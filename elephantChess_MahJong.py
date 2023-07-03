# import
import random
import tkinter as tk
from tkinter import messagebox
from alg import transChi,classify,matchTwo,matchThree
import math




# 類別
class OpenChess:
    # 建構子
    def __init__(self, index, x0, y0):
        x = desk.index(index) % 6
        y = math.floor(desk.index(index) / 6)
        self.point = [x0 + grid * x, y0 + grid * y]
        self.chi = transChi([index])
        self.index = index
    
    # 方法
    def add(self):
        canvas.create_text(self.point, text="●", fill="white", font=("標楷體",34,"bold"))
        if self.index < 16: #黑棋
            canvas.create_text(self.point, text="○", fill="black", font=("標楷體",28,"bold"))
            canvas.create_text(self.point, text=self.chi, fill="black", font=("標楷體",19,"bold"))
        else: #紅棋
            canvas.create_text(self.point, text="○", fill="red", font=("標楷體",28,"bold"))
            canvas.create_text(self.point, text=self.chi, fill="red", font=("標楷體",19,"bold"))
    def delete(self):
        canvas.create_text(self.point, text="●", fill="#002240", font=("標楷體",35,"bold"))

class CloseChess:
    # 建構子
    def __init__(self, index, x1, y1):
        x = math.floor(elephant_num.index(index) / 5)
        y = elephant_num.index(index) % 5
        self.point = [x1 - grid * x, y1 - (grid-10) * y]
        self.chi = transChi([index])
        self.index = index
    
    # 方法
    def add(self):
        canvas.create_text(self.point, text="●", fill="green", font=("標楷體",34,"bold"))
        canvas.create_text(self.point, text=(self.index,self.chi), fill="white", font=("標楷體",10,"bold"))
    def delete(self):
        canvas.create_text(self.point, text="●", fill="#002240", font=("標楷體",35,"bold"))

class BossChess():
    def __init__(self, index, x2, y2, whose):
        if whose == "boss":
            x = boss.index(index) % len(boss) #%4
        elif whose == "user":
            x = user.index(index) % len(user)
        #dx = 50
        self.point = [x2 + grid * x, y2]
        self.chi = transChi([index])
        self.index = index
    def add(self):
        canvas.create_text(self.point, text="●", fill="green", font=("標楷體",34,"bold"))
        canvas.create_text(self.point, text=self.chi, fill="black", font=("標楷體",19,"bold"))
    def delete(self):
        canvas.create_text(self.point, text="●", fill="#002240", font=("標楷體",35,"bold"))
class UserChess(BossChess):
    def add(self):
        canvas.create_text(self.point, text="●", fill="white", font=("標楷體",34,"bold"))
        if self.index < 16: #黑棋
            canvas.create_text(self.point, text="○", fill="black", font=("標楷體",28,"bold"))
            canvas.create_text(self.point, text=self.chi, fill="black", font=("標楷體",19,"bold"))
        else: #紅棋
            canvas.create_text(self.point, text="○", fill="red", font=("標楷體",28,"bold"))
            canvas.create_text(self.point, text=self.chi, fill="red", font=("標楷體",19,"bold"))



# 洗牌
def shuffle(array):
    random.shuffle(array)
    #print(array)
    
# 發牌
def dealingCard(e):
    print("== 發牌 ==")
    #shuffle(elephant)
    # 洗牌
    for i in range(32):
        elephant_num.append(i)
    shuffle(elephant_num)
    print("elephant_num length= ",len(elephant_num))
    # 各發四張
    for i in range(4):
        boss.append(elephant_num[0]) 
        elephant_num.pop(0) 
        user.append(elephant_num[0]) 
        elephant_num.pop(0) 
    log() #log
    # 畫棋子
    for i in boss:
        BossChess(i,xb,yb,"boss").add()
    for i in user:
        UserChess(i,xu,yu,"user").add()
    for i in elephant_num:
        CloseChess(i,x1,y1).add()
    # 輪到
    Flag = "boss"
    print("輪到", Flag)
    flag(Flag)

# 莊家隨機出牌
def bossPlayingCard():
    print("== 莊家出牌 ==")
    # 清除
    for i in boss:
        BossChess(i,xb,yb,"boss").delete()
    shuffle(boss) #洗牌
    # 桌牌
    desk.append(boss[0])
    OpenChess(desk[len(desk)-1],x0,y0).add()
    boss.pop(0)
    # 手牌
    for i in boss:
        BossChess(i,xb,yb,"boss").add()

    log()
    if elephant_num == []:
        tk.messagebox.showinfo("本局", "和局!!!")
    Flag = "user"
    print("輪到", Flag)
    flag(Flag)

# 撿牌
def pickingupCard(who, whose):
    print("==", whose,"撿牌 ==")
    # 手牌
    n = len(desk)-1
    who.append(desk[n])
    if judge(whose) == "boss":
        BossChess(boss[len(boss)-1],xb,yb,"boss").add()
    if judge(whose) == "user":
        UserChess(user[len(user)-1],xu,yu,"user").add()
    # 桌牌
    OpenChess(desk[len(desk)-1],x0,y0).delete()
    desk.pop(n)
    
    Flag = judge(whose)
    log()
    if classify(who) != "KOG":
        print(whose, "win!!!")
        tk.messagebox.showinfo(whose, "胡了!!!")
        Flag = ""
    flag(Flag)

# 抽牌
def drawingCard(who, whose):
    print("==", whose,"抽牌 ==")
    # 桌牌 # 抽最後一張牌
    n = len(elephant_num)-1
    who.append(elephant_num[n]) #elephant_num[0]
    CloseChess(elephant_num[n],x1,y1).delete()
    elephant_num.pop(n)
    # 手牌
    if judge(whose) == "boss":
        BossChess(boss[len(boss)-1],xb,yb,"boss").add()
    if judge(whose) == "user":
        UserChess(user[len(user)-1],xu,yu,"user").add()
    
    Flag = judge(whose)
    log()
    if classify(who) != "KOG":
        print("you win")
        tk.messagebox.showinfo(whose, "胡了!!!")
        Flag = ""
    flag(Flag)

# 出牌 # 玩家
def playingCard(who, whose):
    print("==", whose,"出牌 ==")
    def key(event):
        keysym = repr(event.keysym)
        print ("pressed", keysym)
        
        n = int(event.keysym) # 按下第幾顆棋
        if n<0 or n>4:
            tk.messagebox.showinfo("非數字", "請輸入0-4數字")
        if judge(whose) == "user": 
            for i in user:
                UserChess(i,xu,yu,"user").delete() # 清除
        # 桌牌
        desk.append(who[n])
        OpenChess(desk[len(desk)-1],x0,y0).add()
        # 手牌
        who.pop(n)
        if judge(whose) == "user":
            for i in user:
                UserChess(i,xu,yu,"user").add()

        log()
        if elephant_num == []:
            tk.messagebox.showinfo("本局", "和局!!!")
        Flag = "boss"
        print("輪到", Flag)
        flag(Flag)
        
    win.bind('<Key>', key)
    
# 判定莊家or玩家
def judge(whose):
    if whose == "莊家":
        return "boss"
    if whose == "玩家":
        return "user"
# log
def log():
    print("elephant = ",transChi(elephant_num))
    print(elephant_num)
    print("boss = ",transChi(boss),boss)
    print("user = ",transChi(user),user)
    print("desk = ",transChi(desk),desk)

# 遊戲走向判斷
def flag(Flag):
    if Flag == "":
        canvas.create_rectangle(0, 0, w, h, fill="#002240") #清空背景
        desk.clear()
        boss.clear()
        user.clear()
        elephant_num.clear()
        label['text'] = "請按Enter開始"
        win.bind('<Return>', dealingCard)
        
    elif Flag == "boss":
        label['text'] = "輪到莊家"
        if len(boss) <= 4:
            win.after(1000,lambda:drawingCard(boss, "莊家")) #莊家抽牌
            #if len(desk) > 0:
            #        win.after(1000,lambda:pickingupCard(user, "莊家")) #按p:玩家撿牌
        elif len(boss) > 4:
            win.after(1000,bossPlayingCard) #莊家隨機出牌
        
    elif Flag == "user":
        label['text'] = "輪到玩家"
        if len(user) <= 4:
            def fnEnter(e):
                win.after(1000,lambda:drawingCard(user, "玩家"))
            win.bind('<Return>', fnEnter) #按enter:玩家抽牌
            if len(desk) > 0:
                def fnP(e):
                    win.after(1000,lambda:pickingupCard(user, "玩家")) 
                win.bind('<p>', fnP) #按p:玩家撿牌
        elif len(user) > 4:
            win.after(1000,lambda:playingCard(user, "玩家")) #按0-4:玩家出牌
        
        
global Flag

# 象棋
elephant = [ 
    "將","士","士","象","象","車","車","馬", #0-7 
    "馬","包","包","卒","卒","卒","卒","卒", #8-15
    "帥","仕","仕","相","相","俥","俥","傌", #16-23 
    "傌","炮","炮","兵","兵","兵","兵","兵"  #24-31
]    

elephant_num = [] #象棋序號

boss = [] #莊家
user = [] #玩家
desk = [] #桌面

win = tk.Tk() #產生視窗
win.title("象棋麻將") #視窗標題
win.geometry("600x500") #調整視窗大小

# Canvas
w = 600
h = 500
canvas = tk.Canvas(win, width = w, height = h, bg = "#002240")
canvas.place(x = 0, y = 0)

grid = w / 12 #50
# 莊家牌的錨點
xb = w / 2 - grid * 2
yb = grid * 2
# 丟出牌的錨點
x0 = grid
y0 = yb + grid * 1.5
# 待抽排的錨點
x1 =(x0 + grid * 6) + grid * 4 
y1 = y0 + grid * 3
# 玩家牌的錨點
xu = w / 2 - grid * 2
yu = y1 + grid * 1.5



# 遊戲指示
Flag = ""
label = tk.Label(win, text=Flag, font = ("微軟正黑體", 12))
#label.place(x=270, y=250)
label.place(x=50, y=50)
flag(Flag)

win.mainloop() #持續顯示視窗

