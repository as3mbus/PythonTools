import requests
import argparse
from bs4 import BeautifulSoup

def extract_open_graph(url):
    # Fetch the webpage content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all meta tags with property starting with 'og:'
    og_tags = soup.find_all('meta', property=lambda x: x and x.startswith('og:'))

    # Extract Open Graph parameters
    open_graph_params = {}
    for tag in og_tags:
        property_name = tag['property'][3:]  # Remove 'og:' prefix
        content = tag.get('content', '')
        open_graph_params[property_name] = content

    return open_graph_params

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Extract Open Graph parameters from a webpage.')
    parser.add_argument('url', type=str, help='URL of the webpage to extract Open Graph parameters from')
    args = parser.parse_args()

    url = args.url
    img_style = 'max-width: 100%; max-height: 100px; float: right; clear: right; margin-left: 1rem;margin-bottom: 2px;margin-top: 2px;'
    open_graph_params = extract_open_graph(url)
    for key, value in open_graph_params.items():
        print(f'{key}: {value}')



    print(f'> [!cite] [{open_graph_params.get("title", "")}]({url})')
    print(f'> <img src="{open_graph_params.get("image", "")}" alt="Image" style="{img_style}"/> {open_graph_params.get("description", "")}')