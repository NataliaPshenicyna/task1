import requests
from bs4 import BeautifulSoup
import pytest
import re

def get_table_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    rows = table.find_all('tr')[1:]
    data = []
    for row in rows:
        cols = row.find_all('td')
        website = re.sub(r'\[\d+]', '', cols[0].text.strip())
        popularity= int(re.sub(r'\D', '', cols[1].text.strip().replace(',', '')))
        frontend = cols[2].text.strip()
        backend = re.sub(r'\[\d+]', '', cols[3].text.strip())
        data.append((website, popularity, frontend, backend))
    return data



@pytest.mark.parametrize("threshold_str",
                         ["10 ** 7", "1.5 * 10 ** 7", "5 * 10 ** 7", "10 ** 8", "5 * 10 ** 8", "10 ** 9", "1.5 * 10 ** 9"])
def test_website_popularity(threshold_str):
    threshold = int(eval(threshold_str))
    url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
    websites = get_table_data(url)
    errors = []
    for website, popularity, frontend, backend in websites:
        if popularity < threshold:
            error_msg = f"{website} (Frontend:{frontend}|Backend:{backend}) has {popularity} unique visitors per month. (Expected more than {threshold}))\n"
            errors.append(error_msg)
    assert not errors, "\n".join(errors)