import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i' , '--infile', default='in')
    parser.add_argument ('-o' , '--out' , default='out')
    return parser

def task(f: list[str]) -> list:
    f = map(lambda x: [x.split()[0], int(x.split()[1])], f)
    horizontal = 0
    depth = 0
    for vector, value in f:
        if vector == 'forward':
            horizontal += value
        elif vector == 'down':
            depth += value
        elif vector == 'up':
            depth -= value
    return [horizontal*depth]

if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()

    infile = namespace.infile
    outfile = namespace.out

    f = open(infile, 'r')
    o = open(outfile, 'w') 
    res = task(f.read().splitlines())
    for d in res:
        o.write(str(d)+'\n')
    f.close()
    o.close()