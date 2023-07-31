from paperscraper.pubmed import get_and_dump_pubmed_papers
import pandas as pd


query = ['AI','Breast Cancer','Artificial intelligence','treatment']

get_and_dump_pubmed_papers(query, output_filepath='bcTreatment.jsonl')


# Read the data from the JSONL file
data = pd.read_json('bcTreatment.jsonl', lines=True)

# Save the data to an XLS file
data.to_excel('bcTreatment.xlsx', index=False)
