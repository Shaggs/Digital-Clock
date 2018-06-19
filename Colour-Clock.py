# A small program for learning TK

# Imports
from tkinter import *
from datetime import datetime, time
from pytz import timezone
from ConfigParser import SafeConfigParser
# Load in settings
parser = SafeConfigParser()
parser.read('settings.conf')
style = str(parser.get('settings', 'Font'))#Set
fsize = int(parser.get('settings', 'Size'))#Set
HourColour = str(parser.get('settings', 'BG-Hour-Colour'))#Set
QuarterColour = str(parser.get('settings', 'BG-Quarter-Colour'))#Set
HalfColour = str(parser.get('settings', 'BG-Half-Colour'))#Set
ThreeQuaterColour = str(parser.get('settings', 'BG-ThreeQuater-Colour'))#Set
FGHour  = str(parser.get('settings', 'Text-Hour-Colour'))#Set
FGQuater  = str(parser.get('settings', 'Text-Quater-Colour'))#Set
FGHalf  = str(parser.get('settings', 'Text-Half-Colour'))#Set
GFThreeQuater  = str(parser.get('settings', 'Text-ThreeQuater-Colour'))#Set
textcolour = str(parser.get('settings', 'Text-Colour'))#Set
fheight = int(parser.get('settings', 'Frame-Height'))#Set
fwidth = int(parser.get('settings', 'Frame-Width'))#Set
# Start TK
root = Tk()
clock = Label(root, font=(style, fsize, 'bold'), bg="green")
clock.pack(fill=BOTH, expand=0)
format=("%d/%m/%y  %H:%M:%S")
Minute=("%M")
# Define main program
def main():
	now = datetime.now(timezone('Australia/Adelaide'))
	time = str(now.strftime(format))
	swap = str(now.strftime(Minute))
	clock.config(text=time, height=fheight, width=fwidth)
	clock.after(200, main)
	if swap == "30":
		clock.config(bg=HalfColour, foreground=FGHalf)
	if swap == "45":
		clock.config(bg=ThreeQuaterColour, foreground=FGThreeQuater)
	if swap == "00":
		clock.config(bg=HourColour, foreground=FGHour)
	if swap == "15":
		clock.config(bg=QuarterColour, foreground=FGQuater)
# Run Main Program
if __name__=="__main__":
	main()
	root.mainloop()
