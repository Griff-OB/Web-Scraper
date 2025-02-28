import requests
from bs4 import BeautifulSoup
import csv
import json

def fetch_content(url):
    """Fetches the content of a given URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def parse_content(html_content):
    """Parses the fetched HTML content.

    This is a placeholder for the actual parsing logic, which will depend on
    the structure of the target website.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract all h2 headlines
    data = []
    for headline in soup.find_all('h2'):
        data.append({'headline': headline.text.strip()})

    return data

def save_data(data, filename, output_format='csv'):
    """Saves the parsed data to a file (CSV or JSON)."""
    if not data:
        print("No data to save.")
        return

    try:
        if output_format == 'csv':
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        elif output_format == 'json':
            with open(filename, 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
        else:
            print("Invalid output format. Choose 'csv' or 'json'.")
    except Exception as e:
        print(f"Error saving data to {filename}: {e}")

def main(url, output_filename, output_format):
    html_content = fetch_content(url)
    if html_content:
        parsed_data = parse_content(html_content)
        if parsed_data:
            save_data(parsed_data, output_filename, output_format)

if __name__ == "__main__":
    url = "https://club.ministryoftesting.com/t/my-collection-of-dummy-sites-practical-testing-for-beginners/76939"
    output_filename = "output.csv"
    output_format = "csv"
    main(url, output_filename, output_format)
