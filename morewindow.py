'''
容纳多文档的窗口
QMdiArea
QMdiSubWindow
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MultiWindows(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MultiWindows, self).__init__(parent)
        self.setWindowTitle("容纳多文档的窗口")
        self.mdi = QMdiArea()   # 容纳多文档的对象
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.triggered.connect(self.windowaction)

    def windowaction(self, q):
        print(q.text())
        if q.text() == "New":
            MultiWindows.count = MultiWindows.count + 1
            sub = QMdiSubWindow()   # 创建一个子窗口
            sub.setWidget(QTextEdit())  # 在子窗口设置控件
            sub.setWindowTitle("子窗口" + str(MultiWindows.count))
            self.mdi.addSubWindow(sub)  # 添加
            sub.show()
        elif q.text() == "cascade":
            self.mdi.cascadeSubWindows()    #   排列
        elif q.text() == "Tiled":   # 平铺
            self.mdi.tileSubWindows()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    demo = MultiWindows()

    demo.show()

    sys.exit(app.exec_())