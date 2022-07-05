# -*- coding: utf-8 -*-
import bs4
import requests
import json

def save_ids(url:str):
    """Takes url as string argument, saves dates and ids to a file named ids.json"""
    webpage = requests.get(url)
    soup = bs4.BeautifulSoup(webpage.text, features="lxml")
    
    out_list = []
    for ul in soup.find_all("ul"):
        if "CC-MAIN" in ul.text:
            for idx, li in enumerate(ul.findChildren('li')):
                if "CC-MAIN" in li.text:
                    date_id = li.text.split("CC-MAIN-")[1].split("/")[0].split(" ")[0]
                    out_list.append(date_id)
            break
        
    print(out_list)
    with open('ids.json', 'w') as f:
        json.dump(out_list, f)    

url = "https://commoncrawl.org/the-data/get-started/"
save_ids(url)
