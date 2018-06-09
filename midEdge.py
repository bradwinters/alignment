#!/usr/bin/python
import numpy as np
import sys, math

def readData():
    '''
    Open hardcoded file, parse data anticipataed but may change
    Load just data into a numpy array,
    '''
    #f = open('t2.txt', 'r')   #Extra dataset
    #f = open('t1.txt', 'r')   #Small example dataset  from text
    #f = open('extra', 'r')   #Small example dataset  from text
    #f = open('t3.txt', 'r')   #Small example dataset  from text
    #f = open('t4.txt', 'r')   #Small example dataset  from text
    f = open('test', 'r')   #Small example dataset  from text
    
    cnt=0
    for line in f:
        cnt+=1
        if cnt==1:
            string1=line.rstrip() # get rid of cr
        elif cnt==2:
            string2=line.rstrip() # get rid of cr
        else:
            print("File is not in the form of 2 strings, exit")
            exit()

    print("Read ",cnt," Datapoints")
    return string1, string2

def maxBox(psimScore, pxval, pyval):
    theMax=-99999 
    Dir='$'
    if psimScore > theMax: 
       theMax=psimScore
       Dir='D'
    if pxval > theMax:
       theMax=pxval
       Dir='H'
    if pyval > theMax:
       theMax=pyval
       Dir='V'; 

    return Dir, theMax

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



def middle_edge():
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
        


    seq1, seq2 = readData()
    print ("SEQUENCE 1:@",seq1,"@ ",len(seq1))
    print ("SEQUENCE 2:@",seq2,"@ ",len(seq2))
    print ("gap open      : ", Gap)

    #### initiate and calculate value
    lengthseq1 = len(seq1)
    lengthseq2 = len(seq2)
    row = lengthseq1+1 
    col = lengthseq2+1
    print("Row is ",row," Col is ",col)
    Li=int(lengthseq2/2)
    print("Columes are ",col,"and i is half of col ",int(Li))
    Hs=seq2[:Li+1]
    print("Align",seq1," to ",Hs)
    val = [[0. for j in range(Li+1)] for i in range(row)]

    val[1][0]=Gap
    for i in range(2,row):
        val[i][0] = val[i-1][0]+Gap
    val[0][1]=Gap
    for j in range(2,Li):
        val[0][j] = val[0][j-1]+Gap

    val[0][0] = 0
    print("##############    Initialize Arrays  ##########")     
    print2D(seq1,Hs,val,"Middle Layer, Diagonal Moves")  # prints floats to 3 dec places
    print("##############    Arrays initialized  ##########")     

    for j in range(1,Li+1):
        for i in range(1,row):

            #  Map the Mid grid
            qx=seq1[i-1]
            qy=seq2[j-1]
            tdot=blosum62[qx][qy] 
            fromMid=val[i-1][j-1]+tdot
            fromUp=val[i-1][j]+Gap
            fromLeft=val[i][j-1]+Gap
            val[i][j]=max(fromUp,fromMid,fromLeft)

            if val[i][j] == fromMid:
                Dir='D' 
            elif val[i][j] == fromUp:
                Dir='U' 
            else:
                Dir='L' 
    print2D(seq1,Hs,val,"Middle Layer, Diagonal Moves")  # prints floats to 3 dec places


    Max=-9990
    atx=-9
    for x in range(row):
        print("Checking row ",x," col ",Li," with ",val[x][Li])
        if val[x][Li] > Max:
             Max=val[x][Li]
             atx=x
    s1="("+str(atx)+","+str(Li)+")"
    atx+=1
    Li+=1
    s2="("+str(atx)+","+str(Li)+")"
    print(s1,s2)



if __name__ == "__main__":
    middle_edge()
