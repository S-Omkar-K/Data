# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:31:20 2022

@author: saiom
"""

#__Due Date: Monday, November 7th before midnight__

#__Part 1: Natural Language Processing__

#You are working as a research assistant at a think tank studying international refugees.  The senior researcher you work for tries to follow [the Refugee Brief](https://www.unhcr.org/refugeebrief/) from the UNHCR, but they have been too busy lately to keep up with it.  They ask you to read in the reports and parse them using natural language processing.  They come out every Friday, except for around Christmas.  

#Use basic web scraping to collect every report between the most recent (June 24th, 2022) and April  8th, 2022.  The first one can be found [here](https://www.unhcr.org/refugeebrief/the-refugee-brief-24-june-2022/); use that to locate the rest.

#Describe the sentiment of each article, and show which countries are discussed in the articles.

#Output to save to your repo for this question:
#  * question1.py file with the code - summary statistics can be displayed in your code
#  * question1_plot.png file for a plot that shows sentiment over time


import os
import pandas as pd
import matplotlib.pyplot as plt
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob');
import geonamescache
gc = geonamescache.GeonamesCache()


texts_path = r'E:\Autumn22\Python\PS3\refugee_briefs'

count = 0
final_df = pd.DataFrame(columns = ['Article Date', 'Countries in article', 'Polarity', 'Subjectivity'])
file_names = os.listdir(texts_path)

def read_file(file_name):
    file_path = os.path.join(texts_path, file_name)
    f = open(file_path, mode = 'r', encoding="utf8")
    return f.read()

country_data = gc.get_countries()
def gen_dict_extract(var, key):
    if isinstance(var, dict):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, (dict, list)):
                yield from gen_dict_extract(v, key)
    elif isinstance(var, list):
        for d in var:
            yield from gen_dict_extract(d, key)



def perform_sentiment_analysis(text, count, file_name):
    article_date = file_name
    nlp_text = nlp(text)
    article_country_list = []
    for ent in nlp_text.ents:
        if (ent.label_ == 'GPE') & (ent.text in country_data):
            article_country_list.append(ent.text)
    article_polarity_value = nlp_text._.blob.polarity
    article_subjectivity_value = nlp_text._.blob.subjectivity
    
    final_df.loc[count] = [article_date, set(sorted(article_country_list)),article_polarity_value, article_subjectivity_value]

### Main class starts here
[text_10June, text_13May, text_17June,
text_20May, text_24June, text_27May, text_29April, 
text_3June, text_6May, text_8April]= [read_file(file_name) for file_name in os.listdir(texts_path)]

file_names2 = ['08-April-2022', '29-April-2022', 
               '06-May-2022', '13-May-2022', '20-May-2022', 
               '27-May-2022', '03-June-2022', '10-June-2022',
               '17-June-2022', '24-June-2022']
all_texts = [  text_8April, text_29April,
             text_6May,text_13May, text_20May, text_27May,
             text_3June, text_10June,  text_17June, text_24June ]

country_data = [*gen_dict_extract(country_data, 'name')]

for text in all_texts:
    file_name = file_names2[count].strip('.txt')
    perform_sentiment_analysis(text, count, file_name)
    count = count + 1

print(final_df)



ax1 = final_df.plot(x = 'Article Date', y = 'Polarity', kind = "bar", ylabel = 'Polarity of the Article', title = 'Sentiment Analysis of Articles: Polarity')
plt.xticks(rotation = 45)
plt.tight_layout(rect=(0, 0 , 1, 1))
ax1.axhline(y=0.0, color='black', linestyle='-', linewidth=0.5)
plt.savefig('question1_polarity_plot.png')


#ax2 = final_df.plot.barh(x = 'Article Date', y = 'Polarity', ylabel = 'Polarity of the Article')
#for container in ax2.containers:
#    ax2.bar_label(container)
   
ax4 = final_df.plot(x = 'Article Date', y = 'Subjectivity', kind = "bar", ylabel = 'Subjectivity of the Article', title = 'Sentiment Analysis of Articles: Subjectivity')
plt.xticks(rotation = 45)
plt.tight_layout(rect=(0, 0 , 1, 1))
plt.savefig('question1_subjectivity_plot.png')

#ax3 = final_df.plot(x = 'Article Date', y = 'Subjectivity', kind = "bar", ylabel = 'Subjectivity of the Article')
#for container in ax3.containers:
#    ax3.bar_label(container)

plt.show()