import sys
import re
from numpy.random import choice
from random import randint

def clean_text(text):
    text = re.sub(r"(\||\'|\"|\n|#sarcasm|#sarcastic)","", text,flags=re.IGNORECASE)
    return text

def verify_sarcastic(text):
    sarcastic = re.search(r"(#sarcasm|#sarcastic)",text,flags=re.IGNORECASE)
    return bool(sarcastic)

r = 0
sarcastic_text = []
not_sarcastic_text = []
sarcastic_count = 0
non_sarcastic_count = 0
for line in sys.stdin:
      
        if r > 0:
                row = line.strip().split("|")
                length_row = len(row)
                if row[length_row - 1] == "0":
                    non_sarcastic_count += 1
                    not_sarcastic_text.append(clean_text(row[2]))
                elif row[length_row - 1] == "1":
                    if verify_sarcastic(row[2]):
                        sarcastic_count+=1
                        sarcastic_text.append(clean_text(row[2]))
        r+=1
print(sarcastic_count)
non_sarcastic_examples = choice(not_sarcastic_text, len(sarcastic_text), False)
for non_sarcastic_tweet in non_sarcastic_examples:
    print(non_sarcastic_tweet+"|"+str(0))
   # pass
for sarcastic_tweet in sarcastic_text:
    print(sarcastic_tweet + "|"+str(1))
   # pass
