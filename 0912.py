# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:42:53 2020

@author: User
"""

import tkinter as tk
import tkinter.messagebox

def clickMe():
    tkinter.messagebox.showinfo(title="提示",message="好痛")
window = tk.Tk()
window.title("我的第一個GUI程式",bg="#000",fg="#0ff")
window.geometry('300x300')

label = tk.Label(window,text="我的GUI")
label.pack()

entry=tk.Entry(window,width=20)
entry.pack()

button=tk.Button(window,text="按鈕",command = clickMe)
button.pack()


window.mainloop()