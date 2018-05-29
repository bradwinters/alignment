import numpy as np
'''
'''
###   Multiple scoring methods can be called
##  For Fitting, full string of w, substring of v, find max in bottom row
###
def MaxBottom(npG,shortWord):
    lastRow=npG.shape[0]-2
    numCols=npG.shape[1]-2
    print("Row=",lastRow," collums= ",numCols)
    Max=-9999
    start=len(shortWord)
    for x in range(start,numCols+1):
        if npG[lastRow][x] > Max:
            Max=npG[lastRow][x]
            ix=x 
    Startpoints=[]    
    for x in range(start,numCols+1):
        if npG[lastRow][x] == Max:
           Startpoints.append(x)

    return Max, ix, lastRow, Startpoints



###
##  Scoring "matrix" during cell direction calculation, not final score of global hamming distance
##  Match gets global match value, mismatch and indel get global score for those  
###
def SimpScoreNA(na1,na2):
    aScore=0

    if na1==na2:
        aScore=match
    elif na1=='-' or na2=='-':
        aScore=Gap
    elif na1 != na2:
        aScore=mismatch
    else:
        print("Something is wrong")
        print("undefined match/mismatch/indel for ",na1," ",na2)
        exit()
    return  aScore


###
##    Scoring for final string alignment
###
def CalcScoreNA(FAString,FDString):

    dScore=0
    pmatch=0
    pmismatch=0
    pGap=0
    for x in range(len(FAString)):
        if FAString[x]==FDString[x]:
           pmatch+=match
        elif FAString[x]=='-' or FDString[x]=='-':
           pGap+=Gap
        elif FAString[x] != FDString[x]:
           pmismatch+=mismatch
        else:
           print("Comparing ",FAString," to ",FDString," at x :",x)
           print("at position of ",FAString[x]," to ", FDString[x])
           print("But something is wrong, exiting from CalcScoreNA")
           exit()


    print("Match: ",pmatch," MisMatch: ",pmismatch," Gap: ",pGap)
    print("Lengths: S1 ",len(FAString)," ",len(FDString))
    dScore=pmatch+pmismatch+pGap
    return dScore

###
##  After scoring current row column, consider previous cols and the origin to keep one
###
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
    #if r1 < 1:
    #  r1=0

    return pDir, r1


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
    #f = open('t1.txt', 'r')   #Small example dataset  from text
    #f = open('t2.txt', 'r')   #Small example dataset  from discuss 
    #f = open('t3.txt', 'r')   #Small example dataset  from  discuss
    #f = open('t4.txt', 'r')   #Small example dataset  from discuss 
    #f = open('extra', 'r')   #big example dataset  from text 
    #f = open('test', 'r')   # actual test
    #f = open('quiz', 'r')   # actual test
    f = open('aaa', 'r')   # actual test
     
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

##################################
## Globals go here
##################################
# Turn on profuse debug print statements
debug=True
debug=False
###############   Set before runtime for now, params later
match=1
mismatch=-1
Gap=-1

##################################
def main():


    print("Gap penalty optional Match/MM for NAs:",Gap,"MisMatch is ",mismatch," and Match is ",match)
    
    AncString, DesString = readData() #load Data and Params from file
    print("Strings to compare are:")
    print(AncString)
    print("Which mutates to ")
    print(DesString)


    ###############################################################
    ######   Set Up Grids npGrid for costs and npBackup for path  #
    ###############################################################
    
    AColSize=len(AncString)+1
    DRowSize=len(DesString)+1

    ###############################################################
    # -----------------    create grid for scores
    ###############################################################
    fullGrid=[]
    for i in range(DRowSize):
        tGrid=[]
        for j in range(AColSize):
            tGrid.append(0)
        tGrid.append(0)
        fullGrid.append(tGrid)

    #  add bottom row of sigma, penalty for indel Gaps
    tGrid=[]
    for i in range(AColSize+1):
        tGrid.append(0)
    fullGrid.append(tGrid)

    # convert to numpy array
    npGrid=np.array(fullGrid)
    
    #print("Grid set up ",npGrid)

    # put in penalties or zeros in the first row  Here penalty is -1 
    for j in range(1,AColSize):
        npGrid[0][j]=npGrid[0][j-1]
    # put in penalties or zeros in the first column 
    for i in range(1,DRowSize):
        npGrid[i][0]=npGrid[i-1][0]

    if debug:
       print2D(DesString,AncString,npGrid)

    print ("Create backtrack grid")
    ################################################################## 
    # -----------------    create grid for direction crumbs 
    ################################################################## 
    fullGrid=[]
    for i in range(DRowSize):
        tGrid=[]
        for j in range(AColSize):
            tGrid.append('#')
        tGrid.append(0)
        fullGrid.append(tGrid)


    # convert to numpy array
    npBackTrackGrid=np.array(fullGrid)
    
    # -----------------    create grid for Backtrack path 
    # preload top row and col 1 with Hs and Vs, respectivily
    for j in range(1,AColSize):
        npBackTrackGrid[0][j]='O'
    for i in range(1,DRowSize):
        npBackTrackGrid[i][0]='V'



    ####################################################################
    ######   Fill npGrid with costs note Dir in npBackupGrid for path  #
    ######   Track largest cost and where it is, thats the start pt    #
    ####################################################################
    if debug: 
       print(DesString,AncString,npBackTrackGrid)
       print("Start Main part of DP, score matches")
    
    MaxScore=-999 
    maxRow=-1
    maxCol=-1
    ##########################################################
    ##   Main scoring loop  
    ##########################################################
    for i in range(1,DRowSize):
        for j in range(1,AColSize):
             #print("----  Top of j loop ----")
             simScore=SimpScoreNA(AncString[j-1],DesString[i-1])
             Diag =npGrid[i-1][j-1]+simScore
             prevRow=npGrid[i-1][j] +Gap
             prevCol =npGrid[i][j-1] +Gap
             Dir, Score=MaxOfThree(Diag,prevRow,prevCol)
             if Score >= MaxScore:
                 MaxScore=Score
                 maxRow=i
                 maxCol=j
             if debug: 
                 print(i," ",j,":old Diag->",npGrid[i-1][j-1]," and score of ",simScore,"-> ",AncString[j-1]," ",DesString[i-1])
                 print("New Scores are: Diag->",Diag," PrevRow ->",prevRow,"PrevCol->",prevCol)
                 print("Score is ",Score)
             npGrid[i][j]=Score
             npBackTrackGrid[i][j]=Dir 
    if debug:
       print2D(DesString,AncString,npGrid)
    
    print("Final position answer", npGrid[DRowSize-1][AColSize-1])
    print("Best ending Score was", MaxScore," at ",maxRow," x ",maxCol) 



    ####################################################################
    ######   Using only npBackupGrid for path information              #
    ######   Track largest cost and where it is, thats the start pt    #
    ######    Build lcsString for path directions to make new strings  #
    ####################################################################
    
    lcsString=[]  # to load directions, D, V or H
   
    # print("Start backtrack")
    #  Find starting point at the bottom row somewhere. This is the last value of w
    big, iix, iiy, StartList=MaxBottom(npGrid,DesString) 
    print("Biggest value, last w char, at ",iiy," ",iix," was ",big)
    print("FYI Right Leftmost corner is ",npGrid[iiy][iix])
    print("All potential start points at ",StartList)
    pick = input("Pick a start point by position, 0 to ")
    p=int(pick)
    iix=StartList[p]
    print("Using ", iix," as a start point.") 
    i=iiy
    j=iix
    #i+=1
    #j+=1
    #fishtail
    print(npBackTrackGrid)
    Dir=' '
    Bail=False
    while j > 0 and Bail==False:
        Dir=npBackTrackGrid[i][j] 

        if debug: 
           print("->Row:",i," Col:",j," is ",npBackTrackGrid[i][j])

        if Dir=='D':  
            lcsString.append(Dir)
            i=i-1
            j=j-1
        elif Dir=='V':
            lcsString.append(Dir)
            i=i-1
        elif Dir=='H': 
            lcsString.append(Dir)
            j=j-1
        elif Dir=='O': 
            Bail=True
        else:
            print("Problem, invalid direction found")
            i=i-1
            j=j-1
        I=i+1
        J=j+1
        II=i
        JJ=j
        if debug: 
           print("Reverse Path is ",lcsString)

    #fishhead marker
    if debug:
        print("Grid is in the following range")
        print("Min xy is ",II," x ",JJ) 
        print("Max xy is ",maxRow," x ",maxCol) 
        print("String should be ",AncString[JJ:maxCol+1])
        print("String should be ",DesString[II:maxRow+1])
    
        print(AncString[JJ:maxRow+1])
        for ix in range(II,maxRow+1):
            for iy in range(JJ,maxCol+1):
                print("%3d" % (npGrid[ix][iy]),end=" ")
            print()
        for ix in range(II,maxRow+1):
            for iy in range(JJ,maxCol+1):
                print("%3c" % (npBackTrackGrid[ix][iy]),end=" ")
            print()

    lcsString=lcsString[::-1]
    #print("Corrected Pathway is ",lcsString)
    #print(npBackTrackGrid)
    if debug:
       ####################################################
       print("Translate path to the two strings")
       print("String 1 starts at",I)
       print("String 2 starts at",J)
       print("01234567890123456789")


    ####################################################################
    ######   Build both strings from the lcsString one at a time       # 
    ######   V or H means a dash or not for the source/target.  D is = #  
    ######   Also builds the strings themselves from inside the grid   # 
    ####################################################################

    FAString=""
    FDString=""

    J=J-1
    for x in range(len(lcsString)):
       if lcsString[x]=='D' or lcsString[x]=='H':
           FAString+=AncString[J]
           J+=1
       else: 
           FAString+='-'
       #print(FAString)

    I=I-1
    for x in range(len(lcsString)):
       if lcsString[x]=='D' or lcsString[x]=='V':
           FDString+=DesString[I]
           I+=1
       else: 
           FDString+='-'
       #print(FDString)

    ###   sanity check
    if (len(FAString) != len(FDString)):
        print("Strings are not the same size")

    ##################################
    ######   Show Results            #
    ##################################
    print(AncString)
    print("Which mutates to ")
    print(DesString)
    ans=CalcScoreNA(FAString,FDString)
    #ans=CalcScorePAM(FAString,FDString)
    print("Calculated score is ",ans, " compared to max in grid of ",MaxScore)
    print("Given answer")
    print("2")
    print("TAGGCTTA")
    print("TAGA--TA")
    print("Given answer")
    print("1")
    print("GTAGGCTTA")
    print("ATAGA--TA")
    print("---------------------")
    print(ans)
    print(FAString)
    print(FDString)
  

if __name__ == "__main__":
    main()
