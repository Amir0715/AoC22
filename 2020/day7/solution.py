import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-i' , '--infile', default='in')
    parser.add_argument ('-o' , '--out' , default='out')
    return parser

def parserFile(f):
    data = f.read().splitlines()
    res = []
    for i in data: 
        a = i.split('contain')
        a[1] = a[1].split(',')
        a[0] = a[0].strip()
        a[1][-1] = a[1][-1].strip('.')
        for i in range(len(a[1])):
            a[1][i] = a[1][i].strip()
        a[0] = a[0].replace(' bags','')
        for j in range(len(a[1])):
            a[1][j] = a[1][j].replace(' bags', '')
            a[1][j] = a[1][j].replace(' bag', '')
        res.append(a)

    result = {}
    for j in res:
        subdict = {}
        for k in j[-1]:
            sub = k.split(' ', 1)
            subdict[sub[1]] = int(sub[0]) if sub[0] != 'no' else 0
        result[j[0]] = subdict
    # print(result)

    return result
        

def task(f):
    bags = set(['shiny gold'])
    data = parserFile(f)
    lens = [0,1]
    while lens[-1] != lens[-2] :
        for i in data:
            subbags = []
            for b in bags:
                if b in data[i]:
                    subbags.append(i)
            bags.update(subbags)
        lens.append(len(bags))
    return [lens[-1]-1]

def reduse(bags, data):
    for i in bags:
        bags[i] = reduse(bags,data[bags[i]])


# def recurs_sum(dictionary):
#     sum = 0
#     for i in dictionary:
#         sum += recurs_sum(dictionary[i])
#     return  

def task2(f):
    bags = {1 : 'shiny gold'}
    data = parserFile(f)
    # print(data)
    for i in bags:
        bags[i] = data[bags[i]]
    for i in bags:
        print(i)
    print(bags)
    # for i in data:
    #     subbags = []
    #     for b in bags:
    #         if b in data[i]:
    #             subbags.append(i)
    #     bags.update(subbags)
    
    return []


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