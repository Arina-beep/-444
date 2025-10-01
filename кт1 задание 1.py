class Quadrilateral:
    """Класс, представляющий четырехугольник"""

    def __init__(self, a, b, c, d):
        print(f"\nПопытка создать четырехугольник со сторонами: {a}, {b}, {c}, {d}")

        #Проверка для дураков
        self._validate_basic_input(a, b, c, d)

        #Проверка на существование четырехугольника
        self._validate_quadrilateral_existence(a, b, c, d)

        # Сохраняем длины сторон
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        print(f"Создан четырехугольник со сторонами: {a}, {b}, {c}, {d}")

    def _validate_basic_input(self, a, b, c, d):
        """Проверка базового ввода 'для дураков'"""
        sides = [a, b, c, d]

        # Проверяем что все стороны числа
        for i, side in enumerate(sides, 1):
            if not isinstance(side, (int, float)):
                raise ValueError(f"Сторона {i} должна быть числом! Получено: {type(side)}")

        # Проверяем на отрицательные и нулевые значения
        for i, side in enumerate(sides, 1):
            if side <= 0:
                raise ValueError(f"Сторона {i} должна быть положительной! Получено: {side}")


    def _validate_quadrilateral_existence(self, a, b, c, d):
        """Проверка, что такой четырехугольник может существовать"""
        sides = [a, b, c, d]

        #Любая сторона должна быть меньше суммы трех других сторон
        for i in range(4):
            sum_of_other_three = sum(sides) - sides[i]
            if sides[i] >= sum_of_other_three:
                raise ValueError(
                    f"Четырехугольник не существует! "
                    f"Сторона {sides[i]} должна быть меньше суммы трех других сторон "
                    f"({sum_of_other_three})"
                )


    def perimeter(self):
        """Метод для вычисления периметра"""
        return self.a + self.b + self.c + self.d

    def get_info(self):
        """Вывод информации о четырехугольнике"""
        return f"Четырехугольник [{self.a}, {self.b}, {self.c}, {self.d}] Периметр: {self.perimeter()}"


class Rectangle(Quadrilateral):
    """Класс представляющий прямоугольник"""

    def __init__(self, length, width):
        print(f"\nПопытка создать прямоугольник: длина={length}, ширина={width}")

        # Проверяем входные данные
        self._validate_rectangle_input(length, width)

        #У прямоугольника противоположные стороны равны
        super().__init__(length, width, length, width)
        self.length = length
        self.width = width
        print(f"Создан прямоугольник: длина={length}, ширина={width}")

    def area(self):
        """Метод для вычисления площади прямоугольника"""
        return self.length * self.width

    def get_info(self):
        """Вывод информации о прямоугольнике"""
        return f"Прямоугольник {self.length}×{self.width} Периметр: {self.perimeter()} Площадь: {self.area()}"


class Square(Rectangle):
    """Класс представляющий квадрат"""

    def __init__(self, side):
        print(f"\nПопытка создать квадрат со стороной: {side}")

        # Проверяем входные данные
        self._validate_square_input(side)

        super().__init__(side, side)
        self.side = side
        print(f"Создан квадрат со стороной: {side}")

        def _validate_square_input(self, side):
            """Дополнительные проверки для квадрата"""
            # Проверка на "особые" значения
            if side == 0:
                raise ValueError("Квадрат не может иметь сторону 0!")

        def area(self):
            """Метод для вычисления площади квадрата"""
            return self.side ** 2

        def get_info(self):
            """Вывод информации о квадрате"""
            return f"Квадрат {self.side}×{self.side} Периметр: {self.perimeter()} Площадь: {self.area()}"

    def _get_valid_number(prompt):
        """Получение валидного числа от пользователя с защитой от дураков"""
        while True:
            try:
                value = input(prompt).strip()

                # Защита от пустого ввода
                if not value:
                    print("Пустой ввод! Введите число.")
                    continue


                # Пробуем преобразовать в число
                number = float(value)

                return number

            except ValueError:
                print("Это не число! Попробуйте снова.")

    def main():
        """Основная функция программы для ручного ввода данных"""
        try:
            print("\nВведите 4 стороны четырехугольника:")
            a = _get_valid_number("Сторона 1: ")
            b = _get_valid_number("Сторона 2: ")
            c = _get_valid_number("Сторона 3: ")
            d = _get_valid_number("Сторона 4: ")

        quad = Quadrilateral(a, b, c, d)
        print(f"Результат: {quad.get_info()}")

        except ValueError as e:
            print(f"Ошибка: {e}")
            print("Попробуйте другие значения сторон!")


        # Создание прямоугольника
        try:
            print("\nВведите размеры прямоугольника:")
            length = _get_valid_number("Длина: ")
            width = _get_valid_number("Ширина: ")

            rect = Rectangle(length, width)
            print(f"Результат: {rect.get_info()}")

        except ValueError as e:
                    print(f"Ошибка: {e}")
                    print("Попробуйте другие значения!")


        # Создание квадрата
        try:
            print("\nВведите сторону квадрата:")
            side = _get_valid_number("Сторона: ")

            square = Square(side)
            print(f"Результат: {square.get_info()}")

        except ValueError as e:
            print(f"Ошибка: {e}")
            print("Попробуйте другое значение!")

#Запуск программы
if __name__ == "__main__":
    main()
