#Project 2 - Promotion Bias Simulation
import os 
import json

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


def readFile():
    lineCount=0
    #example file
    companyTxt=open("SampleCo.txt","r")
    companyList=[]
    companyName=companyTxt.readline()
    print(companyName)
    numGen=companyTxt.readline()
    print(numGen)
    for x in companyTxt:
        temp=json.loads(x)
        newList=list(temp.items())
        companyList.append(newList)

    
       
               
       
            


    companyTxt.close()
    print(companyList)
    
readFile()


