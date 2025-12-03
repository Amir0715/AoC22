import argparse
import re

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i' , '--infile', default='in')
    parser.add_argument ('-o' , '--out' , default='out')
    return parser




def task(f):
    requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    invalid = 0
    data = f.read().split(sep='\n\n')
    for i in data:
        for req in requirements:
            if i.count(req) != 1:
                invalid += 1
                break 
    return [len(data) - invalid]



def task2(f):
    
    valid = 0
    data = f.read().split(sep='\n\n')

    for i in data:
        if validation(i):
            valid += 1
            print("Valid")
    return [valid]

def reV(s , regexp):
    if re.fullmatch(regexp, s):
        return True
    return False

def hgt(s):
    if s.count('cm') == 1:
        return 'cm'
    if s.count('in') == 1:
        return 'in'
    return 'false'
        

def validation(passport):
    

    data = passport.replace('\n', ' ').split(' ')

    fields = {}
    for i in data:
        kv = i.split(':')
        fields[kv[0]] = kv[1]

    regexp_color = r'#[a-f0-9]{6}\b'
    regexp_pid = r'\b[\d]{9}\b'
    
    hgtd = {
        'in' : lambda y : 59 <= int(y) <= 76, 
        'cm' : lambda y : 150 <= int(y) <= 193, 
        'false' : lambda y : False}



    requirements = {
    'byr' : lambda x : 1920 <= int(x) <= 2002, 
    'iyr' : lambda x : 2010 <= int(x) <= 2020, 
    'eyr' : lambda x : 2020 <= int(x) <= 2030, 
    'hgt' : lambda x : hgtd[hgt(x)](x[:-2]) ,
    'hcl' : lambda x : reV(x, regexp_color) ,
    'ecl' : lambda x : x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') , 
    'pid' : lambda x : reV(x, regexp_pid) ,
    'cid' : lambda x : True
    }

    for req in requirements:
        if passport.count(req) != 1 and req != 'cid':
            return False


    countOfValidField = 0
    for i in sorted(fields.items()):
        print(i , requirements[i[0]](i[1]))
        if requirements[i[0]](i[1]):
            countOfValidField += 1
    
    print(countOfValidField)
    
    if countOfValidField == 8 or countOfValidField == 7:
        return True

    return False




if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()

    infile = namespace.infile
    outfile = namespace.out

    f = open(infile, 'r')
    o = open(outfile, 'w') 
    res = task2(f)
    for d in res:
        o.write(str(d)+'\n')
    f.close()
    o.close()