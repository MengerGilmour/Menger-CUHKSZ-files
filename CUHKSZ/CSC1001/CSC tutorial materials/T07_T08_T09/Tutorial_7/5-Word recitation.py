import random

file=open("Dictionary.txt",'r')
words={}
for line in file.readlines():
    word=line.split(':')
    words[word[1].strip()]=word[0].strip()
k=list(words.keys())
total=len(k)
##Use "count" to count the correct guesses
count=0
##Notice that bool([])->False
while k:
    i=random.randint(0,len(k)-1)
##  Print how many words you have guessed
    print('(%d/%d)'%(total-len(k)+1,total),k[i])
    answer=input('Please guess the word:')
    if answer==words[k[i]]:
        print("√√√\nYour answer is correct!\n")
        count+=1
    else:
        print("×××\nThe correct answer should be \"%s\".\n"%words[k[i]])
##  Romove the word that you have just guessed
    k.remove(k[i])
print('Finished!You have correctly guess %d out of %d words!'%(count,total))

file.close()
