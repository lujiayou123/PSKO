import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QImage, QPixmap
from cal_equity import *
from Ui_psko import *
# from psko_ui import *
from range_ui import *


class MyWindow(QMainWindow, Ui_PSKO):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('PSKO（chipEV）')
        self.chipMode = True  # chip / bb
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
        self.calculateButton.clicked.connect(self.on_calculate_button_click)
        # 计算赏金价值
        self.button_transferBountyWorth.clicked.connect(self.on_transferBountyWorth_button_click)
        # 切换筹码显示
        self.switchChipButton.clicked.connect(self.on_switchChip_button_click)
        # 显示跟注范围
        self.rangeButton.clicked.connect(self.on_range_button_click)
        self.rangeButton_2.clicked.connect(self.on_range_button2_click)
        self.rangeButton_3.clicked.connect(self.on_range_button3_click)
        self.rangeButton_4.clicked.connect(self.on_range_button4_click)
        self.rangeButton_5.clicked.connect(self.on_range_button5_click)
        self.rangeButton_11.clicked.connect(self.on_range_button11_click)
        self.rangeButton_12.clicked.connect(self.on_range_button12_click)
        self.rangeButton_13.clicked.connect(self.on_range_button13_click)
        self.rangeButton_14.clicked.connect(self.on_range_button14_click)
        self.rangeButton_15.clicked.connect(self.on_range_button15_click)
        # 显示对抗的范围
        self.range_label.mousePressEvent = self.on_range_label_click
        self.range_label_2.mousePressEvent = self.on_range_label2_click
        self.range_label_3.mousePressEvent = self.on_range_label3_click
        self.range_label_4.mousePressEvent = self.on_range_label4_click
        self.range_label_5.mousePressEvent = self.on_range_label5_click
        self.range_label_11.mousePressEvent = self.on_range_label11_click
        self.range_label_12.mousePressEvent = self.on_range_label12_click
        self.range_label_13.mousePressEvent = self.on_range_label13_click
        self.range_label_14.mousePressEvent = self.on_range_label14_click
        self.range_label_15.mousePressEvent = self.on_range_label15_click

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
        self.textBrowser_range.setText("A2s+,A4o+,KQo,KTs+,33+")

    def on_range_label4_click(self, event):
        self.textBrowser_range.setText(
            "A2+,K8o+,K2s+,Q8s+\nQ9o+,JTo+,J9s+,22+")

    def on_range_label5_click(self, event):
        self.textBrowser_range.setText(
            "22+,A2+,K2s+,K8o+\nQ4s+,Q8o+,J6s+,J8o+\nT6s+,T8o+,95s+,98o+\n84s+,87o,74s+,76o\n63s+,53s+,43s"
        )

    # 5bb jaming
    def on_range_label11_click(self, event):
        self.textBrowser_range.setText(
            "A3o+,K9o+,QTo,JTo+\n33+,A2s+,K4s+,Q8s+\nJ8s+,T8s+,89s")

    # cold call short stack jaming, not allin
    def on_range_label12_click(self, event):
        self.textBrowser_range.setText(
            "A5o+,K9o+,QTo+,JTo+\nA2s+,K4s+,Q8s+,J8s+\nT7s+,97s+,86s+,67s\n65s,22+"
        )

    # short stack jam, middle stack cold call, late postion jaming attack
    def on_range_label13_click(self, event):
        self.textBrowser_range.setText("A8o+,KJo+,A4s+,K9s+\nQTs+,JTs+,55+")

    # Multiway, vs 1 big stack, and several(>=1) short stacks
    def on_range_label14_click(self, event):
        self.textBrowser_range.setText(
            "[1]A5o+,KTo+,QJo+,A2s+\nK9s+,QTs+,JTs,44+\n[2]A8o+,KJo+,A3s+,K9s+\nQTs+,JTs,33+\n"
        )

    # Multiway, vs many equal stacks
    def on_range_label15_click(self, event):
        self.textBrowser_range.setText(
            "[1]A5o+,KTo+,QJo+,A2s+\nK9s+,QTs+,JTs,44+\n[2]A8o+,KJo+,A3+,K9s+\nQTs+,JTs,33+\n[3]AJo+,KQo,ATs+,KTs+\nQTs+,JTs,66+"
        )

    def on_range_button_click(self):
        self.child_window = ChildWindow()
        image_path = "images/vs_super_tight_range.png"
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
        image_path = "images/vs_standard_range.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_range_button4_click(self):
        self.child_window = ChildWindow()
        image_path = "images/vs_wide_range.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_range_button5_click(self):
        self.child_window = ChildWindow()
        image_path = "images/vs_super_wide_range.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_range_button11_click(self):
        self.child_window = ChildWindow()
        image_path = "images/vs_5bb_jam.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_range_button12_click(self):
        self.child_window = ChildWindow()
        # excel 130% zoom
        image_path = "images/vs_cold_call.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_range_button13_click(self):
        self.child_window = ChildWindow()
        image_path = "images/vs_rejaming.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_range_button14_click(self):
        self.child_window = ChildWindow()
        image_path = "images/multiway_vs_two.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_range_button15_click(self):
        self.child_window = ChildWindow()
        image_path = "images/multiway_vs_three.png"
        self.showImage(image_path)
        self.child_window.show()

    def on_calculate_button_click(self, Form):
        if self.assure_textInput_notEmpty():
            if self.chipMode:
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
                bb = int(self.textEdit_BB.toPlainText())
                curPot = float(self.textEdit_curPot.toPlainText()) * bb
                toCall = float(self.textEdit_toCall.toPlainText()) * bb
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
            self.textBrowser.setText("左侧输入内容不能为空")

    def on_transferBountyWorth_button_click(self):
        bountyMagnification = float(self.textEdit_bountyMagnification.toPlainText())
        startingChips = float(self.textEdit_startingChips.toPlainText())
        left_players = float(self.textEdit_leftPalyers.toPlainText())
        total_players = float(self.textEdit_totalPlayers.toPlainText())
        bountyWorthValue = calculate_bounty_worth(bountyMagnification, startingChips, left_players, total_players)
        if self.chipMode:
            self.textBrowser_BountyWorth.setText(str(round(bountyWorthValue)))
        else:
            bb = float(self.textEdit_BB.toPlainText())
            self.textBrowser_BountyWorth.setText(str(round(bountyWorthValue/bb, 1)) + "BB")
    
    def on_switchChip_button_click(self):
        # Chip->BB，确保输入非空
        if self.textEdit_BB.toPlainText() == "":
            self.textBrowser.setText("请输入大盲(一个大盲等于多少筹码)")
        # 确保输入合规
        else:
            if not self.textEdit_BB.toPlainText().isnumeric():
                self.textBrowser.setText("请在大盲位置输入合规的数字")
            # 一切合规之后
            else:
                self.chipMode = not self.chipMode
                if self.chipMode:
                    self.switchChipButton.setText("Chip")
                else:
                    self.switchChipButton.setText("BB")
                self.clear()
                # TODO: 不需要对已经输入的筹码进行换算，直接输入BB数量即可
    
    def clear(self):
        self.textBrowser.setText("")
        self.textBrowser_BountyWorth.setText("")

class ChildWindow(QWidget, Ui_Range):
    def __init__(self, parent=None):
        super(ChildWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Range')


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
