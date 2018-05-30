import numpy as np
'''
'''

def Hamming(na1,na2):
    mm=0
    m=0
    x=len(na1)
    y=len(na2)
    if x != y:
        return -1 
    for i in range(x):
        if na1[i]!=na2[i]: 
           mm+=1 
        else:
           m+=1
    return mm



def CalcScore(FAString,FDString,blo):

    dScore=0
    for x in range(len(FAString)):

        if FAString[x]=='-' or FDString[x]=='-':
           dScore-=5
        else:
           dScore+=blo[FDString[x]][FAString[x]] 
             
    return dScore

def scoreMatch(na1,na2):
    if na1==na2:
        return 0
    else:
        return -1

def scoreNA(na1,na2):
    sim_mat = [[2,-1,1,-1],[-1,2,-1,1],[1,-1,2,-1],[-1,1,-1,2]]
    rowDict= {'A':0,'C':1,'G':2,'T':3}
    row=rowDict[na1]
    col=rowDict[na2]
    
    print(sim_mat[row][col])
    return sim_mat[row][col]

def MaxOfThree(pDiag,pVert,pHorz):
    pDir='$'

    if pDiag >= pVert:
        r1 = pDiag;
        pDir='D'  
    else:
        r1= pVert     
        pDir='V'
    
    if  pHorz > r1:
        r1 = pHorz
        pDir='H'

    return pDir, r1



def updateLD(aDict,pKey,pValue):  # update a dict of lists
    
    tList=[] 
    if pKey in aDict:  # exists, extract, update list.  Replace list
       for i in aDict[pKey]:  # make a copy of the list
           tList.append(i)    # 
       if pValue in tList:
           print("Duplicate in list, ignore")
       else:
           tList.append(pValue)   # add the new value if its new
           del aDict[pKey] 
           aDict[pKey]=tList
    else:
       tList.append(pValue)  # create list, put val in it
       aDict[pKey]=tList

    return aDict 

def updateD(aDict,pKey,pValue):  # update a dict of lists
    
    if pKey in aDict:  # exists, extract, update list.  Replace list
       aDict[pKey]=int(pValue)
       print("Possible double entry of an edge in the wts dictionary")
    else:
       aDict[pKey]=int(pValue)

    return aDict 

def printNumpy(Centers):  # prints floats to 3 dec places
    sizeD=len(Centers)
    for i in range(sizeD):
        for j in range(sizeD):
             print(Centers[i][j],end=' ')
        print()

    
def print2D(pDesString,pAncString,Centers):  # prints floats to 3 dec places

    oldString="  "
    topLine="  "
    padDesString=' '+pDesString+'-'
    for i in range(len(pAncString)):
        oldString+=pAncString[i]+"   "
        topLine+="-----"
    print("       ",oldString,"-")
    print(topLine)
    cntr=0
    for row in Centers:
       print(padDesString[cntr],"|",end=" ")
       cntr+=1
       for element in row:
           print("%3d" % (element),end=" ")
       print()


def readData():
    '''
    Open hardcoded file, parse data anticipataed but may change
    Load just data into a numpy array, 
    '''
    #f = open('t.txt', 'r')   #Extra dataset
    #f = open('tt.txt', 'r')   #Extra dataset
    #f = open('na.txt', 'r')   #Small example dataset  from text
    #f = open('na3.txt', 'r')   #Small example dataset  from text
    f = open('ttest', 'r')   #Small example dataset  from text
    #f = open('t1.txt', 'r')   #Small example dataset  from text
    #f = open('t2.txt', 'r')   #Small example dataset  from text
    #f = open('t3.txt', 'r')   #Small example dataset  from text
    #f = open('t4.txt', 'r')   #Small example dataset  from text
    #f = open('extra', 'r')   #Small example dataset  from text
    #f = open('durbin', 'r')   #Small example dataset  from text
    #f = open('hm.txt', 'r')   #Small example dataset  from text
     
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


gWts=[]
debug=False
def main():



    Gap=-1 
    print("Gap penalty is ",Gap)
    
    AncString, DesString = readData() #load Data and Params from file
    print("Strings to compare are:")
    print(AncString)
    print("Which mutates to ")
    print(DesString)
    
    AColSize=len(AncString)+1
    DRowSize=len(DesString)+1

    # -----------------    create grid for scores
    fullGrid=[]
    for i in range(DRowSize):
        tGrid=[]
        for j in range(AColSize):
            tGrid.append(0)
        tGrid.append(Gap)
        fullGrid.append(tGrid)

    #  add bottom row of sigma, penalty for indel Gaps
    tGrid=[]
    for i in range(AColSize+1):
        tGrid.append(Gap)
    fullGrid.append(tGrid)

    # convert to numpy array
    npGrid=np.array(fullGrid)
    
    #print("Grid set up ",npGrid)
    # -----------------    create grid for Backtrack path 

   
    for j in range(1,AColSize):
        npGrid[0][j]=npGrid[0][j-1]+Gap
    for i in range(1,DRowSize):
        npGrid[i][0]=npGrid[i-1][0]+Gap

    if debug:
       print2D(DesString,AncString,npGrid)

    print ("Create backtrack grid")
    # -----------------    create grid for direction crumbs 
    fullGrid=[]
    for i in range(DRowSize):
        tGrid=[]
        for j in range(AColSize):
            tGrid.append('#')
        tGrid.append(Gap)
        fullGrid.append(tGrid)


    # convert to numpy array
    npBackTrackGrid=np.array(fullGrid)
    
    # -----------------    create grid for Backtrack path 

   
    for j in range(1,AColSize):
        npBackTrackGrid[0][j]='H'
    for i in range(1,DRowSize):
        npBackTrackGrid[i][0]='V'

    if debug: 
       print(DesString,AncString,npBackTrackGrid)

    
    for i in range(1,DRowSize):
        for j in range(1,AColSize):
             #print("----  Top of j loop ----")
             simScore=scoreMatch(AncString[j-1],DesString[i-1])
             Diag =npGrid[i-1][j-1]+simScore
             prevRow=npGrid[i-1][j] +Gap
             prevCol =npGrid[i][j-1] +Gap
             Dir, Score=MaxOfThree(Diag,prevRow,prevCol)
             if debug: 
                 print(i," ",j,":old Diag->",npGrid[i-1][j-1]," and score of ",simScore,"-> ",AncString[j-1]," ",DesString[i-1])
                 print("New Scores are: Diag->",Diag," PrevRow ->",prevRow,"PrevCol->",prevCol)
                 print("Score is ",Score)
             npGrid[i][j]=Score
             npBackTrackGrid[i][j]=Dir 
    if debug:
       print2D(DesString,AncString,npGrid)
    
    print("Final position answer", npGrid[DRowSize-1][AColSize-1])
    
    i=DRowSize
    j=AColSize

    lcsString=[]
   
    # print("Start backtrack")
    while i > 1 or j > 1:
        Dir=npBackTrackGrid[i-1][j-1] 

        #print("->Row:",i," Col:",j," is ",npBackTrackGrid[i][j])

        if Dir=='D':  
            i=i-1
            j=j-1
        elif Dir=='V':
            i=i-1
        elif Dir=='H': 
            j=j-1
        else:
            print("Problem, invalid direction found")
            i=i-1
            j=j-1

        lcsString.append(Dir)
        if debug: 
           print("Path is ",lcsString)
 
    lcsString=lcsString[::-1]
    #print("Pathway is ",lcsString)
    #print(npBackTrackGrid)
    #print("Translate path to the two strings")
    FAString=""
    FDString=""

    xx=0
    for x in range(len(lcsString)):
       if lcsString[x]=='D' or lcsString[x]=='H':
           FAString+=AncString[xx]
           xx+=1
       else: 
           FAString+='-'
       #print(FAString)

    xx=0
    for x in range(len(lcsString)):
       if lcsString[x]=='D' or lcsString[x]=='V':
           FDString+=DesString[xx]
           xx+=1
       else: 
           FDString+='-'
       #print(FDString)
    if (len(FAString) != len(FDString)):
        print("Strings are not the same size")

    print("Hamming D score is ")
    ans=Hamming(FAString,FDString)
    print(ans)
    print(FAString)
    print(FDString)

if __name__ == "__main__":
    main()
