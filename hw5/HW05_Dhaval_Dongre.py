

def reverse(seq):
    revStr=''
    for x in range(len(seq)-1,-1,-1):
        revStr+=seq[x]
    return revStr

def rev_enumerate(seq):
    for i in range(len(seq)-1,-1,-1):
        yield(i,seq[i])

def find_second(target, string):
    init=string.find(target)

    if init==-1:
        raise ValueError(target+' Not present in '+string)

    return string.find(target, init+int(len(target)/2))

def get_line(path):
    # fp = open the file safely

    # with fp:
    #     for line in fp:
    #         line = strip the \n from the end of the line
    #         while line ends with '\\':  # merge continued lines
    #             line = line without the \\ last character + fp.readline().strip('\n')

    #     # now we've combined the continued lines, check for comments
    #     if line includes '#':
    #         if the '#' is not the first character in the line:
    #             yield the line up to, but not including the '#'
    #         else:
    #             # ignore this line.  Go back for the next line
    #         else:
    #         yield line

if __name__ == '__main__':
    print(reverse('abc'))
    print(list(rev_enumerate('abc')))
    print(int(1.0))
    print(find_second('abba', 'abbabba'))
    print(find_second('mom', 'momom'))

    # print(reversed(list(enumerate('abc')))


    # unittest.main(exit=False, verbosity=2)