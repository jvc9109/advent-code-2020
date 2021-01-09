#! bin/python
import re

def first_problem(data):
    valid_pass = 0
    for line in data:
        info = line.split(" ")
        number_matches = [int(i) for i in info[0].split("-")]
        pattern = info[1].replace(":", "")
        password = info[2]
        if number_matches[0] <= len(re.findall(pattern, password)) <= number_matches[1]:
            valid_pass += 1
    print(valid_pass)


def second_problem(data):
    valid_pass = 0
    for line in data:
        info = line.split(" ")
        number_matches = [int(i) for i in info[0].split("-")]
        pattern = info[1].replace(":", "")
        password = info[2]
        if len(password) >= number_matches[1]-1:
            if password[number_matches[0]-1] == pattern and password[number_matches[1]-1] != pattern:
                valid_pass += 1
            elif password[number_matches[0]-1] != pattern and password[number_matches[1]-1] == pattern:
                valid_pass += 1
    print(valid_pass)

with open("../data/day2.txt") as file:
    data = file.readlines()
    first_problem(data)
    second_problem(data)
        