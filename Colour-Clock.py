# use Tkinter to show a digital clock

# tested with Python24 vegaseat 10sep2006


from tkinter import *
from datetime import datetime, time
from pytz import timezone
from ConfigParser import SafeConfigParser
parser = SafeConfigParser()
parser.read('settings.conf')
style = str(parser.get('settings', 'Font'))#Set
fsize = int(parser.get('settings', 'Size'))#Set
HourColour = str(parser.get('settings', 'Hour-Colour'))#Set
QuarterColour = str(parser.get('settings', 'Quarter-Colour'))#Set
HalfColour = str(parser.get('settings', 'Half-Colour'))#Set
ThreeQuaterColour = str(parser.get('settings', 'ThreeQuater-Colour'))#Set
textcolour = str(parser.get('settings', 'Text-Colour'))#Set
fheight = int(parser.get('settings', 'Frame-Height'))#Set
fwidth = int(parser.get('settings', 'Frame-Width'))#Set




root = Tk()

format=("%d/%m/%y  %H:%M:%S")
f=("%M")

now = datetime.now(timezone('Australia/Adelaide'))
time = str(now.strftime(format))
swap = str(now.strftime(f))

def ThreeQuater():
	now = datetime.now(timezone('Australia/Adelaide'))
	time = str(now.strftime(format))
	swap = str(now.strftime(f))
	clock.config(text=time, height=fheight, width=fwidth, bg=ThreeQuaterColour)
	clock.after(200, ThreeQuater)
	if swap == "00":
		clock.after(200,Hour)

def Half():
	now = datetime.now(timezone('Australia/Adelaide'))
	time = str(now.strftime(format))
	swap = str(now.strftime(f))
	clock.config(text=time, height=fheight, width=fwidth, bg=HalfColour)
	clock.after(200, Half)
	if swap == "45":
		clock.after(200,ThreeQuater)

def Quarter():
	now = datetime.now(timezone('Australia/Adelaide'))
	time = str(now.strftime(format))
	swap = str(now.strftime(f))

	clock.config(text=time, height=fheight, width=fwidth, bg=QuarterColour)
	clock.after(200, Quarter)
	if swap == "30":
		clock.after(200,Half)


def Hour():
	now = datetime.now(timezone('Australia/Adelaide'))
	time = str(now.strftime(format))
	swap = str(now.strftime(f))
	clock.config(text=time, height=fheight, width=fwidth,bg=HourColour)
	clock.after(200, Hour)
	if swap == "15":
		clock.after(200,Quarter)


print swap
if swap > "15" and swap < "30":
	clock = Label(root, font=(style, fsize, 'bold'))
	clock.pack(fill=BOTH, expand=0)
	Quarter()
elif swap > "30" and swap < "45":
	clock = Label(root, font=(style, fsize, 'bold'))
	clock.pack(fill=BOTH, expand=0)
	Half()
elif swap > "45"and swap < "59":
	clock = Label(root, font=(style, fsize, 'bold'))
	clock.pack(fill=BOTH, expand=0)
	ThreeQuarter()
elif swap > "00"and swap < "15":
	clock = Label(root, font=(style, fsize, 'bold'))
	clock.pack(fill=BOTH, expand=0)
	Hour()

root.mainloop( )

