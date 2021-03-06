from flask import Flask, request, Response

from subprocess import call
import time
import json
import os
import shutil


app = Flask(__name__)

seconds = 0
@app.route('/', methods=['POST'])
def handle_task():
	print "started"
	res = {"status": 200, "result": "DONE"}
	fail = {"status": 200, "result": "ERROR"}
	device = request.form['device']
	jobid = request.form['job_id']
	codes = request.form['code'].split(';')
	print 'code : {}'.format(codes)
	#filename = device +'.conf'
	#copy_rename(filename,'lircd.conf')
	for c in codes:
		if c.startswith('SLEEP'):
			sleeptime = int(c.split('_')[1])
			time.sleep(sleeptime)
			continue
		print c
		try:
			call(['irsend', 'SEND_ONCE', device, c])
			time.sleep(seconds)
		except:
			return Response(json.dumps(fail), mimetype='application/json', status=str(fail["status"]))

	try:
		print "Starting photo sequence"
		filename = 'static/image/'+jobid+'.jpg'
		cmd = 'raspistill -n -o ' + filename
		call(cmd, shell=True)
		print "Finished photo sequence"
	except:
		return Response(json.dumps(fail), mimetype='application/json', status=str(fail["status"]))

	return Response(json.dumps(res), mimetype='application/json', status=str(res["status"]))

def handle_task_test():
	print 'here'
	res = {"status": 200, "detail": "Done"}
	fail = {"status": 404, "detail": "File Not Found."}
	device = 'roku'
	codes = ['KEY_HOME','KEY_RIGHT','KEY_RIGHT','KEY_OK','SLEEP_3','KEY_DOWN','KEY_DOWN','KEY_OK']
	filename = device +'.conf'
	copy_rename(filename,'lircd.conf')

	for c in codes:
		if c.startswith('SLEEP'):
			sleeptime = int(c.split('_')[1])
			time.sleep(sleeptime)
			continue
		print c
		call(['irsend', 'SEND_ONCE', device, c])
		time.sleep(seconds)
	return json.dumps(res)

def copy_rename(old_file_name, new_file_name):
	src_dir= os.path.join(os.curdir , "config")
	print src_dir
	dst_dir= os.path.join('/etc/lirc')
	dst_file = os.path.join(dst_dir, old_file_name)
	new_dst_file_name = os.path.join(dst_dir, new_file_name)
	try:
		os.remove(os.path.join(dst_dir,new_dst_file_name))
	except:	
		print "can not find"
		pass
	src_file = os.path.join(src_dir, old_file_name)
	shutil.copy(src_file,dst_dir)
	os.rename(dst_file, new_dst_file_name)


@app.route('/health_check', methods=['GET'])
def test():
	return Response('OK', content_type='text/plain')


if __name__ == '__main__':
	app.run('0.0.0.0', debug = True)
	#handle_task_test()
