from glob import *
from random import randint

# Done use charlotte/WentzLinda.txt as training file.

outfile = open('SanhuLi.txt', 'w')

for name in glob('charlotte/*.txt'):
    file = open(name, encoding='UTF-16')
    lines = file.readlines()
    file.close()
    lines = [i.strip() for i in lines if i.strip() != '']
    lines = ' '.join(lines)
    words = lines.split(' ')
    # print(words)
    result = []
    if len(words) >= 700:
        st = randint(0, 300)
        result = words[st:st + 400]
        print(name)
        # print(' '.join(result))
        outfile.write(' '.join(result))
        outfile.close()
        break
