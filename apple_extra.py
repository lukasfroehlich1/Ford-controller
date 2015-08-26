import numpy

#APPLE KEYBOARD SUPPORT

KEY_LOC = {'a':(0,0),'b':(1,0),'c':(2,0),'d':(3,0),'e':(4,0),'f':(5,0),
'g':(0,1),'h':(1,1),'i':(2,1),'j':(3,1),'k':(4,1),'l':(5,1),
'm':(0,2),'n':(1,2),'o':(2,2),'p':(3,2),'q':(4,2),'r':(5,2),
's':(0,3),'t':(1,3),'u':(2,3),'v':(3,3),'w':(4,3),'x':(5,3),
'y':(0,4),'z':(1,4),'1':(2,4),'2':(3,4),'3':(4,4),'4':(5,4),
'5':(0,5),'6':(1,5),'7':(2,5),'8':(3,5),'9':(4,5),'0':(5,5),
'.':(0,6),'_':(1,6),'@':(2,6),'.com':(3,6),'.net':(4,6),'.edu':(5,6)
}

#delay is not a feature. code needs to be chagned to become a feature
DELAY = 0

def email_input(name):
    output = []
	caps = False
	current_loc = (0,0)

	for x in name:
		if x.isupper() and not caps:
            send_once('KEY_PLAY')
			caps = True
		elif x.islower() and caps:
			next_loc = (0,-1) 	
			path = numpy.subtract(next_loc, current_loc)		
			issue_command(path)		
			send_once('KEY_LEFT')
			send_once('KEY_DOWN')	
			current_loc = (0,0)
			caps = False
		if x.isupper():
			x = x.lower()
		next_loc = KEY_LOC[x]	
		path = numpy.subtract(next_loc, current_loc)		
		issue_command(path, device)		
		current_loc = next_loc

    return output

#def enable_caps_lock():
	
def issue_command(tuple):

	if tuple[0] < 0:
		for i in range(0,-tuple[0]):
			send_once('KEY_LEFT')
	else:
		for i in range(0,tuple[0]):
			send_once('KEY_RIGHT')

	if tuple[1] < 0:
		for i in range(0,-tuple[1]):
			send_once('KEY_UP')
	else:
		for i in range(0,tuple[1]):
			send_once('KEY_DOWN')

	send_once('KEY_OK')

def send_once(command):
    output.append(command)
