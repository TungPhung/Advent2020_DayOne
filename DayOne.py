#!/usr/bin/env python3

import os,sys

test_input = [1721, 979, 366, 299, 675, 1456]

def read_file():
    all = []
    with open('input.txt', 'r') as f:
        for i in f:
            all.append(int(i.strip('\n')))
    return all

def find_2020(array):
    twenty_twenty_list = [2020 - i for i in array]
    for i in twenty_twenty_list:
        for j in array:
            if i == j:
                return i*(2020-i)

if __name__ == "__main__":
    print(find_2020(read_file()))    
