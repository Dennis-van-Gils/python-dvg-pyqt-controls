#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from typing import List

# Mechanism to support both PyQt and PySide
# -----------------------------------------

PYQT5 = "PyQt5"
PYQT6 = "PyQt6"
PYSIDE2 = "PySide2"
PYSIDE6 = "PySide6"
QT_LIB_ORDER = [PYQT5, PYSIDE2, PYSIDE6, PYQT6]
QT_LIB = None

# Parse optional cli argument to enfore a QT_LIB
# cli example: python benchmark.py pyside6
if len(sys.argv) > 1:
    arg1 = str(sys.argv[1]).upper()
    for i, lib in enumerate(QT_LIB_ORDER):
        if arg1 == lib.upper():
            QT_LIB = lib
            break

if QT_LIB is None:
    for lib in QT_LIB_ORDER:
        if lib in sys.modules:
            QT_LIB = lib
            break

if QT_LIB is None:
    for lib in QT_LIB_ORDER:
        try:
            __import__(lib)
            QT_LIB = lib
            break
        except ImportError:
            pass

if QT_LIB is None:
    this_file = __file__.split(os.sep)[-1]
    raise ImportError(
        f"{this_file} requires PyQt5, PyQt6, PySide2 or PySide6; "
        "none of these packages could be imported."
    )

# fmt: off
# pylint: disable=import-error, no-name-in-module
if QT_LIB == PYQT5:
    from PyQt5 import QtCore, QtGui, QtWidgets as QtWid    # type: ignore
elif QT_LIB == PYQT6:
    from PyQt6 import QtCore, QtGui, QtWidgets as QtWid    # type: ignore
elif QT_LIB == PYSIDE2:
    from PySide2 import QtCore, QtGui, QtWidgets as QtWid  # type: ignore
elif QT_LIB == PYSIDE6:
    from PySide6 import QtCore, QtGui, QtWidgets as QtWid  # type: ignore
# pylint: enable=import-error, no-name-in-module
# fmt: on

# pylint: disable=c-extension-no-member
QT_VERSION = (
    QtCore.QT_VERSION_STR if QT_LIB in (PYQT5, PYQT6) else QtCore.__version__
)
print(f"{QT_LIB:9s} {QT_VERSION}")
# pylint: enable=c-extension-no-member

# \end[Mechanism to support both PyQt and PySide]
# -----------------------------------------------

import dvg_pyqt_controls as c

# ------------------------------------------------------------------------------
#   MainWindow
# ------------------------------------------------------------------------------


class MainWindow(QtWid.QWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.setGeometry(350, 50, 800, 660)
        self.setWindowTitle("Demo: dvg_pyqt_controls")
        self.setStyleSheet(c.SS_GROUP)

        # Adjust font size while keeping default font family
        self.main_font = QtGui.QFont(QtGui.QGuiApplication.font().family(), 9)
        self.setFont(self.main_font)  # Keep
        QtGui.QGuiApplication.setFont(self.main_font)  # Keep

        def add2grid(
            grid: QtWid.QGridLayout,
            labels: List[QtWid.QWidget],
            controls: List[QtWid.QWidget],
        ):
            for idx, control in enumerate(controls):
                row_idx = grid.rowCount()
                grid.addWidget(labels[idx], row_idx, 0)
                grid.addWidget(control, row_idx, 1)

        def add2box(
            hbox,
            create_control_fun,
            N: int = 8,
            unchecked_text: str = "Off",
            checked_text: str = "On",
            **kwargs,
        ):
            controls = list()
            labels = list()
            for k in range(N):
                if k < 2:
                    checked = False
                    enabled = False
                elif k < 4:
                    checked = True
                    enabled = False
                elif k < 6:
                    checked = False
                    enabled = True
                else:
                    checked = True
                    enabled = True

                control_text = checked_text if checked else unchecked_text
                label_text = "Enabled & " if enabled else "Disabled & "
                label_text += "True" if checked else "False"

                control = create_control_fun(
                    checked=checked, text=control_text, **kwargs
                )
                control.setEnabled(enabled)
                controls.append(control)
                labels.append(QtWid.QLabel(text=label_text))

            if N == 8:
                controls[4].clicked.connect(
                    lambda state: controls[4].setText(
                        checked_text if state else unchecked_text
                    )
                )
                controls[5].clicked.connect(
                    lambda state: controls[5].setText(
                        checked_text if state else unchecked_text
                    )
                )
                controls[6].clicked.connect(
                    lambda state: controls[6].setText(
                        checked_text if state else unchecked_text
                    )
                )
                controls[7].clicked.connect(
                    lambda state: controls[7].setText(
                        checked_text if state else unchecked_text
                    )
                )

            grid = QtWid.QGridLayout()
            add2grid(grid, labels, controls)
            grid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

            if create_control_fun.__name__ == "create_Relay_button":
                grid.setVerticalSpacing(0)

            descr = create_control_fun.__name__
            descr = descr.replace("create_", "")
            descr = descr.replace("_", " ")
            grpb = QtWid.QGroupBox(descr)
            grpb.setLayout(grid)

            hbox.addWidget(
                grpb
            )  # , stretch=0, alignment=QtCore.Qt.AlignmentFlag.AlignTop)
            return (controls, labels)

        # ----------------------------------------------------------------------
        #   LEDs
        # ----------------------------------------------------------------------

        hbox_1 = QtWid.QHBoxLayout()
        add2box(hbox_1, c.create_LED_indicator, 4, "0", "1")
        add2box(hbox_1, c.create_LED_indicator_rect, 4)
        add2box(hbox_1, c.create_error_LED, 4, "0", "1")
        add2box(hbox_1, c.create_tiny_LED, 4, "", "")
        add2box(hbox_1, c.create_tiny_error_LED, 4, "", "")

        # ----------------------------------------------------------------------
        #   Buttons
        # ----------------------------------------------------------------------

        hbox_2 = QtWid.QHBoxLayout()
        add2box(hbox_2, c.create_Relay_button, 8, "0", "1")
        add2box(
            hbox_2, c.create_Toggle_button, 8, "False", "True", minimumWidth=80
        )
        add2box(
            hbox_2,
            c.create_Toggle_button_2,
            8,
            "Off Okay",
            "!! ON !!",
            minimumWidth=80,
        )
        add2box(
            hbox_2,
            c.create_Toggle_button_3,
            8,
            "!! OFF !!",
            "On Okay",
            minimumWidth=80,
        )

        # ----------------------------------------------------------------------
        #   Other style sheets
        # ----------------------------------------------------------------------

        hbox_3 = QtWid.QHBoxLayout()

        # SS_TEXTBOX_READ_ONLY
        qlin_1 = QtWid.QLineEdit("Normal")
        qlin_2 = QtWid.QLineEdit("Read-only")
        qpte_1 = QtWid.QPlainTextEdit("Normal")
        qpte_2 = QtWid.QPlainTextEdit("Read-only")
        qlin_2.setReadOnly(True)
        qpte_2.setReadOnly(True)
        for control in [qlin_1, qlin_2, qpte_1, qpte_2]:
            control.setStyleSheet(c.SS_TEXTBOX_READ_ONLY)

        grid = QtWid.QGridLayout()
        grid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        grid.addWidget(qlin_1, 0, 0)
        grid.addWidget(qlin_2, 1, 0)
        grid.addWidget(qpte_1, 2, 0)
        grid.addWidget(qpte_2, 3, 0)

        grpb = QtWid.QGroupBox("SS_TEXTBOX_READ_ONLY")
        grpb.setLayout(grid)

        hbox_3.addWidget(grpb)

        # SS_TEXTBOX_ERRORS
        qlin_1 = QtWid.QLineEdit("Normal")
        qlin_2 = QtWid.QLineEdit("Read-only --> ERROR")
        qpte_1 = QtWid.QPlainTextEdit("Normal")
        qpte_2 = QtWid.QPlainTextEdit("Read-only --> ERROR")
        qlin_2.setReadOnly(True)
        # qlin_2.setEnabled(False)
        qpte_2.setReadOnly(True)
        # qpte_2.setEnabled(False)
        for control in [qlin_1, qlin_2, qpte_1, qpte_2]:
            control.setStyleSheet(c.SS_TEXTBOX_ERRORS)

        grid = QtWid.QGridLayout()
        grid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        grid.addWidget(qlin_1, 0, 0)
        grid.addWidget(qlin_2, 1, 0)
        grid.addWidget(qpte_1, 2, 0)
        grid.addWidget(qpte_2, 3, 0)

        grpb = QtWid.QGroupBox("SS_TEXTBOX_ERRORS")
        grpb.setLayout(grid)

        hbox_3.addWidget(grpb)

        # SS_TITLE
        qlbl = QtWid.QLabel(
            "QLabel using SS_TITLE", font=QtGui.QFont("Verdana", 12)
        )
        qlbl.setStyleSheet(c.SS_TITLE)

        # PyQt defaults
        grid = QtWid.QGridLayout()
        grid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        grid.addWidget(QtWid.QPushButton("Default QPushButton"), 0, 0)
        grid.addWidget(QtWid.QLineEdit("Default QLineEdit"), 1, 0)
        grid.addWidget(QtWid.QTextEdit("Default QTextEdit"), 2, 0)

        grpb = QtWid.QGroupBox("PyQt defaults using SS_GROUP_RECT")
        grpb.setStyleSheet(c.SS_GROUP_RECT)
        grpb.setLayout(grid)

        vbox_sub = QtWid.QVBoxLayout()
        vbox_sub.addWidget(qlbl)
        vbox_sub.addWidget(grpb)

        hbox_3.addLayout(vbox_sub)

        # -------------------------
        #   Round up full window
        # -------------------------

        hbox_1.addStretch()
        hbox_2.addStretch()
        hbox_3.addStretch()

        vbox = QtWid.QVBoxLayout(self)
        vbox.addLayout(hbox_1, stretch=0)
        vbox.addLayout(hbox_2, stretch=0)
        vbox.addLayout(hbox_3, stretch=0)
        vbox.addStretch()


# ------------------------------------------------------------------------------
#   Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QtWid.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    if QT_LIB in (PYQT5, PYSIDE2):
        sys.exit(app.exec_())
    else:
        sys.exit(app.exec())
