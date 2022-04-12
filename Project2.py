import os
import json
import random
import copy
"""
Rank1=["A":10, "B":10]
[(5,5),(5,4)]

SampleCo Output
Rank 1A:7, B:3
Rank 2A:8, B:2
A:5, B:5
A:6, B:4
A:4, B:6

"""
def FindTenPercent( companyList):
        total= sum(companyList)
     
        return round((total*0.10))


def Promotion(companyList,numToPromote,rowToInsert,colToInsert):
    
    if rowToInsert==0:#promotion can't happen in the first list
        return companyList
    if rowToInsert<len(companyList) and colToInsert<len(companyList[0]):
        #insert a new number at the row and col
        #subtract one from pervious row and col
        copyOfCompany=copy.deepcopy(companyList)
        copyOfCompany[rowToInsert][colToInsert]+=numToPromote
        copyOfCompany[rowToInsert+1][colToInsert]-=numToPromote
        return copyOfCompany
def DeMotion(companyList, numToPromote, rowToInsert,colToInsert):
    if rowToInsert==len(companyList)-1:#only need to -1 if where doing zero based indexing 
        return companyList#demotion can't happen at the last spot in the list, need to fire them to make this correct
    if rowToInsert<len(companyList) and colToInsert<len(companyList[0]):
        copyOfCompany=copy.deepcopy(companyList)
        copyOfCompany[rowToInsert][colToInsert]-=numToPromote
        copyOfCompany[rowToInsert+1][colToInsert]+=numToPromote
        return copyOfCompany
    



    

def Simulate(numGen, biasDict, compayList):
    for i in range(numGen):
        biasList= ApplyBias(companyList,biasDict)
        for j in companyList:
            #print(FindTenPercent(j))
            return


def ApplyBias(companyList,biasDict):
    defaultMin=1
    defaultMax=100
    currentKey='A'
    size=len(companyList[0])-1
    index=0
    biasList=[]
    temp=[]
    for i in range(len(companyList)):
        for j in range(len(companyList[i])):
        
            biasMin=defaultMin-abs(biasDict[currentKey])
            biasMax=defaultMax+biasDict[currentKey]
            num=random.randrange(biasMin,biasMax)
            temp.append(num)

        
            if index==size:
                index=0
                currentKey='A'
                biasList.append(copy.deepcopy(temp))
                temp.clear()

            else:
                index+=1
                currentKey=chr(ord(currentKey)+1)

    return biasList






   
        

         

def readFile():
    companyList=[]
    companyTxt=open("SampleCo.txt","r")
    companyName=companyTxt.readline()
    numGen=companyTxt.readline()

    bias=json.loads(companyTxt.readline())

    for x in companyTxt:
        companyList.append(list(json.loads(x).values()))
        
    companyTxt.close()
    return (companyList,bias,companyName,numGen)


readFile()
companyList,bias,name,gen=readFile()
#print(ApplyBias(companyList,bias))
#Simulate(int(gen),bias,companyList)
d=Promotion(companyList,1,1,0)
a=DeMotion(companyList,1,1,0)

print(f"dict before promotion happens {companyList} ")
print(f"dict after promotion happens {d}")
print(f"dict after demotion happens {a}")

#Promotion(companyList)
