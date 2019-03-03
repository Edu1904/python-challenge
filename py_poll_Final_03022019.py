import csv
import os

total_profit=0

with open('election_data.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
    Voter_IDs = []
    Countys = []
    Candidates = []
    
    header=next(readcsv)
#    header=header.split(',')

#read the csv file and create separate list for 
#each variable (voter_id,countys and candidates)   
    for row in readcsv:
        Voter_ID = row[0]
        County = row[1]
        Candidate= row[2]

        Voter_IDs.append(Voter_ID)
        Countys.append(County)
        Candidates.append(Candidate)
    
#def a function to count number of time each item in list appear
def countCandidates (lst):
    elems={}
    for item in lst:
        if item in elems.keys():
            elems[item] +=1
        else:
            elems[item] = 1
    return elems

#count the number of time each candidate shows in candidates list, 
#and create a dictionary
votes_per_candidate ={}           
votes_per_candidate = countCandidates(Candidates)
#print (votes_per_candidate)

#Calculate the number of vote cast
total_votes=0
total_votes = sum(votes_per_candidate.values())
#print (total_votes)

#calculate the maximun number of votes to determine the winner
maxvote= max(votes_per_candidate.values())

for key, value in votes_per_candidate.items():

    if value == maxvote:
        winner_name=(key)
        winner_votes=(value)
        winner_data=(key,value)

votes_per_candidate_lenght=len(votes_per_candidate.keys())
#print(votes_per_candidate)
#print(votes_per_candidate_lenght)

#print the output for all files show the elections results
print (' ')
print (' ')
print ('Election Results')
print (' ')
print ('----------------------------- ')
print (' ')
print ('Total Votes:  '+ str(total_votes))
print (' ')
print ('----------------------------- ')
print (' ')
for key,value in votes_per_candidate.items():
    print((key) + ':  ' +str(("%.3f" % round((value)*100/total_votes))) +'%'+ '  ('+str(value) +')')
print (' ')
print ('----------------------------- ')
print (' ')
print ('winner: '+str(winner_name))
print (' ')

#create one string to make it easier to append to the text file
total_v=('Total Votes:    '+ str(total_votes))
winner_print=('Winner: '+str(winner_name))

#create the text file with the same data that print from the script
f1= open('file_test.txt','w')
f1.write(' \n')
f1.write(' \n')
f1.write('Election Results\n')
f1.write(' \n')
f1.write('----------------------------- \n')
f1.write(' \n')
f1.write(total_v)
f1.close()

f1= open('file_test.txt','a')
f1.write(' \n')
f1.write(' \n')
f1.write('----------------------------- \n')
f1.write(' \n')
f1.close()
for key,value in votes_per_candidate.items():
    output=((key) + ':  ' +str(("%.3f" % round((value)*100/total_votes))) +'%'+ '  ('+str(value) +')')
    f1= open('file_test.txt','a')
    f1.write(output)
    f1.write(' \n')
    f1.close()
f1= open('file_test.txt','a')
f1.write(' \n')
f1.write('----------------------------- \n')
f1.write(' \n')
f1.write(winner_print)
f1.close()