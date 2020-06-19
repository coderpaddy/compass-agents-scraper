# compass agents scraper
 Scrape agent info from compass.com, by Zip Code

# Install
 ```
 git clone https://github.com/coderpaddy/compass-agents-scraper
 cd compass-agents-scraper
 git submodule update --recursive --remote
 # you may want to create a virtual environment
 # python -m venv env
 pip install -r requirements.txt
 ```

# Usage
 * Single Zip Code
    ```
    python scrape.py

    >>Please enter a zip to search ie 10010:

    >> 10010
    ```

    Program will count total agents, and count through progress

    CSV will be saved as {zip_code}-agents.csv

 * All zip codes
    ```
    python scrape_all.py
    >> all_agents.csv
    ```
    
    clean when finished if you want (remove duplicates and placeholder urls)
    ```
    python clean.py
    >> all_agents_cleaned.csv
    ```