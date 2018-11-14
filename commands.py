import subprocess
import json
import do
import globalVars

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

# Fetchs keys from stream
def liststreamkeys(blockchain_name, user_key_stream):
	msg = "multichain-cli " + blockchain_name + " liststreamkeys " + user_key_stream
	result = subprocess.check_output(msg, shell = True)
	return json.loads(result)

# this function publishes hex to the stream with key0
def publish_hex(hex_value):
	msg = "multichain-cli " + globalVars.blockchain + " publish " + globalVars.stream_hex + " key0 " + hex_value
	subprocess.call(msg, shell=True)

# this function returns last data in hex format, from user_key stream
def return_hex():
	msg = "multichain-cli " + globalVars.blockchain + " liststreamitems " + globalVars.stream_hex + " false 1"
	result = subprocess.check_output(msg, shell = True)
	result = json.loads(result)
	return result[0]["data"]
	# for item in result:
	# print(item["data"])

