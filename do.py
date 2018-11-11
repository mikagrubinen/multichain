import commands
import json

# function add_new_user() will fill user_key with username and unique key for that usernamae
user_key = {'miro' : 'key1', 'mire' : "key2"}

# @param data - dictionary with mandatory keys 'username', 'email address', 'wallet'
def add_new_user(blockchain, stream_name, data):

	username = data['username']
	# check if usermane is already taken
	if username in user_key:
		print("Error: Username \"{}\" already exists!".format(username))
	else:
		# if username is available, create unique key for new user, add it to user_key dict
		# and publish all user's data to stream
		key = "key" + str(1 + len(user_key))
		user_key[username] = key 
		commands.publish(blockchain, stream_name, key, data)
	
# retrieve user key from 'user_key' based on username (used after login)
def get_user_key(username):
	if username in user_key:
		return user_key[username]

# After fetch from stream, return a value from received dict based on key in dict. 
# @param fetched_data - dict retrieved after fetch_data is called
# @param param - 'username', 'wallet', 'balance', 'email' and so on
def get_value(fetched_data, param):
	for key, value in fetched_data.iteritems():
		for sk, sv in value.iteritems():
			if sk == param:
				return sv




	
	

	
			