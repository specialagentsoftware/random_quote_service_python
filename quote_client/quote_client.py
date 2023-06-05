import os,csv,sys
from quote import quote
import configparser
import random

class quote_client:
    
    config = configparser.ConfigParser()
    quotelist = []
    config.read('config/config.ini')
    quote_file_path = config['DEFAULT']['CsvFilePath']
    
    def __init__(self) -> str:
        with open(self.quote_file_path, newline='\n') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    q = quote.quote(row[0],row[1],row[2])
                    self.quotelist.append(q)
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(self.quote_file_path, reader.line_num, e))    

    def randomquote(self):
        selectedquote = self.quotelist[random.randint(0,48390)]
        author = selectedquote.get_author()
        quote = selectedquote.get_quote()
        category = selectedquote.get_category()
        return f'<div style="margin: 25px 50px 75px 100px"><ul style="list-style-type: none"><li>Author: {author}</li> <li>Category: {category}</li> <li>Quote: {quote}</li></ul></div>'
