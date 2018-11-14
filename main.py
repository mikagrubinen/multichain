# import subprocess
import json

import commands
import do

blockchain = 'cmpe'
stream_name = 'stream99'

u1 = {"miro" : "key1"}
u2 = {"mire" : "key2"}
u3 = {"miri" : "key3"}

# this will be generated by chaitras code
data = {'username':'miri', 'wallet':'14td6', 'email':'miro@miro.com'}
data1 = {'balance' : 65}
username = 'miro'

##########################################################################################
# working with files

# user_key = open("user_key.txt", "a")
# user_key.write(bytes(str(u1) + '\n'))
# user_key.close()

# user_key = open("user_key.txt", "a")
# user_key.write(bytes(str(u2) + '\n'))
# user_key.close()

# user_key = open("user_key.txt", "r")


# for line in user_key:
# 	line1 = str(line)
# 	line1 = json.loads(line1)
# 	print(line1)

##########################################################################################
# commands.liststreams(blockchain)
# commands.createstream(blockchain, stream_name)
# commands.subscribe(blockchain, stream_name)
# commands.liststreamitems(blockchain, stream_name)
# commands.publish(blockchain, stream_name, key, data)

# need to work on this
# do.add_new_user(blockchain, stream_name, data)

# to retrieve unique key based on username (after login)
do.get_user_key(username)

# to see publish history made with key "liststreamkeyitems stream5 key1"
# to see only last updated fields "getstreamkeysummary stream5 key1 jsonobjectmerge,ignoreother"

# fetch data for username from a stream
# fetched_data = commands.fetch(blockchain, stream_name, username)
# print(type(fetched_data))

# prints one of parameters (eg. email) with help of key 'json'. First need to fetch_data
# param = 'email'
# value = do.get_value(fetched_data, param)

#list stream keys
# commands.liststreamkeys(blockchain, user_key_stream)

# this can be done only once at the beggining to publish first hex to a stream
# hex_value = do.make_hex()
# commands.publish_hex(hex_value)

# returns hex value from user_key stream
# commands.return_hex()

# Why do we need private blockchain? 
# Keep track of everything because public networks are not safe
# and they can be attacked by hackers to steal data and assets