

def reverse(seq):
    """return a reversed sequence of the given sequence"""
    revStr=''
    for x in range(len(seq)-1,-1,-1):
        revStr+=seq[x]
    return revStr

def rev_enumerate(seq):
    """a generator which returns the offset and each element of the sequence in a reverse order"""
    for i in range(len(seq)-1,-1,-1):
        yield(i,seq[i])

def find_second(target, string):
    """returns the offset of the second occurence of the given target in the desired string, otherwise returns -1"""
    init=string.find(target)

    if init==-1:
        return -1

    if len(target)==1:
        init+=1
    return string.find(target, init+round(len(target)/2))

def get_lines(path):
    """generator that opens a file for reading and returns one line from the file at a time.
    combine lines that end with a backslash with the subsequent line or lines until a line is found that does not end with a backslash
    Also ignores comments which start with '#' """
    try:
        fp = open(path,'r')
    except FileNotFoundError:
        print(f'Cannot open the file in the path {path}')

    else:
        with fp:
            for line in fp:
                line = line.strip()
                while line.endswith('\\'):
                    line = line[:-1]+fp.readline().strip()

                if line.find('#')!=-1:
                    if line.startswith('#')==False:
                        yield line[0:line.find('#')]
                    else:
                        continue
                else:
                    yield line

