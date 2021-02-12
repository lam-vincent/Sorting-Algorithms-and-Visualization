# Python program for implementation of Insertion Sort 
from tkinter import*
import tkinter as tk
import random
import time
import sys
from SelectionSort import *
from Bubble Sort import *
sys.setrecursionlimit(10000)

fen=tk.Tk()
fen.title ("Insertion Sort Visualization")
fen.geometry ("1500x1000")
Zone=Canvas(fen,width=1500,height=1000,bg="grey")
Zone.place(x=0,y=0)

def visualization(arr):
    for i in range(len(arr)):
        Zone.create_rectangle(i*200, i*200+200, 0 , arr[i]/13*800, width=5, outline="blue", fill="royalblue")
  
arr = [0]*100
createArray(arr)
random.shuffle(arr)
insertionSort(arr) 

