import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from cal_equity import *
from Ui_psko import *
class MyWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
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
        self.calculateButton.clicked.connect(self.on_button_click)
    
    def assure_textInput_notEmpty(self):
        for textInput in self.textInputs:
            if textInput.toPlainText() == '':
                return False
        return True
    
    def on_button_click(self, Form):
        if self.assure_textInput_notEmpty():
            curPot = float(self.textEdit_curPot.toPlainText())
            toCall = float(self.textEdit_toCall.toPlainText())
            bountyMagnification = float(self.textEdit_bountyMagnification.toPlainText())
            startingChips = float(self.textEdit_startingChips.toPlainText())
            left_players = float(self.textEdit_leftPalyers.toPlainText())
            total_players = float(self.textEdit_totalPlayers.toPlainText())
            equity = calculate_equity_to_call(curPot, toCall, bountyMagnification, startingChips, left_players, total_players)
            equity_percentage = "{:.2%}".format(equity)
            self.textBrowser.setText(str(equity_percentage))
        else:
            self.textBrowser.setText("输入内容不能为空")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
