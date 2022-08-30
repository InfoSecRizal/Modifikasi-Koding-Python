# 10 Tantangan Untuk Pemula

# 1. Konversikan radian ke dalam derajat
radian = float(input('Masukan angka dalam radian!: '))
derajat = (radian*180)
print(derajat, 'derajat')

'''
2. Sort a list
Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that 
can be one of the following values: asc, desc, and none. If the second parameter is "asc," then the function should return a list with the
numbers in ascending order. If it's "desc," then the list should be in descending order, and if it's "none," it should return the original
list unaltered.

# versi 1
numbers = [0, 1, 2, 3]
strings = input('asc/desc/none: ')

if strings == 'asc':
  numbers.sort()
  print(numbers)
elif strings == 'desc':
  numbers.sort(reverse = True)
  print(numbers)
elif strings == 'none':
  print(numbers)
else:
  print('Input tidak valid!')

# versi 2:
def lists(numbers, strings):
  
  numbers = [0, 1, 2,]
  strings = input('asc/desc/none: ')

  if strings == 'asc':
    print(numbers)
  elif strings == 'desc':
    print(numbers.reverse)
  elif strings == 'none':
    print(numbers)
  else:
    print('Input tidak valid!')

lists([0, 1, 2], 'asc')
lists([2, 1, 0], 'desc')
lists([0, 1, 2], 'none')

# versi 3 
def lists(input):
  if input == 'asc':
    return [0, 1, 2]
  elif input == 'desc':
    return [2, 1, 0]
  elif input == 'none':
    return [0, 1, 2]
  
print(lists('none'))

Belum bisa pake fungsi karena belum terlalu ngerti parameter
'''

'''
3. Convert a decimal number into binary
Write a function in Python that accepts a decimal number and returns the equivalent binary number. To make this simple, the decimal number
will always be less than 1,024, so the binary number returned will always be less than ten digits long.

def dectobin()

'''

'''
4. Count the vowels in a string
Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function, only a, e, i, o, 
and u will be counted as vowels — not y.

def single_word

'''

'''
5. Hide the credit card number
Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an 
asterisk except the last four. For example, if the function gets sent "4444444444444444", then it should return "4444".
'''

import re


def mask_cc_number(cc_string, digits_to_keep=4, mask_char='*'):
   cc_string_total = sum(map(str.isdigit, cc_string))

   if digits_to_keep >= cc_string_total:
       print("Not enough numbers. Add 10 or more numbers to the credit card number.")

   digits_to_mask = cc_string_total - digits_to_keep
   masked_cc_string = re.sub('\d', mask_char, cc_string, digits_to_mask)

   return masked_cc_string


print(mask_cc_number("4444444444444444"))

'''
6. Are the Xs equal to the Os?
Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string. It should 
then return a boolean value of either True or False.If the count of Xs and Os are equal, then the function should return True. If the count
isn't the same, it should return False. If there are no Xs or Os in the string, it should also return True because 0 equals 0. The string 
can contain any type and number of characters.

def 
'''

'''
7. Create a calculator function
Write a Python function that accepts three parameters. The first parameter is an integer. The second is one of the 
following mathematical operators: +, -, /, or . The third parameter will also be an integer.The function should 
perform a calculation and return the results.For example, if the function is passed 6 and 4, it should return 24.

def calculator(integer, operators):
  
'''

'''
8. Give me the discount
Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be
the discount percentage as an integer.The function should return the price of the item after the discount has been applied. For example, 
if the price is 100 and the discount is 20, the function should return 80.
'''

def discount(full_price, discount_percentage):
  discount = full_price - discount_percentage
  print(f'Harga setelah diskon adalah: {discount}')

discount(100, 20)

'''
9. Just the numbers
Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. The function should
return a list with only the integers in the original list in the same order.

def list_length:


'''

'''
10. Repeat the characters
Create a Python function that accepts a string. The function should return a string, with each character in the original string doubled.
If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".
'''

def repeatCharacters(n,string):
  new_string = ""
  for char in string:
    new_string = new_string + char*n
  return new_string

print(repeatCharacters(2,"123a!"))