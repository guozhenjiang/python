import sys
import p008_MainWinVerticalLayout

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()

    ui = p008_MainWinVerticalLayout.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    sys.exit(app.exec_())
