import argparse
from functools import reduce

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i' , '--infile', default='in')
    parser.add_argument ('-o' , '--out' , default='out')
    return parser

def task(f):
    i = 0
    prev = None
    data = map(int, f.read().splitlines())
    for a in data:
        if prev is not None and prev < a: 
            i += 1
        prev = a
    return (i, )
        

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