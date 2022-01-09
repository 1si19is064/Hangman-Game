import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

#Selecting a Random Word From Hangman_words File
random_word1=(random.choice(word_list))
random_word=list(random_word1)

#Printing Logo Of Hangman
print(logo)

#creating a list and appending underscores of length of a word
word_length=len(random_word)
blank_list=[]

for i in range(word_length):
  blank_list.append('_')

lives=6
while(lives!=0):
  #Asking using to enter the letter and converting it into lower case
  user_input=input("Predict the letter in the word  =  ").lower()

  #Checking if that element is in the choosen word_length
  if(user_input in random_word):

    #checking that the user already entered this letter or not(If yes then the user has to enter the letter again)

    while(user_input in blank_list):
      print("Your letter is already in word")
      user_input=input("Again Predict the letter   =  ").lower()
    else:
      print("Your Letter is in the word")

    #Checking how many user predicted letter are there in the word and filling all blank spaces with that letter 
    
    for i in range(word_length):
      if(user_input==random_word[i]):
        blank_list[i]=user_input
    #Printing the blank list after modification
    print(*blank_list)
    #Printing the stages of hangman
    print(stages[lives])
  else:
    print("You Have Entered the letter that is not in word")
    lives=lives-1
    #printing the remaining Lives
    print("Left lives="+str(lives))
    print(stages[lives])
  #Checking whether the blank spaces are their in random_word or not
  if('_' not in blank_list):
    print("You Won!")
    break
if(lives==0):
  print("You Lost")
  print("Better Luck Next Time")
  print("Word is  ="+str(random_word1))



        
