import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import locale
import json
import os



BASE_URL = "https://www.skyscanner.fr/transport/vols-de/"

def import_countries_codes():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, '..', 'data', f"africa-countries-codes.json")
    with open(json_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def get_site_content():
    # url = f"{url_base}{competition}"
    url = f"https://www.skyscanner.fr/transport/vols-de/pari/?adultsv2=2&cabinclass=economy&childrenv2=10%7C11&ref=home&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=2408&iym=2408"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
    response = requests.get(url, headers=headers)
    print(response)
    html = response.content
    site_content = BeautifulSoup(html, 'html.parser')
    return site_content
    
country = import_countries_codes()["Tanzanie"]
get_site_content()