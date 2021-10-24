from operator import itemgetter


class ProgrammLang:
    """ProgrammingLanguage"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Library:
    """Library"""

    def __init__(self, id, name, use, num_operation, prog_lang_id):
        self.id = id
        self.name = name
        self.use = use
        self.num_operation = num_operation
        self.prog_lang_id = prog_lang_id


class ProgrammLangLibrary:
    """
    'Библиотеки языков программирования' для реализации
    связи многие-ко-многим
    """

    def __init__(self, prog_lang_id, library_id):
        self.prog_lang_id = prog_lang_id
        self.library_id = library_id


# Языки программирования
programm_lang = [
    ProgrammLang(1, 'Python'),
    ProgrammLang(2, 'C#'),
    ProgrammLang(3, 'JavaScript'),
    ProgrammLang(11, 'TypeScript'),
    ProgrammLang(22, 'C++'),
    ProgrammLang(33, 'Java'),
]

# Библиотеки
library = [
    Library(1, 'Delorean', 'time', 2, 1),
    Library(2, 'Snowballstemmer', 'stemming', 1,  2),
    Library(3, 'cmath', 'calculations', 30, 11),
    Library(4, 'eigen', 'linear algebra', 20,  3),
    Library(5, 'LinqToSql', 'SQLite', 7,  22),
    Library(6, 'WPF', 'graphics', 10,  1),
    Library(7, 'React', 'interface', 3,  3),
    Library(8, 'D3', 'visualization', 23,  2),
    Library(9, 'Maven', 'assembly', 1, 33),
    Library(10, 'Guava', 'Google library', 15,  11),
    Library(11, 'Highlight', 'syntax', 1, 1),
    Library(12, 'Pandas', 'Data Science', 13,  3),
]

prog_lang_library = [
    ProgrammLangLibrary(1, 1),
    ProgrammLangLibrary(1, 2),
    ProgrammLangLibrary(1, 12),

    ProgrammLangLibrary(2, 3),
    ProgrammLangLibrary(2, 4),
    ProgrammLangLibrary(2, 5),

    ProgrammLangLibrary(3, 6),
    ProgrammLangLibrary(3, 7),
    ProgrammLangLibrary(3, 8),
    ProgrammLangLibrary(3, 9),
    ProgrammLangLibrary(3, 10),
    ProgrammLangLibrary(3, 11),

    ProgrammLangLibrary(11, 6),
    ProgrammLangLibrary(11, 7),
    ProgrammLangLibrary(11, 8),
    ProgrammLangLibrary(11, 9),
    ProgrammLangLibrary(11, 10),
    ProgrammLangLibrary(11, 11),

    ProgrammLangLibrary(22, 5),
    ProgrammLangLibrary(22, 6),

    ProgrammLangLibrary(33, 7),
    ProgrammLangLibrary(33, 8),
    ProgrammLangLibrary(33, 9),
    ProgrammLangLibrary(33, 10),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(l.name, l.use, l.num_operation, p.name)
                   for p in programm_lang
                   for l in library
                   if p.id == l.prog_lang_id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(p.name, pl.prog_lang_id, pl.library_id)
                         for p in programm_lang
                         for pl in prog_lang_library
                         if p.id == pl.prog_lang_id]

    many_to_many = [(l.name, l.num_operation, name)
                    for name, _, library_id in many_to_many_temp
                    for l in library if l.id == library_id]


    print('Задание В1')
    b1 = list(filter(lambda x: (str)(x[0]).startswith('D'), one_to_many))
    b1 = [
        (el[0], el[3])
        for el in b1
    ]
    print(b1)
    print('\nЗадание В2')
    res_unsorted = []
    # Перебираем все языки
    for p in programm_lang:

        # сравниваем
        p_library = list(filter(lambda i: i.id == p.id, library))

        if len(p_library) > 0:
            min_size = min([f.num_operation for f in p_library])
            res_unsorted.append((p.name, min_size))
    # сортировка по минимальному размеру
    res_b2 = sorted(res_unsorted, key=itemgetter(1), reverse=False)  # сортировка размера по возрастанию
    print(res_b2)
    print('\nЗадание В3')
    b3 = sorted(many_to_many, key=lambda y: y[0])
    print(b3)


if __name__ == '__main__':
    main()