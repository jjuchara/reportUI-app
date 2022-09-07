import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

import utils.get_data_from_ui as ui_data


class RidersSchoolUi(QMainWindow):
    def __init__(self):
        super(RidersSchoolUi, self).__init__()
        uic.loadUi("design/RidersSchoolReportUi.ui", self)
        self.show()

        self.save_btn.clicked.connect(self.save_data)

    def save_data(self):
        lesson_type = ui_data.get_lessons_type(self)
        price_type = ui_data.get_price_type(self)
        student_quantity = self.student_quantity.value()
        worked_hour = self.worked_hour.value()
        selected_date = self.calendar.selectedDate().toPyDate().strftime("%d-%m-%Y")


def main():
    app = QApplication(sys.argv)
    UIWindow = RidersSchoolUi()
    app.exec_()


if __name__ == "__main__":
    main()
