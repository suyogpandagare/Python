# 1st example of while loop
secret_no = 7
guess_no = int(input("Enter your number:"))

while(guess_no != secret_no):
    guess_no = int(input("Not Correct, guess again:"))
else:
    print("Congratulations! you guessed it right")

# 2nd good example for while loop
i = 5
while True:
    if i % 0o11 == 0:
        break
    print(i)
    i += 1

# output is 5, 6, 7, 8 as octal of 11 is 9 when 9%9== 0 condition meets loop breaks

# 3rd example
i = 1
while True:
    if i % 0o7 == 0:    # octal of 7 is 7 as it is less than 8
        break
    print(i)
    i += 1

# for loop

for i in range(1, 10):
    if(i < 5):
        i+=1
        print(i)
    else:
        continue

# ex 1
x = 'abcd'
for num in range(5, 11):
  print(num)              

# ex 2 - This converts the string x to uppercase — BUT the result is NOT stored back into x. upper() returns a new uppercase string, but you are not assigning it.
x = 'abcd'
for i in x:
    print(i)
    x.upper()

# We want to iterate over the values from 0 to 10, and print their values. However, we want to skip all the values that are even. How can we achieve this?

for i in range(0,11):
     if(i%2 == 0):
        continue
     print(i)

# ex 3   --- error Hint: range(str) is not allowed.
x = 'abcd'
for i in range(x):
    print(i)      

# ex 4 -- error --Hint: Objects of type int are not iterable instead a list, dictionary or a tuple should be used.
x = 2021
for i in x:
  print(i)

# very bad score in loops lab Quiz