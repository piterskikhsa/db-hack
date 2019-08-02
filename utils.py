import random


def fix_mark(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=(2, 3)).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, lesson):
    Commendation.objects.create(text=get_praise(), created=lesson.date, schoolkid=schoolkid, subject=lesson.subject,
                                teacher=lesson.teacher)


def get_praise():
    praises = ["Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!", "Ты меня приятно удивил!",
               "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!", "Именно этого я давно ждал от тебя!",
               "Сказано здорово – просто и ясно!", "Ты, как всегда, точен!", "Очень хороший ответ!", "Талантливо!",
               "Ты сегодня прыгнул выше головы!", "Я поражен!", "Уже существенно лучше!", "Потрясающе!",
               "Замечательно!", "Прекрасное начало!", "Так держать!", "Ты на верном пути!", "Здорово!",
               "Это как раз то, что нужно!", "Я тобой горжусь!", "С каждым разом у тебя получается всё лучше!",
               "Мы с тобой не зря поработали!", "Я вижу, как ты стараешься!", "Ты растешь над собой!",
               "Ты многое сделал, я это вижу!", "Теперь у тебя точно все получится!"]
    return random.choice(praises)


user_name = 'Фролов Иван'
subject = 'Математика'
class_year_letter = (6, 'А')
kid = Schoolkid.objects.get(full_name__contains=user_name)
fix_mark(kid)
remove_chastisements(kid)

lessons = Lesson.objects.filter(year_of_study=class_year_letter[0],
                                group_letter=class_year_letter[1],
                                subject__title=subject)

create_commendation(kid, lessons[0])
