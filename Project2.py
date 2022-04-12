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


def Promotion(companyList):
    for i in range(1,len(companyList)):
        companyList[i]+=FindTenPercent(companyList[i])

def Simulate(numGen, biasDict, compayList):
    for i in range(numGen):
        biasList= ApplyBias(companyList,biasDict)
        for j in companyList:
            print(FindTenPercent(j))
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
Simulate(int(gen),bias,companyList)
#Promotion(companyList)
