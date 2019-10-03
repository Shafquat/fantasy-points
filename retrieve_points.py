__author__ = "Shafquat Arefeen"

import yffpy
from yffpy.query import YahooFantasyFootballQuery
import json
import openpyxl
from datetime import date

# Function that pulls data from Yahoo's Fantasy API and returns a sorted list of tuples with (team_id,current points)
def pull_data(season,league_id,game_id,game_code,auth_dir):
	# Query yffpy to get data
	yahoo_query = YahooFantasyFootballQuery(auth_dir, league_id, game_id=game_id, game_code=game_code, offline=False)
	
	# Get standings data to get the points for the day
	standings_data = yahoo_query.get_league_standings()
	
	# Convert Standings Object to json
	parsed_json = (json.loads(str(standings_data)))
	
	# Initialize a list that can store the data
	team_list = []
	# Iterate over the Standings json to get teamids and their respective points
	for team in parsed_json['teams']:
		team_list.append((int(team['team']['team_id']),team['team']['team_standings']['points_for']))
		
	# Sort the team list by the team id
	team_list = sorted(team_list)
	
	return team_list


# Function that takes in a sorted list of tuples with (team_id,current points) and puts it in an excel sheet
def write_to_sheet(working_dir,excel_file_name,team_list):

	# open file and go to active sheet
	book = openpyxl.load_workbook(working_dir+excel_file_name)
	sheet = book.active
	
	# Create a list with the first column being the date and the following columns being the points for each respective team
	new_excel_row = []
	new_excel_row.append(date.today().strftime("%d/%m/%Y"))

	for team in team_list:
		new_excel_row.append(team[1])
	
	# Add new row to sheet and save the file	
	sheet.append(new_excel_row)
	book.save(working_dir+excel_file_name)

	return "Inserted new row in " + excel_file_name + " for date: " + date.today().strftime("%d/%m/%Y")
	
if __name__ == "__main__":
	league_id = '43832' # put your real league id here
	game_id = "396" # put the game id here (game id's reflect the type of sport and the year)
	game_code = "nhl" # put the game code here
	season = "2019" # put the year of the current fantasy season
	auth_dir = 'X:/yffpy-batch/' # put the location where you are storing the client_id/secret
	working_dir = 'X:/yffpy-batch/fantasy-points/' # put the location where you want excel file to be saved
	excel_file_name = 'Points.xlsx' # Name your file after you set up the headers
	
	team_list_today = pull_data(season,league_id,game_id,game_code,auth_dir)
	write_to_sheet(working_dir,excel_file_name,team_list_today)