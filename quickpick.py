"""
File: quickpick.py
Author: Daniel D'Angelo

About: This is a program that will generate 5 random numbers between 1 and 50 for a lottery "Quick Pick" game.

***GAMBLING PROBLEM? 24-Hour Confidential HopeLine, Call: 516-555-1212. (Not a results line)***
"""

import tkinter as tk
import random

class QuickPick:
   def __init__(self, master):
       """Sets up the window and widget"""
       self.frame = tk.Frame(master)
       self.text = tk.StringVar()
       self.ranNumLabel = tk.Label(self.frame, textvariable = self.text, font = "bold")
       self.ranNumLabel.grid(row = 1, ipadx = 10, ipady = 10)
       self.genButton = tk.Button(self.frame, text = "Click here for your 5 lucky numbers!", command = self.genLuckyNum, bg = "cyan", font = "bold")
       self.genButton.grid(row = 0, ipadx = 2, ipady = 6)
       self.frame.pack()

   def genLuckyNum(self):
       """Number bank from 1-50 to be randomized"""
       self.text.set(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],  5))

def main():
   """Instantiate and pop up the window"""    
   root = tk.Tk(className = "~Quick Pick Number Generator~")
   app = QuickPick(root)
   root.mainloop()

main()