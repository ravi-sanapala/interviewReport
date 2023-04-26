## Interview Report Generator

This script is designed to help interviewers generate a report on a candidate's performance in an interview. The script reads questions from an Excel file and prompts the interviewer for Yes or No answers. It then calculates the percentage of correct and incorrect answers for each skill and writes the results to a file.

### How to use the script

1. Install the required dependencies:

   ```
   pip install pandas 
   ```

2. Create an Excel file with the questions for each skill. The file should have one sheet for each skill, and each sheet should have a column called "Question" with the questions to ask.

3. Run the script:

   ```
   python interview.py
   ```

4. Enter your name and the candidate's name when prompted.

5. Answer the questions for each skill by entering Y for Yes or N for No.

6. After all the questions have been answered, the script will ask whether the candidate can be considered for further rounds. Enter Y for Yes or N for No.

7. The script will then ask for a summary of the candidate's performance in the interview.

8. The final report will be generated in a file named `{candidate_name}_{date}.txt` in the same directory as the script.

### Dependencies

- pandas

### Compatibility

The script was developed and tested using Python 3.9. It may not work with earlier versions of Python.