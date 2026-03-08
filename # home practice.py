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
# ----------------------------------------

import numpy as np

data = [10, 20, 30, 40, 50]
result = np.mean(data)

print("Mean:", result)


# -------------------------------------------

import numpy as np

data = [10, 50, 20, 40, 30]
result = np.median(data)

print("Median:", result)


# -----------------------------------

import statistics

data = [10, 20, 20, 30, 40]
result = statistics.mode(data)

print("Mode:", result)

# --------------------------------

import numpy as np

# 1D Array (Ek seedhi line)
a1 = np.array([1, 2, 3])

# 2D Array (Table ki tarah: 2 Rows, 3 Columns)
a2 = np.array([[1, 2, 3], 
               [4, 5, 6]])

# 3D Array (Do 2D tables ka set)
a3 = np.array([[[1, 2], [3, 4]], 
               [[5, 6], [7, 8]]])

print("--- 1D ---")
print(a1)

print("\n--- 2D ---")
print(a2)

print("\n--- 3D ---")
print(a3)

# try and except error ("agar program mai koi error aye ga tu except chalye ga our our program crash hone se bach jaye ga ")

try:
    # 1. Woh kaam jo hum karna chahte hain
    number1 = int(input("Pehla number: "))
    number2 = int(input("Doosra number: "))
    
    result = number1 / number2
    print(f"Answer hai: {result}")

except ZeroDivisionError:
    # 2. Agar user ne 0 se divide karne ki koshish ki
    print("Ghalti: Aap zero (0) se divide nahi kar sakte!")

except ValueError:
    # 3. Agar user ne number ki jagah 'abc' likh diya
    print("Ghalti: Sirf numbers likhein, words nahi!")

except Exception as e:
    # 4. Koi bhi aur anjan ghalti
    print(f"Kuch ajeeb masla hua: {e}")

print("Program khatam! (Code crash nahi hua)")


# to do list in python 
tasks = []

while True:
    print("\n--- MERA TO-DO LIST ---")
    print("1. Task Add Karein")
    print("2. Saare Tasks Dekhein")
    print("3. Task Delete Karein")
    print("4. Exit")
    
    choice = input("\nOption select karein: ")
    
    if choice == '1':
        item = input("Naya task: ")
        tasks.append(item)
    elif choice == '2':
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == '3':
        val = int(input("Kaunsa number delete karna hai? "))
        tasks.pop(val - 1)
    elif choice == '4':
        print("Bye Bye!")
        break





