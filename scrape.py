import csv
import math
import time

import agent
from id_get import get_location_id
from ScraperTools import tools

zip_to_search = input(" Please enter a zip to search ie 10010: ")
location_id = get_location_id(zip_to_search)
parent_soup = tools.get_soup(f"https://www.compass.com/agents/search-results/?coverageLocationId={location_id}")
agent_count = tools.get_elem(parent_soup, "div", "class", "searchResults-count").get_text().replace("       ", "").replace("\n", "").split(" ")[1]
page_count = math.ceil(int(agent_count) / 50)
with open(f'{location_id}-agents.csv', 'w') as file:
    fieldnames = ["zip", "name", "email", "phone", "facebook", "instagram", "url"] # linkedin
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    count = 0
    for i in range(1, page_count + 1):
        main_url = f"https://www.compass.com/agents/search-results/?coverageLocationId={location_id}&page={i}"
        soup = tools.get_soup(main_url)
        agents_a_s = [x for x in tools.get_elems(soup, "a", "class", "agentCard-imageWrapper")]
        for agents_a in agents_a_s:
            count += 1
            #agent_objs[count] = agent.Agent(f"https://www.compass.com{agents_a.attrs['href']}")
            agent_scraped = agent.Agent(f"https://www.compass.com{agents_a.attrs['href']}", zip_to_search)
            writer.writerow(agent_scraped.profile)
            print(f"{count} / {agent_count}")

print(f'{location_id}-agents.csv finished with {agent_count} Records')
