def main():
    file=open("JaneEyre.txt",'r')
    text=file.read()
    index=0
    numTypo=0
    while index<=len(text):
##      Find those SINGLE 'amd's, that is, excluding those contained in other words.
        if text[index:index+3]=='amd' and not text[index-1].isalpha() and not text[index+3].isalpha():
##          Change that 'amd' into 'and'
            text=text[:index+1]+'n'+text[index+2:]
            numTypo+=1
            index+=2  # jump "md"
        index+=1
    file.close()
    print('There are %d tyops of "amd" in the file JaneEyre.txt.'%numTypo)
    file=open("JaneEyrenew.txt",'w')
    file.write(text)
    file.close()

main()
