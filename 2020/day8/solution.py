import argparse
from pprint import pprint
import copy

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i' , '--infile', default='in')
    parser.add_argument ('-o' , '--out' , default='out')
    return parser

def task(f):
    acc = 0
    index = 0
    indexesOfComand = set()

    data = f.read().split(sep='\n')
    for i in range(len(data)):
        data[i] = data[i].split(' ')
        data[i][1] = int(data[i][1])
    
    while True:
        if index not in indexesOfComand:
            indexesOfComand.add(index)
            if data[index][0] == 'acc':
                acc += data[index][1]
                index += 1
            elif data[index][0] == 'jmp':
                index += data[index][1]
            elif data[index][0] == 'nop':
                index += 1
        else:
            return [acc]

def task2(f):


    data = f.read().split(sep='\n')
    for i in range(len(data)):
        data[i] = data[i].split(' ')
        data[i][1] = int(data[i][1])
    
    indexOfFaultComand = 0
    while True:
        tmpdata = copy.deepcopy(data)
        acc = 0
        index = 0
        indexesOfComand = set()

        if tmpdata[indexOfFaultComand][0] == 'jmp':
            print('jmp' , indexOfFaultComand)
            tmpdata[indexOfFaultComand][0] = 'nop'
        elif tmpdata[indexOfFaultComand][0] == 'nop':
            tmpdata[indexOfFaultComand][0] = 'jmp'
            print('nop' ,indexOfFaultComand)


        while True:
            if index not in indexesOfComand:
                indexesOfComand.add(index)

                if tmpdata[index][0] == 'acc':
                    acc += tmpdata[index][1]
                    index += 1
                
                elif tmpdata[index][0] == 'jmp':
                    if index > indexOfFaultComand:
                        indexOfFaultComand = index
                        # print(indexOfFaultComand)
                    index += tmpdata[index][1]

                elif tmpdata[index][0] == 'nop':
                    if index > indexOfFaultComand:
                        indexOfFaultComand = index
                        # print(indexOfFaultComand)
                    index += 1

            elif index == len(data)-1:
                return [acc]
            else:
                break
        


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