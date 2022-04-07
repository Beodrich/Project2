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
    
    companyName=companyTxt.readline()
    print(companyName)
    numGen=companyTxt.readline()
    print(numGen)
    for x in companyTxt:
        print(x[2])
        if x[0] in companyDict:
            companyDict[x[2]].append(x[5])
        else:
            companyDict[x[2]]=[x[5]]

        
            


    companyTxt.close()
    print(companyDict)
    
readFile()


