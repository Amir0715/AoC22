import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i' , '--infile', default='in')
    parser.add_argument ('-o' , '--out' , default='out')
    return parser

def task(f):
    data = f.read().splitlines()
    res = 0
    for row in data:
        line = row.split( )
        interval = line[0].split('-')
        char = line[1].split(':')[0]
        string = line[2]
        if int(interval[0]) <= string.count(char) <= int(interval[1]):
            res+=1
            print(interval, char, string, string.count(char))

    return [res]

def task2(f):
    data = f.read().splitlines()
    res = 0
    for row in data:
        line = row.split( )
        interval = line[0].split('-')
        char = line[1].split(':')[0]
        string = line[2]
        if (string[int(interval[0])-1] == char) ^ (string[int(interval[1])-1] == char):
            res+=1
            print(interval, char, string)
            
    return [res]

if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()

    infile = namespace.infile
    outfile = namespace.out

    f = open(infile, 'r')
    o = open(outfile, 'w') 
    res = task2(f)
    f.close()
    for d in res:
        o.write(str(d)+'\n')
    o.close()