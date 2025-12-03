import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i' , '--infile', default='in')
    parser.add_argument ('-o' , '--out' , default='out')
    return parser



def task(f):
    data = f.read().splitlines()
    for i in range(len(data)):
        for j in range(len(data)):
            if int(data[i]) + int(data[j]) == 2020:
                return [int(data[i])*int(data[j])]

def task2(f):
    data = f.read().splitlines()
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if int(data[i]) + int(data[j]) + int(data[k]) == 2020:
                    return [int(data[i])*int(data[j])*int(data[k])]

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