# ---------------------------------------
# Name: Abdinoor Moallin
# Program: Password_Evaluator.py
# ---------------------------------------
# Purpose: Creating a password analyzer using different functions 
# ---------------------------------------
def get_password():
#Gets password from the user and error checks so that its >= 10 characters
   pswrd = input("Enter a password (min 10 characters): ")
   while (len(pswrd) < 10):
      print("-> Too short! Try again: ", pswrd) 
      pswrd = input("Enter a password (min 10 characters): ")
   return pswrd
   
def check_flaws(pswrd):
   #displays the total amount of flaws the password contains, & tells the flaws
   possible_flaws = 4
   digit_count = 0
   upper_count = 0
   lower_count = 0
   special_count = 0 
   for letter in pswrd: 
      
      if letter.isdigit():
         digit_count = 1
      
      if letter.isupper():
         upper_count = 1
      
      if letter.islower():
         lower_count = 1 
      
      if letter.isalnum() == False:
         special_count = 1  
   
   flaws = possible_flaws - (digit_count + upper_count + lower_count + special_count)
   print("Flaw check: \t", pswrd, "has", flaws, "flaw(s)" ) 

   if digit_count == 0:
      print("->No digits ")
   
   if upper_count == 0:
      print("->No uppercase chars ")
   
   if lower_count == 0:
      print("->No lowercase chars ")
   
   if special_count == 0:
      print("->No special chars ")
   
def show_stats(pswrd):
   #displays the strings first letter, shows the length, fifth character, and last two characters.
   pswrd_length = len(pswrd)
   star_string = "*" * len(pswrd)
   if (pswrd_length > 9) or (pswrd_length > 10):
      pswrd_length = star_string
   print("\nStatistics for: ", pswrd[0]+ star_string)
   print("(a) Length: \t\t", len(pswrd), "characters")
   print("(b) Fifth char:\t\t", pswrd[4])
   print("(c) Last two chars:\t", pswrd[-2]+pswrd[-1],"\n")

def hash_swap(pswrd):
#generates a hash for the password and swaps the first 2 values with the next two chars
   pswrd_hash = str(hash(pswrd))
   swapped_hash = pswrd_hash.replace(pswrd_hash[0:1],pswrd_hash[2:3])
   print("(d) Hash generated:\t", pswrd_hash)
   print("(e) Two pairs swapped:\t", swapped_hash)

def examine_password():
#Calls the 4 helper functions created
   password = get_password()
   check_flaws(password)
   show_stats(password)
   hash_swap(password)
examine_password()
