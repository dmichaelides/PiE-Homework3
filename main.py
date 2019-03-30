"""
'Python-is-Easy' Homework #3 (If Statements)
DESCRIPTION: 
The main goal of this file created, is to get acquianted with If Statements in Python.  It is the third homework assigment in the
'Python is Easy' course, from Pirple.

This assignment includes a basic example of an automated trading program.  The variables "Open, High, Low and Close" defines a candlestick for a given trading instrument.
The If statement sets rules on when to BUY or SELL the instrument. 
"""

Open = 10
High = 12
Low = 9
Close = "11" # Added as string for the extra credit.  Function in the If statement converts string to integer. KACHING! Extra credit please, thanks :) 
Order = "unknown"

if Open <= int(Close) and High - Low > 3:
	Order = "BUY"
else: Order = "SELL"

print(Order)