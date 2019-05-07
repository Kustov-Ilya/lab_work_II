from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtGui import QPen, QBrush, QColor
from itertools import product
import numpy as np


class Paint(QGraphicsView):

    def __init__(self):
        QGraphicsView.__init__(self)
        self.setSceneRect(QRectF(self.viewport().rect()))
        self.scene = QGraphicsScene()
        self.paint = False
        self.put_clusters = False
        self.isdelete = False
        self.coords_points = []
        self.coords_clusters = []
        self.clusters = []
        self.points = []
  
    def tools(self, e):
        x = e.x()
        y = e.y()
        if self.paint:
            brush = QBrush(Qt.SolidPattern)
            if self.put_clusters:
                pen = QPen(Qt.blue)
                self.coords_clusters.append([x, y])
                self.clusters.append(self.scene.addEllipse(x, y, 15, 15, pen, brush))
                self.scene.addItem(self.clusters[-1])
                self.setScene(self.scene)
            else:
                pen = QPen(Qt.black)
                self.coords_points.append([x, y])
                self.points.append(self.scene.addEllipse(x, y, 8, 8, pen, brush))
                self.scene.addItem(self.points[-1])
                self.setScene(self.scene)
            
            

        if self.isdelete:
            _ = [self.scene.removeItem(item) for item in self.items()]
            self.isdelete = False

    def mousePressEvent(self, event):
        e = QPointF(self.mapToScene(event.pos()))
        self.tools(e)

    def redraw_points(self, coords_poins):
        colors = {0: Qt.black,
                  1: Qt.green,
                  2: Qt.cyan,
                  3: Qt.yellow,
                  4: Qt.gray,
                  5: Qt.magenta,
                  6: Qt.red,
                  7:Qt.darkYellow}
        set = []
        for i in [list(product([i], set)) for i, set in coords_poins.items()]:
            set.extend(i)
        _ = [self.scene.removeItem(item) for item in self.points]
        self.points.clear()
        self.scene.clearFocus()
        brush = QBrush(Qt.SolidPattern)
        pen = QPen()
        for point in set:
            pen.setColor(colors[point[0] % 8])
            self.points.append(self.scene.addRect(point[1][0], point[1][1], 10, 10, pen, brush))
            self.scene.addItem(self.points[-1])
