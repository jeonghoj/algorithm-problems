
sentence = " The Curious Case of Benjamin Button "
sentence_list = sentence.split(" ")
ab_count = 0
for word in sentence_list:
    if word == '':
        count = count+1
answer = len(sentence_list) - count
print(answer)