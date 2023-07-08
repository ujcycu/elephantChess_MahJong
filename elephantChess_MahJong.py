# import
import random
import tkinter as tk
from tkinter import messagebox
from alg import transChi,classify,matchTwo,matchThree
import math




# 類別
# 檯面丟出來的牌
class OpenChess:
    # 建構子
    def __init__(self, index, x0, y0):
        # 一列6顆
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
# 檯面待抽的牌
class CloseChess:
    # 建構子
    def __init__(self, index, x1, y1):
        # 一行5顆
        x = math.floor(elephant_num.index(index) / 5)
        y = elephant_num.index(index) % 5
        self.point = [x1 - grid * x, y1 - (grid-10) * y]
        self.chi = transChi([index])
        self.index = index
    
    # 方法
    def add(self):
        canvas.create_text(self.point, text="●", fill="green", font=("標楷體",34,"bold"))
        #canvas.create_text(self.point, text=(self.index,self.chi), fill="white", font=("標楷體",10,"bold"))
    def delete(self):
        canvas.create_text(self.point, text="●", fill="#002240", font=("標楷體",35,"bold"))
# 莊家手上的牌
class BossChess():
    def __init__(self, index, x2, y2, whose):
        # 一列
        if whose == "boss":
            x = boss.index(index) % len(boss)
        elif whose == "user":
            x = user.index(index) % len(user)
        self.point = [x2 + grid * x, y2]
        self.chi = transChi([index])
        self.index = index
    def add(self):
        canvas.create_text(self.point, text="●", fill="green", font=("標楷體",34,"bold"))
        #canvas.create_text(self.point, text=self.chi, fill="black", font=("標楷體",19,"bold"))
    def delete(self):
        canvas.create_text(self.point, text="●", fill="#002240", font=("標楷體",35,"bold"))
# 玩家手上的牌
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

t = 400 #間隔毫秒數
# 發牌
def dealingCard(e):
    print("== 發牌 ==")
    # 防止重複發牌
    if len(elephant_num) > 0:
        return
    
    labelStart['text'] = "發牌中"
    # 洗牌
    for i in range(32):
        elephant_num.append(i)
    shuffle(elephant_num)
    print("elephant_num length= ",len(elephant_num))

    # 畫棋子
    def bossChess():
        boss.append(elephant_num[0])
        elephant_num.pop(0)
        BossChess(boss[-1],xb,yb,"boss").add()
    def userChess():
        user.append(elephant_num[0])
        UserChess(user[-1],xu,yu,"user").add()
        elephant_num.pop(0) 
    # 各發四張
    for i in range(4):
        win.after(i * 2 * t, bossChess) #after:0,2,4,6
        win.after((i*2-1) * t, userChess) #after:1,3,5,7
    
    # 畫待抽的牌
    def closechess():
        labelStart.place_forget()
        for i in elephant_num:
            CloseChess(i,x1,y1).add()
    win.after(8 * t, closechess) #after:8
    
    log() #print log
    Flag = "boss"
    print("輪到", Flag)
    win.after(9 * t, lambda:flag(Flag)) #遊戲走向判斷 #after:9

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
    log() #print log
    Flag = "user"
    print("輪到", Flag)
    flag(Flag) #遊戲走向判斷

# 撿牌
def pickingupCard(who, whose):
    print("==", whose,"撿牌 ==")
    # 手上超過4張不能撿
    if len(who) > 4:
        return
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
    
    Flag = judge(whose) #判定莊家or玩家
    log() #print log
    # 判斷胡了
    if classify(who) != "KOG":
        print(whose, "win!!!")
        tk.messagebox.showinfo(whose, "胡了!!!")
        Flag = ""
    # 和局判斷
    if elephant_num == []:
        tk.messagebox.showinfo("本局", "和局!!!")
        Flag = ""
    flag(Flag) #遊戲走向判斷

# 抽牌
def drawingCard(who, whose):
    print("==", whose,"抽牌 ==")
    # 手上超過4張不能抽
    if len(who) > 4:
        return
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
    
    Flag = judge(whose) #判定莊家or玩家
    log() #print log
    # 判斷胡了
    if classify(who) != "KOG":
        print("you win")
        tk.messagebox.showinfo(whose, "胡了!!!")
        Flag = ""
    if elephant_num == []:
        tk.messagebox.showinfo("本局", "和局!!!")
        Flag = ""
    flag(Flag) #遊戲走向判斷

# 出牌 # 玩家
def playingCard(who, whose):
    print("==", whose,"出牌 ==")
    def key(event):
        # 手上少於5張不能出牌
        if len(who) < 5:
            return
        # 防輸入法切成中文沒keysym值
        if event.keysym == "??":
            tk.messagebox.showinfo("", "請切換輸入法")
        #keysym = repr(event.keysym)
        print ("pressed", event.keysym)
        
        # 檢查是否輸入數字
        isNum = False
        n = int(event.keysym) 
        for i in range(1,6):
            if n == i:
                isNum = True
        if isNum == False:
            tk.messagebox.showinfo("", "請輸入數字1-5")
        else:
            n = n-1 # 按下第幾顆棋
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

            log() #print log
            Flag = "boss"
            print("輪到", Flag)
            flag(Flag) #遊戲走向判斷
        
    win.bind('<Key>', key) #鍵盤事件
    
# 判定莊家or玩家
def judge(whose):
    if whose == "莊家":
        return "boss"
    if whose == "玩家":
        return "user"
    
# Print Log
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
        # 清空陣列
        desk.clear()
        boss.clear()
        user.clear()
        elephant_num.clear()
        # label隱藏&文字
        labelTurn.place_forget()
        #labelTip['text'] = ""
        labelTip.place_forget()
        labelStart['text'] = "請按Enter開始"
        labelStart.place(x=w/2, y=h/2)
        
        win.bind('<Return>', dealingCard) #按enter發牌
        
    elif Flag == "boss":
        # label隱藏顯示&文字
        labelTurn['text'] = "輪到莊家"
        labelTurn.place(x=450, y=50)
        #labelTip['text'] = ""
        labelTip.place_forget()
        labelStart.place_forget()
        
        if len(boss) <= 4:
            win.after(1000,lambda:drawingCard(boss, "莊家")) #莊家抽牌
            #if len(desk) > 0:
            #        win.after(1000,lambda:pickingupCard(user, "莊家")) #按p:玩家撿牌
        elif len(boss) > 4:
            win.after(1000,bossPlayingCard) #莊家隨機出牌
        
    elif Flag == "user":
        # label隱藏顯示&文字
        labelStart.place_forget()
        labelTurn['text'] = "輪到玩家"
        labelTurn.place(x=450, y=450)
        labelTip.place(x=50, y=450)
        
        if len(user) <= 4:
            labelTip['text'] = "抽牌：按Enter \n撿牌：按p"
            def fnEnter(e):
                win.after(1000,lambda:drawingCard(user, "玩家"))
            win.bind('<Return>', fnEnter) #按enter:玩家抽牌
            if len(desk) > 0:
                def fnP(e):
                    win.after(1000,lambda:pickingupCard(user, "玩家")) 
                win.bind('<p>', fnP) #按p:玩家撿牌
        elif len(user) >= 4:
            labelTip['text'] = "選擇要丟出的牌編號 \n由左至右1-5"
            win.after(1000,lambda:playingCard(user, "玩家")) #按1-5:玩家出牌

        
        
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


fontStyle = ["微軟正黑體", 12]
# 遊戲指示
Flag = ""

# label
labelStart = tk.Label(win, text="", bg = "#002240", fg="white", font = fontStyle)
labelStart.place(x=w/2, y=h/2)
labelTurn = tk.Label(win, text=Flag, bg = "#002240", fg="white", font = fontStyle)
labelTip = tk.Label(win, text="", anchor="w", justify="left", bg = "#002240", fg="white", font = ("微軟正黑體", 10))

flag(Flag) #遊戲走向判斷

win.mainloop() #持續顯示視窗

