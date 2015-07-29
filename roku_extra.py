import numpy
from subprocess import call
import time

KEY_LOC = {'a':(0,0),'b':(1,0),'c':(2,0),'d':(3,0),'e':(4,0),'f':(5,0),'g':(6,0),'1':(7,0),'2':(8,0),'3':(9,0),
'h':(0,1),'i':(1,1),'j':(2,1),'k':(3,1),'l':(4,1),'m':(5,1),'n':(6,1),'4':(7,1),'5':(8,1),'6':(9,1),' ':(10,1),
'o':(0,2),'p':(1,2),'q':(2,2),'r':(3,2),'s':(4,2),'t':(5,2),'u':(6,2),'7':(7,2),'8':(8,2),'9':(9,2),
'v':(0,3),'w':(1,3),'x':(2,3),'y':(3,3),'z':(4,3),'-':(5,3),'_':(6,3),'@':(7,3),'.':(8,3),'0':(9,3)}

	  
ONE_SHIFT = (-1,0)
SHIFT = (-2,0)
DELAY = 0.2

def test_init(device):
	codes = ['KEY_HOME','SLEEP_2','KEY_RIGHT','KEY_RIGHT','KEY_OK','SLEEP_4','KEY_DOWN','KEY_OK','KEY_OK']
	for c in codes:
		if c.startswith('SLEEP'):
			sleeptime = int(c.split('_')[1])
			time.sleep(sleeptime)
			continue

		send_once(c,device)

def email_input(name, device):
	caps = False
	current_loc = (0,0)

	for x in name:
		next_loc = KEY_LOC[x]	
		path = numpy.subtract(next_loc, current_loc)		
		print "CURRENT PATH to {} : {}".format(x,path)
		issue_command(path, device)		
		current_loc = next_loc

	print "yo"	

#def enable_caps_lock():
	
def issue_command(tuple, device):

	if tuple[0] < 0:
		for i in range(0,-tuple[0]):
			send_once('KEY_LEFT', device)
	else:
		for i in range(0,tuple[0]):
			send_once('KEY_RIGHT', device)

	if tuple[1] < 0:
		for i in range(0,-tuple[1]):
			send_once('KEY_UP', device)
	else:
		for i in range(0,tuple[1]):
			send_once('KEY_DOWN', device)

	send_once('KEY_OK', device)

def send_once(command, device):
	call(['irsend','SEND_ONCE',device,command])
	time.sleep(DELAY)

		
##test_init('roku')
email_input('hello world','roku')
