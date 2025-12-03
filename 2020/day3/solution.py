import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i' , '--infile', default='in')
    parser.add_argument ('-o' , '--out' , default='out')
    return parser

def task(f):
    data = f.read().splitlines()
    x = 0 
    res = [0,0,0,0,0]
    sum = 1
    for y in data:
        if y[x] == '#':
            res[0] += 1
            # print(y[x])
        x = (x + 1) % len(y)
    x = 0 
    for y in data:
        if y[x] == '#':
            res[1] += 1
            # print(y[x])
        x = (x + 3) % len(y)
    x = 0 
    for y in data:
        if y[x] == '#':
            res[2] += 1
            # print(y[x])
        x = (x + 5) % len(y)
    x = 0 
    for y in data:
        if y[x] == '#':
            res[3] += 1
            # print(y[x])
        x = (x + 7) % len(y)
    x = 0 
    for y in data[::2]:
        if y[x] == '#':
            res[4] += 1
            # print(y[x])
        x = (x + 1) % len(y)
    for i in res:
        sum *= i
    return [sum]


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()

    infile = namespace.infile
    outfile = namespace.out

    f = open(infile, 'r')
    o = open(outfile, 'w') 
    res = task(f)
    for d in res:
        o.write(str(d)+'\n')
    f.close()
    o.close()