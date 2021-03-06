"""
时间与日期
dateTimeEdit1 = QDateTimeEdit()
dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))

    setDisplayFormat("yyyy/MM/dd HH-mm-ss")

dateTimeEdit1.dateChanged.connect(self.onDateChanged)
dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)

datetime = self.dateTimeEdit1.dateTime()
"""

import sys
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel


class calendarDemo(QWidget):
    def __init__(self):
        super(calendarDemo, self).__init__()
        self.initUI()
        self.resize(500, 500)

    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988, 1, 1))
        self.cal.setMaximumDate(QDate(2088, 1, 1))
        self.cal.setGridVisible(True)   # 以网格形式显示

        self.cal.clicked.connect(self.showDate)
        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd dddd"))
        self.label.move(100, 400)

    def showDate(self, date):
        # self.label.setText((date.toString("yyyy-MM-dd dddd")))
        self.label.setText((self.cal.selectedDate().toString("yyyy-MM-dd dddd")))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = calendarDemo()
    main.show()
    sys.exit(app.exec_())