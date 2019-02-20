words = {}
new_words =""
for i in range(0,255):
    words[chr(i)] = i

print(words)

input_word = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for ii in input_word:
    if ii == " ":
        new_words = new_words + " "
        continue
    else:
        new_num = words[ii] + 2
        new_words = new_words + chr(new_num)

print(new_words)
