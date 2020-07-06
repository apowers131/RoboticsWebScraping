from requests_html import HTMLSession
from lxml import html
import json

url = 'https://www.thebluealliance.com/"
data_json_path = "/Users/Kitsune/Src/RoboticsWebScraping/site_data.json"

def main():
    team_num = input("What team number do you want to find the average endgame score of?")
    url += team_num
    session = HTMLSession()
    page = session.get(url)
    
    
    # match_scores = [25, 25, 25, 5, 25, 25, 0, 25, 25, 0]
    # average = sum(match_scores) / len(match_scores)
    # print (average)
    pass

if __name__ == "__main__":
    main()
