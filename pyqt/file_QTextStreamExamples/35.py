def load_stylesheet(pyside=True):
    """
    Loads the stylesheet. Takes care of importing the rc module.

    :param pyside: True to load the pyside rc file, False to load the PyQt rc file

    :return the stylesheet string
    """
    # Smart import of the rc file
    if pyside:
        import qdarkstyle.pyside_style_rc
    else:
        import qdarkstyle.pyqt_style_rc

    # Load the stylesheet content from resources
    if not pyside:
        # PyQt 4/5 compatibility
        try:
            from PyQt4.QtCore import QFile, QTextStream
        except ImportError:
            from PyQt5.QtCore import QFile, QTextStream
    else:
        from PySide.QtCore import QFile, QTextStream

    f = QFile(":qdarkstyle/style.qss")
    if not f.exists():
        _logger().error("Unable to load stylesheet, file not found in "
                        "resources")
        return ""
    else:
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        stylesheet = ts.readAll()
        if platform.system().lower() == 'darwin':  # see issue #12 on github
            mac_fix = '''
            QDockWidget::title
            {
                background-color: #31363b;
                text-align: center;
                height: 12px;
            }
            '''
            stylesheet += mac_fix
        return stylesheet 