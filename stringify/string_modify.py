import string
import time

class string_manipulation:

  def clean(self , text):
    final_text = ""
    for t in text:
      if t == " ":
        continue
      final_text = final_text + t
    
    print("AFTER REMOVING SPACES: ")
    print(final_text)

  def string_analysis(self , text):
    time.sleep(2)
    vowel = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    consonants = "aeiouAEIOU"
    count_vowel = 0
    for charv in text:
      for v in vowel:
        if charv == v:
          count_vowel += 1 
    
    count_consonants = 0
    for charc in text:
      for c in consonants:
        if charc == c:
          count_consonants += 1 
    print(" ")
    print(f"Total vowels: {count_vowel}")
    print(f"Total consonanats: {count_consonants}")

  def string_formatting(self , text):
    time.sleep(2)
    after_format = text.upper()
    print(" ")
    print(f"after formatting: {after_format}")

