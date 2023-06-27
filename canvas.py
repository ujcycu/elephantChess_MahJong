# import
import tkinter as tk

# 描繪視窗
win = tk.Tk()
win.geometry("600x400")

# Canvas
canvas = tk.Canvas(win, width = 600, height = 400, bg = "#002240")
canvas.place(x = 0, y = 0)

x = 300
y = 200

#canvas.create_oval(x-50, y-50, x+50, y+50, fill="white", width=4, outline="#f00")
#canvas.create_oval(x-15, y-15, x+15, y+15, fill="white", width=3, outline="#f00")
#canvas.create_text(x, y, text="象", fill="#f00", font=("標楷體",18,"bold"))

a = 200
b = 200

circle = [
    a-20, b,
    a, b-20,
    a+20, b,
    a, b+20,
    a-20, b
    ]

#canvas.create_oval(a-20, b-20, a+20, b+20, smooth=True, fill="white", width=4, outline="#f00")

#canvas.create_text(a, b, text="○", fill="red", font=("標楷體",28,"bold"))
#canvas.create_text(a, b, text="相", fill="#f00", font=("標楷體",16,"bold"))

fontAttr = ["標楷體",16,"bold"]

canvas.create_text(a+150, b, text="●", fill="white", font=("標楷體",34,"bold"))
canvas.create_text(a+150, b, text="●", fill="black", font=("標楷體",29,"bold"))
canvas.create_text(a+150, b, text="●", fill="white", font=("標楷體",25,"bold"))
canvas.create_text(a+150, b, text="將", fill="black", font=("標楷體",19,"bold"))

canvas.create_text(a, b, text="●", fill="white", font=("標楷體",30,"bold"))
canvas.create_text(a, b, text="●", fill="black", font=("標楷體",26,"bold"))
canvas.create_text(a, b, text="●", fill="white", font=("標楷體",22,"bold"))
canvas.create_text(a, b, text="將", fill="black", font=("標楷體",18,"bold"))

canvas.create_text(a+50, b, text="●", fill="white", font=("標楷體",32,"bold"))
canvas.create_text(a+50, b, text="○", fill="black", font=("標楷體",28,"bold"))
canvas.create_text(a+50, b, text="將", fill="black", font=("標楷體",20,"bold"))

canvas.create_text(a+100, b, text="●", fill="white", font=("標楷體",34,"bold"))
canvas.create_text(a+100, b, text="○", fill="black", font=("標楷體",28,"bold"))
canvas.create_text(a+100, b, text="將", fill="black", font=("標楷體",19,"bold"))

x1 = 420
y1 = 200
#canvas.create_arc(x1-20, y1, x1, y1+20, start=0, extent=360, width=3, fill='white')

#canvas.create_oval(x1-50, y1-50, x1+50, y1+50, fill="white")
#canvas.create_arc(x1-50, y1-50, x1+50, y1+50, extent=359.5, width=4, outline="red", style='arc')
#canvas.create_text(x1, y1, text="象", fill="#f00", font=("標楷體",18,"bold"))
#canvas.create_arc(110, 10, 200, 100, start=60, extent=180)
#canvas.create_arc(210, 10, 300, 100, start=60, extent=70, width=8, fill='#f00')
#canvas.create_arc(10, 110, 100, 200, start=60, extent=180, width=8, fill='#f00', outline='#00f')
#canvas.create_arc(110, 110, 200, 200, start=-60, extent=-120, width=3, fill='#fff', outline='#0a0', dash=(5,5))
#canvas.create_arc(210, 110, 300, 200, start=-60, extent=-90, width=3, fill='#ff0', outline='#f50', dash=(5,10), style='arc')


#label = tk.Label(win, text="象", font=("標楷體",12), fg="#f00")
#label.place(100,200)

win.mainloop()
