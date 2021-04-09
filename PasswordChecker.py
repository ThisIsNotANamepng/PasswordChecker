
print ("The procedures for this tool is based on this paper by Microsoft,\n\n https://www.microsoft.com/en-us/research/wp-content/uploads/2016/06/Microsoft_Password_Guidance-1.pdf\n\n\nThis guidebook by the EFF, part of the Surveillence Self Defense project\nhttps://ssd.eff.org/en/module/creating-strong-passwords\n\n\nAnd this guidebook by the National Institute for Technology Standards (A US government agency\nhttps://www.nist.gov/video/password-guidance-nist-0\n\n")
print ("Requirments for passing this test, is \n 1. Must be at leats 8 characters long\n 2. Password is checked against a 10 million leaked passwords\n 3. Password must have 2 special characters (This rule is disregarded if the password is more than 15 characters long)")
print ("\n\nRemember, some rules that this tool cannot check is \n 1. Password rotation makes people ceate weaker passwords\n 2. Special Characters make people write donw passwords")

password = input("\nEnter you password here (Not your actual password): ")
print (" \n")
string1 = (password)
file1 = open("10millionpasswords.txt", "r")
print ("Your password is now being checked against a database of 10 million of the most commonly used passwords\n")
flag = 0
index = 0
stop = 0
total = 0
for line in file1:  
    index += 1 

    if string1 in line:  
      flag = 1
      break 
          
if flag == 0: 
  print ("Your password has not yet been leaked as a common password")
  print("Passed Check 1") 
if flag == 1:   
  print(string1, "Is already leaked as a commonly used password\n\n\n")
  stop = 1
file1.close() 


if stop == 0:
  print ("Beginning check 2\n")

for i in password:
    total = total + 1

if total < 8:
  stop = 1

print("Total Number of Characters in your password - ", total, "\n")
fla = 0

find = password.find("!")
if find >= 0:
  find = -1
  fla = fla + 1
  
find = password.find("?")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("b")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("@")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("#")
if find >= 0:
  find = -1
  fla = fla + 1
find = password.find("$")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("%")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("^")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("&")
if find >= 0:
  find = -1
  fla = fla + 1
  
find = password.find("*")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("(")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find(")")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("-")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("_")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("=")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("+")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("[")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find("]")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find(",")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find(".")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find(";")
if find >= 0:
  find = -1
  fla = fla + 1

find = password.find(":")
if find >= 0:
  find = -1
  fla = fla + 1

if total >= 16:
  if fla >= 3:
    print ("Your password has a sufficient amount of special characters\n")
    print (fla)
  if fla < 3:
    print ("Your password has less than 3 special characters, but since your password is", (total), "characters long, it's fine\n")

if total < 16:
  if fla >= 3:
    print ("Your password has a sufficient amount of special characters\n")
    print (fla)
  if fla < 3:
    print ("Your password has less than 3 special characters")
print ("Check 3 finished\n")

if stop == 1:
  print ("\n\n\n\n\n\nYour password has failed the test, do not use it")
if stop == 0:
  print ("Your password is probably sufficient for most uses")
print ("\n\n\n\n\n\n\n")




