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
            team_names = specific_div.find_all('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')
            if len(team_names) == 2:
                team1 = team_names[0].text.strip()
                team2 = team_names[1].text.strip()

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
