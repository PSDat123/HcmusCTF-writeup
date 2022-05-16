from random import shuffle

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = len(ALPHABET)
sbox = [i for i in range(n)]
shuffle(sbox)

def transform(msg, offset):
    msg = ALPHABET.index(msg)
    return (sbox[msg] + offset) % n

msg = ''
with open('../Secret/msg.txt') as file:
    msg = file.read().upper()

special_symbols = "`~!@#$%&*()-=+[]\\;',./{}|:\"<>? "
for ch in special_symbols:
    msg = msg.replace(ch, '')

msg_enc = ''
offset = 1
for i in range(0, len(msg), 5):
    for j in range(5):
        print(j)
        # Sorry the code looks so ugly, but you know what it does :))
        if msg[i+j] == '_':
            msg_enc += '_'
        else:
            msg_enc += ALPHABET[transform(msg[i+j], offset)]
    offset = (offset * 3 + 4) % n
    
with open('msg_enc.txt', 'w+') as file:
    file.write(msg_enc)
