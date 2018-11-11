
# @param data - dictionary with mandatory keys 
# 'username', 'email address', 'wallet'
def add_new_user(user_key, data):

	username = data['username']
	key = "key" + str(1 + len(user_key))

	user_key[username] = key 
	print(user_key)
	