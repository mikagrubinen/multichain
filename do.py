import os
import commands
import json
import globalVars
import binascii
from itertools import izip
import ast


# @param data - dictionary with mandatory keys 'username', 'email address', 'wallet'
def add_new_user(blockchain, stream_name, data):

	username = data['username']

	if "nouser" == get_user_key(username):
		user_key = return_dict()
		key = "key" + str(len(user_key))
		user_key[username] = key
		commands.publish(blockchain, stream_name, key, data)
		# make hex from dictionary
		new_hex = binascii.hexlify(str(user_key))
		commands.publish_hex(new_hex)
		return "new user registered"
	else:
		return "User already registered"

	# open a file to read from
	# f = open("user_key.txt", "r")

	# check if file is empty
	# is_file_empty = os.stat('user_key.txt').st_size == 0

	# for line in f:
	# 	(saved_username, saved_key) = line.split()
	# 	if saved_username == username:
	# 		print ("user already registered")
	# 	else:
	# 		print("user added")


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
	
# retrieve user key from 'user_key' stream, based on username (used after login)
def get_user_key(username):
	user_key = return_dict()
	if username in user_key:
		return user_key[username]
	else:
		return "nouser"

# After fetch from stream, return a value from received dict based on key in dict. 
# @param fetched_data - dict retrieved after fetch_data is called
# @param param - 'username', 'wallet', 'balance', 'email' and so on
def get_value(fetched_data, param):
	for key, value in fetched_data.iteritems():
		for sk, sv in value.iteritems():
			if sk == param:
				return sv

# This function converts dict it to hex and publish to user-key stream
def make_hex():
	content = {"user" : "key0"}
	hex_value = binascii.hexlify(str(content))
	commands.publish_hex(hex_value)

# this function returns dictionary made from hax value retrieved from a user-key stream
def return_dict():
	content = commands.return_hex()
	output = content.decode('hex')
	# converts string to dict and returns it
	return ast.literal_eval(output)

	# output = output.split()
	# i = iter(output)
	# return dict(izip(i, i))





	
	

	
			