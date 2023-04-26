#Author : Ravi Sanapala (sanapalaravi@outlook.com)
#Interview Report Generator Tool
import pandas as pd
import datetime
# Prompt the Interviewer to enter their name and the candidate's name
user_name = input("Please enter your name: ")
candidate_name = input("Please enter the candidate's name: ")
green = "\033[32m"
reset = "\033[0m"
# Print a welcome message
print(f"Thank you, {user_name}, for considering to interview {candidate_name}.")
print("The final result will be generated in the results.txt file.\n")
# Get the current date and time
now = datetime.datetime.now()
date= datetime.datetime.now().date()
# Record the start time of the interview
start_time = now
# Create a filename based on the candidate's name
filename = f"{candidate_name}_{date}.txt"

# Set the path to your Excel file
excel_file = './Interview.xlsx'
#Author : Ravi Sanapala (sanapalaravi@outlook.com)
# Read the Excel file into a dictionary of dataframes
df_dict = pd.read_excel(excel_file, sheet_name=None)

# Loop through each sheet in the dictionary
for sheet_name, df in df_dict.items():
    # Initialize counters for Yes and No answers
    yes_count = 0
    no_count = 0
    
    # Loop through each row in the dataframe
    for index, row in df.iterrows():
        # Print the question and prompt the user for an answer
        question = row['Question']
        while True:
            answer = input(f'{question} (Y/N): ').upper()
            if answer in ('Y', 'N'):
                break
            else:
                print("Invalid response. Please enter 'Y' for Yes or 'N' for No.")
        
        # Increment the Yes or No counter based on the user's answer
        if answer == 'Y':
            yes_count += 1
        elif answer == 'N':
            no_count += 1
    
    # Calculate the percentages
    total_count = yes_count + no_count
    if total_count != 0:
        yes_percent = round((yes_count / total_count) * 100, 2)
        no_percent = round((no_count / total_count) * 100, 2)
        
        # Print the results
        print('------------------')
        print(f'Skill: {sheet_name}')
        print(f'Yes: {yes_percent}%')
        print(f'No: {no_percent}%')
        print('------------------')
        
        # Write the results to a file
        with open(filename, 'a') as f:
            f.write(f'Skill: {sheet_name}\n')
            f.write(f'Correct: {yes_percent}%\n')
            f.write(f'Wrong: {no_percent}%\n')
            f.write('--------******----------\n')
    else:
        print(f"Skipping sheet {sheet_name} because there are no rows in the dataframe.")

# Calculate the interview duration and write it to the file
end_time = datetime.datetime.now()
duration = end_time - start_time
duration_seconds = round(duration.total_seconds(), 2)
duration_string = str(datetime.timedelta(seconds=duration_seconds))


# Ask the Interviewer if the candidate can be considered for further rounds
while True:
    print(f"|")
    print(f"|")
    print(f"|")
    print(f"=")
    print(f"--------------------------------------------------------AWESOME {user_name} !!!-----------------------------------------------------------------------------")
    print(f"-----------------------------------------------Couple of Questions more regarding the Final verdict-----------------------------------------------------------------------------")
    print(f"|")
    print(f"|")
    print(f"|")
    print(f"=")
    candidate_consider = input("Can the candidate be considered for further rounds? (Y/N): ").upper()
    if candidate_consider in ('Y', 'N'):
        break
    else:
        print("Invalid response. Please enter 'Y' for Yes or 'N' for No.")
#Author : Ravi Sanapala (sanapalaravi@outlook.com)
# Ask the Interviewer to give a summary of the candidate's performance in the interview
summary = input("Please provide a summary of the candidate's performance in the interview: ")
print("Thank You , The final report has been generated.")

with open(filename, 'a') as f:
    f.write(f'{user_name} interviewed {candidate_name}\n')
    f.write(f'Start time: {start_time}\n')
    f.write(f'End time: {end_time}\n')
    f.write(f'Interview duration: {duration_string}\n')
    f.write('------------------\n')
    f.write('===================\n')
    f.write(f'Candidate can be considered for further rounds: {candidate_consider}\n')
    f.write(f'Summary of candidate performance: {summary}\n')
    f.write('====================\n')
