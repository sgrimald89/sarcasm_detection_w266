import numpy as np
#import pandas as pd
#import ast
import json

import re
def clean_text(text):
	text = re.sub(r"(\||\'|\"|\n|)","", text)
	return text

filename = "fetched_tweets_copy.txt"
file = open(filename, "r")
headers = ['id',
'user',
'full_text_ext',
'hashtags_ext',
'in_reply_to_screen_name',
'in_reply_to_user_id',
'in_reply_to_status_id',
'lang',
'place',
'geo',
'sarcastic']

delimiter = '|'

write_to_file = 'training_data_non_sarcastic.txt'

#with open(write_to_file,'a') as tf:
#    tf.write(','.join(headers)+'\n')

outfile = open(write_to_file,'a')
outfile.write(delimiter.join(headers)+'\n')
n = 0
for line in file:
    n+=1
    tweet = json.loads(line)
    
    if n%10000==0:
        print(n)
    if 'extended_tweet' in tweet.keys():
        tweet_text = clean_text(tweet['extended_tweet']['full_text'])
        hashtags = str(tweet['extended_tweet']['entities']['hashtags'])
    elif 'text' in tweet.keys():           
        tweet_text = clean_text(tweet['text'])
        hashtags = '' 
    else:
        continue

    out_line = delimiter.join([str(tweet['id']),                         
                         tweet['user']['screen_name'],
                         tweet_text,
                         hashtags,
                         str(tweet['in_reply_to_screen_name']),
                         str(tweet['in_reply_to_user_id_str']),
                         str(tweet['in_reply_to_status_id_str']),
                         tweet['lang'],
                         str(tweet['place']),
                         str(tweet['geo']),
                         "0"])
    outfile.write(out_line.encode('utf-8')+'\n')


outfile.close()





