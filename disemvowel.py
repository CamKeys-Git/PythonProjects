# Removes all vowel charecters from strings

def disemvowel(string):
  new = ''
  for letter in string:
    if letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u' and letter != 'A' and letter != 'E' and letter != 'I' and letter != 'O' and letter != 'U':
      new += letter
       
  return new

print(disemvowel("This website is for losers LOL!"))


def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

print(disemvowel("This website is for losers LOL!"))


