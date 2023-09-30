import discord
import os
from dotenv import load_dotenv
from scraper import get_cricket_data
import csv

# Load environment variables
load_dotenv()
TOKEN = 'MTE1NjI0ODUxODA4MDU5ODEyOA.GX_JHw.CdBu43HXTfgZ8Sx-m2uVsoCLmJhOvlg1ZS6vTU'

# Define the intents for your bot
intents = discord.Intents.all()
# intents.typing = True
# intents.presences = False
intents.message_content = True

# Create a Discord client with intents
client = discord.Client(intents=intents)

# List to store live scores data
live_scores_data = []

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/livescore'):
        # Get live cricket data using your scraper function
        data = get_cricket_data()

        if data:
            response = f"Team 1: {data['team1']}\nTeam 2: {data['team2']}\nStatus: {data['status']}"
        else:
            response = "No live scores available! Try again later."

        await message.channel.send(response)

    elif message.content.startswith('/generate'):
        # Generate a CSV file with live scores
        generate_live_scores_csv()
        
        # Send the generated CSV file
        with open('live_scores.csv', 'rb') as file:
            await message.channel.send("Here's the generated live scores CSV file:", file=discord.File(file, 'live_scores.csv'))

    elif message.content.startswith('/help'):
        # Provide information about available commands
        help_message = """
    Available commands:
    /livescore   : Get live cricket match data.
    /generate    : Generate a CSV file with live scores.
    /help        : Show this help message.
    """


def generate_live_scores_csv():
    # Get live cricket data using your scraper function
    data = get_cricket_data()

    if data:
        formatted_data = f"Team 1: {data['team1']}\nTeam 2: {data['team2']}\nStatus: {data['status']}"

        # Write the formatted data to a CSV file as a list
        with open('live_scores.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([formatted_data])
# Run the bot
client.run(TOKEN)