from fnmatch import translate
from random import shuffle

msg = ''
with open('../Secret/msg.txt') as file:
    msg = file.read().upper()

ALPHABET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SUB_ALPHABET = list(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
shuffle(SUB_ALPHABET)

translate_dict = {}
for u, v in zip(ALPHABET, SUB_ALPHABET):
    translate_dict[u] = v
    
with open('msg_enc.txt', 'w+') as file:
    file.write(msg.translate(translate_dict))

