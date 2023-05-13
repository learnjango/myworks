import pyshorteners

s = pyshorteners.Shortener()
full_url = input("Please paste your URL > ")
print(s.isgd.short(full_url))