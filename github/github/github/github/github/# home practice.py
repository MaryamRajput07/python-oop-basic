# home practice concatenation
# --------------------------
str1='hello'
str2="world"
strings=str1+str2
print(strings)
# length function(length maloom karna)
# -------------------------
str='lahore' 
len1=len(str)
print(len1)
# indexicing(charecters ki postion excess karna )
# ------------------------
word='islamabad'
ch=word[1]
print(ch)
# slicing (matlb charcters ke beach mai se koi words lena )
# ------------------------
sen='apna karachi'
print(sen[0:3])
#*print(sen[5:len(sen)])asy bhe kar sakhty han*
# ------------------------
# oposite side(slicing)
# ------------------------
sen2="apple"
print(sen2[-5:-2])
# srtring function(endwith)
# ------------------------
intro="my name is maryam"
print(intro.endswith("yam"))
# (string.capitalize)first latter ko capital kerna mai help karta hai 
# ------------------------
print(intro.capitalize())
# (string.replace)purane word ko new se replace karta hai 
# ------------------------
print(intro.replace('my',"first"))
# (string.find)yeh words ko dhooondhne mai help karta hai
# ------------------------
print(intro.find('is'))
# (string.count)yeh aik word existance bata hai count kerke
print(intro.count("m"))
# ------------------------
# lets practice input your name and defind your length
practice=input('my name is:')
print('defind your name is:',len(practice))
# practice your count funtion
num='hi i am$ and$ used for$ currencey'
print(intro.count("$"))
# uses of if and else and elif
number=0
age=int(input('enter a number: '))
if age>number:
    print("positive")
elif age<number:
    print("negative")
else:
    print('zero')


num=2
check=int(input("enter a number: "))
if num!=check:
    print("odd number")
else :
    print("even number")






