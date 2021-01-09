import re

def set_passports(lines):
    passports = [{}]
    current_passport = 0
    for line in lines:
        if line != '':
            info_string = line.split(' ')
            for info in info_string:
                key_value = info.split(':')
                passports[current_passport][key_value[0]] = key_value[1] 
        else:
            current_passport += 1
            passports.append({})
    return passports

def get_height_and_units(height_string):
    height_pattern = r'(\d{1,3})(cm|in)'
    height_att = re.findall(height_pattern, height_string)
    if height_att:
        return height_att[0]
    else:
        return None

def is_valid_passport(passport):
    keys = passport.keys()
    number_of_keys = len(keys)

    if number_of_keys < 7:
        return False
    if number_of_keys == 7 and 'cid' in keys:
        return False

    

    if (len(passport['byr']) != 4) or  not (1920 <= int(passport['byr']) <= 2002):
        return False
    if (len(passport['iyr']) != 4) or  not (2010 <= int(passport['iyr']) <= 2020):
        return False
    if (len(passport['eyr']) != 4) or  not (2020 <= int(passport['eyr']) <= 2030):
        return False
    if len(passport['pid']) != 9:
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'hzl', 'oth']:
        return False
    if not re.match(r'^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$', passport['hcl']):
        return False
    height = get_height_and_units(passport['hgt'])
    if height == None:
        return False
    if (height[1] == 'cm' and not (150 <= int(height[0]) <= 193)):
        return False
    if (height[1] == 'in' and not (59 <= int(height[0]) <= 76)):
        return False
    return True


with open("../data/day4.txt") as file:
    data = file.read()
    lines = data.split('\n')
    passports = set_passports(lines)
    valid_passports = 0
    for passport in passports:
        if is_valid_passport(passport):
            valid_passports += 1
    print(f'There are {valid_passports} valid passports')
