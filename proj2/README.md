# README for CISC882 homework 2

__By: Sanhu Li__

## Introduction
It's a character prediction program using the HMM model. Please see details in Assignment2 details. Please use python3 to run it.

## Usage
```sh
python3 predict.py <training_files> <testing_file>
```

Note: You can only have one test file and the rest will be treated as training file.
You can use "\*" within the training_files like
```sh
python3 predict.py charlotte/*.txt SanhuLi.txt
```
The script above will train on all text files under charlotte folder and build predict windows for SanhuLi.txt.

## Sample test cases
```sh
python3 predict.py SanhuLi.txt SanhuLi.txt > p1.txt
python3 predict.py charlotte/*.txt SanhuLi.txt > p2.txt
python3 predict.py charlotte/*.txt BranchElbert.txt > p3.txt

perl GetScanTime/GetScanTime.pl -k GetScanTime/Keyboard.txt -t SanhuLi.txt
perl GetScanTime/GetScanTime.pl -k GetScanTime/Keyboard.txt -t SanhuLi.txt -p p1.txt
perl GetScanTime/GetScanTime.pl -k GetScanTime/Keyboard.txt -t SanhuLi.txt -p p2.txt
perl GetScanTime/GetScanTime.pl -k GetScanTime/Keyboard.txt -t BranchElbert.txt
perl GetScanTime/GetScanTime.pl -k GetScanTime/Keyboard.txt -t BranchElbert.txt -p p3.txt
```

## How large is the corpus
The size of my corpus is just all files under charlotte. It's under ANC folder (Not sure the folder name is this, should be this) for the blizzard corpus. But the folder cannot be accessed through 882 vm, but I do have a copy of the corpus under the folder.

## n-gram?
This program is using 6-gram, but you can always change it within letter_predict.py. The variable called ngram is controlling it.

## How to fill the window?
For current cursor at pos x, we want to predict which letter should be put at x. But because the previous characters are fixed and the path for all the possible characters will only change at position x, so we do not even need to consider the characters before x, what we need to do is to test among all characters within the keyboard, let's say we are currently testing c, we only need to find the most 5 probable characters, and I use a PriorityQueue. The priority is represented as the negation of probability of c given the previous 5 characters of it, and the content is using the character c. After doing that for all characters within keyboard, I'll pick the best one and remove it from the queue, until the window is filled (when meeting with ' ', only remove it but don't put it into the window).

For the accuracy problem, I use logarithm values for the probability.

## How to smooth?
I add 0.5 to the counting when I try to calculate the frequency and I cannot find it (say the prefix and current character c), but I don't add one to the number of the prefix. I have two considerations:
  1. because this is not a small table for 6 gram, so it's not efficient to add 0.5 to all 0s, but if we do not do that for all cells, we cannot know the exact number to add to the prefix counting.
  2. because we want to compare the probability, but we don't need them to add to 1, we only need the relationship between them (which one is larger), so it doesn't matter if we don't add that number to the full counts and because we are using 0.5, for the same prefix, the 0s items will be less likely to be added into the window, which is exactly what we want.
From the above reasons, I decide to only add 0.5 to the 0s when doing calculation for frequency and and don't try to normalize it.

## Contacts
If you have any question, feel free to contact [lisanhu@udel.edu](mailto:lisanhu@udel.edu).
