import sys

prev_blank = False

for line in sys.stdin:
    line=line.strip()
    if line == '':
        if not prev_blank:
             print(line, end='\n')
             prev_blank = True
    else:
        i = line.find('%')
        if i == -1:
            if line == '':
                if not prev_blank:
                    print(line, end='\n')
                    prev_blank = True
            else:
                print(line, end='\n')
                prev_blank = False
        elif i==0:
            rest = line[1:].rstrip('\n')
            if rest.strip() == '':
                print(line, end='\n')
                prev_blank = False
        else:
            line = line[:i]
            print(line, end='\n')
            prev_blank = False



             


