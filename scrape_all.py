import csv
import math
import time

import agent
from id_get import get_location_id
from ScraperTools import tools

list_of_zips = []
with open("zips_might_work.csv") as lines:
    line_list = lines.readlines()
    for zip_line in line_list:
        if zip_line == "\n":
            continue
        else:
            list_of_zips.append(zip_line.replace("\n", ""))
amount_of_zips = len(list_of_zips)

#
#
# Write header first
#
#Check for duplicates
#
#

def scrape_zip(zip_to_do, writer):
    location_id = get_location_id(zip_to_do)
    if location_id is not False:
        try:
            parent_soup = tools.get_soup(f"https://www.compass.com/agents/search-results/?coverageLocationId={location_id}")
            agent_count = tools.get_elem(parent_soup, "div", "class", "searchResults-count").get_text().replace("       ", "").replace("\n", "").split(" ")[1]
            page_count = math.ceil(int(agent_count) / 50)
            count = 0
            for i in range(1, page_count + 1):
                main_url = f"https://www.compass.com/agents/search-results/?coverageLocationId={location_id}&page={i}"
                soup = tools.get_soup(main_url)
                agents_a_s = [x for x in tools.get_elems(soup, "a", "class", "agentCard-imageWrapper")]
                for agents_a in agents_a_s:
                    count += 1
                    #agent_objs[count] = agent.Agent(f"https://www.compass.com{agents_a.attrs['href']}")
                    agent_scraped = agent.Agent(f"https://www.compass.com{agents_a.attrs['href']}", zip_to_do)
                    writer.writerow(agent_scraped.profile)
                    print(f"{count} / {agent_count}")            
            return [f'{zip_to_do} with {agent_count} Records']
        except Exception as ex:
            #print(ex)
            return f"No agents in {zip_to_do}"
    else:
        return f"No agents in {zip_to_do}"

zip_code_count = 0

with open(f'all-agents.csv', 'a') as file:
    fieldnames = ["zip", "name", "email", "phone", "facebook", "instagram", "url"] # linkedin
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for zip_code in list_of_zips:
        new_zip_code = zip_code
        zip_task = scrape_zip(new_zip_code, writer)
        zip_code_count += 1
        print(f"{zip_task}. {zip_code_count} zips / {amount_of_zips} possible")
