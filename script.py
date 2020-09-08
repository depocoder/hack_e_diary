from datacenter.models import Chastisement, Schoolkid, Mark, Lesson, Commendation



def get_schoolkid_info(child):
    child_info = Schoolkid.objects.filter(full_name=child)[0]
    return child_info


def change_bad_mark(child):
    schoolkid_info = get_schoolkid_info(child)
    all_bad_marks = Mark.objects.filter(schoolkid=schoolkid_info, points__in=[2,3])
    for bad_mark in all_bad_marks:
        bad_mark.points = 5
        bad_mark.save()


def remove_chastisements(child):
    schoolkid_info = get_schoolkid_info(child)
    all_bad_marks = Chastisement.objects.filter(schoolkid=schoolkid_info)
    for bad_mark in all_bad_marks:
        bad_mark.delete()


def add_lesson(child):
    schoolkid_info = get_schoolkid_info(child)
    lessons_info = Lesson.objects.filter(
        group_letter=schoolkid_info.group_letter,
        year_of_study=schoolkid_info.year_of_study,
        subject__title='Математика')
    Commendation.objects.create(
    teacher = lessons_info[0].teacher,
    subject = lessons_info[0].subject,
    created = lessons_info[0].date,
    schoolkid = schoolkid_info,
    text = 'Хвалю!')

child = 'Фролов Иван Григорьевич'
add_lesson(child)