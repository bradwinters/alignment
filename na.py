import numpy as np
'''
'''

def scoreNA(na1,na2):
    sim_mat = [[2,-1,1,-1],[-1,2,-1,1],[1,-1,2,-1],[-1,1,-1,2]]
    rowDict= {'A':1,'C':2,'G':3,'T':4}
    row=rowDict[na1]
    col=rowDict[na2]
    return sim_mat[row][col]

def MaxOfThree(pOne,pTwo,pThree):
    r1 = max(pOne,pTwo) 

    return max(r1,pThree) 

def IterativeOutputLCS(Backtrack, v, w):
    LCS=""
    i =len(v)
    j =len(w)
    while i > 0 and j > 0:
        if Backtrack(i, j) == 'S':      #South
            i = i-1
        elif Backtrack(i,j) == 'E':     #East
            j = j-1
        elif Backtrack(i,j) == 'D':     #Diag
            LCS =  LCS+v[i]             #concatenate v[i] with LCS
            i = i-1
            j = j-1

    return LCS



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
    for i in range(len(pAncString)):
        oldString+=pAncString[i]+"   "
        topLine+="-----"
    print("   ",oldString)
    print(topLine)
    cntr=0
    for row in Centers:
       print(pDesString[cntr],"|",end=" ")
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
    f = open('t.txt', 'r')   #Extra dataset
    #f = open('test.txt', 'r')   #Small example dataset  from text
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


   
    AncString, DesString = readData() #load Data and Params from file
    print("Strings to compare are:")
    print(AncString)
    print("Which mutates to ")
    print(DesString)

    print("Test drive blosom array")
    tGrid=[]
    fullGrid=[]
    for i in range(len(DesString)):
        tGrid=[]
        for j in range(len(AncString)):
             a1=AncString[j]
             d1=DesString[i]

             if a1==d1:
                 MDiag=tGrid[i-1][j-1]+1
             else:
                 MDiag=tGrid[i-1][j-1]-2

             PrevRow=tGrid[i-1][j]-1
             PrevCol=tGrid[i][j-1]-1
             Score=MaxOfThree(MDiag,PrevRow,PrevCol)
             print("Match",MDiag,"MisM ",MMDiag,"PRow",PevRow,"PCol",PrevCol)
             print("Compare ",a1," to ",d1," => ",MaxOfThree)
             tGrid.append(Score)
        fullGrid.append(tGrid)
        print()
    print2D(DesString,AncString,fullGrid)

    exit()


    ans = find_path(graph, startNode, endNode, path=[])
    print("The first answer is ",ans)

    ans = find_shortest_path(graph,startNode,endNode,path=[])
    print("Shortest of all paths is ",ans)

    ans = find_all_paths(graph, startNode, endNode, path=[])
    pnum=0
    for apath in ans:
       pnum+=1
       print("Path (",pnum,") ",apath)

    # make a list of tuples, Score,Path, then show the longest
    FinalAns=[]
    for apath in ans:
        last=len(apath)-1
        nump_apath=np.array(apath)
        Cost=0.0
        for ele in range(last):
            print(nump_apath[ele],"->",nump_apath[ele+1],end=" ") 
            pnode1=nump_apath[ele]
            pnode2=nump_apath[ele+1]
            wtsKey=pair2tupal(pnode1,pnode2)
            Cost+=wts[wtsKey]
            print("add ",wts[wtsKey])
            print(Cost)
        FinalAns.append((Cost,apath))        
        print()

    print("All paths are ",FinalAns)
    Max= -1
    Min = 10000000000000
    for i in FinalAns:
       if i[0] > Max:
           MaxTuple=(i[0],i[1]) 
           Max=i[0]
       if i[0] < Min:
           MinTuple=(i[0],i[1]) 
           Min=i[0]
 


    print(MaxTuple[0])
    print(List2ArrowPath(MaxTuple[1]))
    print("----------------------------------------")
    print(MinTuple[0])
    print(List2ArrowPath(MinTuple[1]))

    print("*****Finally ******")


    print(blosum62['A']['A'])
    
if __name__ == "__main__":
    main()

