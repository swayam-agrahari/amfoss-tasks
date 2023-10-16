import requests
from bs4 import BeautifulSoup

def get_cricket_data():
    # URL of the webpage
    url = "https://www.espncricinfo.com/live-cricket-score"

    # Send an HTTP GET request to fetch the webpage content
    response = requests.get(url)

    # Initialize variables to store information
    team1 = ""
    team2 = ""
    status = ""

    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the specific div element
        specific_div = soup.find('div', class_='ds-px-4 ds-py-3')

        if specific_div:
            # Extract team names
            team_names_div = specific_div.find_all('div', class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')
            
            if len(team_names_div) == 2:
                # Team 1
                team1_elem = team_names_div[0].find('div', class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')
                if team1_elem:
                    team1 = team1_elem.find('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate !ds-text-typo-mid3').text.strip()

                # Team 2
                team2_elem = team_names_div[1].find('div', class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')
                if team2_elem:
                    team2 = team2_elem.find('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate').text.strip()

            # Extract status
            status_elem = specific_div.find('p', class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')
            if status_elem:
                status = status_elem.text.strip()

    cricket_data = {
        "team1": team1,
        "team2": team2,
        "status": status,
    }

    return cricket_data
