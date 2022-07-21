from enum import unique
from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple


def readFile(csv_file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content
        
        Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    sport_club_content = []

    with csv_file.open() as file:
        rows = 0
        csv_reader = csv.reader(file)
        for i, row in enumerate(csv_reader):
            if len(row) >= 3 and i > 0:
                rows += 1
                sport_club_content.append((row[0], row[1], row[2]))
            if len(row) < 3:
                raise ValueError
            if row == "":
                raise ValueError
        if rows == 0:
            raise ValueError

    return sport_club_content



def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Returns:
        a list of unique SportClub objects with their respective counts
    """
    # TODO: Complete the function
    sport_clubs = []
    error_file_names = []
    good_files_read = 0
    good_lines_read = 0

    file_path = Path("./").glob("**/*.csv")
    for file_name in file_path:
        if file_name.name != "survey_database.csv":
            #good file read
            try:
                club_info = readFile(file_name)

                for club in club_info:
                    new_club = SportClub(club[0], club[1], club[2], 0)
                    sport_clubs.append(new_club) 
                
                good_files_read += 1
                for team in club_info:
                    good_lines_read += 1

            #bad file read
            except ValueError:
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

    # create copy list
    copy_clubs = sport_clubs
    # set of uniqe clubs 
    unique_clubs = set(sport_clubs)
    for club in unique_clubs:
        for club2 in copy_clubs:
            if club.__eq__(club2):
                club.incrementCount()
                
    return list(unique_clubs)
