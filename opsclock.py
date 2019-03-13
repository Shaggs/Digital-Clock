# A small program for learning TK

# Imports
from tkinter import *
from datetime import datetime, time
from pytz import timezone
#from ConfigParser import SafeConfigParser
# Load in settings
# Start TK
root = Tk()
clock = Label(root, font=("aerial", 30, 'bold'), bg="green")
clock.pack(fill=BOTH, expand=0)
format=("%d/%m/%y  %H:%M:%S")
Minute=("%M")
# Define main program
def main():
	now = datetime.now(timezone('Australia/Adelaide'))
	time = str(now.strftime(format))
	swap = str(now.strftime(Minute))
	clock.config(text=time, height=2, width=120)
	clock.after(200, main)
	if swap == "30":
		clock.config(bg="orange", foreground="black")
	if swap == "45":
		clock.config(bg="cyan", foreground="black")
	if swap == "00":
		clock.config(bg="green", foreground="black")
	if swap == "15":
		clock.config(bg="red", foreground="black")
# Run Main Program
if __name__=="__main__":
	main()
	root.mainloop()
