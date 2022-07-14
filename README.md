Purpose of this Lab:

The main objective of this lab is to get you familiar with the libraries discussed in the class (PathLib and the CSV library), and get you comfortable using abstractions and standard coding formats.

Introduction to the Lab :

A research team was administering a survey of random people to get their favorite team in their favorite sport. The survey was taking down this information in comma separate files (.csv files) and saving these files in a single directory. 

Each CSV file that is stored by the collectors has 3 columns with these self-identifying column headers:

"City", "Team Name", "Sport"

Here is an example of a file:

EXCEL_jnLraHkv75.png 

Lab Overview:

Your job is to create a program that will do the following:

Consolidate all the information from the csv files they have provided into a single csv file called "survey_database.csv"
Create a summary of the collected data in a file called "report.txt”
Create an error log of the collected data in a file called "error_log.txt"
The following are their detailed requirements for the program:

Survey Database
They want the program to be able to search, find and read all the .csv files in the current working directory to create the "survey_database.csv" file in the current working directory.
The CSV should contain the following information (defined in self-identifying column header names):
"City" , "Team Name",  "Sport",  "Number of Times Picked"
The rows following that header should contain that information for the top 3 most picked teams in each sport
"picked" in this context is the team appearing once in the CSV files
The ranking of the team is defined by the inverse of the times they were picked and their alphabetic Team Name. In other words, teams that appear more often in the read csv files are at the top. In the event of ties in their count, their names are used to resolve the ties.
Example of a survey_database.csv file:

EXCEL_VMB9fmhAEQ.png 

Report
They want a new report created every time they run the program. The following is the content of the summary report in a "report.txt" file created in the current working directory. The report is simply a text file with the following information:
Number of files read: {num good files read}
Number of lines read: {num lines read in good files read}

Example of a report.txt file:

notepad++_bTJj3ifdBC.png 

Error log
They want a new error log created every time they run the program. This error log simply has the name of the files that contain errors, on their separate line. An error could be missing strings or empty strings. Create a file called "error_log.txt" in the current working directory with that information. 
Example error_log.txt file:

notepad++_pesgkQ5tUO.png 

Important details:

If a file has an error (i.e it is missing one of the 3 fields it should have (City, Team Name or Sport)), it file is considered corrupted and it will not count AT ALL. In other words, if you read 5 rows already then you encounter an empty filed on the sixth, you will discard those 5 rows with the whole file as well.
Every line, including the last, in report.txt and error_log.txt ends in a new line character.
If there are no error files encountered, simply create the error_log.txt file with nothing in it.
If there are less than 3 teams in a sport, simply output the teams that you do have.
Every CSV file you read will have an header, and the survery_database.csv file you create must also have a header.
The order of sports in survey_database.csv does not matter.
Lab 2 Starter Code Download Download Lab 2 Starter Code Download

Lab 2 Sample Test Files:

junesurvey.csv Download junesurvey.csv

marchsurvey.csv Download marchsurvey.csv

You will get 4 files  (main.py, read.py, write.py and sportclub.py). The instructions here are also present in the files themselves:

main.py: Do not change anything in main.py. Your code must run with the main given to you, and will be run the same way by the autograder.
sportclub.py: Contains the class SportClub. Read through the class to understand how it works, and complete the following functions:
__eq__(other): Function to check if the current instance of the class (self) is equal to another object. This can be useful in sortSport(sport).
__lt__(other): Function to check if the current instance of the class (self) is less than another object. This can also be useful in sortSport(sport).
read.py: Contains two functions you need to complete:
readFile(file): Function to read one .csv file. Returns a list of tuples of three fields (City, Name and Sport). The output should not include raw input formatting like commas, the header, etc. Raises ValueError if it finds that the file it's reading is an error file.
readAllFiles(): Function to read all .csv files in the current working directory. Returns a list of SportClub objects. This function should call the readFile(file), and gather its output into a list of unique SportClub objects. Each of these unique SportClub objects will store the identifying information of the team, and how many times the participants have picked the team. This is the function that will also produce the report.txt and error_log.txt files you read about.
write.py: Contains three functions you need to complete:
separateSports(all_clubs): Function to separate a list of all sport clubs by their sport. Takes as input the list of all clubs seen, and returns an iterable of lists of sport clubs. Each of those lists only contain sport clubs that play the same sport. The order of the sports does not matter.
sortSport(sport): Function to sort a list of SportClub objects by their counts and name. Takes a list of SportClub objects of the same sport as an argument. Returns a list of the sorted SportClub objects.
Hint: make use of the standard __lt__ and __eq__ functions you defined earlier by calling standard Python sorting functions. You can read how to do this and sort by multiple keys by reading the documentation provided in the hints of those functions.
outputSports(sorted_sports): Function to create the survey_database.csv file output file and output the top 3 most picked teams of each sport. Takes an iterable of lists of sorted SportClub objects of the as an argument.
