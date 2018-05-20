import numpy as np
'''
'''

def TTarget(prBackPath,pDesString):
    alignedString=""
    
    for x in range(len(prBackPath)):
        if prBackPath[x]=='H':
            alignedString+='-'
        else:
            alignedString+=pDesString[x]

    return alignedString 

def CalcScore(FAString,FDString,blo):

    dScore=0
    for x in range(len(FAString)):

        if FAString[x]=='-' or FDString[x]=='-':
           dScore-=5
        else:
           dScore+=blo[FDString[x]][FAString[x]] 
             
    return dScore



def TSource(prBackPath,pAncString):
    alignedString=""
    
    for x in range(len(prBackPath)):
        if prBackPath[x]=='V':
            alignedString+='-'
        else:
            alignedString+=pAncString[x]

    return alignedString 


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


def LCS(pBacktrack, v, w):
    lcs=""
    i =len(w)
    j =len(v)
    while i > 0 and j > 0:
        if pBacktrack[i-1][j-1] == 'V':      #South
            i = i-1
            lcs+='V'
        elif pBacktrack[i-1][j-1] == 'H':     #East
            j = j-1
            lcs+='H'
        elif pBacktrack[i-1][j-1] == 'D':     #Diag
            lcs+='D'
            i = i-1
            j = j-1
        else:   
            lcs+='$'
            i = i-1
            j = j-1
        print("---",lcs,"---",)
    return lcs 



def List2ArrowPath(aList):
   
    sz=len(aList) 
    NicePath=""
    # all nodes get arrows except the last 
    for i in range(sz-1):
        pst=str(i)+"->"
        NicePath+=pst
    NicePath+=str(aList[-1]) 

    return NicePath


def find_shortest_path(graph,start,end,path=[]):
    path = path + [start]
    if start == end:
        return path
 
    if start not in graph:
        return None

    shortest = None

    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph,node,end,path)
            if newpath:
                 if not shortest or len(newpath) < len(shortest):
                     shortest = newpath

    return shortest






#  find some path, perhaps arbitrarily 
#
def find_path(graph, start, end, path=[]):
    path = path + [start]  

    print("In find_path, start is ",start," end is ", end)
    print("Graph is ",graph)


    if start == end:
        return path

    if start not in graph:
        print("Start is not in the graph dict")
        return None
  
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath

    return None



#  find all the paths, arbitrarily ordered
#  Recursive function that builds a list of the paths
#
def find_all_paths(graph, start, end, path=[]):
    # start at the start, put init node in the list
    path = path + [start]  

    # base relation, end of the line, done 
    if start == end:
        return [path]

    # safeguard impossible search, return empty list 
    if start not in graph:
        print("Start is not in the graph dict")
        return [] 

    #paths list will contain results to be returned
    paths = []
  
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths 


# convert a tuple to a string to use as a key in wts dict, node1_node2
def tupalize(pEdge):
    part1=pEdge[0]
    part2=pEdge[1]
    result=part1+"_"+part2
    return  result

def pair2tupal(pnode1,pnode2):
    result=pnode1+"_"+pnode2
    return  result


def EdgeWt(pStart,pEnd,pwts):
    # convert edges into wts by looking them up in wts

    cpStart=str(pStart)
    cpEnd  =str(pEnd)
    tup=cpStart+"_"+cpEnd  #Create the key
    if tup in pwts:
        jj=pwts[tup]
        #print(tup," weighs ",jj[0])   maybe useful later
    else:
        #print("Edge ",tup," does not exist.")
        return -1 

    return jj 

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

def GraphIncident(aGraph):
    
    for key, value in aGraph.items():
        newGraph[value]=key

    print("whoa  ")
    print(newGraph)

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

def ParseU(astring):
    facter=astring.count('_') 
    return facter

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
    # f = open('hm.txt', 'r')   #Small example dataset  from text
     
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

def FindX(nGrid):

    sizeD=len(nGrid)
    for i in range(sizeD):
        for j in range(sizeD):
             if nGrid[i][j]==-1:
                return str(i), str(j)
    return -99, -99 

def ezGrid(nGrid,pwts):

    sizeD=len(nGrid)
    for i in range(sizeD):
        for j in range(sizeD):
             if j!=i:
                 nGrid[i][j]=EdgeWt(i,j,pwts)
             else:
                 nGrid[i][j]=0
                 

    return nGrid

gWts=[]
debug=False
def main():


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


    Gap=-5 
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
             simScore=blosum62[AncString[j-1]][DesString[i-1]]
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

    print("Calculated score is ")
    ans=CalcScore(FAString,FDString,blosum62)
    print(ans)
    print(FAString)
    print(FDString)

if __name__ == "__main__":
    main()

