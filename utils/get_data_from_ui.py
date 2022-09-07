from app import RidersSchoolUi 
from typing import Tuple


def get_lessons_type(object: RidersSchoolUi) -> str:

    if object.individual_lesson.isChecked():
        return object.individual_lesson.text()
    elif object.group_lesson.isChecked():
        return object.group_lesson.text()
    else:
        return object.course_lesson.text()

def get_price_type(object: RidersSchoolUi) -> Tuple['str', 'str'] | Tuple['str'] | None:
    
    if object.basik_price.isChecked() and object.special_price.isChecked():
        return (object.basik_price.text(), object.special_price.text())
    elif object.pro_price.isChecked() and object.special_price.isChecked():
        return (object.pro_price.text(), object.special_price.text())
    elif object.basik_price.isChecked():
        return (object.basik_price.text(),)
    elif object.pro_price.isChecked():
        return (object.pro_price.text(),)
    return None
