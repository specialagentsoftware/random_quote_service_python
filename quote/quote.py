class quote():
    _author = str()
    _text = str()
    _category = str()

    def __init__(self,author,category,quote):
        self._author = author
        self._text = quote
        self._category = category

    def returnstring(self) -> str:
        return str(f'Author: {self._author} \n Category: {self._category} \n Quote {self._text} \n')
    
    def get_author(self) -> str:
        return self._author
    
    def get_quote(self) -> str:
        return self._text
    
    def get_category(self) -> str:
        return self._category