#!/usr/bin/env python

import simplejson
from pandas import Series,DataFrame
import pandas as pd

with open('sample.json') as f:
    data = simplejson.load(f)

dframe = DataFrame(data['conversation'])
pd.set_option('display.max_colwidth', -1)

html_out = DataFrame.to_html(dframe)

Html_file = open("chats.html", "w")
Html_file.write(html_out.encode('utf8'))
Html_file.close()

