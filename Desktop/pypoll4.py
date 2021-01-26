import os

import csv


csv_path = os.path.join('Resources', 'election_data.csv')

voter_ids = []
counties = []
candidates = []
spacer = ("---------------------")
vote_count = []
k_votes = []
c_votes = []
l_votes = []
o_votes = []



#Open and read csv
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Read the header row
    csv_header = next(csv_file)
    
    # append create lists and start formulas
    for row in csv_reader:
        voter_ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])
                
        #    The total number of votes cast
        vote_count = len(voter_ids)

        # tried really hard to iterate thru names and define function here...couldn't get it
        k_votes = candidates.count("Khan")
        # c_votes = candidates.count("Correy")
        # l_votes = candidates.count("Li")
        # o_votes = candidates.count("O'Tooley")

        # k_calc = (int(k_votes) / int(vote_count)) * 100
        # # c_calc = (c_votes / vote_count) * 100
        # # l_calc = (l_votes / vote_count) * 100
        # # o_calc = (o_votes / vote_count) * 100        

       
        
# print all values to the terminal
print("Election Results")
print(spacer)
print(f"Total Votes: {vote_count}")
print(spacer)
print(k_calc)




#export results to a text file
output_path = os.path.join("new.csv")

with open(output_path, 'w') as csvfile:

    # Initialize csv.writer and write to file new
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"]) 
    csvwriter.writerow([spacer])
    csvwriter.writerow([f"Total Votes: %5d " % (int(vote_count))])
    csvwriter.writerow([spacer])
    
    
