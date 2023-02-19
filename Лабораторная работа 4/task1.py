import doctest


class animal:
    """
    Класс животное
    методы
    _init__(self,name:str,fullness:bool,sleeping:bool,drink_need:bool)
    move(self,way:str)
    __str__(self)
    __repr__(self)
    свойство
    duration_way(self,duration:float)
    """
    def __init__(self, name: str, fullness: bool, sleeping: bool, drink_need: bool):
        """
        Создание объекта класса животное

        :param name: имя животного
        :param fullness: сытость животного, где 1- сыт, 0-голоден
        :param sleeping: сонливость животного, где 1-сонливый, 0-бодрый
        :param drink_need: нужда в воде животного, где 1-хочет пить, 0-не хочет

        Пример:
        ">>>test_animal = animal("Кеша",1,1,1)"
        #Инициализация объекта
        """
        self.name = name
        self.fullness = fullness
        self.sleeping = sleeping
        self.drink_need = drink_need
        self.way = None
        self._duration_way = None

    def move(self, way: str):
        """
        перемещение животного вперед или назад
        :param way: перемещение, принимает значения forward или backward
        :return: установленное направление перемещения
        """
        if isinstance(way, str):
            if way == "forward" or "backward":
                    self.way = way
                    return self.way
            else:
                raise ValueError(f'way can be forward or back, while incoming {way}')
        else:
            raise TypeError(f'way must be str, while incoming {type(way)}')

    @property
    def duration_way(self):
        """
        геттер для длительности пути
        :return: длительность пути
        """
        return self._duration_way

    @duration_way.setter
    def duration_way(self, duration: float):
        """
        сеттер для длительности пути
        :param duration: длитетельность пути
        :return:
        """
        if isinstance(duration, float):
            if duration > 0:
                 self._duration_way = duration
            else:
                raise ValueError(f'duration of moving must be positive number, while incoming {duration}')
        else:
            raise TypeError(f'duration of way must be float, while incoming {type(duration)}')

    def __str__(self):
        """
        магический метод __str__
        :return: возвращает полное состояние животного (перемещение и самочувствие)

        Пример:
        ">>>test_animal = animal("Кеша",1,1,1)
        ">>>print(test_animal)

        """
        return f'animal"{self.name}" feels fullness {self.fullness}, sleeping {self.sleeping},' \
               f'drink_need {self.drink_need}, moves {self.way} {self._duration_way}'

    def __repr__(self):
        """
        магический метод, выдающий строку, необходимую для инициализации животного
        :return:

        Пример:
        ">>>test_animal = animal("Кеша",1,1,1)
        ">>>repr(test_animal)

        """
        return f"{self.__class__.__name__}(name={self.name!r}, fullness={self.fullness}, sleeping={self.sleeping}," \
               f"drink_need={self.drink_need}, way={self.way} duration_way={self._duration_way})"


class bird(animal):
    """
        Класс птица
        методы
        _init__(self,name:str,fullness:bool,sleeping:bool,drink_need:bool)
        move(self,way:str)
        __str__(self)
        __repr__(self)
        свойства
        duration_way(self,duration:float)
        type_of_moving(self,type_move:str)
        """
    def __init__(self, name: str, fullness: bool, sleeping: bool, drink_need: bool):
        """
                Создание объекта класса птицы

                :param name: имя птицы
                :param fullness: сытость птицы, где 1- сыт, 0-голоден
                :param sleeping: сонливость птицы, где 1-сонливый, 0-бодрый
                :param drink_need: нужда в воде птицы, где 1-хочет пить, 0-не хочет

                Пример:
                ">>>test_bird = bird("Кеша",1,1,1)"
                #Инициализация объекта
                """
        super().__init__(name, fullness, sleeping, drink_need)
        self._type_of_moving = None
        self.way = None

    @property
    def type_of_moving(self):
        """
        геттер для типа движения
        :return: тип движения
        """
        return self._type_of_moving

    @type_of_moving.setter
    def type_of_moving(self, type_move: str):
        """
        сеттер для типа движения
        :param type_move: тип движения,принимает значения fly, swim
        :return:
        """
        if isinstance(type_move, str):
            if type_move == "fly" or "swim":
                self._type_of_moving = type_move
            else:
                raise ValueError(f'type of moving must be fly or swim, while incoming {type_move}')
        else:
            raise TypeError(f'type of moving must be str, while incoming {type_move}')

    @property
    def duration_way(self):
        """
        геттер для длительности пути
        :return: длительность пути
        """
        return self._duration_way

    @duration_way.setter
    def duration_way(self, duration: float):
        """
        сеттер для длительности пути
        :param duration: длитетельность пути
        :return:
        """
        if isinstance(duration, float):
            if duration > 0:
                self._duration_way = duration
            else:
                raise ValueError(f'duration of moving must be positive number, while incoming {duration}')
        else:
            raise TypeError(f'duration of way must be float, while incoming {type(duration)}')

    def move(self, way: str):
        """
                перемещение птицы вперед или назад
                :param way: перемещение, принимает значения forward-up или backward-up, forward-down или backward-down
                :return: установленное направление перемещения
                """
        if isinstance(way, str):
            if way == "forward-up" or "backward-up" or "forward-down" or "backward-down":
                self.way = way
            else:
                raise ValueError(f'way can be forward-up or backward-up or forward-down or backward-down, '
                                 f'while incoming {way}')
        else:
            raise TypeError(f'way must be str, while incoming {type(way)}')

    def __str__(self):
        """
         магический метод __str__
        :return: возвращает полное состояние птицы (перемещение и самочувствие)

        Пример:
        ">>>test_bird = bird("Кеша",1,1,1)
        ">>>print(test_bird)

        """
        return f'bird"{self.name}" feels fullness {self.fullness}, ' \
               f'sleeping {self.sleeping},drink_need {self.drink_need},' \
               f' moves {self.type_of_moving} {self.way} {self._duration_way}'

    def __repr__(self):
        """
        магический метод, выдающий строку, необходимую для инициализации птицы
         :return:

        Пример:
        ">>>test_bird = bird("Кеша",1,1,1)
        ">>>repr(test_bird)

        """
        return f"{self.__class__.__name__}(name={self.name!r}, fullness={self.fullness}, " \
               f"sleeping={self.sleeping},drink_need={self.drink_need},type of moving={self.type_of_moving}, " \
               f"way={self.way} duration_way={self._duration_way})"



if __name__ == "__main__":
    # Write your solution here
    """
    Метод move перегружен так как птица в отличии от любого животного может перемещаться в воде и в воздухе вверх или вниз
    
    """

    doctest.testmod()
    pass
