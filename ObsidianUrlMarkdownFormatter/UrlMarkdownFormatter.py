import requests
import argparse
from bs4 import BeautifulSoup

def extract_open_graph(url):
    # Fetch the webpage content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # TODO: Is there other possible pattern to extract meta data from the HTML content
    # Find all meta tags with property starting with 'og:'
    og_tags = soup.find_all('meta', property=lambda x: x and x.startswith('og:'))
    
    # Extract Open Graph parameters
    meta_params = {}
    meta_params['title'] = soup.title.string.strip() if soup.title else "No Title Found"
    for tag in og_tags:
        print (tag)
        tag_name = tag.get('name', tag.get('property', ''))
        tag_content = tag.get('content', '')
        # print(f"{tag_name}: {tag_content}")
        meta_params[tag_name] = tag_content

    return meta_params

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Extract Open Graph parameters from a webpage.')
    parser.add_argument('url', type=str, help='URL of the webpage to extract Open Graph parameters from')
    args = parser.parse_args()

    url = args.url
    open_graph_params = extract_open_graph(url)
    for key, value in open_graph_params.items():
        print(f'{key}: {value}')

    img_style = 'max-width: 100%; max-height: 100px; float: right; clear: right; margin-left: 1rem;margin-bottom: 2px;margin-top: 2px;'
    img_url = open_graph_params.get("image", open_graph_params.get("og:image"))
    img_text = f'<img src="{img_url}" alt="Image" style="{img_style}"/>' if img_url else ''

    print('============= Copy From Here =============')
    print(f'> [!cite] [{open_graph_params.get("title", "Title Not Found")}]({url})')
    print(f'> {img_text} {open_graph_params.get("og:description", "No Description")}')