def load_stylesheet_pyqt5():
    """
    Load the stylesheet for use in a pyqt5 application.

    :param pyside: True to load the pyside rc file, False to load the PyQt rc file

    :return the stylesheet string
    """
    warnings.warn(
        "load_stylesheet_pyqt5() will be deprecated in version 3,"
        "set QtPy environment variable to specify the Qt binding and "
        "use load_stylesheet()",
        PendingDeprecationWarning
    )
    # Smart import of the rc file
    import qdarkstyle.pyqt5_style_rc

    # Load the stylesheet content from resources
    from PyQt5.QtCore import QFile, QTextStream

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