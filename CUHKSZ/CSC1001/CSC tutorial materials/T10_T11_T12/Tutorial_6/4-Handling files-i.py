def main():
    filename=input("Enter a filename:")
    file=open(filename,'r')
##    Number of characters
    numOfCh=len(file.read())
    file.close()
    file=open(filename,'r')
##    Number of words
    numOfWord=0
##    Number of lines
    for line in file.readlines():
        numOfWord+=len(line.split())
    file.close()
    file=open(filename,'r')
    numOfLine=len(file.readlines())
    file.close()
    print("In the file %s, there are"%filename)
    print(numOfCh,"characters,")
    print(numOfWord,"words,")
    print(numOfLine,"lines.")

main()
