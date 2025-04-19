# Импортируйте необходимые модули.
from datetime import datetime
from exceptions import FieldFormatError

def validate_record(name: str, birthdate: str) -> bool:
    # Напишите код, верните булево значение.
    try:
        datetime.strptime(birthdate, "%d.%m.%Y")
        return True
    except ValueError as e:
        print(f'Некорректный формат даты в записи: {name}, {birthdate}')
        return False


def process_people(entries: list[tuple]) -> dict:
    # Объявите счётчики.
    good_count = 0
    bad_count = 0
    # Распакуйте кортежи из полученного списка entries.
    for i in entries:
        name, date = i
        if validate_record(name, date):
            good_count += 1 
        else:
            bad_count += 1
    dict_with_result = {
        "good": good_count,
        "bad": bad_count
    }
             
    # Каждую пару значений передайте в validate_record(),
    # чтобы проверить корректность формата даты рождения.
    # В зависимости от результата проверки увеличьте один из счётчиков.

    # Верните словарь.
    return dict_with_result


data = [('Иван Васильевич', '25 января 1530 года от Рождества Христова'),
 ('Родион Расколов', '13.06.1866'),
 ('Александр Сергеев', '6.06.1799'),
 ('Владимир Маяков', '14 апреля 1930 года')] 
statistics = process_people(data)
print(f'Корректных записей: {statistics["good"]}')
print(f'Некорректных записей: {statistics["bad"]}')
