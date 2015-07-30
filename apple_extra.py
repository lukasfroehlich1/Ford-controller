import numpy
from subprocess import call
import time

KEY_LOC = {'a':(0,0),'b':(1,0),'c':(2,0),'d':(3,0),'e':(4,0),'f':(5,0),
'g':(0,1),'h':(1,1),'i':(2,1),'j':(3,1),'k':(4,1),'l':(5,1),
'm':(0,2),'n':(1,2),'o':(2,2),'p':(3,2),'q':(4,2),'r':(5,2),
's':(0,3),'t':(1,3),'u':(2,3),'v':(3,3),'w':(4,3),'x':(5,3),
'y':(0,4),'z':(1,4),'1':(2,4),'2':(3,4),'3':(4,4),'4':(5,4),
'5':(0,5),'6':(1,5),'7':(2,5),'8':(3,5),'9':(4,5),'0':(5,5),
'.':(0,6),'_':(1,6),'@':(2,6),'.com':(3,6),'.net':(4,6),'.edu':(5,6)
}
	  
DELAY = 0

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
		if x.isupper() and not caps:
			print "change to lower"
			call(['irsend','SEND_ONCE',device,'KEY_PLAY'])
			caps = True
		elif x.islower() and caps:
			print "changing to upper"
			next_loc = (0,-1) 	
			path = numpy.subtract(next_loc, current_loc)		
			issue_command(path, device)		
			send_once('KEY_LEFT',device)
			send_once('KEY_DOWN',device)	
			current_loc = (0,0)
			caps = False
		if x.isupper():
			x = x.lower()
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
email_input('plustest3','apple')
for i in range(0,7):
	send_once('KEY_RIGHT','apple')	
send_once('KEY_OK','apple')
time.sleep(1)
email_input('123456','apple')
for i in range(0,7):
	send_once('KEY_RIGHT','apple')	
send_once('KEY_OK','apple')
time.sleep(3)
for i in range(0,6):
	send_once('KEY_RIGHT','apple')	
send_once('KEY_OK','apple')
time.sleep(1)
email_input('seinfeld','apple')
time.sleep(5)
for i in range(0,7):
	send_once('KEY_RIGHT','apple')	
send_once('KEY_OK','apple')

send_once('KEY_OK','apple')
send_once('KEY_OK','apple')
