# -*- coding: utf-8 -*-
"""
Created on 6  Oct 6th


Brett Gedvilas and David Ward
CSCI 5451
Last Updated: 10/6/2017

Rod Cutting Educational Program
"""

import time
import random

# Computes the Solution to a Rod Cutting problem of given length and an array of prices
# Note: Introduction to Algorithms Ch.15 Dynamic Programming for reference.
def bottomUpCutRod(prices, length, printSteps):
    #Populate the array with hashmarks indicated values not calculated yet
    revenueArray = fillInRevenueArray(length)
    #Array that indicates the optimal cuts for printing to the screen
    cutsArray = fillInCutsArray(length)

    if(printSteps):
        print("\nSolving via optimal sub-problems:")
        print("----------------------------------")
    else:
        print("\nSolution:")
        print("----------")

    #Loop through all sub-problems
    for j in range(1, length + 1):
        subPrice = 0
        for i in range(0,j):
            if subPrice < (prices[i] + revenueArray[j-i-1]):
                subPrice = prices[i] + revenueArray[j-i-1]
                cutsArray[j] = i+1
        revenueArray[j] = subPrice

        #If user specified to show steps
        if(printSteps):
            if(j == length):
                print("\nSolution:")
                print("----------")
            printTable(length, revenueArray)

            #Sleep to allow the print-out to be spaced
            time.sleep(2)

    printCutNumbers(cutsArray, length)
    return revenueArray

# Computes the Solution to a Rod Cutting problem of given length and an array of prices
# taking into acccount the a unit cost of $1/cut
def bottomUpCutRodNetRev(prices, length, printSteps):
    #Populate the array with hashmarks indicated values not calculated yet
    revenueArray = fillInRevenueArray(length)
    #Array that indicates the optimal cuts for printing to the screen
    cutsArray = fillInCutsArray(length)

    if(printSteps):
        print("\nSolving via optimal sub-problems:")
        print("----------------------------------")
    else:
        print("\nSolution:")
        print("----------")

    #Loop through all sub-problems
    for j in range(1, length + 1):
        subPrice = 0
        for i in range(0,j):
            #Determine the cost per sub-problem ($Cost/cut)
            if(i == j-1):
                cost = 0
            else:
                cost = 1

            #Determine if this net-profit is greater than previously solved sub-problems
            if subPrice < (prices[i] + revenueArray[j-i-1] - cost):
                subPrice = prices[i] + revenueArray[j-i-1] - cost
                cutsArray[j] = i+1
        revenueArray[j] = subPrice

        #If user specified to show steps
        if(printSteps):
            if(j == length):
                print("\nSolution:")
                print("----------")
            printTable(length, revenueArray)

            #Sleep to allow the print-out to be spaced
            time.sleep(2)

    printCutNumbers(cutsArray, length)
    return revenueArray

def optimalRevLoop(menu_option, prices, length, printSteps):
    # Ensure valid input from user
    while (True):
        try:
            menu_option = int(input())
        except ValueError:
            print("\nIncorrect input format. Please try again.")
        else:
            break

    if menu_option == 1:
        printPriceTable(length, prices)
        if not printSteps:
            printTable(length, bottomUpCutRodNetRev(prices, length, printSteps))
        else:
            bottomUpCutRodNetRev(prices, length, printSteps)
    else:
        return


def printCutNumbers(cutsArray, length):
    cutString = "\nThe optimal cuts are:"
    while (length > 0):
        cutString += " " + str(cutsArray[length]) + ","
        length = length - cutsArray[length]
    if(len(cutString) > 0):
        newString = cutString[:len(cutString) -1]
    print(newString)

def printTable(length, revenueArray):
    tableHeader = "\nlength   i | "
    values = "revenue  r | "

    #start with 11 spaces due to the header
    totalLength = 11
    for i in range(length+1):
        indexConvert = str(i)
        valueConvert = str(revenueArray[i])
        indexLength = len(indexConvert)
        valueLength = len(valueConvert)
        if(indexLength < valueLength):
            for j in range(valueLength - indexLength):
                indexConvert += " "
        elif(valueLength < indexLength):
            for j in range(indexLength - valueLength):
                valueConvert += " "
            valueLength = len(valueConvert)
        tableHeader += indexConvert + " "
        values += valueConvert + " "

        #increment the total lenght for drawing hash marks
        totalLength += valueLength + 1

    #Print the table display of the sub-problem results
    print(tableHeader)
    printHashMarks(totalLength +  1)
    print(values)

def printPriceTable(length, prices):
    tableHeader = "\nlength i | "
    values = "price  p | "

    #start with 11 spaces due to the header
    totalLength = 11
    for i in range(0, length):
        #Extract lengths of number strings for formatting the table
        indexConvert = str(i+1)
        valueConvert = str(prices[i])
        indexLength = len(indexConvert)
        valueLength = len(valueConvert)
        if(indexLength < valueLength):
            for j in range(valueLength - indexLength):
                indexConvert += " "
        tableHeader += indexConvert + " "
        values += valueConvert + " "

        #increment the total lenght for drawing hash marks
        totalLength += valueLength + 1

    #Print the table display of the sub-problem results
    print(tableHeader)
    printHashMarks(totalLength +  1)
    print(values)


def printHashMarks(number):
    hashMarks = ""
    for i in range(number):
        hashMarks += "-"
    print(hashMarks)

def fillInRevenueArray(length):

    revenueArray = [0]
    for i in range(1, length + 1):
        revenueArray += ["-"]

    return revenueArray

def fillInCutsArray(length):
    cutsArray = [0]
    for i in range(1, length + 1):
        cutsArray += [0]

    return cutsArray

def optimalRevPrompt():
    print("\nView solution to problem considering an incurred cost/cut?")
    print("------------------------------------------------------------")
    print("1. Yes")
    print("2. No")

def main():


    print("\nRod Cutting Problem: A Dynamic Programming Illustration\nBrett Gedvilas and David Ward")
    menu = True

    # keep looping until user chooses to quit
    while menu:
        print("\nInput rod integer length or type 0 to quit: ")

        #Ensure valid input from user
        while(True):
            try:
                length = int(input())
            except ValueError:
                print("\nIncorrect input format. Please try again.")
            else:
                break

        #Ensure value from user is within problem constraints
        if(length == 0):
            break;
        while(length > 40):
            print("\nRod length must be less than or equal to 40. Please try again: ")
            length = int(input())

        print("\nType the number of solution form:")
        print("-------------------")
        print("1. Step-by-step")
        print("2. Solve")
        print("0. Quit")

        # Ensure valid input from user
        while (True):
            try:
                menu_option2 = int(input())
            except ValueError:
                print("\nIncorrect input format. Please try again.")
            else:
                break

        #Construct an example problem with random price input
        prices = [1]
        randomPrice = 1
        for i in range(1,length):
            if i <= 5:
                randomPrice += random.randint(0, 5)
            elif i <=10:
                randomPrice += random.randint(0, 3)
            else:
                randomPrice += random.randint(0, 2)
            prices += [randomPrice]

        if menu_option2 == 1:
            print("\nThe prices per length i: ")
            printPriceTable(length, prices)
            print("\nTry to solve on your own. Press ENTER to show steps.")
            input()
            bottomUpCutRod(prices, length, True)
            optimalRevPrompt()
            optimalRevLoop(menu_option2, prices, length, True)

        elif menu_option2 == 2:
            print("\nThe prices per length i: ")
            printPriceTable(length, prices)
            printTable(length, bottomUpCutRod(prices, length, False))
            optimalRevPrompt()
            optimalRevLoop(menu_option2, prices, length, False)

        else:
            break



if __name__ == '__main__':
    main()
