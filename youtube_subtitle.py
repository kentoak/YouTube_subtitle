import numpy as np
import pandas as pd
import re
import sys

def main():
    if len(sys.argv)==1:
        print("Please type file name")
    file=""
    for i in range(len(sys.argv)-2):
        file+=sys.argv[i+1]+" "
    file+=sys.argv[-1]+'.txt'
    sc=""
    with open(file) as f:
        l=[s for s in f.readlines()]
        
    #print(l)
    u=3

    for i in range(len(l)):
        l[i]=l[i].replace('\n','')
        
        if re.fullmatch('\d\d:\d\d',l[i]):
            u+=1
            if u>=4:
                if re.match('\d\d:59',l[i]):
                    tao=re.match('\d\d:59',l[i]).group()
                    u=0
                    rep='\n'+tao+'\n'
                    l[i]=re.sub('^[0-9]{2}:[0-9]{2}',rep,l[i])
                elif re.match('\d\d:29',l[i]):
                    tao=re.match('\d\d:29',l[i]).group()
                    u=0
                    rep='\n'+tao+'\n'
                    l[i]=re.sub('^[0-9]{2}:[0-9]{2}',rep,l[i])
                elif re.match('\d\d:00',l[i]):
                    tao=re.match('\d\d:00',l[i]).group()
                    u=0
                    rep='\n'+tao+'\n'
                    l[i]=re.sub('^[0-9]{2}:[0-9]{2}',rep,l[i])
                elif re.match('\d\d:30',l[i]):
                    tao=re.match('\d\d:30',l[i]).group()
                    u=0
                    rep='\n'+tao+'\n'
                    l[i]=re.sub('^[0-9]{2}:[0-9]{2}',rep,l[i])
                elif re.match('\d\d:01',l[i]):
                    tao=re.match('\d\d:01',l[i]).group()
                    u=0
                    rep='\n'+tao+'\n'
                    l[i]=re.sub('^[0-9]{2}:[0-9]{2}',rep,l[i])
                elif re.match('\d\d:31',l[i]):
                    tao=re.match('\d\d:31',l[i]).group()
                    u=0
                    rep='\n'+tao+'\n'
                    l[i]=re.sub('^[0-9]{2}:[0-9]{2}',rep,l[i])
                elif re.match('\d\d:02',l[i]):
                    tao=re.match('\d\d:02',l[i]).group()
                    u=0
                    rep='\n'+tao+'\n'
                    l[i]=re.sub('^[0-9]{2}:[0-9]{2}',rep,l[i])
                elif re.match('\d\d:32',l[i]):
                    tao=re.match('\d\d:32',l[i]).group()
                    u=0
                    rep='\n'+tao+'\n'
                    l[i]=re.sub('^[0-9]{2}:[0-9]{2}',rep,l[i])
            #print(u)
            if u==0:
                pass
            else:
                l[i]=" "
        sc+=l[i]
    #print(sc)
    with open('out_'+file,'w') as fw:
        fw.write(sc)
        print('out_'+file)

if __name__=="__main__":
    main()
