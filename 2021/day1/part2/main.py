import argparse
from functools import reduce
import logging
 
logging.basicConfig(filename="log.log", filemode="w", level=logging.DEBUG)


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i' , '--infile', default='in')
    parser.add_argument ('-o' , '--out' , default='out')
    return parser

def task(f):
    max = 0
    data = list(map(int, f.read().splitlines()))
    for i in range(1, len(data) - 2):
        debug_str = f"{data[i-1:i+2]}, sum = {sum(data[i-1:i+2])}, {data[i:i+3]}, sum = {sum(data[i:i+3])}, {sum(data[i-1:i+2]) < sum(data[i:i+3])}"
        logging.debug(debug_str)
        if sum(data[i-1:i+2]) < sum(data[i:i+3]):
            max += 1
    return (max, )

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