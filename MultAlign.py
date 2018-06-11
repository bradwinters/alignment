#!/usr/bin/python
import numpy as np
import sys, math


def show(dir,a,b,c):
    print(dir)
    print(a)
    print(b)
    print(c)

def alMatch(s1,s2,s3):
    ls1=len(s1) 
    ls2=len(s2) 
    ls3=len(s3) 
    skor=0

    if (ls1 != ls2)  or (ls1 != ls3) or (ls2 != ls3):
        print("Something is wrong, strings are not the same size.")
        return -1
    for xx in range(len(s1)):
        if s1[xx]==s2[xx]==s3[xx]:
           skor+=1

    return skor
 
def score(vv,ww,kk):
    if vv==ww==kk:
       return 1
    return 0

def readData():
    '''
    Open hardcoded file, parse data anticipataed but may change
    Load just data into a numpy array,
    '''
    #f = open('t2.txt', 'r')   #Extra dataset
    #f = open('t1.txt', 'r')   #Small example dataset  from text
    #f = open('extra', 'r')   #Small example dataset  from text
    #f = open('trival.txt', 'r')   #Small example dataset  from text
    #f = open('t4.txt', 'r')   #Small example dataset  from text
    f = open('test', 'r')   #Small example dataset  from text
    
    cnt=0
    for line in f:
        cnt+=1
        if cnt==1:
            string1=line.rstrip() # get rid of cr
        elif cnt==2:
            string2=line.rstrip() # get rid of cr
        elif cnt==3:
            string3=line.rstrip() # get rid of cr
        else:
            print("File is not in the form of 2 strings, exit")
            exit()

    print("Read ",cnt," Datapoints")
    return string1, string2, string3

def print2D(pDesString,pAncString,Centers,title="Table Title"):  # prints floats to 3 dec places

    oldString="   "
    topLine="    "
    padDesString=' '+pDesString+'-'
   
    for i in range(len(pAncString)):
        oldString+=pAncString[i]+"     "
        topLine+="-------"
    print() 
    print() 
    print("       ",title)
    print("          ",oldString)
    print(topLine)
    
    cntr=0
    for row in Centers:
       print(padDesString[cntr],"|",end=" ")
       cntr+=1
       for element in row:
           if isinstance(element,float):
              if element == math.inf*-1:
                 element=-10
              print("%5d" % (element),end=" ")
           else:
               print(" ",element," ",end=" ")

       print()

def whowon(pone,ptwo,pthree,pfour,pfive,psix,pseven):
    Max=-9999
    MaxDir='$' 

    if pone > Max:
       Max = pone
       MaxDir=1
    if ptwo > Max:
       Max = ptwo
       MaxDir=2
    if pthree > Max:
       Max = pthree
       MaxDir=3
    if pfour > Max:
       Max = pfour
       MaxDir=4
    if pfive > Max:
       Max = pfive
       MaxDir=5
    if psix > Max:
       Max = psix
       MaxDir=6
    if pseven > Max:
       Max = pseven
       MaxDir=7

    print("1:",pone," 2:",ptwo," 3:",pthree," 4:",pfour," 5:",pfive," 6:",psix," 7:",pseven)
    print(MaxDir)
       
    return MaxDir

def mult_align():
    debug7=True
    #### default gap value
    Gap = -5.
    blosum62 = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2},
'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2},
'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2},
'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3},
'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3},
'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3},
'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1},
'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2},
'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2},
'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1},
'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1},
'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2},
'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1},
'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3},
'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2},
'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2},
'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2},
'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2},
'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1},
'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}
        


    v, w, u = readData()
    print ("SEQUENCE 1:@",v,"@ ",len(v))
    print ("SEQUENCE 2:@",w,"@ ",len(w))
    print ("SEQUENCE 2:@",u,"@ ",len(u))
    print ("gap open      : ", Gap)

    #### initiate and calculate value
    lengthseq1 = len(v)
    lengthseq2 = len(w)
    lengthseq3 = len(u)
    row = lengthseq1+1 
    col = lengthseq2+1
    depth= lengthseq3+1
    print("Row is ",row," Col is ",col," Depth is ",depth)
    val = [[[0. for k in range(depth)] for j in range(col)] for i in range(row)]
    backtrack = [[['#' for k in range(depth)] for j in range(col)] for i in range(row)]
    # linear end
    for v1 in range(row):
        backtrack[v1][0][0]=1
    for w1 in range(col):
        backtrack[0][w1][0]=2
    for u1 in range(depth):
        backtrack[0][0][u1]=3
    # planar end
    for v1 in range(row):
        for w1 in range(col):
           backtrack[v1][w1][0]=4
    for v1 in range(row):
        for u1 in range(depth):
           backtrack[v1][0][u1]=5
    for w1 in range(col):
        for u1 in range(depth):
           backtrack[0][w1][u1]=6



    print(" &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print(backtrack)
    
    val[0][0][0] = 0
    
    val[1][0][0]=Gap
    for i in range(2,row):
        val[i][0][0] = val[i-1][0][0]+Gap

    val[0][1][0]=Gap
    for j in range(2,col):
        val[0][j][0] = val[0][j-1][0]+Gap

    val[0][0][1]=Gap
    for k in range(2,depth):
        val[0][0][k] = val[0][0][k-1]+Gap

    val[0][0][0] = 0
    print(val)

    print("##############    Initialized Arrays  ##########")     
    #  output strings of v,w and u that will have dashes added
    sv=""
    sw=""
    su=""
    for i in range(1,row):
       for j in range(1,col):
           for k in range(1,depth):

              #  Map the Mid grid
              #print("i j k = ",i," ",j," ",k)
              one  =val[i-1][j][k] + score(v[i-1],'-','-')
              two  =val[i][j-1][k] + score('-',w[j-1],'-')
              three=val[i][j][k-1] + score('-','-',u[k-1])

              four =val[i-1][j-1][k] + score(v[i-1],w[j-1],'-')
              five =val[i-1][j][k-1] + score(v[i-1],'-',u[k-1])

              six  =val[i][j-1][k-1] + score('-',w[j-1],u[k-1])
              seven=val[i-1][j-1][k-1] + score(v[i-1],w[j-1],u[k-1])
              
              winner=max(one,two,three,four,five,six,seven)
              Fromptr=whowon(one,two,three,four,five,six,seven)
              backtrack[i][j][k]=Fromptr

              if winner > 0:
                  print("match at ",i," ",j," ",k)           
              # All 7 reccurances have been calculated
              val[i][j][k]=winner
              I=i
              J=j
              K=k
    print("** backtrack 000  **")
    print(backtrack[0][0][0])
    print("** backtrack 100  **")
    print(backtrack[1][0][0])
    print("** backtrack 010  **")
    print(backtrack[0][1][0])
    print("** backtrack 001  **")
    print(backtrack[0][0][1])
    print("** backtrack 111  **")
    print(backtrack[1][1][1])

    print("** backtrack 110  **")
    print(backtrack[1][1][0])

    print("** backtrack 011  **")
    print(backtrack[0][1][1])

    print("** backtrack 101  **")
    print(backtrack[1][0][1])


    print("Grid Score is ",val[I][J][K])
    print("Backtrack trace max ",backtrack[I][J][K])
    safeMax=10000000
    safe=0
    endi=len(v)-1
    endj=len(w)-1
    endk=len(u)-1
    #while endi>=0 or endj>=0 or endk>=0:
    while (I>0 or J>0 or K>0):
       print("Backtrack at top, I:",I," J:",J," K: ",K," found ",backtrack[I][J][K])
       ##   All three
       if backtrack[I][J][K]==7:
           if endi>=0:
              sv+=v[endi] 
           else:
              sv+='-'
           if endj>=0:
              sw+=w[endj]
           else:
              sw+='-'
           if endk>=0:
              su+=u[endk]
           else:
              su+='-'
           I-=1
           J-=1
           K-=1
           endi-=1
           endj-=1
           endk-=1
           show(7,sv,sw,su)
       ##  two at a time, one dash 
       elif backtrack[I][J][K]==6:
           sv+='-'
           if endj>=0:
              sw+=w[endj]
           else:
              sw+='-'
           if endk>=0:
              su+=u[endk]
           else:
              su+='-'
           J-=1
           K-=1
           endj-=1
           endk-=1
           show(6,sv,sw,su)
       elif backtrack[I][J][K]==5:
           if endi>=0:
              sv+=v[endi]
           else:
              sv+='-'
           sw+='-'
           if endk>=0:
              su+=u[endk]
           else:
              su+='-'
           I-=1
           K-=1
           endi-=1
           endk-=1
           show(5,sv,sw,su)
       elif backtrack[I][J][K]==4:
           if endi>=0:
              sv+=v[endi]
           else:
              sv+='-'
           if endj>=0:
              sw+=w[endj]
           else:
              sw+='-'
           su+='-'
           I-=1
           J-=1
           endi-=1
           endj-=1
           show(4,sv,sw,su)
       ##  Two dashes at a time, only one dir 
       elif backtrack[I][J][K]==1:
           if endi>=0:
              sv+=v[endi]
           else:
              sv+='-'
           sw+='-'
           su+='-'
           I-=1
           endi-=1
           show(1,sv,sw,su)
       elif backtrack[I][J][K]==3:
           sv+='-'
           sw+='-'
           if endk>=0:
              su+=u[endk]
           else:
              su+='-'
           K-=1
           endk-=1
           show(3,sv,sw,su)
       elif backtrack[I][J][K]==2:
           sv+='-'
           if endj>=0:
              sw+=w[endj]
           else:
              sw+='-'
           su+='-'
           J-=1
           endj-=1
           show(2,sv,sw,su)


       print("ijk",I,":",J,":",K,"--->v: ",sv," w:",sw," u:",su)
       safe+=1
    if (safe==safeMax):
       print("**** Safety valve was used**** ")
    print("---------------------")


    print(v)
    print(w)
    print(u)
    ans=alMatch(sv,sw,su)
    print(ans) 
    sv=sv[::-1]
    sw=sw[::-1]
    su=su[::-1]
    print(sv)
    print(sw)
    print(su)
if __name__ == "__main__":
    mult_align()
