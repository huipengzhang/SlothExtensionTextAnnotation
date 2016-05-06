"""
Configuration file for annotation tool SLOTH: https://github.com/cvhciKIT/sloth

TextRectItem: Extented RectItem. Add text annotation for text detection data preparation

Author: Yiye Lin 

version 1.0

"""

from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4.Qt import *
from sloth.items import *
from PyQt4.QtCore import *
import sys


class textRectItem(BaseItem):
    def __init__(self, model_item=None, prefix="", parent=None):
        BaseItem.__init__(self, model_item, prefix, parent)

        self._rect = None
        self._resize = False
        self._resize_start = None
        self._resize_start_rect = None
        self._upper_half_clicked = None
        self._left_half_clicked = None

        self._updateRect(self._dataToRect(self._model_item))
        LOG.debug("Constructed rect %s for model item %s" %
                  (self._rect, model_item))

    def __call__(self, model_item=None, parent=None):
        item = RectItem(model_item, parent)
        item.setPen(self.pen())
        item.setBrush(self.brush())
        return item

    def _dataToRect(self, model_item):
        if model_item is None:
            return QRectF()

        try:
            return QRectF(float(model_item[self.prefix() + 'x']),
                          float(model_item[self.prefix() + 'y']),
                          float(model_item[self.prefix() + 'width']),
                          float(model_item[self.prefix() + 'height']))
        except KeyError as e:
            LOG.debug("RectItem: Could not find expected key in item: "
                      + str(e) + ". Check your config!")
            self.setValid(False)
            return QRectF()

    def _updateRect(self, rect):
        if rect == self._rect:
            return

        self.prepareGeometryChange()
        self._rect = rect
        self.setPos(rect.topLeft())

    def updateModel(self):
        self._rect = QRectF(self.scenePos(), self._rect.size())
        self._model_item.update({
            self.prefix() + 'x':      float(self._rect.topLeft().x()),
            self.prefix() + 'y':      float(self._rect.topLeft().y()),
            self.prefix() + 'width':  float(self._rect.width()),
            self.prefix() + 'height': float(self._rect.height()),
        })

    def boundingRect(self):
        return QRectF(QPointF(0, 0), self._rect.size())

    def paint(self, painter, option, widget=None):
        BaseItem.paint(self, painter, option, widget)

        pen = self.pen()
        if self.isSelected():
            pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawRect(self.boundingRect())

    def dataChange(self):
        rect = self._dataToRect(self._model_item)
        self._updateRect(rect)

    def mousePressEvent(self, event):
        #if event.modifiers() & Qt.ControlModifier != 0:
        if event.button() & Qt.RightButton != 0:
            self._resize = True
            self._resize_start = event.scenePos()
            self._resize_start_rect = QRectF(self._rect)
            self._upper_half_clicked = (event.scenePos().y() < self._resize_start_rect.center().y())
            self._left_half_clicked  = (event.scenePos().x() < self._resize_start_rect.center().x())
            event.accept()
        else:
            BaseItem.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if self._resize:
            diff = event.scenePos() - self._resize_start
            if self._left_half_clicked:
                x = self._resize_start_rect.x() + diff.x()
                w = self._resize_start_rect.width() - diff.x()
            else:
                x = self._resize_start_rect.x()
                w = self._resize_start_rect.width() + diff.x()

            if self._upper_half_clicked:
                y = self._resize_start_rect.y() + diff.y()
                h = self._resize_start_rect.height() - diff.y()
            else:
                y = self._resize_start_rect.y()
                h = self._resize_start_rect.height() + diff.y()

            rect = QRectF(QPointF(x,y), QSizeF(w, h)).normalized()

            self._updateRect(rect)
            self.updateModel()
            event.accept()
        else:
            BaseItem.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        if self._resize:
            self._resize = False
            event.accept()
        else:
            BaseItem.mouseReleaseEvent(self, event)

    def popDialog(self):
        self.dialog = QDialog()
        self.le = QLineEdit()
        self.le.setObjectName("class")
        self.le.setText(self._model_item.get("class", ""))
        self.le.selectAll()
        self.pb = QPushButton()
        self.pb.setObjectName("submit")
        self.pb.setText("Submit")
        layout = QFormLayout()
        layout.addWidget(self.le)
        layout.addWidget(self.pb)
        self.dialog.setLayout(layout)
        self.dialog.connect(self.pb, SIGNAL("clicked()"), self.button_click)
        self.dialog.exec_()

    def button_click(self):
        self._text = self.le.text()
        self._model_item.update({self.prefix() + 'class':  unicode(self.le.text())})
        self.dialog.accept()

    def keyPressEvent(self, event):
        BaseItem.keyPressEvent(self, event)
        step = 1
        if event.modifiers() & Qt.ShiftModifier:
            step = 5
        if event.key() == Qt.Key_E:
            self._model_item.update({self.prefix() + 'class':  unicode("2")})
        if event.key() == Qt.Key_W:
            self._model_item.update({self.prefix() + 'class':  unicode("1")})
        if event.key() == Qt.Key_Q:
            self._model_item.update({self.prefix() + 'class':  unicode("0")})
            #self.popDialog()
            #self.updateModel()
            #event.accept()
        ds = {Qt.Key_Left:  (-step, 0),
              Qt.Key_Right: (step, 0),
              Qt.Key_Up:    (0, -step),
              Qt.Key_Down:  (0, step),
             }.get(event.key(), None)
        if ds is not None:
            if event.modifiers() & Qt.ControlModifier:
                rect = self._rect.adjusted(*((0, 0) + ds))
            else:
                rect = self._rect.adjusted(*(ds + ds))
            self._updateRect(rect)
            self.updateModel()
            event.accept()



LABELS = (
    {
        'attributes': {
            'class':      '0',
        },
        'inserter': RectItemInserter,
        'item':     textRectItem, 
        'hotkey':   '1',
        'text':     'text',
    },
    {
        'attributes': {
            'class':      '1',
        },
        'inserter': RectItemInserter,
        'item':     textRectItem, 
        'hotkey':   '2',
        'text':     'text',
    },{
        'attributes': {
            'class':      '2',
        },
        'inserter': RectItemInserter,
        'item':     textRectItem,  
        'hotkey':   '3',
        'text':     'text',
    },
)

