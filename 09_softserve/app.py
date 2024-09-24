'''
Jayden Zhang, Margie Cao, Ziyad Hamed
SoftDev
K09 -- Softserve -- Using the random occupation from csv file and returning it through the use of the Flask import.
2024-09-20
time spent: 1 hours
'''

from flask import Flask # imports the flask command
import csv
import random

with open('occupations.csv', newline='') as csvfile: # reads the csv file using python's csv import
    occupations = csv.reader(csvfile)
    dict = {} # initatizes a new dictionary
    for row in occupations:
        if (row[0] != 'Job Class') and (row[0] != 'Total'): # removes the first and last keys
            dict.update({row[0]:float(row[1])}) # updates the dictionary with the occupations as keys and the percentage as values.
    
app = Flask(__name__) ## initalizes the flask application
@app.route("/") # routes using the '/' directory
    
def randomSelection(): # function for choosing a random number with a weighted percentage
    x = random.uniform(0.0,99.8)
    for key, value in dict.items():
        x = x - value # each key has a range and this subtracts until it is chosen
        if x <= 0:
            return key
            break

app.run()
