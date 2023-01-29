class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author
    @property
    def name(self):
        return self.name
    @property
    def author(self):
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages=None
        self.pages=pages
        @property
        def pages(self):
            return self._pages
        @pages.setter
        def pages(self,number):
            if isinstance(number,int):
                if number >0:
                    self._pages = number
                else:
                    raise ValueError(f'Invalid number of pages: {number!r}')
            else:
                raise ValueError(f'Error type number of pages')

    def __str__(self):
        tmp_str=super.__str__(self)
        return f'{tmp_str},количество страниц {self.pages}'
    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})'



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration=None
        self.duration = duration
        @property
        def duration(self):
            return self._duration
        @duration.setter
        def duration(self,time):
            if isinstance(time,float):
                if time >0:
                    self._duration = time
                else:
                    raise ValueError(f'Invalid duration: {time!r}')
            else:
                raise ValueError(f'Error type duration')

    def __str__(self):
        tmp_str = super.__str__(self)
        return f'{tmp_str},длительность {self.duration}'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})'

