# db-hack

Правка оценок и замечаний в базе данных электронного дневника.

### Описание функционала проекта
Функция `fix_mark` получает на вход объект ученика `schoolkid`, исправляет все оценки (2, 3) ученика на 5.

Функция `remove_chastisements` получает на вход объект ученика `schoolkid`, удаляет все замечания у ученика.

Функция `create_commendation`  получает на вход объект ученика `schoolkid` и объект урока `lesson`. Добавляет случайную похвалу ученику.


### Запуск проекта
Для работы скрипта необходимо импортировать `utils.py` или скопировать файл и положить в папку с проектом, рядом с `manage.py`.

Пример использования:

```python
def main():
    user_name = 'Фролов Иван'
    subject = 'Математика'
    class_year_letter = (6, 'А')
    lessons = Lesson.objects.filter(year_of_study=class_year_letter[0],
                                    group_letter=class_year_letter[1],
                                    subject__title=subject)

    kid = Schoolkid.objects.get(full_name__contains=user_name)
    fix_mark(kid)
    remove_chastisements(kid)
    create_commendation(kid, lessons[0])
```

### Цель проекта

Правка оценок и замечаний ученика в электронном дневнике

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).