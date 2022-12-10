import doctest

class movements:
    def __init__(self, angle: float, coord: float):
        """
        Создание и подготовка к работе объекта "Движения"
        :param angle: Угол  в градусах задаваемый в виде одного оборота вокруг оси
        :param coord: Координата в диапозоне от -300 до 300
        Примеры:
        >>> move1 = movements(90, 10)  # инициализация экземпляра класса
        """
        if not isinstance(angle, (int, float)):
            raise TypeError("Угол должен быть типа int или float")
        if angle < -360 or angle >360:
            raise ValueError("Угол должен быть от -360 до 360")
        self.angle = angle

        if not isinstance(coord, (int, float)):
            raise TypeError("Кордината должна быть int или float")
        if coord < -300 or coord>300:
            raise ValueError("Координата находится в диапозоне от -300 до 300 условных единиц")
        self.coord = coord

        def rotate(self,angle:float)->float:
            """
            Изменение угла ориентации объекта
            :param angle: + угол и преобразование угла, если выходит из диапозона
            :return:none
            Примеры:
        >>> move1 = movements(90, 10)
        >>> move1.rotate(30) #поворот против часовой

            """
            ...
        def move(self,coord:float)->float:
            """
            Изменение координаты
            :param coord: + координата, отражение если выходит из диапозона
            :return: none
            Примеры:
        >>> move1 = movements(90, 10)
        >>> move1.move(30) #сдвиг на 30 условных единиц
            """
            ...
class texture:
    def __init__(self, roughness: float):
        """
        Создание и подготовка к работе объекта "Текстура"
        :param roughness: Шершавость поверхности от 0 до 1
        Примеры:
        >>> texture_ice = texture(0.1)  # инициализация экземпляра класса
        """
        if not isinstance(roughness, ( float)):
            raise TypeError("Шершавость должна быть типа float")
        if roughness <= 0 or roughness>1:
            raise ValueError("Шершавость поверхности от 0 до 1")
        self.roughness = roughness

        def scratch(self,roughness:float)->float:
            """
            Текстура объекта царапается
            :param roughness: + шершавость
            :raise ValueError: нельзя царапать больше, чем 1 шершавость или меньше имеющейся
            :return: none
            Примеры:
             >>> texture_ice = texture(0.1)
             >>> texture_ice.scratch(0.1)  # царапаем
            """
            ...
        def glue_up(self,roughness:float)->float:
            """
            Текстура объекта выравнивается (например подтаивание льда от движения и после вода подмораживается из-за разницы температур или спекание кристалла)
            :param roughness: - шершавость
            :raise ValueError: нельзя выравнять больше, чем 0 шершавости или меньше имеющейся
            :return: none
            Примеры:
             >>> texture_ice = texture(0.1)
             >>> texture_ice.glue_up(0.1)  #выравниваем на некоторую степень
            """
            ...


class interaction:
    def __init__(self, coord_to_obj: float, number_of_will: int):
        """
        Создание и подготовка к работе объекта "Взаимодействие с обЬектами"
        :param coord_to_obj: расстояние, с которого мы можем повлиять на объект
        :param number_of_will: Объем занимаемой жидкости
        Примеры:
        >>> interaction_ice_cube = interaction(5, 1)  # инициализация экземпляра класса
        """
        if not isinstance(coord_to_obj, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if coord_to_obj <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        self.coord_to_obj = coord_to_obj

        if not isinstance(number_of_will, (int)):
            raise TypeError("Номер воздействия должен быть int")
        if number_of_will < 0:
            raise ValueError("Номер воздействия не может быть отрицательным числом")
        self.number_of_will = number_of_will

        def rotate(self, coord_to_obj:float,number_of_will:int)->float:
            """
            Заставить объект вращаться
            :param coord_to_obj: 1 и менее условных единиц
            :param number_of_will: 1-10 прописанные типы вращений
            :raise ValueError: нельзя превышать указанные диапозоны
            :return: Заставить объект вращаться
            Примеры:
            >>> interaction_ice_cube = interaction(0.1, 1)
            >>> interaction_ice_cube.rotate(0.1,1)
            """
            ...
        def move(self, coord_to_obj:float,number_of_will:int)->float:
            """
            Заставить объект двигаться
            :param coord_to_obj: 10 и менее условных единиц
            :param number_of_will: 1-10 прописанные типы перемещений
            :raise ValueError: нельзя превышать указанные диапозоны
            :return: Заставить объект перемещаться относительно начала координат
            Примеры:
            >>> interaction_ice_cube = interaction(10, 2)
            >>> interaction_ice_cube.move(10,2)
            """
            ...
        def change_texture(self, coord_to_obj:float,number_of_will:int)->float:
            """
            Заставить объект менять структуру поверхности
            :param coord_to_obj: 1 и менее условных единиц
            :param number_of_will: 1-10 прописанные типы воздействий от инструментов
            :raise ValueError: нельзя превышать указанные диапозоны
            :return: Заставить объект становиться шершавее
            Примеры:
            >>> interaction_ice_cube = interaction(0.1, 3)
            >>> interaction_ice_cube.change_texture(0.1,3)
            """
            ...
if __name__ == "__main__":
    doctest.testmod()
    pass
