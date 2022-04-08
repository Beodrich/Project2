#Project 2 - Promotion Bias Simulation
from audioop import bias
from glob import glob
import os 
import json
import random
import copy
from typing import Dict

"""
file name: SampleCo.txt
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
biasDict={}

#look through the bias dict
#grab the first key,value pair
#look at the bias number
#loop through the company dict
#if bias key match empolyee category, generate number
#do stuff after

def ApplyBias(biasDict,companyDict):#A->0, B->-2
    minNum=1
    maxNum=100
    companyCopy=copy.deepcopy(companyDict)
    for i,j in  companyCopy.items():#i is key, j is value list
        for value in j:
            #figure out current key,value pair and figure out bias...
            if isinstance(value ,list):
                biasMin=minNum-biasDict[i]
                biasMax=maxNum+biasDict[i]
                
                value[0]+=random.randrange(biasMin,biasMax)
            else:
                biasMin=minNum-biasDict[i]
                biasMax=maxNum+biasDict[i]
                value+=random.randrange(biasMin,biasMax)
    return companyCopy

            
            
    


def Simulate(companyDict,numGen,companyName):
    global biasDict

    for i in range(numGen):
        copy= ApplyBias(biasDict,companyDict)
        print(f"company dict after {i} is {companyDict}")
        print(f"bias for company dict after {i} is {copy}")

        

        #do stuff :( 
    
    

def readFile():
    global biasDict
    #example file
    #fileName=input("Enter a file name: ")
    companyTxt=open("SampleCo.txt","r")
    companyList=[]
    companyName=companyTxt.readline()
    numGen=companyTxt.readline()
    #load jason into a list
    biasDict=json.loads(companyTxt.readline())
   
    for x in companyTxt:
        temp=json.loads(x)
        newList=list(temp.items())
        companyList.append(newList)
    #convert that list to a dict--- rest of lines I guess
    for row in range(len(companyList)):
        for col in range(len(companyList[row])):
            temp=companyList[row][col]
            if temp[0] in companyDict:
                companyDict[temp[0]].append([temp[1]])
            else:
                companyDict[temp[0]]=[temp[1]]
    companyTxt.close()

    return (companyName,numGen)

    
       
               
       
            


    
companyName, numGen= readFile()
Simulate(companyDict,int(numGen),companyName)
print(f"number is {numGen}")
print(f"company name is {companyName}")


