# Python program for implementation of Sorting Algorithms Visualization
from tkinter import*
import tkinter as tk
import random
import time
import sys
sys.setrecursionlimit(10000)

fen=tk.Tk()
fen.title ("Insertion Sort Visualization")
fen.geometry ("1920x1030")
width, height = 1920, 1030
Zone=Canvas(fen,width=width,height=height,bg="grey")
Zone.place(x=0,y=0)

#PARTIE 1
def SelectionSort(A):
    for i in range(len(A)): 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
        A[i], A[min_idx] = A[min_idx], A[i] 
        visualization(A)

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
        visualization(arr)

def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key
        visualization(arr)

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
    for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    visualization(arr)
    return ( i+1 ) 

def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        visualization(arr)

def countingSort(arr, exp1): 
    n = len(arr) 
    output = [0] * (n) 
    count = [0] * (10) 
    for i in range(0, n): 
        index = (arr[i] / exp1) 
        count[int(index % 10)] += 1
    for i in range(1, 10): 
        count[i] += count[i - 1] 
    i = n - 1
    while i >= 0: 
        index = (arr[i] / exp1) 
        output[count[int(index % 10)] - 1] = arr[i] 
        count[int(index % 10)] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)): 
        arr[i] = output[i] 

def radixSort(arr): 
    max1 = max(arr) 
    exp = 1
    while max1 / exp > 0: 
        countingSort(arr, exp) 
        exp *= 10
        visualization(arr)

#PARTIE 2
def printArray(array):
    Zone.create_rectangle(0, 0, width, height, fill="grey")
    for i in range(len(array)):
        MAX = max(array)
        Zone.create_rectangle((width-200)/len(array)*i+100, (MAX-array[i])*((height-200)/MAX)+100, (width-200)/len(array)*(i+1)+100, height-100, width=5, outline="blue", fill="royalblue")
        time.sleep(1/len(arr))
        Zone.update()

def visualization(array):
    Zone.create_rectangle(0, 0, width, height, fill="grey")
    for i in range(len(array)):
        MAX = max(array)
        Zone.create_rectangle((width-200)/len(array)*i+100, (MAX-array[i])*((height-200)/MAX)+100, (width-200)/len(array)*(i+1)+100, height-100, width=5, outline="blue", fill="royalblue")
    Zone.update()

def reset(arr, shuffled_array):
    printArray(arr)
    printArray(shuffled_array)

#___MAIN___:
arr = list(range(1, 31))

message = tk.Label(fen,text="Algorithme 1/6 - SelectionSort !",fg = "light green",bg = "dark green",font = "Helvetica 16 bold italic")
message.place(x= 800,y=50)
message.after(5000, message.destroy)
shuffled_array = random.sample(arr, len(arr))
reset(arr, shuffled_array)
SelectionSort(shuffled_array)

message = tk.Label(fen,text="Algorithme 2/6 - bubbleSort !",fg = "light green",bg = "dark green",font = "Helvetica 16 bold italic")
message.place(x= 800,y=50)
message.after(10000, message.destroy)
shuffled_array = random.sample(arr, len(arr))
reset(arr, shuffled_array)
bubbleSort(shuffled_array)

message = tk.Label(fen,text="Algorithme 3/6 - insertionSort !",fg = "light green",bg = "dark green",font = "Helvetica 16 bold italic")
message.place(x= 800,y=50)
message.after(15000, message.destroy)
shuffled_array = random.sample(arr, len(arr))
reset(arr, shuffled_array)
insertionSort(shuffled_array)

message = tk.Label(fen,text="Algorithme 4/6 - quickSort !",fg = "light green",bg = "dark green",font = "Helvetica 16 bold italic")
message.place(x= 800,y=50)
message.after(15000, message.destroy)
shuffled_array = random.sample(arr, len(arr))
reset(arr, shuffled_array)
quickSort(shuffled_array, 0, len(shuffled_array)-1)

message = tk.Label(fen,text="Algorithme 5/6 - heapSort !",fg = "light green",bg = "dark green",font = "Helvetica 16 bold italic")
message.place(x= 800,y=50)
message.after(10000, message.destroy)
shuffled_array = random.sample(arr, len(arr))
reset(arr, shuffled_array)
heapSort(shuffled_array)

message = tk.Label(fen,text="Algorithme 6/6 - radixSort !",fg = "light green",bg = "dark green",font = "Helvetica 16 bold italic")
message.place(x= 800,y=50)
message.after(10000, message.destroy)
shuffled_array = random.sample(arr, len(arr))
reset(arr, shuffled_array)
radixSort(shuffled_array)

fen.mainloop()

