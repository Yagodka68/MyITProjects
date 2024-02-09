
# Реализуй класс File
# Он должен уметь конструироваться из пути к файлу на твоем компьютере
# Он должен позволять читать ВСЕ данные из файла и записывать данные в файл
# Твой класс в конструкторе получает режим открытия - либо запись, либо чтение
# При попытке вызвать чтение у объекта, который открыт на запись, должно возвращаться None

# Таким образом, твой класс имеет:

# конструктор от строки (путь) и числа (0 - чтение, 1 - запись)
# Метод read
# Метод write
# Метод is_opened_for_read - возвращает bool 
# Метод close, закрывающий файл

# Тебе поможет стандартная функция open - прочитай про нее
# Либо можно воспользоваться pathlib.Path - нагугли информацию и воспользуйся ей)

from test import testCases # Imports the file where are the test functions for the file with object

def main():
    testCases()

if __name__ == "__main__":
    main()

