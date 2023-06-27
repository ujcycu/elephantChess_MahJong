# import
import tkinter as tk
import math

# 描繪視窗
win = tk.Tk()
win.geometry("600x400")

# Canvas
canvas = tk.Canvas(win, width = 600, height = 400, bg = "#002240")
canvas.place(x = 0, y = 0)

x0 = 50
y0 = 100
fontAttr = ["標楷體",16,"bold"]
"""
canvas.create_text(x, y, text="●", fill="white", font=("標楷體",34,"bold"))
canvas.create_text(x, y, text="○", fill="black", font=("標楷體",28,"bold"))
canvas.create_text(x, y, text="將", fill="black", font=("標楷體",19,"bold"))
"""
# 類別
class OpenChess:
    # 建構子
    def __init__(self, index):
        self.index = index
        x = self.index % 6
        y = math.floor(self.index / 6)
        dx = 50
        dy = 50
        self.point = [x0 + dx * x, y0 + dy * y]
    
    # 方法
    def add(self):
        #print(self.point)
        #canvas.create_text(self.point[0]+2, self.point[1]+2, text="●", fill="#00172b", font=("標楷體",34,"bold"))
        canvas.create_text(self.point, text="●", fill="white", font=("標楷體",34,"bold"))
        if self.index < 16: #黑棋
            canvas.create_text(self.point, text="○", fill="black", font=("標楷體",28,"bold"))
            canvas.create_text(self.point, text="將", fill="black", font=("標楷體",19,"bold"))
        else: #紅棋
            canvas.create_text(self.point, text="○", fill="red", font=("標楷體",28,"bold"))
            canvas.create_text(self.point, text="帥", fill="red", font=("標楷體",19,"bold"))
    def delete(self):
        canvas.create_text(self.point, text="●", fill="#002240", font=("標楷體",35,"bold"))

class ClosrChess:
    # 建構子
    def __init__(self, index):
        self.index = index
        x = math.floor(self.index / 5)
        y = self.index % 5
        dx = 50
        dy = 40
        self.point = [x1 - dx * x, y1 - dy * y]
    
    # 方法
    def add(self):
        canvas.create_text(self.point, text="●", fill="green", font=("標楷體",34,"bold"))
        canvas.create_text(self.point, text=self.index, fill="white", font=("標楷體",20,"bold"))
    def delete(self):
        canvas.create_text(self.point, text="●", fill="#002240", font=("標楷體",35,"bold"))


x1 =(x0 + 50 * 6) + 50 * 4 + 10
y1 = y0 + 50 * 3
for i in range(24):
    OpenChess(i).add()
    ClosrChess(i).add()
OpenChess(23).delete()
ClosrChess(23).delete()

"""
canvas.create_rectangle(x1-25, y1-20, x1+25, y1+20, fill="red")
canvas.create_text(x1, y1, text="●", fill="white", font=("標楷體",34,"bold"))
def addClose(x1,y1):
    point = [x1-20, y1, x1+20, y1+20]
    point2 = [x1-20, y1-5, x1+20, y1+10]
    point3 = [x1-20, y1-10, x1+20, y1+10]
    point4 = [x1-20, y1-15, x1+20, y1+5]
    canvas.create_oval(point, fill="white")
    canvas.create_rectangle(point2, fill="white", width=0)
    canvas.create_oval(point3, fill="green")
    canvas.create_oval(point4, fill="green")
    canvas.create_line(x1-20, y1-5, x1-20, y1+10, fill="black")
    canvas.create_line(x1+20, y1-5, x1+20, y1+10, fill="black")
addClose(x1,y1)
addClose(x1,y1-15)
"""

win.mainloop()
