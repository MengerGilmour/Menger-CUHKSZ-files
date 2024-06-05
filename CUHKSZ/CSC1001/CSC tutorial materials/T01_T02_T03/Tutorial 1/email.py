#Given a file "idlist.txt" with student id numbers of many students,
#add "@link.cuhk.edu.cn" after them to get a list of email addresses
#in a file "emailist.txt", output the number of students on the shell.

position=0    #position of the element in a string
email=""      #the string of an email address
list=[]       #the list of all email addresses
while email!="@link.cuhk.edu.cn":
    with open('idlist.txt','rt') as f:
        studentid=f.read()[position:(position+9)]
        email=studentid+"@link.cuhk.edu.cn"
        list.append(email)
        position+=10
with open('emaillist.txt','wt') as f:
    amount=0      #the number of students
    email=list[amount]
    while email!="@link.cuhk.edu.cn":
        f.write(email)
        f.write('\n')
        amount+=1
        email=list[amount]
