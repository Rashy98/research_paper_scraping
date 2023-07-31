import pandas as pd
from scholarly import scholarly
from Config import Config

search_query = scholarly.search_pubs(Config.SEARCHKEY)

# Create an empty DataFrame to store the data
data = pd.DataFrame(columns=['Title', 'Author', 'Abstract', 'Publication URL'])

for i in range(Config.NUMRECORDS):
    item = next(search_query)
    if 'title' not in item['bib'] or 'pub_url' not in item or 'url_related_articles' not in item:
        continue
    
    title = item['bib']['title']
    author = item['bib']['author']
    abstract = item['bib']['abstract']
    pub_url = item['pub_url']
    year = item['bib']['pub_year']
    

    # Append the data to the DataFrame
    data = data.append({'Title': title, 'Author': author, 'Abstract': abstract,
                        'Publication URL': pub_url, 'Year' : year},
                       ignore_index=True)

# Save the DataFrame to an Excel file
data.to_excel('papers_Chemo_in_Oncology_with_year.xlsx', index=False)
