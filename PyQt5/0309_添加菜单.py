# https://www.learnpyqt.com/courses/start/actions-toolbars-menus/

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QPushButton, QToolBar, QAction, QStatusBar, QCheckBox
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon

# Subclass QMainWindow to customise your application's main window
# 创建 QMainWindow 的子类 MainWindow 来自定义自己应用程序的主窗口
class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle('My Awesom App')
        
        label = QLabel('THIS IS AWESOM!!!')

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        
        # Qt 命名空间有很多参数可以自定义
        # 关于 widgets 的可以参考: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        
        # 设置 central widget 时 内容默认会占据整个窗口
        self.setCentralWidget(label)
        
        toolbar = QToolBar('My main toolbar')
        self.addToolBar(toolbar)
        
        button_action = QAction(QIcon(r'.\icons\bug_16x16.png'), 'Your button', self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        
        toolbar.addSeparator()
        
        button_action2 = QAction(QIcon(r'.\icons\bug_16x16.png'), 'Your button2', self)
        button_action2.setStatusTip('This is your button2')
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        
        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar(self))
        
        menu = self.menuBar()
        menu.setNativeMenuBar(False)    # Disables the global menu bar on MacOS
        
        file_menu = menu.addMenu('&File')
        file_menu.addAction(button_action)
    
    def onMyToolBarButtonClick(self, s):
        print('click', s)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) is fine.

# 每个应用程序需要（且仅需要）一个 QApplication 实例
# 通过在命令行中传入 sys.argv 向应用程序传入参数
# 如果你确定自己不用传入参数 用 QApplication([]) 也没问题
app = QApplication(sys.argv)

window = MainWindow()
window.show()   # IMPORTANT!!!!! Windows are hidden by default.
                # 这句很重要 窗口默认是隐藏状态

# Start the event loop.
# 启动应用程序的事件循环
app.exec_()

# Your application won't reach here until you exit and the event
# loop has stopped.

# 在退出事件循环之前 应用程序不会运行到这里