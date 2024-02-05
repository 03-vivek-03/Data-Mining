#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from bs4 import BeautifulSoup
import chardet
from tqdm import tqdm

total = 0

target_words1 = ["infective etiology", "infective etology"]
target_words2 = ["homogeneous opacit", "homogenous opacit"]

found_counts = {combo: 0 for combo in itertools.product(target_words1, target_words2)}

main_path = "F:/JAN_2023_REPORTS/01_2023"

for folder in tqdm(os.listdir(main_path)):
    new_path = os.path.join(main_path, folder)
    for rep in os.listdir(new_path):
        if rep.startswith('Approved'):
            total += 1
            report_file_path = os.path.join(new_path, rep)
            with open(report_file_path, 'rb') as f:
                raw_data = f.read()
                encoding_result = chardet.detect(raw_data)
                file_encoding = encoding_result['encoding']
            with open(report_file_path, 'r', encoding=file_encoding) as f:
                content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text().lower()

            # Check for each combination
            for combo in itertools.product(target_words1, target_words2):
                word1, word2 = combo
                if word1 in text and word2 in text:
                    found_counts[combo] += 1

print("Total Reports: ", total)
                    
print("Combination-wise counts:")
for combo, count in found_counts.items():
    print(f"{combo}: {count}")

