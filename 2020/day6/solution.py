import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i' , '--infile', default='in')
    parser.add_argument ('-o' , '--out' , default='out')
    return parser

def task(f):
    data = f.read().split(sep='\n\n')
    res = 0
    for i in data:
        a = set(i)
        a.discard('\n')
        res += len(a)
            
    return [res]


def task2(f):
    data = f.read().split(sep='\n\n')
    res = 0
    for i in data:
        p = i.split('\n')
        sets = []
        for j in p: 
            sets.append(set(j))
        
        for k in range(len(sets)-1):
            sets[k+1].intersection_update(sets[k], sets[k+1])
        
        res += (len(sets[-1]))



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