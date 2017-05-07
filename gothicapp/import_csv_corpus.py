import django
import json
from django.conf import settings
from datetime import datetime
import csv
data_reader = csv.reader(open('./gothic_texts.csv'), delimiter=",", quotechar='"')

import sys, os
sys.path.append('/Users/eleanorstrib/Documents/dev_projects/gothic_colors/gothicapp/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'gothicapp.settings'

django.setup()
from gothiccolors.models import Corpus


for row in data_reader:
    if row[0] != 'Title': #skip header row
        corpus = Corpus()  # instantiate the class
        corpus.title = row[0]
        corpus.author = row[1]
        corpus.year = row[2] # date in spreadhsheet
        corpus.period = row[3]
        corpus.mode = row[4]
        corpus.genre = row[5]
        corpus.nationality = row[6]
        corpus.pseudonym = row[7]
        corpus.role = row[12]
        corpus.authority = row[13]
        corpus.filename = row[14]
        corpus.full_text_source = row[15]
        corpus.illustrator = row[16]
        corpus.translator = row[17]
        corpus.ebook_source = row[18]
        corpus.more_info = row[19]
        corpus.notes = row[20]
        corpus.etext_publisher = row[21]
        corpus.ebook_num = row[22]
        corpus.etext_pub_date = row[23]
        corpus.date_accessed = row[24]
        corpus.editor = row[25]
        corpus.edition = row[26]
        corpus.color_list = row[27].replace("'", "\"")
        corpus.color_dict = row[28].replace("'", "\"")
        corpus.save()
        print("this record was saved: ", corpus.title)
    else:
        print('skipping row')
print("done")
