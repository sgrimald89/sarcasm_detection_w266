import sys
import re
from numpy.random import choice
from random import randint
import numpy as np

def clean_text(text):
    text = re.sub(r"(\||\'|\"|\n|#sarcasm|#sarcastic)"," ", text,flags=re.IGNORECASE)
    return text

def verify_sarcastic(text):
    sarcastic = re.search(r"(#sarcasm|#sarcastic)",text,flags=re.IGNORECASE)
    return bool(sarcastic)

r = 0
sarcastic_text = []
not_sarcastic_text = []

sarcastic_count = 0
non_sarcastic_count = 0
print("id|text|in_reply_to_screen_name|in_reply_to_user_id|in_reply_to_status_id|sarcastic")
for line in sys.stdin:
        if r > 0:
                row = line.strip().split("|")
                if row[7] != "en":
                    continue
                length_row = len(row)
                if row[length_row - 1] == "0":
                    non_sarcastic_count += 1
                    row_to_add = [str(row[0]), clean_text(row[2]), row[4], row[5], row[6],"0"]
                    not_sarcastic_text.append(row_to_add)
             
                elif row[length_row - 1] == "1":
                    if verify_sarcastic(row[2]):
                        sarcastic_count+=1
                        row_to_add = [str(row[0]),clean_text(row[2]), row[4], row[5], row[6],"1"]
                        sarcastic_text.append(row_to_add)
        r+=1

sampled_rows = choice(len(not_sarcastic_text), len(sarcastic_text), False)
for non_sarcastic_tweet in np.array(not_sarcastic_text)[sampled_rows]:
    print("|".join(non_sarcastic_tweet))

for sarcastic_tweet in sarcastic_text:
    print("|".join(sarcastic_tweet))
