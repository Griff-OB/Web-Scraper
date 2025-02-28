# Web Scraper

This Python script fetches content from a given URL, parses it to extract H2 headlines, and saves the extracted data to a CSV or JSON file.

## Functionality

The script performs the following tasks:

1.  **Fetches Content:** It retrieves the HTML content of a specified URL using the `requests` library. It includes headers to mimic a browser request, which can help avoid being blocked by some websites.
2.  **Parses HTML:** It uses `BeautifulSoup` to parse the HTML content and extract all H2 headlines.
3.  **Saves Data:** It saves the extracted headlines to a file. The output format can be either CSV or JSON, specified by the user.

## Dependencies

-   requests
-   beautifulsoup4

You can install these dependencies using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

The script is currently configured to scrape the following URL: `https://club.ministryoftesting.com/t/my-collection-of-dummy-sites-practical-testing-for-beginners/76939`

It saves the output to `output.csv` in CSV format.

To run the script, execute the following command in the terminal:

```bash
python scraper.py
```

You can modify the `url`, `output_filename`, and `output_format` variables within the `if __name__ == "__main__":` block to scrape a different URL or change the output file/format.

```python
if __name__ == "__main__":
    url = "https://club.ministryoftesting.com/t/my-collection-of-dummy-sites-practical-testing-for-beginners/76939"  # Change this to your target URL
    output_filename = "output.csv"  # Change this to your desired output filename
    output_format = "csv"  # Change this to 'json' for JSON output
    main(url, output_filename, output_format)

```

## Error Handling

-   The script includes error handling for fetching the URL. If there's an issue with the request (e.g., network error, invalid URL), it prints an error message.
-   It also includes error handling for saving the data to the output file.

## Notes

-   The parsing logic in `parse_content` is specific to extracting H2 headlines. If you want to extract different elements or data, you'll need to modify this function accordingly.
-   Web scraping can be fragile. Changes to the target website's structure may break the scraper, requiring updates to the parsing logic.
