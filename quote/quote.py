class quote:
    _author = str()
    _text = str()
    _category = str()

    def __init__(self, author, category, quote):
        """quote data class constructor takes author,category and quote and generates quote object"""
        self._author = author
        self._text = quote
        self._category = category

    def returnstring(self) -> str:
        """returns formatted string of current quote object"""
        return str(
            f"Author: {self._author} \n Category: {self._category} \n Quote {self._text} \n"
        )

    def get_author(self) -> str:
        """returns author of current quote object"""
        return self._author

    def get_quote(self) -> str:
        """returns quote from current quote object"""
        return self._text

    def get_category(self) -> str:
        """returns category from curent quote object"""
        return self._category
