import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i' , '--infile', default='in')
    parser.add_argument ('-o' , '--out' , default='out')
    return parser

def task(f):
    ids = []
    data = f.read().splitlines()
    for i in data:
        rows = [i for i in range(128)]
        cols = [i for i in range(8)]
        for j in i:
            if j == 'F':
                rows = rows[:int(len(rows)/2)]
            elif j == 'B':
                rows = rows[int(len(rows)/2):]
            elif j == 'R':
                cols = cols[int(len(cols)/2):]
            elif j == 'L':
                cols = cols[:int(len(cols)/2)]
        
        ids.append(rows[0]*8 + cols[0])
        

    return [max(ids)]


def task2(f):
    ids = []
    data = f.read().splitlines()
    for i in data:
        rows = [i for i in range(128)]
        cols = [i for i in range(8)]
        for j in i:
            if j == 'F':
                rows = rows[:int(len(rows)/2)]
            elif j == 'B':
                rows = rows[int(len(rows)/2):]
            elif j == 'R':
                cols = cols[int(len(cols)/2):]
            elif j == 'L':
                cols = cols[:int(len(cols)/2)]
        
        ids.append(rows[0]*8 + cols[0])
        
    ids = sorted(ids)
    res = 0
    for i in range(len(ids)-2):
        if ids[i] + 1 != ids[i+1]:
            res = ids[i] + 1

    return [res]


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