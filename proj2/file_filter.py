from glob import *


def filter_file(file_name):
    file = open(file_name, encoding='UTF-16')
    lines = file.readlines()
    file.close()
    lines = [i.strip() for i in lines if i.strip() != '']
    lines = ' '.join(lines)
    file = open(file_name, 'w')
    file.write(lines)
    file.close()


for name in glob('charlotte/*.txt'):
    filter_file(name)
