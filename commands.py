import subprocess
import json
import do

def subscribe(blockchain_name, stream_name):
	msg = "multichain-cli " + blockchain_name + " subscribe " + stream_name
	subprocess.call(msg, shell=True)

def liststreams(blockchain_name):
	msg = "multichain-cli " + blockchain_name + " liststreams"
	result = subprocess.check_output(msg, shell=True)
	return json.loads(result) 

def createstream(blockchain_name, stream_name):
	streams = liststreams(blockchain_name)
	flag = False

	for x in streams:
		if x['name'] == stream_name:
			flag = True
			break

	if flag == True:
		print("Error: Stream with name \"{}\" already exists!".format(stream_name))
	elif flag == False:
		msg = "multichain-cli " + blockchain_name + " create stream " + stream_name + " false"
		subprocess.call(msg, shell=True)

def liststreamitems(blockchain_name, stream_name):
	subscribe(blockchain_name, stream_name)
	msg = "multichain-cli " + blockchain_name + " liststreamitems " + stream_name
	subprocess.call(msg, shell=True)

# publish json data to stream
def publish(blockchain_name, stream_name, key, data=""):
	msg = "multichain-cli " + blockchain_name + " publish " + stream_name + " " + key + " \'{\"json\":" + json.dumps(data) + "}\'"
	subprocess.call(msg, shell=True)

# fetch last updated data related to specified key and return as dict
def fetch(blockchain_name, stream_name, username):
	key = do.get_user_key(username)
	msg = "multichain-cli " + blockchain_name + " getstreamkeysummary " + stream_name + " " + key + " jsonobjectmerge,ignoreother"
	result = subprocess.check_output(msg, shell = True)
	return json.loads(result)