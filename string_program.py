from stringify import string_modify

s = string_modify.string_manipulation()

text = input("enter text that you want to modify: ")
s.clean(text)
s.string_analysis(text)
s.string_formatting(text)