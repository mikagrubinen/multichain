import os
import commands
import json
import globalVars
import binascii
from itertools import izip

# function add_new_user() will fill user_key with username and unique key for that usernamae
user_key = {'miro' : 'key1', 'mire' : "key2"}

# @param data - dictionary with mandatory keys 'username', 'email address', 'wallet'
def add_new_user(blockchain, stream_name, data):

	username = data['username']

	# open a file to read from
	f = open("user_key.txt", "r")

	# check if file is empty
	# is_file_empty = os.stat('user_key.txt').st_size == 0

	for line in f:
		(saved_username, saved_key) = line.split()
		if saved_username == username:
			print ("user already registered")
		else:
			print("user added")


	# check if usermane is already taken
	# returned_data = commands.liststreamkeys(blockchain, stream_name)

	# for item in returned_data:
	# 	if item['key'] == 

	# if returned_data == []:
	# 	return 'empty'
	# else:
	# 	key = "key" + str(1 + len(user_key))
	# 	user_key = {}
	# 	user_key[username] = key 
	# 	commands.publish(blockchain, stream_name, key, data)
	# 	commands.publish(blockchain, globalVars.user_key_stream, key, user_key)

	# 	for item in returned_data:
	# 		print(type(item))
	# 		print(item["key"])







	# if username in user_key:
	# 	print("Error: Username \"{}\" already exists!".format(username))
	# else:
	# 	# if username is available, create unique key for new user, add it to user_key dict
	# 	# and publish all user's data to stream
	# 	key = "key" + str(1 + len(user_key))
	# 	user_key[username] = key 
	# 	commands.publish(blockchain, stream_name, key, data)
	
# retrieve user key from 'user_key' based on username (used after login)
def get_user_key(username):
	content = commands.return_hex()
	output = content.decode('hex')
	output = output.split()
	i = iter(output)
	user_key = dict(izip(i, i))

	if username in user_key:
		print(user_key[username]) 

# After fetch from stream, return a value from received dict based on key in dict. 
# @param fetched_data - dict retrieved after fetch_data is called
# @param param - 'username', 'wallet', 'balance', 'email' and so on
def get_value(fetched_data, param):
	for key, value in fetched_data.iteritems():
		for sk, sv in value.iteritems():
			if sk == param:
				return sv

# This function opens a .txt file, read its content and converts it to hex
def make_hex():
	with open(globalVars.filename, 'rb') as f:
		content = f.read()
	return binascii.hexlify(content)







	
	

	
			