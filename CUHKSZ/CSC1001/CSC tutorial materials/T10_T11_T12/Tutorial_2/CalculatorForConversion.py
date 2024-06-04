b=16     #base=2,8 or 16
#The symbols
a7=0
a6=0
a5=0
a4=0
a3=0
a2=0
a1=6
a0=2
a_1=12
a_2=15
a_3=4
a_4=1
a_5=15
a_6=2
#The decomposition of the number, below "\" means the code line after that is to continue the expression not being cut
#Interger part and Fractional part
decimal=a7*b**7+a6*b**6+a5*b**5+a4*b**4+a3*b**3+a2*b**2+a1*b+a0+\
         a_1*b**(-1)+a_2*b**(-2)+a_3*b**(-3)+a_4*b**(-4)+a_5*b**(-5) +a_6*b**(-6)  
print(decimal)
