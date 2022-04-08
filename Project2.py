#Project 2 - Promotion Bias Simulation
import os 
import json
from typing import Dict

"""
SampleCo
10
{"A":0,"B":-2}
{"A":5,"B":5}
{"A":5,"B":5}
{"A":5,"B":5}
{"A":5,"B":5}
{"A":5,"B":5}

(0,99)
(6,105)
A:[0,5,5,5,5,5]
B:[-2,5,5,5,5,5]
"""
companyName=""
numGen=0
companyDict={}

def ProcessDict(companyDict:Dict):
    for i,j in  companyDict.items():
        for ugh in j:
            print(ugh)
    print()


def Simulate(companyDict,numGen,companyName):
    minNum=0
    maxNum=99
    for i in range(numGen):
        ProcessDict(companyDict)

        #do stuff :( 
    
    

def readFile():
    #example file
    fileName=input("Enter a file name: ")
    companyTxt=open(fileName,"r")
    companyList=[]
    companyName=companyTxt.readline()
    numGen=companyTxt.readline()
    #load jason into a list
    for x in companyTxt:
        temp=json.loads(x)
        newList=list(temp.items())
        companyList.append(newList)
    #convert that list to a dict 
    for row in range(len(companyList)):
        for col in range(len(companyList[row])):
            temp=companyList[row][col]
            if temp[0] in companyDict:
                companyDict[temp[0]].append([temp[1]])
            else:
                companyDict[temp[0]]=[temp[1]]
    return (companyName,numGen)

    
       
               
       
            


    companyTxt.close()
    
companyName, numGen= readFile()
Simulate(companyDict,int(numGen),companyName)
print(f"number is {numGen}")
print(f"company name is {companyName}")


