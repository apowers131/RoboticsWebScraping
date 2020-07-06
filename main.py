from requests_html import HTMLSession
from lxml import html
import json
def main():
    match_scores = (25, 25, 25, 5, 25, 25, 0, 25, 25, 0)
    average = sum(match_scores) / len(match_scores)
    print (average)
    pass

if __name__ == "__main__":
    main()
