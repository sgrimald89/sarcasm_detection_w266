import sys
import re
from numpy.random import choice
from random import randint
import numpy as np

def clean_text(text):
    #remove delimiters, newlines, quotes, and sarcasm hashtags
    text = re.sub(r"(\||\'|\"|\n|#sarcasm|#sarcastic)","", text,flags=re.IGNORECASE)
    # removes the word sarcas and sarcastic
    text = re.sub(r"(sarcasm|sarcastic)","", text,flags=re.IGNORECASE)
    text = re.sub(r"##", "#",  text,flags=re.IGNORECASE)
    text = re.sub(r"  ", " ",  text,flags=re.IGNORECASE)
    return text

def verify_sarcastic(text):
    sarcastic = re.search(r"(sarcasm|sarcastic)",text,flags=re.IGNORECASE)
    return bool(sarcastic)

r = 0
sarcastic_text = []
sarcastic_messages = []

not_sarcastic_text = []
not_sarcastic_messages = []

sarcastic_count = 0
non_sarcastic_count = 0
print("id|text|in_reply_to_screen_name|in_reply_to_user_id|in_reply_to_status_id|sarcastic")
for line in sys.stdin:
        if r > 0:
                row = line.strip().split("|")
                # only want english text
                if row[7] != "en":
                    continue
                length_row = len(row)
                if row[length_row - 1] == "0":
                    message = clean_text(row[2])
                    row_to_add = [str(row[0]), message, row[4], row[5], row[6],"0"]
                    # deduplicate!
                    if message not in not_sarcastic_messages:
                        sarcastic_messages.append(message)
                        non_sarcastic_count += 1
                        not_sarcastic_text.append(row_to_add)
                elif row[length_row - 1] == "1":
                    message = clean_text(row[2])
                    row_to_add = [str(row[0]), message, row[4], row[5], row[6],"1"]
                    if verify_sarcastic(row[2]) and message not in sarcastic_messages :
                        sarcastic_messages.append(message)
                        sarcastic_count+=1
                        sarcastic_text.append(row_to_add)
        r+=1
print(len(sarcastic_text))
print(len(not_sarcastic_text))
sampled_rows = choice(len(not_sarcastic_text), len(sarcastic_text), False)
for non_sarcastic_tweet in np.array(not_sarcastic_text)[sampled_rows]:
    print("|".join(non_sarcastic_tweet))

for sarcastic_tweet in sarcastic_text:
    print("|".join(sarcastic_tweet))
