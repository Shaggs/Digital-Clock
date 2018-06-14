# Custom Clock by S.Rees 2018

# Imports
from tkinter import *
from datetime import datetime, time
from pytz import timezone
from ConfigParser import SafeConfigParser
# Call in Settings
parser = SafeConfigParser()
parser.read('settings.conf')
style = str(parser.get('settings', 'Font'))
fsize = int(parser.get('settings', 'Size'))
bgcolour = str(parser.get('settings', 'Background-Colour'))
textcolour = str(parser.get('settings', 'Text-Colour'))
fheight = int(parser.get('settings', 'Frame-Height'))
fwidth = int(parser.get('settings', 'Frame-Width'))

#Launch TK Root
root = Tk()
clock = Label(root, font=(style, fsize, 'bold'), bg=bgcolour)
clock.pack(fill=BOTH, expand=0)
format=("%d/%m/%y  %H:%M:%S")
def tick():
	now = datetime.now(timezone('Australia/Adelaide'))
	now = str(now.strftime(format)
	clock.config(text=now, height=fheight, width=fwidth)
	clock.after(200, tick)
tick()
root.mainloop( )
