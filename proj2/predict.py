from letter_predict import *
from glob import *
from sys import argv


def get_file_content(file_name):
    file = open(file_name)
    lines = file.readlines()
    file.close()
    lines = [i.strip() for i in lines if i.strip() != '']
    lines = ' '.join(lines)
    return lines


def usage():
    print('''\
    python3 predict <training_files> <test_file>
    To output the result to a file,
    python3 predict <training_files> <test_file> > <predict_output_file>
    ''')


def train(files: list, stat: dict):
    for file in files:
        for name in glob(file):
            lines = get_file_content(name)
            training(lines, stat)


if len(argv) < 3:
    usage()
    exit(-1)

stat = dict()
train(argv[1:-1], stat)

text = get_file_content(argv[-1])
predict(text, stat)
