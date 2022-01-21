#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mishmash of PyQt5 stylesheets and custom controls that I personally use in
many of my projects.
"""
__author__ = "Dennis van Gils"
__authoremail__ = "vangils.dennis@gmail.com"
__url__ = "https://github.com/Dennis-van-Gils/python-dvg-pyqt-controls"
__date__ = "21-01-2021"
__version__ = "1.1.0"

from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QColor, QCursor

# fmt: off
# Legacy v1.0
COLOR_INDIAN_RED_2   = "rgb(225, 102, 102)"  # Changed to COLOR_LED_RED
COLOR_SPRING_GREEN_2 = "rgb(  0, 238, 118)"  # Changed to COLOR_LED_GREEN
COLOR_BISQUE_5       = "rgb(252, 218, 183)"  # Changed to COLOR_GROUP_BG
COLOR_BUTTON_BG      = "rgb(232, 232, 232)"  # Changed to COLOR_BG

# v1.1
COLOR_BG             = "rgb(240, 240, 240)"
COLOR_LED_GREEN      = "rgb(  0, 238, 118)"
COLOR_LED_RED        = "rgb(225, 102, 102)"
COLOR_LED_NEUTRAL    = "rgb(240, 240, 240)"
COLOR_GROUP_BG       = "rgb(252, 208, 173)"
COLOR_READ_ONLY      = "rgb(250, 230, 210)"
COLOR_TAB_ACTIVE     = "rgb(207, 225, 225)"
COLOR_TAB            = "rgb(234, 235, 233)"
COLOR_HOVER          = "rgb(229, 241, 251)"
COLOR_HOVER_BORDER   = "rgb(  0, 120, 215)"
COLOR_ERROR_RED      = "rgb(255,   0,   0)"
COLOR_WARNING_YELLOW = "yellow"

# Default colors for PyQtGraph, resulting in a nice contrast
# Usage:
#  import pyqtgraph as pg
#  pg.setConfigOption("background", COLOR_GRAPH_BG)
#  pg.setConfigOption("foreground", COLOR_GRAPH_FG)
#  PEN_01 = pg.mkPen(color=COLOR_PEN_PINK, width=3)
COLOR_GRAPH_BG = QColor(  0,  20,  20)  # Background
COLOR_GRAPH_FG = QColor(240, 240, 240)  # Foreground
COLOR_PEN_RED       = [255,  20,  20]
COLOR_PEN_ORANGE    = [255, 127,  39]
COLOR_PEN_YELLOW    = [255, 255,  90]
COLOR_PEN_GREEN     = [  0, 255,   0]
COLOR_PEN_TURQUOISE = [  0, 255, 255]
COLOR_PEN_BLUE      = [  0, 130, 255]
COLOR_PEN_PINK      = [255,  30, 180]
COLOR_PEN_WHITE     = [255, 255, 255]
# fmt: on

# ------------------------------------------------------------------------------
#   Style sheets
# ------------------------------------------------------------------------------

# fmt: off
SS_HOVER = (
    "QLineEdit:hover {"
        "background: " + COLOR_HOVER + ";"
        "border: 1px solid " + COLOR_HOVER_BORDER + ";}"
    "QPlainTextEdit:hover {"
        #"background: " + COLOR_HOVER + ";"  # Commented out: Ugly
        "border: 1px solid " + COLOR_HOVER_BORDER + ";}"
    "QCheckBox:hover {"
        "background: " + COLOR_HOVER + ";"
        "border: 0px solid " + COLOR_HOVER_BORDER + ";}"
    "QRadioButton:hover {"
        "background: " + COLOR_HOVER + ";"
        "border: 0px solid " + COLOR_HOVER_BORDER + ";}")

SS_TEXTBOX_READ_ONLY = (
    "QLineEdit {"
        "padding: 0 2px;"
        "border: 1px solid black;}"
    "QLineEdit:read-only {"
        "border: 1px solid gray;"
        "background: " + COLOR_READ_ONLY + ";}"
    "QLineEdit:hover {"
        "background: " + COLOR_HOVER + ";"
        "border: 1px solid " + COLOR_HOVER_BORDER + ";}"
    "QLineEdit:read-only:hover {"
        "background: " + COLOR_READ_ONLY + ";"
        "border: 1px solid " + COLOR_HOVER_BORDER + ";}"

    "QPlainTextEdit {"
        "border: 1px solid black;}"
    'QPlainTextEdit[readOnly=\"true\"] {'
        "background-color: " + COLOR_READ_ONLY + ";"
        "border: 1px solid gray;}"
    "QPlainTextEdit:hover {"
        #"background: " + COLOR_HOVER + ";"  # Commented out: Ugly
        "border: 1px solid " + COLOR_HOVER_BORDER + ";}"
    'QPlainTextEdit[readOnly=\"true\"]:hover {'
        "background-color: " + COLOR_READ_ONLY + ";"
        "border: 1px solid " + COLOR_HOVER_BORDER + ";}"
)

SS_TEXTBOX_ERRORS = (
    "QLineEdit {"
        "padding: 0 2px;"
        "border: 1px solid gray;"
        "background: " + COLOR_READ_ONLY + ";}"
    "QLineEdit:hover {"
        #"background: " + COLOR_HOVER + ";"  # Commented out: Ugly
        "border: 1px solid " + COLOR_HOVER_BORDER + ";}"
    "QLineEdit:read-only {"
        "border: 2px solid red;"
        "background: " + COLOR_WARNING_YELLOW + ";"
        "color: black;}"

    "QPlainTextEdit {"
        "border: 1px solid gray;"
        "background-color: " + COLOR_READ_ONLY + ";}"
    "QPlainTextEdit:hover {"
        "border: 1px solid " + COLOR_HOVER_BORDER + ";}"
    'QPlainTextEdit[readOnly=\"true\"] {'
        "border: 2px solid red;"
        "background-color: " + COLOR_WARNING_YELLOW + ";"
        "color: black;}")

SS_TABS = (
    "QTabWidget::pane {"
        "border: 0px solid gray;}"
    "QTabBar::tab:selected {"
        "background: " + COLOR_TAB_ACTIVE + "; "
        "border-bottom-color: " + COLOR_TAB_ACTIVE + ";}"
    "QTabWidget>QWidget>QWidget {"
        "border: 2px solid gray;"
        "background: " + COLOR_TAB_ACTIVE + ";} "
    "QTabBar::tab {"
        "background: " + COLOR_TAB + ";"
        "border: 2px solid gray;"
        "border-bottom-color: " + COLOR_TAB + ";"
        "border-top-left-radius: 4px;"
        "border-top-right-radius: 4px;"
        "min-width: 119px;"
        "padding: 6px;} "
    "QTabBar::tab:hover {"
        "background: " + COLOR_HOVER + ";"
        "border: 2px solid " + COLOR_HOVER_BORDER + ";"
        "border-bottom-color: " + COLOR_HOVER + ";"
        "border-top-left-radius: 4px;"
        "border-top-right-radius: 4px;"
        "padding: 6px;} "
    "QTabWidget::tab-bar {"
        "left: 0px;}")

SS_GROUP = (
    "QGroupBox {"
        "background-color: " + COLOR_GROUP_BG + ";"
        "border: 2px solid gray;"
        "border-radius: 5px;"
        "font: bold;"
        "padding: 8 0 0 0px;"
        "margin-top: 2ex;}"
    "QGroupBox:title {"
        "subcontrol-origin: margin;"
        "subcontrol-position: top left;"
        "padding: 0 3px;}"
    "QGroupBox:flat {"
        "border: 0px;"
        "border-radius: 0 0px;"
        "padding: 0;}"
)

SS_GROUP_RECT = (
    "QGroupBox {"
        "background-color: " + COLOR_GROUP_BG + ";"
        "border: 2px solid gray;"
        "border-radius: 0px;"
        "font: bold;"
        "margin: 0;"
        "padding: 14 0 0 0px;}"
    "QGroupBox::title {"
        "subcontrol-origin: margin;"
        "subcontrol-position: top left;"
        "margin: 0;"
        "padding: 0;"
        "top: 4 px;"
        "left: 4 px;}"
    "QGroupBox:flat {"
        "border: 0px;"
        "border-radius: 0 0px;"
        "padding: 0;}"
)

SS_TITLE = (
    "QLabel {"
        "background-color: " + COLOR_GROUP_BG + ";"
        "padding: 10px;"
        "border-radius: 5px;"
        "font: bold;}"
)

# ------------------------------------------------------------------------------
#   LEDs
# ------------------------------------------------------------------------------

# fmt: off
SS_LED_INDICATOR = (
    "QPushButton {"
        "background-color: " + COLOR_LED_RED + ";"
        "color: black;"
        "border: 1px solid black;"
        "border-radius: 15px;"
        "max-height: 30px;"
        "max-width: 30px;"
        "height: 30px;"
        "width: 30px;}"
    "QPushButton:checked {"
        "background-color: " + COLOR_LED_GREEN + ";}")

SS_LED_INDICATOR_RECT = (
    "QPushButton {"
        "background-color: " + COLOR_LED_RED + ";"
        "color: black;"
        "border: 1px solid black;"
        "border-radius: 0px;"
        "min-height: 30px;"
        "min-width: 60px;}"  # Was 76px in v1.0
    "QPushButton:checked {"
        "background-color: " + COLOR_LED_GREEN + ";}")

SS_ERROR_LED = (
    "QPushButton {"
        "background-color: " + COLOR_LED_GREEN + ";"
        "color: black;"
        "border: 1px solid black;"
        "border-radius: 0px;"
        "min-height: 30px;"
        "min-width: 30px;}"
    "QPushButton:checked {"
        "background-color: " + COLOR_ERROR_RED + ";"
        "font-weight: bold;}")

SS_TINY_LED =  (
    "QPushButton {"
        "background-color: " + COLOR_LED_NEUTRAL + ";"
        "color: black;"
        "border: 1px solid black;"
        "border-radius: 5px;"
        "max-height: 10px;"
        "max-width: 10px;"
        "height: 10px;"
        "width: 10px;}"
    "QPushButton:checked {"
        "background-color: " + COLOR_LED_GREEN + ";}")

SS_TINY_ERROR_LED = (
    "QPushButton {"
        "background-color: " + COLOR_LED_NEUTRAL + ";"
        "color: black;"
        "border: 1px solid black;"
        "border-radius: 5px;"
        "max-height: 10px;"
        "max-width: 10px;"
        "height: 10px;"
        "width: 10px;}"
    "QPushButton:checked {"
        "background-color: " + COLOR_ERROR_RED + ";}")
# fmt: on


def create_LED_indicator(**kwargs) -> QPushButton:
    """Useful kwargs:
      text: str, icon: QIcon, checked: bool, parent

    checked=False -> LED red
    checked=True  -> LED green
    """
    button = QPushButton(checkable=True, enabled=False, **kwargs)
    button.setStyleSheet(SS_LED_INDICATOR)
    return button


def create_LED_indicator_rect(**kwargs) -> QPushButton:
    """
    Useful kwargs:
      text: str, icon: QIcon, checked: bool, parent

    checked=False -> LED red
    checked=True  -> LED green
    """
    button = QPushButton(checkable=True, enabled=False, **kwargs)
    button.setStyleSheet(SS_LED_INDICATOR_RECT)
    return button


def create_error_LED(**kwargs) -> QPushButton:
    """
    Useful kwargs:
      text: str, icon: QIcon, checked: bool, parent

    checked=False -> LED green
    checked=True  -> error red
    """
    button = QPushButton(checkable=True, enabled=False, **kwargs)
    button.setStyleSheet(SS_ERROR_LED)
    return button


def create_tiny_LED(**kwargs) -> QPushButton:
    """
    Useful kwargs:
      text: str, icon: QIcon, checked: bool, parent

    checked=False -> LED neutral
    checked=True  -> LED green
    """
    button = QPushButton(checkable=True, enabled=False, **kwargs)
    button.setStyleSheet(SS_TINY_LED)
    return button


def create_tiny_error_LED(**kwargs) -> QPushButton:
    """
    Useful kwargs:
      text: str, icon: QIcon, checked: bool, parent

    checked=False -> LED neutral
    checked=True  -> error red
    """
    button = QPushButton(checkable=True, enabled=False, **kwargs)
    button.setStyleSheet(SS_TINY_ERROR_LED)
    return button


# ------------------------------------------------------------------------------
#   Toggle buttons
# ------------------------------------------------------------------------------

DFLT_TOGGLE_BTN_PADDING = "6px 6px 6px 6px"
DFLT_TOGGLE_BTN_BORDER_WIDTH = "2px"
DFLT_TOGGLE_BTN_BORDER_RADIUS = "5px"

# fmt: off
SS_RELAY_BUTTON = (
    "QPushButton {"
        "background-color: " + COLOR_LED_RED + ";"
        "border-style: inset;"
        "border-width: 1px;"
        "max-height: 30px;"
        "max-width: 30px;"
        "height: 30px;"
        "width: 30px;}"
    "QPushButton:hover {"
        "border-width: 2px;"  # Was 1px in v1.0
        "border-color: black;}"
    "QPushButton:disabled {"
        "border: 1px solid black;"
        "border-radius: 15px;"
        "color: black;}"
    "QPushButton:checked {"
        "border-style: outset;"
        "background-color: " + COLOR_LED_GREEN + ";}")

SS_TOGGLE_BUTTON = (
    "QPushButton {"
        "background-color: " + COLOR_BG + ";"
        "border-style: outset;"
        "border-color: gray dimgray dimgray gray;"
        "border-width: " + DFLT_TOGGLE_BTN_BORDER_WIDTH + ";"
        "border-radius: " + DFLT_TOGGLE_BTN_BORDER_RADIUS + ";"
        "color: black;"
        "padding: " + DFLT_TOGGLE_BTN_PADDING + ";}"
    "QPushButton:hover {"
        "background: " + COLOR_HOVER + ";"
        "border-color: " + COLOR_HOVER_BORDER + ";}"
    "QPushButton:checked {"
        "background-color: " + COLOR_LED_GREEN + ";"
        "border-style: inset;"
        "border-color: dimgray mediumspringgreen mediumspringgreen dimgray;}"
    "QPushButton:checked:hover {"
        "border-color: " + COLOR_HOVER_BORDER + ";}"
    "QPushButton:disabled {"
        "color: dimgrey;}")

SS_TOGGLE_BUTTON_2 = (
    "QPushButton {"
        "background-color: " + COLOR_BG + ";"
        "border-style: outset;"
        "border-color: gray dimgray dimgray gray;"
        "border-width: " + DFLT_TOGGLE_BTN_BORDER_WIDTH + ";"
        "border-radius: " + DFLT_TOGGLE_BTN_BORDER_RADIUS + ";"
        "color: black;"
        "padding: " + DFLT_TOGGLE_BTN_PADDING + ";}"
    "QPushButton:hover {"
        "background: " + COLOR_HOVER + ";"
        "border-color: " + COLOR_HOVER_BORDER + ";}"
    "QPushButton:checked {"
        "background-color: " + COLOR_WARNING_YELLOW + ";"
        "border-style: groove;"
        "border-color: firebrick red red firebrick;"
        "font-weight: bold;}"
    "QPushButton:checked:hover {"
        "border-color: " + COLOR_HOVER_BORDER + ";}"
    "QPushButton:disabled {"
        "color: dimgray;}")

SS_TOGGLE_BUTTON_3 = (
    "QPushButton {"
        "background-color: " + COLOR_WARNING_YELLOW +";"
        "border-style: ridge;"
        "border-color: red firebrick firebrick red;"
        "border-width: " + DFLT_TOGGLE_BTN_BORDER_WIDTH + ";"
        "border-radius: " + DFLT_TOGGLE_BTN_BORDER_RADIUS + ";"
        "color: black;"
        "padding: " + DFLT_TOGGLE_BTN_PADDING + ";"
        "font-weight: bold;}"
    "QPushButton:hover {"
        "border-color: " + COLOR_HOVER_BORDER + ";}"
    "QPushButton:checked {"
        "background-color: " + COLOR_LED_GREEN + ";"
        "border-style: inset;"
        "border-color: dimgray mediumspringgreen mediumspringgreen dimgray;"
        "border-width: " + DFLT_TOGGLE_BTN_BORDER_WIDTH + ";"
        "font-weight: normal;}"
    "QPushButton:checked:hover {"
        "border-color: " + COLOR_HOVER_BORDER + ";}"
    "QPushButton:disabled {"
        "color: dimgray;}")
# fmt: on


def create_Relay_button(text: str = "", **kwargs) -> QPushButton:
    """
    Useful kwargs:
      text: str, icon: QIcon, checked: bool, parent

    checked=False -> LED red
    checked=True  -> LED green
    """
    button = QPushButton(text=text, checkable=True, **kwargs)
    button.setStyleSheet(SS_RELAY_BUTTON)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # NOTE: Do not enable below code. There is a good reason to not change the
    # relay button label immediately at click. The text-value "0" or "1" can
    # better be set after the relay operation was deemed successful by the main
    # program.
    #
    # def set_text_clicked(button):
    #    button.setText("1" if button.isChecked() else "0")
    # button.clicked.connect(lambda: set_text_clicked(button))
    # set_text_clicked(button)

    return button


def create_Toggle_button(text: str = "", **kwargs) -> QPushButton:
    """
    Useful kwargs:
      text: str, icon: QIcon, checked: bool, parent

    checked=False -> default
    checked=True  -> LED green
    """
    button = QPushButton(text=text, checkable=True, **kwargs)
    button.setStyleSheet(SS_TOGGLE_BUTTON)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    return button


def create_Toggle_button_2(text: str = "", **kwargs) -> QPushButton:
    """
    Useful kwargs:
      text: str, icon: QIcon, checked: bool, parent

    checked=False -> default
    checked=True  -> red-lined warning yellow
    """
    button = QPushButton(text=text, checkable=True, **kwargs)
    button.setStyleSheet(SS_TOGGLE_BUTTON_2)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    return button


def create_Toggle_button_3(text: str = "", **kwargs) -> QPushButton:
    """
    Useful kwargs:
      text: str, icon: QIcon, checked: bool, parent

    checked=False -> red-lined warning yellow
    checked=True  -> LED green
    """
    button = QPushButton(text=text, checkable=True, **kwargs)
    button.setStyleSheet(SS_TOGGLE_BUTTON_3)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    return button
