"""
@Author : Hishallyi
@Date   : 2024/7/22
@Code   : Calculate the similarity of gendered words in batches
"""

from utils import get_news_data
import pprint

folder_path = 'news'  # replace with your folder path
news_data = get_news_data(folder_path)

# print nested dictionary results beautifully
pprint.pprint(news_data)

# Go through and print the Word document name in the folder for each news type
for news_type, docs in news_data.items():
    print(f"News type: {news_type}")
    for doc_file in docs.keys():
        print(f"  - Document name: {doc_file}")
