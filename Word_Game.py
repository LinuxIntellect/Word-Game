import pandas as pd
import string, random

#============ Word List Gen ============
minimum=int(input('Please enter the minimum length of any give word to be generated: '))
maximum=int(input('Please enter the maximum length of any give word to be generated: '))
wmaximum=int(input('Please enter the max number of words to be generate in the dictionary: '))
 
alphabet = string.ascii_letters[0:]
string=''
FILE = open("word_list.txt","w")
for count in range(0,wmaximum):
  for x in random.sample(alphabet,random.randint(minimum,maximum)):
      string+=x
  FILE.write(string.upper()+'\n')
  string=''
FILE.close()
print('DONE!')

print("Welcome to password Gusser 2000 Pro!")
print()
print("Choose [e]asy, [m]edium, [h]ard:\n")
print()
chs = input("Enter Your Desire Choose, Please.")
if chs =='e':
    f = open("word_list.txt", "r")
    print("The password is one of these words:\n")
    correct_pass = []
    word_list = []
    for s, i in enumerate(f):
        print("{})".format(s),i)
        word_list.append(i.rstrip("\n"))
        if s == 3:
            correct_pass.append(str(i))
            
    for j in range(0, 10):
        guess = int(input("Guess (Enter (0-9)): "))
        if guess != 3:
            chance = 4
            print("\nGuesses Remaining: {}".format(chance-j))
            count = []
            for c in str(correct_pass[0]):
                match_word = 0
                for k in word_list[guess]:
                    if c == k:
                        match_word+=1
                        count.append(match_word)
                        
            print("\nGuesses Password : {}".format(word_list[guess]))            
            print("Password Is Incorrect. Please Try Again.")
            print("{}/6 Correct word.".format(sum(count)))
            print()
            print("The password is one of these words:\n")
            f = open("word_list.txt", "r")
            for s, i in enumerate(f):
                print("{})".format(s),i)
            a = chance - j
            if a == 0:
                break
        
        if guess == 3:
            print("\n\n")
            print("Correct Password : {}".format(str(correct_pass[0])))
            print("Password is Correct.\nCongratulations, You win!")
            break
            

if chs =='m':
    f = open("word_list.txt", "r")
    print("The3 password is one of these words:\n")
    correct_pass = []
    word_list = []
    for s, i in enumerate(f):
        print("{})".format(s),i)
        word_list.append(i.rstrip("\n"))
        if s == 5:
            correct_pass.append(str(i))
            
    for j in range(0, 10):
        guess = int(input("Guess (Enter (0-9)): "))
        if guess != 5:
            chance = 4
            print("\nGuesses Remaining: {}".format(chance-j))
            count = []
            for c in str(correct_pass[0]):
                match_word = 0
                for k in word_list[guess]:
                    if c == k:
                        match_word+=1
                        count.append(match_word)
                        
            print("\nGuesses Password : {}".format(word_list[guess]))            
            print("Password Is Incorrect. Please Try Again.")
            print("{}/6 Correct word.".format(sum(count)))
            print()
            print("The password is one of these words:\n")
            f = open("word_list.txt", "r")
            for s, i in enumerate(f):
                print("{})".format(s),i)
            a = chance - j
            if a == 0:
                break
        
        if guess == 5:
            print("\n\n")
            print("Correct Password : {}".format(str(correct_pass[0])))
            print("Password is Correct.\nCongratulations, You win!")
            break
            

if chs =='h':
    f = open("word_list.txt", "r")
    print("The3 password is one of these words:\n")
    correct_pass = []
    word_list = []
    for s, i in enumerate(f):
        print("{})".format(s),i)
        word_list.append(i.rstrip("\n"))
        if s == 7:
            correct_pass.append(str(i))
            
    for j in range(0, 10):
        guess = int(input("Guess (Enter (0-9)): "))
        if guess != 7:
            chance = 4
            print("\nGuesses Remaining: {}".format(chance-j))
            count = []
            for c in str(correct_pass[0]):
                match_word = 0
                for k in word_list[guess]:
                    if c == k:
                        match_word+=1
                        count.append(match_word)
                        
            print("\nGuesses Password : {}".format(word_list[guess]))            
            print("Password Is Incorrect. Please Try Again.")
            print("{}/6 Correct word.".format(sum(count)))
            del count
            print()
            print("The password is one of these words:\n")
            f = open("word_list.txt", "r")
            for s, i in enumerate(f):
                print("{})".format(s),i)
            a = chance - j
            if a == 0:
                break
        
        if guess == 7:
            print("\n\n")
            print("Correct Password : {}".format(str(correct_pass[0])))
            print("Password is Correct.\nCongratulations, You win!")
            break
            