from tkinter import*
import tkinter as tk
import random
import time
import sys
sys.setrecursionlimit(10000)

fen=tk.Tk()
fen.title ("Insertion Sort Visualization")
fen.geometry ("1500x1000")
width, height = 1000, 1000
Zone=Canvas(fen,width=width,height=height,bg="grey")
Zone.place(x=0,y=0)

def visualization(array):
    Zone.create_rectangle(0, 0, width, height, fill="grey")
    for i in range(len(array)):
        MAX = max(array)
        Zone.create_rectangle(width/len(array)*i, (MAX-array[i])*(height/MAX), width/len(array)*(i+1), height, width=5, outline="blue", fill="royalblue")

arr = list(range(1, 101))
shuffled_array = random.sample(arr, len(arr))
visualization(arr)
time.sleep(1)
visualization(shuffled_array)

fen.mainloop()
