#Project 2 - Promotion Bias Simulation 
#By: Ben Odrich and Emily Joyce

import os
import json
import random
import copy

#find 10 percent of each rank in order to find how many to demote or promote
def FindTenPercent( biasList):
        total= abs(sum(biasList)) #sum the values of each rank
        return round((total*0.10)) #find 10% of the sum

#promote top 10% people across ranks 
def Promotion(companyList,numToPromote,rowToInsert,colToInsert):
    if rowToInsert==0:#promotion can't happen in the first list
        return companyList
    if rowToInsert<len(companyList)-1 and colToInsert<len(companyList[0]):
        #insert a new number at the row and col
        #subtract one from pervious row and col
        #causing a promotion to happen
        copyOfCompany=copy.deepcopy(companyList) #copy company so to not overwrite it
        copyOfCompany[rowToInsert+1][colToInsert]=max(copyOfCompany[rowToInsert+1][colToInsert]+numToPromote,0)#this is to prevent negative empolyess from happening
        copyOfCompany[rowToInsert+1][colToInsert]=max(copyOfCompany[rowToInsert+1][colToInsert]-numToPromote,0)
        return copyOfCompany
    return companyList

#Demote botom 10% of people across ranks
def DeMotion(companyList, numToPromote, rowToInsert,colToInsert):
    if rowToInsert==len(companyList)-1:
        #"fire people at the bottom rank if demotion happens and replace the bottom ten percent with a uniformly random selection of people across the different categories.
        index=0 #pos within each sublist
        for i in range(len(companyList[rowToInsert])):
            companyList[rowToInsert][index]=random.randrange(0,100)
            index+=1 #increment pos by 1
    if rowToInsert<len(companyList)-1 and colToInsert<len(companyList[0]):#this if statment demotes by one rank
        copyOfCompany=copy.deepcopy(companyList)
        copyOfCompany[rowToInsert][colToInsert]= max(copyOfCompany[rowToInsert][colToInsert]-numToPromote,0)
        copyOfCompany[rowToInsert+1][colToInsert]=max(copyOfCompany[rowToInsert+1][colToInsert]+numToPromote,0)
        return copyOfCompany
    return companyList

def Simulate(numGen, biasDict, companyList):
    ranNum=0
    for i in range(numGen):#run through x number of generations
        biasList= ApplyBias(companyList,biasDict)#get a bias list
        for j in range(len(biasList)):#go through the bias list
            num=FindTenPercent(biasList[j])#figure out the ten percent
            for value in range(num):#randomly promote or demote people based on the number generated 
                ranNum=random.randrange(0,100)
                if ranNum%2==0:
                    companyList=Promotion(biasList,num,j,random.randrange(0,len(biasList[j])))
                else:
                    companyList=DeMotion(biasList,num,j,random.randrange(0,len(biasList[j])))

    return companyList
    

def OutPut(compayList, companyName):#output the list generated 
    currentLetter='A'
    print(companyName)
    for i in range(len(companyList)):
        currentLetter='A'
        for j in range(len(companyList[i])):
            print(f"{currentLetter}: {companyList[i][j]} ",end="")
            currentLetter=chr(ord(currentLetter)+1)
        print()

#appy bias generates a random bias between a set min and max
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
        
            biasMin=defaultMin-abs(biasDict[currentKey])#generate the bias min
            biasMax=defaultMax+biasDict[currentKey]#generate the bias max
            num=random.randrange(biasMin,biasMax)#generate a random number between [biasmin,biasmax]
            temp.append(num)#append a num to a temp list
            
            if index==size:#if index is == to size reset the index and append the temp list to the bias
                index=0
                currentKey='A'
                biasList.append(copy.deepcopy(temp))
                temp.clear()

            else:#incremenent the index and the key
                index+=1
                currentKey=chr(ord(currentKey)+1)

    return biasList

def readFile(): #read in first 2 lines, assign the company name and number of generations to variables. Then read in bias, and then remaining lines
    companyList=[]
    fileName= input("Please enter a file name: ")
    companyTxt=open(fileName,"r")
    companyName=companyTxt.readline()
    numGen=companyTxt.readline()

    bias=json.loads(companyTxt.readline())
    for x in companyTxt:#convert remaining lines of json to dictionary
        companyList.append(list(json.loads(x).values()))
    companyTxt.close()
    return (companyList,bias,companyName,numGen)#return a tuple of values 

readFile()
companyList,bias,name,gen=readFile()
companyList=Simulate(int(gen),bias,companyList)
OutPut(companyList,name)
