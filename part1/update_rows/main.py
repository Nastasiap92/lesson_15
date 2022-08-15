# Изменение данных
#
#
# Когда мы начали работать с получившейся таблицей,
# то поняли, что тип животных не стоит разделять по полу.
# Так что теперь нам нужно заменить
# в столбце AnimalType значение Кот на Кошка, Пес на Собака.
# Напишите соответствующий запрос.
# +----+------------+-------+-----+-------------+-----+--------+
# | Id | AnimalType |  Name | Sex | DateOfBirth | Age | Weight |
# +----+------------+-------+-----+-------------+-----+--------+
# | 1  |   Кошка    |  Соня |  Ж  |  2013-12-02 |  7  |  2.15  |
# | 2  |    Кот     | Семен |  М  |  2017-05-03 |  4  |  4.5   |
# | 3  |   Собака   | Алина |  Ж  |  2018-11-12 |  2  |  20.8  |
# | 4  |    Пес     | Бобик |  М  |  2015-08-25 |  6  |  5.75  |
# +----+------------+-------+-----+-------------+-----+--------+

import sqlite3
import prettytable
from tools import create_table

con = sqlite3.connect(":memory:")
con = create_table(con)  # сформируем таблицу из предыдущих уроков
cur = con.cursor()
sqlite_query_first = ("UPDATE animals SET `AnimalType` = 'Кошка' WHERE `Name` = 'Семен';")  # TODO напишите здесь запрос на изменение строки
cur.execute(sqlite_query_first)
sqlite_query_second = ("UPDATE animals SET `AnimalType` = 'Собака' WHERE `Name` = 'Бобик';")  # TODO напишите здесь запрос на изменение строки
cur.execute(sqlite_query_second)

# Не удаляйте этот код, он используется
# для вывода результата


def print_result():
    result_query = ('SELECT * from animals')
    table = cur.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result()
