import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QImage, QPixmap
from cal_equity import *
# from Ui_psko import *
from psko_ui import *
from range_ui import *


class MyWindow(QMainWindow, Ui_PSKO):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('PSKO')
        self.textEdit_leftPalyers.setPlainText("900")
        self.textEdit_totalPlayers.setPlainText("1000")
        self.textEdit_startingChips.setPlainText("10000")
        self.textEdit_bountyMagnification.setPlainText("1")
        self.textInputs = []
        self.textInputs.append(self.textEdit_bountyMagnification)
        self.textInputs.append(self.textEdit_totalPlayers)
        self.textInputs.append(self.textEdit_toCall)
        self.textInputs.append(self.textEdit_curPot)
        self.textInputs.append(self.textEdit_startingChips)
        self.textInputs.append(self.textEdit_leftPalyers)
        # 计算equity
        self.calculateButton.clicked.connect(self.on_button_click)
        # 显示跟注范围
        self.rangeButton.clicked.connect(self.on_range_button_click)
        self.rangeButton_2.clicked.connect(self.on_range_button2_click)
        self.rangeButton_3.clicked.connect(self.on_range_button3_click)
        self.rangeButton_4.clicked.connect(self.on_range_button4_click)
        self.rangeButton_5.clicked.connect(self.on_range_button5_click)
        # 显示对抗的范围
        self.range_label.mousePressEvent = self.on_range_label_click
        self.range_label_2.mousePressEvent = self.on_range_label2_click
        self.range_label_3.mousePressEvent = self.on_range_label3_click
        self.range_label_4.mousePressEvent = self.on_range_label4_click
        self.range_label_5.mousePressEvent = self.on_range_label5_click

    def assure_textInput_notEmpty(self):
        for textInput in self.textInputs:
            if textInput.toPlainText() == '':
                return False
        return True

    def showImage(self, image_path):
        frame = QImage(image_path)
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene()
        scene.addItem(item)
        self.child_window.graphicsView.setScene(scene)

    def on_range_label_click(self, event):
        self.textBrowser_range.setText("88+,AQo+,AJs+")

    def on_range_label2_click(self, event):
        self.textBrowser_range.setText("66+,AJo+,ATs+,KQs")

    def on_range_label3_click(self, event):
        self.textBrowser_range.setText("22+,A2+,K8o+,K2s+,Q8s+,Q9o+,JTo+,J9s+")

    def on_range_label4_click(self, event):
        self.textBrowser_range.setText(
            "22+,A2+,K2s+,K8o+\nQ4s+,Q8o+,J6s+,J8o+\nT6s+,T8o+,95s+,98o+\n84s+,87o,74s+,76o\n63s+,53s+,43s"
        )

    def on_range_label5_click(self, event):
        self.textBrowser_range.setText("除了27o,26o这些垃圾，Almost AnyTwo")

    def on_range_button_click(self):
        self.child_window = ChildWindow()
        image_path = "images/vs_tight_range.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_range_button2_click(self):
        self.child_window = ChildWindow()
        # excel 130% zoom
        image_path = "images/vs_tight_range.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_range_button3_click(self):
        self.child_window = ChildWindow()
        image_path = "images/vs_tight_range.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_range_button4_click(self):
        self.child_window = ChildWindow()
        image_path = "images/vs_tight_range.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_range_button5_click(self):
        self.child_window = ChildWindow()
        image_path = "images/vs_tight_range.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_button_click(self, Form):
        if self.assure_textInput_notEmpty():
            curPot = float(self.textEdit_curPot.toPlainText())
            toCall = float(self.textEdit_toCall.toPlainText())
            bountyMagnification = float(
                self.textEdit_bountyMagnification.toPlainText())
            startingChips = float(self.textEdit_startingChips.toPlainText())
            left_players = float(self.textEdit_leftPalyers.toPlainText())
            total_players = float(self.textEdit_totalPlayers.toPlainText())
            equity = calculate_equity_to_call(curPot, toCall,
                                              bountyMagnification,
                                              startingChips, left_players,
                                              total_players)
            equity_percentage = "{:.2%}".format(equity)
            self.textBrowser.setText(str(equity_percentage))
        else:
            self.textBrowser.setText("输入内容不能为空")


class ChildWindow(QWidget, Ui_Range):
    def __init__(self, parent=None):
        super(ChildWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Range')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
