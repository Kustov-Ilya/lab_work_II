from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QCheckBox, QSpacerItem, QWidget, QLabel, \
    QApplication, QPushButton, QGroupBox, QGridLayout, QHBoxLayout
from mainwindow import Ui_MainWindow
import sys
from net import HopfieldNet

SHAPE_SIDE_HEIGHT = 5
SHAPE_SIDE_WIDHT = 3


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.numberShapes = 0
        self.dict = {2: 1, 0: -1}
        self.cb = []
        self.layouts = []
        self.spasers = []
        self.layout = QHBoxLayout()
        self.sp = QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                QtWidgets.QSizePolicy.Minimum)
        self.hopfieldnet = HopfieldNet(SHAPE_SIDE_HEIGHT, SHAPE_SIDE_WIDHT)
        self.create_ui()

    def create_ui(self):
        gb = QGroupBox()
        gb.setLayout(self.layout)
        self.layout.addItem(self.sp)

        self.ui.scrollArea.setWidget(gb)
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setFixedHeight((SHAPE_SIDE_HEIGHT + 2) * 30)

        self.ui.incorrect_share.addLayout(self.Add_Shape('Incorrect'))
        self.ui.correct_share.addLayout(self.Add_Shape('Reshare'))

        self.ui.save.clicked.connect(self.Save)
        self.ui.recognize.clicked.connect(self.Recognize)
        self.ui.recognize.setEnabled(False)
        self.ui.delete_shape.clicked.connect(self.Delete_Shape)
        self.ui.add_shape.clicked.connect(self.Add_Learned_Shape)

        for _ in range(3):
            self.Add_Learned_Shape()

    def Add_Shape(self, name):
        grid = QGridLayout()
        l1 = QLabel(name)
        l1.setFont(QtGui.QFont("SansSerif", 11))
        grid.addWidget(l1, 0, 0, 1, 3)
        cb1 = [QCheckBox('', self) for _ in range(SHAPE_SIDE_HEIGHT * SHAPE_SIDE_WIDHT)]
        _ = [cb.setFixedSize(20, 20) for cb in cb1]
        for i in range(len(cb1)):
            grid.addWidget(cb1[i], i // SHAPE_SIDE_WIDHT + 1, i % SHAPE_SIDE_WIDHT)
        self.cb.append(cb1)
        self.layouts.append(grid)
        return grid

    def Add_Learned_Shape(self):
        self.numberShapes += 1
        self.layout.removeItem(self.sp)
        if self.numberShapes > 1:
            sp = QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.spasers.append(sp)
            self.layout.addItem(sp)
        l1 = QLabel(f'{self.numberShapes} share')
        l1.setFont(QtGui.QFont("SansSerif", 11))
        self.layout.addLayout(self.Add_Shape(f"{self.numberShapes} shape"))
        self.layout.addItem(self.sp)

    def Save(self):
        self.hopfieldnet.clear()
        for i in range(2, len(self.cb)):
            tmp = [self.dict[check.checkState()] for check in self.cb[i]]
            if 1 in tmp:
                self.hopfieldnet.teach(tmp)
        if len(self.hopfieldnet.shapes):
            self.ui.recognize.setEnabled(True)

    def Recognize(self):
        redict = {1: 2, -1: 0}
        rezult, reshare = self.hopfieldnet.recognize([self.dict[check.checkState()] for check in self.cb[0]])
        _ = [checkbox.setCheckState(redict[reshare[i]]) for i, checkbox in enumerate(self.cb[1])]
        self.ui.status.setText(rezult)
        self.ui.status.setFont(QtGui.QFont("SansSerif", 16))
        self.ui.status.setStyleSheet(f"color: {'red' if rezult == 'Failed' else 'green'}")

    def Delete_Shape(self):
        if self.numberShapes < 3:
            return
        self.numberShapes -= 1
        self.cb.pop()
        for i in reversed(range(self.layouts[-1].count())):
            self.layouts[-1].itemAt(i).widget().deleteLater()
        self.layout.removeItem(self.layouts[-1])
        self.layout.removeItem(self.spasers[-1])
        self.spasers.pop()
        self.layouts.pop()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
