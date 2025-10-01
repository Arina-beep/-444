from collections import deque


def main():
    try:
        # Чтение первой строки
        print("Введите количество вершин N и стартовую вершину S")
        print("(через пробел, например: '5 1'):")
        first_line = input().split()

        if len(first_line) != 2:
            raise ValueError("Ошибка: нужно ввести ровно два числа через пробел")

        N = int(first_line[0])
        S = int(first_line[1])

        if not (1 <= N <= 100):
            raise ValueError("Ошибка: N должно быть от 1 до 100")
        if not (1 <= S <= N):
            raise ValueError(f"Ошибка: S должно быть от 1 до {N}")

        print(f"граф из {N} вершин, стартовая вершина {S}")
        print()

        # Чтение матрицы смежности
        print(f"Введите матрицу смежности размером {N}x{N}:")
        print("(в каждой строке через пробел, 0 - нет ребра, 1 - есть ребро)")
        print()

        matrix = []
        for i in range(N):
            print(f"Строка {i + 1}: ", end="")
            row_input = input().split()

            if len(row_input) != N:
                raise ValueError(f"Ошибка: в строке должно быть ровно {N} чисел")

            row = []
            for num in row_input:
                if num not in ['0', '1']:
                    raise ValueError("Ошибка: матрица должна содержать только 0 и 1")
                row.append(int(num))

            matrix.append(row)

        print()

        # Проверка матрицы на симметричность (для неориентированного графа)
        for i in range(N):
            for j in range(N):
                if matrix[i][j] != matrix[j][i]:
                    raise ValueError("Ошибка: матрица не симметрична - граф должен быть неориентированным")

        print("Матрица корректна(симметрична)")
        print()

        # BFS для поиска компоненты связности
        visited = [False] * (N + 1)
        queue = deque([S])
        visited[S] = True
        component = []

        while queue:
            current = queue.popleft()
            component.append(current)

            for neighbor in range(1, N + 1):
                if matrix[current - 1][neighbor - 1] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        #Вывод
        print(f"Компонента связности с вершиной {S}:")
        print(f"Количество вершин: {len(component)}")
        print(f"Вершины: {' '.join(map(str, sorted(component)))}")



    except ValueError as e:
        print()
        print("=" * 50)
        print("ОШИБКА ВВОДА")
        print("=" * 50)
        print(str(e))
        print("Пожалуйста, проверьте введенные данные и попробуйте снова.")

    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем")

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        print("Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()