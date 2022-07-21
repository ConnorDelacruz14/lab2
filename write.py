import csv
from os import sep
from sportclub import SportClub
from typing import List, Iterable

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    """Separate a list of SportClubs into their own sports

    For example, given the list [SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA"), SportClub("LA", "Angels", "MLB")],
    return the iterable [[SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA")], [SportClub("LA", "Angels", "MLB")]]

    Args:
        all_clubs: A list of SportClubs that contain SportClubs of 1 or more sports.

    Returns:
        An iterable of lists of sportclubs that only contain clubs playing the same sport. 
    """
    sports = set([club.getSport() for club in all_clubs])
    sports_dict = {}
    for sport in sports:
        sports_dict.update({sport: []})

    for club in all_clubs:
        if club.getSport() in sports_dict.keys():
            sports_dict[club.getSport()].append(club)

    separated_sports = [sport for sport in sports_dict.values()]

    return separated_sports


def sortSport(sport: List[SportClub]) -> List[SportClub]:
    """
    For example, given the list [SportClub("Houston", "Rockets", "NBA", 80), SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)] 
    return the list [SportClub("LA", "Lakers", "NBA", 130), SportClub("LA", "Warriors", "NBA", 130), SportClub("Houston", "Rockets", "NBA", 80)] 
    """
    sorted_clubs = sorted(sport)

    return sorted_clubs

 
def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    """Create the output csv given an iterable of list of sorted clubs

    Create the csv "survey_database.csv" in the current working directory, and output the information:
    "City,Team Name,Sport,Number of Times Picked" for the top 3 teams in each sport.

    Args:
        sorted_sports: an Iterable of different sports, each already sorted correctly
    """
    # TODO: Complete the function
    with open("survey_database.csv", "w", newline="") as survey_database:
        csvwriter = csv.writer(survey_database)
        csvwriter.writerow(['City', 'Team Name', 'Sport', 'Number of Times Picked'])
        for sport in sorted_sports:
            if len(sport) < 3:
                top_rated = sport[:]
                for team in top_rated:
                    csvwriter.writerow([team.getCity(), team.getName(), team.getSport(), team.getCount()])
            else:
                top_rated = sport[:3]
                for team in top_rated:
                    csvwriter.writerow([team.getCity(), team.getName(), team.getSport(), team.getCount()])