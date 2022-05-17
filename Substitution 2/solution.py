from random import shuffle

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = len(ALPHABET)

offset = 1
enc = 'MOTRVZLGEYDQCWBHDHDLYJZDQDESRKSAGGUYMNLYDWOFGTFDGOZMGAQKZMFEGTFESLWBYWRYRMESHFETMMZUJQDVYIJLHFSMNQLJIKCREGTODKGGBUHFESGQOYHFQSUZXBRDYFRDJKOTQOZUMSRMRFDSAUSUYGMZMFBEFAXHDGUNRBMFIDIKETGGTUJMAYEFBMIVQUEYMAZJYHRKIMSEJKDMYKKJQHNCRDKMGUYMKYLOTQORMKOHFJMYLGROFGRFSDTAMNQLQKRDOCHDUESLWBYWRREQQFXKSOZMAZPIBEYIJJKFBANKZTPAQDVZSOTOYUZKNURZFBTGUTOQLYLDQDQMRGUTJKJMGQPHIDNQHODKMKZMMZMBERMJTXLHWUYPJIMVFOOSPUDYLDJJRREEQFXMMSUZMAZHIBEYKJJKFUZVZYEBESRFKFDTLJZVAMQBRRGSKHFJAUDKTMRNMTDTFGJMAZPIBEKMTRVTFMKZMMRMBFDGYPHAYKZLWCFBSCSFQVSWZMZIESYHTDAGMFQ_JVYYRB_QFX_PKKEYKVSQJREHA_HD_JZGBMR_FBFG_HG'
msg = ''

sbox_rev = []
for i in range(0,len(enc),5):
    for j in range(5):
        letter = enc[i+j]
        if letter == "_":
            sbox_rev.append(letter)
            continue
        temp = ALPHABET.index(letter)
        
        if temp - offset < 0:
            temp += n
            
        sbox_rev.append(temp-offset)
    offset = (offset*3+4 )%n
    
print(sbox_rev)
sbox_string = ''
for i in sbox_rev:
    if i =="_":
        sbox_string+="_"
    else:
        sbox_string += ALPHABET[i]
print(sbox_string)

#LNSQUSEZSEESWAMGCGCKRCSWEESWAMRZUYKRFGERESWAMSECFNSFZSELSWAMFSEDREPUSESSWAMRGEDSFFSNCRSWAMIKGERFGJECJSWAMFSNCJZKOSEGSWAMNXGEPLNSQUSSWAMCIJNSJHSNFTSWAMCRZYKNRZSENSWAMZQUYKNGKUEGSWAMDSFFSNCFTEFSWAMUPTDXFTOSEISWAMRDIJCFRDDCRSWAMCJLFTRFDREPSWAMLJNGECFREZSSWAMERCSZFGJEJLSWAMGCTDREPUSESSWAMEWJRNSFTSEJSWAMIIJEATKOSEQSWAMYRNSNRNSDGVSWAMSFTSNJEREWRSWAMFTSIJCFZSEISWAMGNCJLDSFFSNSWAMISWKGPNRICJSWAMNROTCREWSESSWAMEWLLRNSFTEISWAMJIIJENSOSRFSWAMEJECSECSOTNSWAMFRJGECTOSEUSWAMSCSEFCFTSEJSWAMSQUSEFDSFFSSWAMFXOGZRDSEPDSWAMREPURPSFSBFSWAMCZUYKJ_CORZSWAMEW_OJDXOSETSWAMGZUYK_CSZENSWAMEF_GF
#hcmusctf no spaces and polyalphabetic is secure isnt it
#https://www.boxentriq.com/code-breaking/cryptogram
