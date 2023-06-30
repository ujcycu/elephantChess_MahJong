# import
import tkinter as tk
import math

# 描繪視窗
w = 600
h = 500
win = tk.Tk()
#win.geometry("600x400")
win.geometry("600x500")

# Canvas
#canvas = tk.Canvas(win, width = 600, height = 400, bg = "#002240")
canvas = tk.Canvas(win, width = w, height = h, bg = "#002240")
canvas.place(x = 0, y = 0)


# 類別
class OpenChess:
    # 建構子
    def __init__(self, index, x0, y0):
        self.index = index
        x = self.index % 6
        y = math.floor(self.index / 6)
        #dx = 50
        #dy = 50
        self.point = [x0 + grid * x, y0 + grid * y]
    
    # 方法
    def add(self):
        canvas.create_text(self.point, text="●", fill="white", font=("標楷體",34,"bold"))
        if self.index < 16: #黑棋
            canvas.create_text(self.point, text="○", fill="black", font=("標楷體",28,"bold"))
            canvas.create_text(self.point, text="將", fill="black", font=("標楷體",19,"bold"))
        else: #紅棋
            canvas.create_text(self.point, text="○", fill="red", font=("標楷體",28,"bold"))
            canvas.create_text(self.point, text="帥", fill="red", font=("標楷體",19,"bold"))
    def delete(self):
        canvas.create_text(self.point, text="●", fill="#002240", font=("標楷體",35,"bold"))

class CloseChess:
    # 建構子
    def __init__(self, index, x1, y1):
        x = math.floor(index / 5)
        y = index % 5
        #dx = 50
        #dy = 40
        self.point = [x1 - grid * x, y1 - (grid-10) * y]
        self.index = index
    
    # 方法
    def add(self):
        canvas.create_text(self.point, text="●", fill="green", font=("標楷體",34,"bold"))
        canvas.create_text(self.point, text=self.index, fill="white", font=("標楷體",16,"bold"))
    def delete(self):
        canvas.create_text(self.point, text="●", fill="#002240", font=("標楷體",35,"bold"))

class BossChess():
    def __init__(self, index, x2, y2):
        x = index % 5
        #dx = 50
        self.point = [x2 + grid * x, y2]
        self.index = index
    def add(self):
        canvas.create_text(self.point, text="●", fill="green", font=("標楷體",34,"bold"))
    def delete(self):
        canvas.create_text(self.point, text="●", fill="#002240", font=("標楷體",35,"bold"))
class UserChess(BossChess):
    def add(self):
        canvas.create_text(self.point, text="●", fill="white", font=("標楷體",34,"bold"))
        if self.index < 16: #黑棋
            canvas.create_text(self.point, text="○", fill="black", font=("標楷體",28,"bold"))
            canvas.create_text(self.point, text="將", fill="black", font=("標楷體",19,"bold"))
        else: #紅棋
            canvas.create_text(self.point, text="○", fill="red", font=("標楷體",28,"bold"))
            canvas.create_text(self.point, text="帥", fill="red", font=("標楷體",19,"bold"))

grid = w / 12#50
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
for i in range(24):
    OpenChess(i,x0,y0).add()
    CloseChess(i,x1,y1).add()
#OpenChess(23).delete()
#CloseChess(23).delete()
for i in range(5):
    BossChess(i,xb,yb).add()
for i in range(5):
    UserChess(i,xu,yu).add()
UserChess(1,xu,yu).delete()

win.mainloop()
