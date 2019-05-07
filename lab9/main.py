import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QRectF
from paint import Paint
from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
from cluster_analysis import Cluster_Analysis, RANGE_OF_CHEBYSHEV, RANGE_OF_EUCLID, deepcopy


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.mode = RANGE_OF_EUCLID
        self.cluster_analysis = None
        self.btnDefault = "background-color: #87CEFA"
        self.btnActive = "background-color: #4682B4"

    def init_UI(self):
        self.paint = Paint()
        self.ui.layout.addWidget(self.paint)
        self.ui.put_points.clicked.connect(self.put_points)
        self.ui.put_clusters.clicked.connect(self.put_clusters)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.calculation.clicked.connect(self.calculation)
        self.ui.step.clicked.connect(self.step)
        self.ui.comboBox.addItems(['Euclid', 'Chebyshev'])
        self.ui.comboBox.activated.connect(self.select_mode)

    def select_mode(self, index):
        dictionary = {0: RANGE_OF_EUCLID, 1: RANGE_OF_CHEBYSHEV}
        self.mode = dictionary[index]
    
    def resizeEvent(self, event):
        self.paint.setSceneRect(QRectF(self.paint.viewport().rect()))

    def put_points(self):
        self.paint.paint = True
        self.paint.put_clusters = False
        self.ui.put_points.setStyleSheet(self.btnActive)
        self.ui.put_clusters.setStyleSheet(self.btnDefault)

    def put_clusters(self):
        self.paint.paint = True
        self.paint.put_clusters = True
        self.ui.put_points.setStyleSheet(self.btnDefault)
        self.ui.put_clusters.setStyleSheet(self.btnActive)

    def clear(self):
        self.paint.isdelete = True
        self.ui.comboBox.setEnabled(True)
        self.ui.put_points.setStyleSheet(self.btnDefault)
        self.ui.put_clusters.setStyleSheet(self.btnDefault)
        self.ui.put_points.setEnabled(True)
        self.ui.put_clusters.setEnabled(True)
        self.ui.step.setDisabled(True)
        self.ui.calculation.setEnabled(True)
        self.paint.paint = False
        self.paint.coords_clusters.clear()
        self.paint.coords_points.clear()
        self.paint.clusters.clear()
        self.paint.points.clear()
        self.paint.scene.clear()
        self.cluster_analysis = None

    def calculation(self):
        if len(self.paint.clusters) < 1: return
        self.ui.put_points.setStyleSheet(self.btnDefault)
        self.ui.put_clusters.setStyleSheet(self.btnDefault)
        self.ui.put_points.setDisabled(True)
        self.ui.put_clusters.setDisabled(True)
        self.ui.step.setEnabled(True)
        self.ui.comboBox.setDisabled(True)
        self.ui.calculation.setDisabled(True)
        self.cluster_analysis = Cluster_Analysis(
                                                 self.paint.coords_points, 
                                                 self.paint.coords_clusters, 
                                                 self.mode)

    def step(self):
        result, coords = self.cluster_analysis.step()
        self.last_step(coords) if result else self.intermed_step(coords)
            
    def intermed_step(self, coords_clusters):
        self.paint.coords_clusters = deepcopy(coords_clusters)
        for coords, clusters in zip(coords_clusters, self.paint.clusters):
            clusters.setRect(QRectF(coords[0], coords[1], 15, 15))

    def last_step(self, coords_poins):
        self.ui.put_points.setEnabled(True)
        self.ui.put_clusters.setEnabled(True)
        self.ui.step.setDisabled(True)
        self.ui.comboBox.setEnabled(True)
        self.ui.calculation.setEnabled(True)
        self.paint.redraw_points(coords_poins)

    
            





if __name__ == '__main__':
    application = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    sys.exit(application.exec_())