# Project Overview: What we need to retrieve
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
   #how to only view header row
    headers = next(reader)
    print(headers)
#how would you retrieve the first item from each row?
    for row in reader:
        print(row[0])


with open(file_to_save, 'w') as txt_file:
    txt_file.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")
    txt_file.close()
   
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote