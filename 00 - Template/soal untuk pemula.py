'''
Given a string containing the first name and last name, \
check if the name string is formatted in the title case.
'''

string = 'Kyla Kameron'
is_title = string.istitle()
print(is_title)

'''
Check whether a given Python string is a palindrome.
Palindrom adalah string ynag jika dibalik maka hasilnya akan
tetap sama, contoh: radar'
'''

def isPalindrome(s):
  rev = ''.join(reversed(s))

  if (s == rev):
    return True
  return False

s = 'radar'
ans = isPalindrome(s)

if (ans):
  print('Yes')
else:
  print('No')
  
'''
Verify whether or not two strings are anagrams.
Anagram adalah kondisi di mana dua string memiliki kata 
yang terdiri dari huruf dan jumlah yang sama tapi disusun 
dengan cara yang berbeda, contoh:
s1 = 'listen' s1 = 'dad'
s2 = 'silent' s2 = 'dad'
'''

def check(string1, string2):

  if(sorted(string1)== sorted(string2)):
    print('Kedua string ini adalah anagram')
  else:
    print('Kedua string ini bukan anagram')
    
string1 = 'Java'
string2 = 'avaJ'
check(string1, string2)
