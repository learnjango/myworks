text = 'Hello World'
new_text = ''
regex = '*lo'
new_regex = ''
for i in regex:
    if i != '*':
        new_regex += i
for word in text:
    if word != ' ':
        new_text += word
    