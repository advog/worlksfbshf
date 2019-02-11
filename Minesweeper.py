import tkinter as tk
import random
import time

mines = 200
flags = 0
frameWidth = 200
frameHeight = 200
open = frameHeight*frameWidth-mines
reved = 0

mloc = []

values = [[0] * frameHeight for _ in range(frameWidth)]
labels = [[None] * frameHeight for _ in range(frameWidth)]
floc = [[False] * frameHeight for _ in range(frameWidth)]
revealed = [[False] * frameHeight for _ in range(frameWidth)]

root = tk.Tk()


class bob():
    import time

    def __init__(self):
        return

    def bo(self):
        print(time.time())
        for i in range(10):
            for n in range(10):
                for k in range(10):
                    i*n*k
        print(time.time())

def setMines():
    global mloc
    global balues

    mloc = random.sample(range(frameWidth*frameHeight), mines)
    for i in mloc:
        values[int(i % frameWidth)][int(i / frameWidth)] = -1

def setVals():
    global frameWidth
    global values
    global frameHeight

    for i in mloc:
        y = int(i / frameWidth)
        x = int(i % frameWidth)

        if x+1 != frameWidth and values[x + 1][y] != -1:
            values[x+1][y] += 1
        if x-1 != -1 and values[x-1][y] != -1:
            values[x-1][y] += 1
        if y+1 != frameHeight and values[x][y + 1] != -1:
            values[x][y+1] += 1
        if y-1 != -1 and values[x][y-1] != -1:
            values[x][y-1] += 1

        if x+1 != frameWidth and y+1 != frameHeight and values[x + 1][y + 1] != -1:
            values[x+1][y+1] += 1
        if x-1 != -1 and y+1 != frameHeight and values[x - 1][y + 1] != -1:
            values[x-1][y+1] += 1
        if x+1 != frameWidth and y-1 != -1 and values[x + 1][y - 1] != -1:
            values[x+1][y-1] += 1
        if x-1 != -1 and y-1 != -1 and values[x-1][y-1] != -1:
            values[x-1][y-1] += 1

def setLabels():
    global frameWidth
    global frameHeight
    global values

    for x in range(frameWidth):
        for y in range(frameHeight):
            labels[x][y] = tk.Button(root, text = "", height=1, width=2, relief="groove", bg = 'white')
            labels[x][y].grid(row = y, column = x)
            labels[x][y].bind('<Button-1>', lambda event, id = y*frameWidth+x: onClickR(event, id))
            labels[x][y].bind('<Button-3>', lambda event, id=y * frameWidth + x: onClickL(event, id))

def onClickR(event, i):
    global values
    global revealed
    global labels
    global floc
    global reved

    global t
    t.bo()

    y = int(i / frameWidth)
    x = int(i % frameWidth)

    if floc[x][y] or revealed[x][y]:
        return
    elif values[x][y] == -1:
        reveal()
    else:
        revealed[x][y] = True
        reved += 1
        if values[x][y] == 0:
            labels[x][y].config(bg = 'grey')
            if x + 1 != frameWidth:
                recur(x+1, y)
            if x - 1 != -1:
                recur(x-1,y)
            if y + 1 != frameHeight:
                recur(x,y+1)
            if x - 1 != -1:
                recur(x,y-1)
            if x + 1 != frameWidth and y + 1 != frameHeight:
                recur(x+1,y+1)
            if x - 1 != -1 and y + 1 != frameHeight:
                recur(x - 1, y + 1)
            if x + 1 != frameWidth and y - 1 != -1:
                recur(x + 1, y - 1)
            if x - 1 != -1 and y - 1 != -1:
                recur(x - 1, y - 1)
        else:
            labels[x][y].config(text = values[x][y])

    checkWin()
    #debug()

def recur(x,y):
    global revealed
    global values
    global labels
    global reved

    if revealed[x][y] or floc[x][y]:
        return
    elif values[x][y] == 0:
        revealed[x][y] = True
        labels[x][y].config(bg = 'grey')
        reved+=1
        if x + 1 != frameWidth:
            recur(x + 1, y)
        if x - 1 != -1:
            recur(x - 1, y)
        if y + 1 != frameHeight:
            recur(x, y + 1)
        if y - 1 != -1:
            recur(x, y - 1)
        if x + 1 != frameWidth and y + 1 != frameHeight:
            recur(x + 1, y + 1)
        if x - 1 != -1 and y + 1 != frameHeight:
            recur(x - 1, y + 1)
        if x + 1 != frameWidth and y - 1 != -1:
            recur(x + 1, y - 1)
        if x - 1 != -1 and y - 1 != -1:
            recur(x - 1, y - 1)
    else:
        labels[x][y].config(text = values[x][y])
        revealed[x][y] = True
        reved+=1


def onClickL(event, i):
    global values
    global floc
    global flags
    y = int(i / frameWidth)
    x = int(i % frameWidth)

    floc[x][y] = not floc[x][y]
    if floc[x][y]:
        labels[x][y].config(bg='red')
        flags += 1
    else:
        labels[x][y].config(bg = 'white')
        flags -= 1

    checkWin()

def reveal():
    global frameWidth
    global frameHeight
    global labels

    print("run")

    for x in range(frameWidth):
        for y in range(frameHeight):
            labels[x][y].config(text=values[x][y])

def checkWin():
    global mloc
    global mines
    global flags
    global revealed
    global open

    if flags == mines:
        miss = False
        for i in mloc:
            y = int(i / frameWidth)
            x = int(i % frameWidth)
            if not floc[x][y]:
                miss = True
                break

        if not miss:
            reveal()

    elif reved == open:
        reveal()


t = bob()

setMines()
setVals()
setLabels()

tk.mainloop()

