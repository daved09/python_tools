#!/usr/bin/python3

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("source_dir")
parser.add_argument("dest_dir")
args = parser.parse_args()

def get_all_files(directory: str) -> list:
    return os.listdir(directory)

def compare(source_list: list, dest_list: list) -> list:
    newList = []
    for file in source_list:
        if file not in dest_list:
            newList.append(file)
    return newList

def print_list(my_list: list):
    for element in my_list:
        print(element)

source = get_all_files(args.source_dir)
dest = get_all_files(args.dest_dir)

list1 = compare(source, dest)
list2 = compare(dest, source)

all = []
all.extend(list1)
all.extend(list2)
print_list(all)