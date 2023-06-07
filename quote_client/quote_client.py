import os, csv, sys
from quote import quote
import configparser
import random


class quote_client:
    """quote client handles opening the csv file, parsing it,
    creating quote objects, creating a list of quotes and allowing
    the return of a random quote from the list"""

    config = configparser.ConfigParser()
    quotelist = []
    config.read("config/config.ini")
    quote_file_path = config["DEFAULT"]["CsvFilePath"]

    def __init__(self) -> str:
        """the quote client constructor opens the csv file, parses it, and creates a list of quote objects"""
        try:
            with open(self.quote_file_path, newline="\n") as f:
                reader = csv.reader(f)
                try:
                    for row in reader:
                        q = quote.quote(row[0], row[1], row[2])
                        self.quotelist.append(q)
                except csv.Error as e:
                    sys.exit(
                        "file {}, line {}: {}".format(
                            self.quote_file_path, reader.line_num, e
                        )
                    )
        except IOError as e:
            sys.exit(
                "The following error occurred when trying to open the file {}".format(e)
            )

    def randomquote(self):
        """the randomquote function selects a random quote from the quote list and
        returns a formatted string related to the selected random quote"""

        selectedquote = self.quotelist[random.randint(0, len(self.quotelist))]
        author = selectedquote.get_author()
        quote = selectedquote.get_quote()
        category = selectedquote.get_category()
        return f'<div style="margin: 25px 50px 75px 100px"><ul style="list-style-type: none"><li>Author: {author}</li> <li>Category: {category}</li> <li>Quote: {quote}</li></ul></div>'
