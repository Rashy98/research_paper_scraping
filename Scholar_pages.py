import requests
import pandas as pd
from bs4 import BeautifulSoup

def GetGoogleScholarData(query,num_pages):
    URL = 'https://scholar.google.com/scholar'
    results = []
    for page in range(0, num_pages):
        params = {
            'q': query,
            'hl': 'en',
            'start': page * 10  # Each page displays 10 results
        }

        response = requests.get(URL, params=params)
        soup = BeautifulSoup(response.content, 'html.parser')

        for item in soup.select('.gs_r'):
            title = item.select_one('.gs_rt a')
            abstract = item.select_one('.gs_rs')
            journal = item.select_one('.gs_a')

            title_text = title.get_text() if title else 'Title not available'
            abstract_text = abstract.get_text() if abstract else 'Abstract not available'
        
            if journal and title_text != 'Title not available':
                bib_text = journal.get_text()
                publisher_text = bib_text.split('-')[-1].strip()
                authors_text = bib_text.split('-')[0].strip()
                journal_text = bib_text.split('-')[1].strip()

            else:
                journal_text = 'Journal information not available'
                publisher_text = 'Publisher not available'
                authors_text = 'Authors information not available'

            results.append({
                'Title': title_text,
                'Abstract': abstract_text,
                'Journal': journal_text,
                'Publisher': publisher_text,
                'Authors': authors_text
            })
    df = pd.DataFrame(results)
    df.to_excel('Sheet11_go.xlsx', index=False)
    return results

if __name__ == '__main__':
    #query = input("Enter your query: ")
    num_pages = 10
    #int(input("Enter the number of pages to scrape: "))
    matchedData = GetGoogleScholarData("AI,Breast Cancer,Artificial intelligence,radiotherapy", num_pages)
    for entry in matchedData:
        print(f"Title: {entry['Title']}")
        print(f"Abstract: {entry['Abstract']}")
        print(f"Journal: {entry['Journal']}")
        print(f"Publisher: {entry['Publisher']}")
        print(f"Authors: {entry['Authors']}")
        print("=" * 75)
    print(f"Found {len(matchedData)} in total {num_pages}")
