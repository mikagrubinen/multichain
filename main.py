# import subprocess
# import json

import commands
import do

blockchain = 'cmpe'
stream_name = 'stream1'
user_key = {}

# this will be generated by chaitras code
data = {'key':'key1 ', 'username':'miro', 'wallet':'14td6', 'email':'miro@miro.com'}

# commands.liststreams(blockchain)
# commands.createstream(blockchain, stream_name)
# commands.subscribe(blockchain, stream_name)
# commands.liststreamitems(blockchain, stream_name)

do.add_new_user(user_key, data)
do.add_new_user(user_key, data)