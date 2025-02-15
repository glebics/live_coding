"""
4. Задача "Матричная алгебра"
Реализовать класс для работы с матрицами произвольного размера, поддерживающий операции:
Сложение матриц – Done
Умножение матриц – Done
Транспонирование – Done
Вычисление определителя (для квадратных матриц)
"""

from typing import List
import copy

"""–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––"""


class Matrix():

    def __init__(self, matrix: List[List[int]]):
        """
        Присваиваем матрице в качестве значения список
        """
        self.matrix = matrix

    def multiply(self, matrix: 'Matrix') -> 'Matrix':
        """
        Для перемножения матриц:
            Количество столбцов первой матрицы должно равняться количеству строк второй матрицы.
            Результатом будет матрица, где элемент c[i][j] вычисляется как скалярное произведение i-й строки первой матрицы и j-го столбца второй матрицы:
            Умножьте попарно соответствующие элементы строки и столбца.
            Сложите получившиеся произведения.
            Пример для матриц A (m×n) и B (n×p):
            Результирующая матрица C будет размера (m×p), где каждый элемент c[i][j] = Σ(a[i][k] * b[k][j]) для k от 1 до n.
        """
        if len(self.matrix) != len(matrix.matrix[0]):
            # print(self.matrix, len(self.matrix))
            # print(matrix.matrix, len(matrix.matrix[0]))
            return "columns not equal rows, it's impossible to multiply these matrices"
        # в нашем тестовом варианте будет 2 строки и 2 столбца (m=2, p=2)
        # print(self.matrix, len(self.matrix))
        # print(matrix.matrix[0], len(matrix.matrix[0]))
        result_matrix = [[0] * len(matrix.matrix[0])
                         for _ in range(len(self.matrix))]
        # print(f"1st matrix, quantity of columns is: {len(self.matrix[0])}")
        for i in range(len(self.matrix)):  # кол-во строк (2)
            temp = 0
            for j in range(len(matrix.matrix[0])):  # кол-во столбцов (2)
                for k in range(len(matrix.matrix)):
                    temp = self.matrix[i][k] * matrix.matrix[k][j]
                    result_matrix[i][j] += temp

        return Matrix(result_matrix)

    def sum(self, matrix: 'Matrix') -> 'Matrix':
        """
        Матрицы можно складывать только если они имеют одинаковые размеры, 
        то есть одинаковое количество строк и столбцов.
        """
        if len(self.matrix) != len(matrix.matrix) or len(self.matrix[0]) != len(matrix.matrix[0]):
            return "matrices have a different size, it's impossible to sum these matrices"
        result_matrix = [[0] * len(self.matrix[0])
                         for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result_matrix[i][j] = matrix.matrix[i][j] + self.matrix[i][j]
        return Matrix(result_matrix)

    def transporation(self) -> 'Matrix':
        """
        строки меняются местами с столбцами
        """
        result_matrix = [[0] * len(self.matrix[0])
                         for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result_matrix[i][j] = self.matrix[j][i]

        return Matrix(result_matrix)

    def determinant(self) -> int:
        """
        только для квадратных матриц
        для матриц большого размера (больше 2X2) используется
        метод Лапласа:
        Выберите строку или столбец для разложения (обычно берут первую строку для удобства).
        Для каждого элемента строки/столбца:
            Вычислите минор (подматрицу, полученную удалением строки и столбца этого элемента).
            Умножьте элемент на его алгебраическое дополнение ((−1) i+j⋅M ij). (либо 1, либо -1)
        """
        # в голове есть представление как это сделать только для матрицы 4х4
        # но это хотя бы лучше, чем 3х3
        # нам нужно проверить размер матрицы, после чего можно посчитать 4 раза 
        # определитель матрицы 3х3

        @staticmethod
        def square_determinant(matrix: List[List[int]]) -> int:
            return int(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])

        @staticmethod
        def cube_determinant(matrix: List[List[int]]) -> int:
            first_det = square_determinant([[matrix[1][1], matrix[1][2]],
                                           [matrix[2][1], matrix[2][2]]])
            second_det = square_determinant([[matrix[1][0], matrix[1][2]],
                                            [matrix[2][0], matrix[2][2]]])
            third_det = square_determinant([[matrix[1][0], matrix[1][1]],
                                           [matrix[2][0], matrix[2][1]]])
            
            result = matrix[0][0] * first_det - matrix[0][1] * second_det + matrix[0][2] * third_det
            return result
        
        # хочу удалить из минорной матрицы i строку и j столбец
        # Использовать copy.deepcopy для копирования матрицы (списка списков):
        # Обычный copy скопирует только внешний список, но не вложенные.
        determinants = [0] * 4
        for i in range(len(self.matrix[0])):
            minor = copy.deepcopy(self.matrix)
            del minor[0]
            for row in minor:
                del row[i]
            determinants[i] = cube_determinant(minor)

        result = int(
            self.matrix[0][0] * determinants[0] - self.matrix[0][1] * determinants[1] +
            self.matrix[0][2] * determinants[2] - self.matrix[0][3] * determinants[3])

        return result
    

    """ вариант от gpt с рекурсией и любой размерностью – не понял пока
    import copy
    from typing import List

    class Matrix:
        def __init__(self, matrix: List[List[int]]):
            self.matrix = matrix

        def determinant(self) -> int:
            if len(self.matrix) == 1:  # Базовый случай для матрицы 1x1
                return self.matrix[0][0]

            if len(self.matrix) == 2:  # Базовый случай для матрицы 2x2
                return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

            determinants = [0] * len(self.matrix[0])  # Для хранения определителей миноров
            for i in range(len(self.matrix[0])):  # Перебираем элементы первой строки
                minor = copy.deepcopy(self.matrix)
                del minor[0]  # Удаляем первую строку
                for row in minor:
                    del row[i]  # Удаляем i-й столбец

                # Рекурсивно вычисляем определитель минора
                determinants[i] = self.determinant(minor)

            result = 0
            for i in range(len(self.matrix[0])):
                sign = (-1) ** i  # Определяем знак алгебраического дополнения
                result += sign * self.matrix[0][i] * determinants[i]

            return result
    """

            

"""–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––"""


matrix_1 = Matrix(
    [[11, 1, 1, 1],
     # [2,2,2,2],
     [3, 4, 3, 3],
     [4, 4, 7, 4],
     [5, 5, 5, 5]])
# Matrix([[1,1,1],
#        [2,2,2]]) # это количество строк, их 2, а столбцов 3

matrix_2 = Matrix(
    [[1, 2, 3, 4],  # ,5],
     [1, 2, 3, 4],  # ,5],
     [1, 2, 3, 4],  # ,5],
     [1, 2, 3, 4]])  # ,5],])
# Matrix([[3,3],
#       [2,2],
#       [1,1]]) # 3 строки, 2 столбца

# result_matrix = Matrix([[6, 6],
#                         [12, 12]])

# result = matrix_1.multiply(matrix_2)
# result = matrix_1.sum(matrix_2)
# result = matrix_1.transporation()
result = matrix_1.determinant()

print(result, type(result), sep='\t')
# print(f"the counted matrix is: ")
# for i in range(len(matrix_1.matrix)):
#     print(result.matrix[i])
