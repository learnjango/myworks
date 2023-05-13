usr_list = ['Aren', 'Davo', 'Karen']
with open('usr.txt', 'w') as f:
    for i in usr_list:
        f.write(f'{i}\n')