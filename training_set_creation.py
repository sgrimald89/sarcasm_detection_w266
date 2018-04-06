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

for line in sys.stdin:
        if r > 0:
                row = line.strip().split(",")
                length_row = len(row)
                if length_row <5:
                    continue
                if row[length_row - 1] == "False":
                    not_sarcastic_text.append(clean_text(row[4]))
                elif row[length_row - 1] == "True":
                    if verify_sarcastic(row[4]):
                        sarcastic_text.append(clean_text(row[4]))
        r+=1

non_sarcastic_examples = choice(not_sarcastic_text, len(sarcastic_text), False)

for non_sarcastic_tweet in non_sarcastic_examples:
    print(non_sarcastic_tweet+"|"+str(0))
   # pass
for sarcastic_tweet in sarcastic_text:
    print(sarcastic_tweet + "|"+str(1))
   # pass
