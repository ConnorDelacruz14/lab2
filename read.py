from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple

def readFile(csv_file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content
        
        Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    # TODO: Complete the function
    sport_club_content = []

    with csv_file.open() as file:
        csv_reader = csv.reader(file)
        good_file_lines = 0
        for i, row in enumerate(csv_reader):
            if len(row) == 4 and i > 0:
                sport_club_content.append((row[0], row[1], row[2]))
                good_file_lines += 1
            elif len(row) < 4:
                good_file_lines = 0
                raise ValueError
                continue

    return sport_club_content


def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the number of good files and good lines read. 
    Create a new file called "error_log.txt" in the current working directory containing the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """
    # TODO: Complete the function
    sport_clubs = []
    error_file_names = []
    good_files_read = 0
    
    global good_lines_read
    good_lines_read = 0
    
    file_path = Path("").glob('*.csv')
    for file_name in file_path:
        if file_name.name != "survey_database.csv":
            #good file read
            try:
                club_info = readFile(file_name)
                new_club = SportClub(club_info[0], club_info[1], club_info[2], 0)
                sport_clubs.append(new_club)
                good_files_read += 1
            #bad file read
            except:
                error_file_names.append(file_name.name)

    #Create report and error text files
    report = open('report.txt', 'w')
    report.write(f'Number of files read: {good_files_read}\n')
    report.write(f'Number of lines read: {good_lines_read}\n')

    error = open('error_log.txt', 'w')
    for name in error_file_names:
        error.write(f'{name}\n')

    report.close()
    error.close()
    
    return sport_clubs
