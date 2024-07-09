# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QStackedWidget,
    QVBoxLayout, QWidget)
import ui_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1007, 644)
        icon = QIcon()
        icon.addFile(u":/forms/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: r"
                        "gb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#leftbotton_logo .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#leftbotton_logo .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#ti"
                        "tleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extr"
                        "a Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPu"
                        "shButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* ////////////////////"
                        "/////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-to"
                        "p-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QS"
                        "crollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: no"
                        "ne;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub"
                        "-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background: 3px solid rgb(94, 106, 130);\n"
"}\n"
"\n"
"\n"
"/* ///////////////////////////////////////"
                        "//////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, "
                        "150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/forms/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover "
                        "{\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
""
                        "}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.stylesheet)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.contentBox = QFrame(self.stylesheet)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setMinimumSize(QSize(0, 0))
        self.contentBox.setMaximumSize(QSize(16777215, 16777215))
        self.contentBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contentBox)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.contentBox)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(65, 0))
        self.leftMenuBg.setMaximumSize(QSize(65, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.run_btn = QPushButton(self.leftMenuBg)
        self.run_btn.setObjectName(u"run_btn")
        self.run_btn.setMinimumSize(QSize(50, 50))
        self.run_btn.setMaximumSize(QSize(50, 50))
        self.run_btn.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(220, 147, 249);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    border-radius: 25px;\n"
"    background-image: url(:/forms/icons/cil-media-play.png);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 200, 249); /* \u8bbe\u7f6e\u60ac\u505c\u72b6\u6001\u4e0b\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.run_btn.setIconSize(QSize(60, 60))

        self.verticalLayout_5.addWidget(self.run_btn)

        self.frame_4 = QFrame(self.leftMenuBg)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setStyleSheet(u"background-color: transparent;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.home = QPushButton(self.frame_4)
        self.home.setObjectName(u"home")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy)
        self.home.setMinimumSize(QSize(0, 45))
        self.home.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.home.setFont(font)
        self.home.setCursor(QCursor(Qt.PointingHandCursor))
        self.home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	background-image: url(:/forms/icons/cil-home.png);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.verticalLayout_10.addWidget(self.home)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.leftMenuBg)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 80))
        self.frame_5.setStyleSheet(u"background-color: transparent;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.console_btn = QPushButton(self.frame_5)
        self.console_btn.setObjectName(u"console_btn")
        sizePolicy.setHeightForWidth(self.console_btn.sizePolicy().hasHeightForWidth())
        self.console_btn.setSizePolicy(sizePolicy)
        self.console_btn.setMinimumSize(QSize(0, 45))
        self.console_btn.setMaximumSize(QSize(16777215, 45))
        self.console_btn.setFont(font)
        self.console_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.console_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.console_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;    \n"
"	background-image: url(:/forms/icons/cil-window-maximize.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_6.addWidget(self.console_btn)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_10 = QFrame(self.leftMenuBg)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 80))
        self.frame_10.setStyleSheet(u"background-color: transparent;")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.equalizer_btn = QPushButton(self.frame_10)
        self.equalizer_btn.setObjectName(u"equalizer_btn")
        sizePolicy.setHeightForWidth(self.equalizer_btn.sizePolicy().hasHeightForWidth())
        self.equalizer_btn.setSizePolicy(sizePolicy)
        self.equalizer_btn.setMinimumSize(QSize(0, 45))
        self.equalizer_btn.setMaximumSize(QSize(16777215, 45))
        self.equalizer_btn.setFont(font)
        self.equalizer_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.equalizer_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.equalizer_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;    \n"
"	background-image: url(:/forms/icons/cil-equalizer.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_9.addWidget(self.equalizer_btn)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_6 = QFrame(self.leftMenuBg)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: transparent;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.frame_6)

        self.setting_btn = QPushButton(self.leftMenuBg)
        self.setting_btn.setObjectName(u"setting_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.setting_btn.sizePolicy().hasHeightForWidth())
        self.setting_btn.setSizePolicy(sizePolicy1)
        self.setting_btn.setMinimumSize(QSize(0, 45))
        self.setting_btn.setFont(font)
        self.setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.setting_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	background-image: url(:/forms/icons/cil-settings.png);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.verticalLayout_5.addWidget(self.setting_btn)


        self.horizontalLayout_2.addWidget(self.leftMenuBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setMinimumSize(QSize(0, 0))
        self.contentBottom.setStyleSheet(u"border:none")
        self.contentBottom.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mian = QFrame(self.contentBottom)
        self.mian.setObjectName(u"mian")
        self.mian.setMinimumSize(QSize(0, 0))
        self.mian.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(47,54,60);\n"
"    color: rgb(221, 221, 221);\n"
"    font: 15pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"")
        self.mian.setFrameShape(QFrame.Shape.StyledPanel)
        self.mian.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.mian)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.mian)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_12 = QVBoxLayout(self.page_home)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea = QScrollArea(self.page_home)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"	border: none;\n"
"}\n"
"QLineEdit{\n"
"    color: rgb(221, 221, 221);\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"QComboBox{\n"
"    color: rgb(221, 221, 221);\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 831, 733))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.setting_frame = QFrame(self.scrollAreaWidgetContents)
        self.setting_frame.setObjectName(u"setting_frame")
        self.setting_frame.setMinimumSize(QSize(0, 0))
        self.setting_frame.setMaximumSize(QSize(16777215, 550))
        self.setting_frame.setStyleSheet(u"QFrame{border: none;}")
        self.setting_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.setting_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.setting_frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.audio_slicer_label = QLabel(self.setting_frame)
        self.audio_slicer_label.setObjectName(u"audio_slicer_label")
        self.audio_slicer_label.setMinimumSize(QSize(0, 60))
        self.audio_slicer_label.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_15.addWidget(self.audio_slicer_label)

        self.slicer_para_frame = QFrame(self.setting_frame)
        self.slicer_para_frame.setObjectName(u"slicer_para_frame")
        self.slicer_para_frame.setMinimumSize(QSize(0, 300))
        self.slicer_para_frame.setMaximumSize(QSize(16777215, 300))
        self.slicer_para_frame.setStyleSheet(u"border:none;")
        self.slicer_para_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.slicer_para_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.slicer_para_frame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.select_slicer_frame = QFrame(self.slicer_para_frame)
        self.select_slicer_frame.setObjectName(u"select_slicer_frame")
        self.select_slicer_frame.setAcceptDrops(True)
        self.select_slicer_frame.setStyleSheet(u"QFrame{\n"
"border:1px solid rgb(107, 114, 120);\n"
"border-radius: 10px;\n"
"border-radius: 10px;\n"
"}")
        self.select_slicer_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.select_slicer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.select_slicer_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.avatarParameter_setting = QLabel(self.select_slicer_frame)
        self.avatarParameter_setting.setObjectName(u"avatarParameter_setting")
        self.avatarParameter_setting.setStyleSheet(u"border:none;\n"
"")

        self.verticalLayout_2.addWidget(self.avatarParameter_setting)

        self.select_avatarParameter_lineedit = QLineEdit(self.select_slicer_frame)
        self.select_avatarParameter_lineedit.setObjectName(u"select_avatarParameter_lineedit")
        self.select_avatarParameter_lineedit.setMinimumSize(QSize(0, 25))
        self.select_avatarParameter_lineedit.setMaximumSize(QSize(16777215, 25))
        self.select_avatarParameter_lineedit.setStyleSheet(u"border:1px solid rgb(107, 114, 120);\n"
"border-radius: 10px;\n"
"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"border-radius: 5px;	")
        self.select_avatarParameter_lineedit.setReadOnly(False)

        self.verticalLayout_2.addWidget(self.select_avatarParameter_lineedit)

        self.avatar_listWidget = QListWidget(self.select_slicer_frame)
        self.avatar_listWidget.setObjectName(u"avatar_listWidget")
        self.avatar_listWidget.setMinimumSize(QSize(200, 150))
        self.avatar_listWidget.setAcceptDrops(False)
        self.avatar_listWidget.setStyleSheet(u"QListWidget\n"
"{\n"
"	border:1px solid rgb(107, 114, 120);\n"
"	border-radius: 10px;\n"
"	font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	border-radius: 10px;	\n"
"}\n"
"QListWidget::item:selected\n"
"{\n"
"	background-color:rgb(38,71,99);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.avatar_listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.avatar_listWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.avatar_listWidget.setProperty("showDropIndicator", False)
        self.avatar_listWidget.setDragEnabled(False)
        self.avatar_listWidget.setDragDropOverwriteMode(False)
        self.avatar_listWidget.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.avatar_listWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.avatar_listWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)

        self.verticalLayout_2.addWidget(self.avatar_listWidget)

        self.select_slicer_frame_3 = QFrame(self.select_slicer_frame)
        self.select_slicer_frame_3.setObjectName(u"select_slicer_frame_3")
        self.select_slicer_frame_3.setStyleSheet(u"border:none;")
        self.select_slicer_frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.select_slicer_frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.select_slicer_frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.change_avater_btn = QPushButton(self.select_slicer_frame_3)
        self.change_avater_btn.setObjectName(u"change_avater_btn")
        self.change_avater_btn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(42, 62, 80);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(110, 119, 138);\n"
"   	color: rgb(221, 221, 221);\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	border-radius: 7px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.change_avater_btn)

        self.add_avatar_btn = QPushButton(self.select_slicer_frame_3)
        self.add_avatar_btn.setObjectName(u"add_avatar_btn")
        self.add_avatar_btn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(42, 62, 80);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(110, 119, 138);\n"
"   	color: rgb(221, 221, 221);\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	border-radius: 7px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.add_avatar_btn)

        self.delect_avatar_btn = QPushButton(self.select_slicer_frame_3)
        self.delect_avatar_btn.setObjectName(u"delect_avatar_btn")
        self.delect_avatar_btn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(42, 62, 80);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(110, 119, 138);\n"
"   	color: rgb(221, 221, 221);\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	border-radius: 7px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.delect_avatar_btn)


        self.verticalLayout_2.addWidget(self.select_slicer_frame_3)


        self.horizontalLayout_17.addWidget(self.select_slicer_frame)

        self.slicer_setting_frame = QFrame(self.slicer_para_frame)
        self.slicer_setting_frame.setObjectName(u"slicer_setting_frame")
        self.slicer_setting_frame.setStyleSheet(u"QFrame{\n"
"border:1px solid rgb(107, 114, 120);\n"
"border-radius: 10px;\n"
"border-radius: 10px;\n"
"}")
        self.slicer_setting_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.slicer_setting_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.slicer_setting_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.slicer_setting_label = QLabel(self.slicer_setting_frame)
        self.slicer_setting_label.setObjectName(u"slicer_setting_label")
        self.slicer_setting_label.setStyleSheet(u"border:none;\n"
"")

        self.verticalLayout_8.addWidget(self.slicer_setting_label)

        self.slicer_para_frame1 = QFrame(self.slicer_setting_frame)
        self.slicer_para_frame1.setObjectName(u"slicer_para_frame1")
        self.slicer_para_frame1.setMinimumSize(QSize(0, 40))
        self.slicer_para_frame1.setMaximumSize(QSize(16777215, 40))
        self.slicer_para_frame1.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.slicer_para_frame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.slicer_para_frame1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.slicer_para_frame1)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.slicer_setting_label1 = QLabel(self.slicer_para_frame1)
        self.slicer_setting_label1.setObjectName(u"slicer_setting_label1")
        self.slicer_setting_label1.setMinimumSize(QSize(150, 0))
        self.slicer_setting_label1.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.slicer_setting_label1.setFont(font1)
        self.slicer_setting_label1.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.slicer_setting_label1)

        self.judgemode_comboBox = QComboBox(self.slicer_para_frame1)
        self.judgemode_comboBox.addItem("")
        self.judgemode_comboBox.addItem("")
        self.judgemode_comboBox.addItem("")
        self.judgemode_comboBox.setObjectName(u"judgemode_comboBox")

        self.horizontalLayout_12.addWidget(self.judgemode_comboBox)


        self.verticalLayout_8.addWidget(self.slicer_para_frame1)

        self.select_judge_lineedit = QLineEdit(self.slicer_setting_frame)
        self.select_judge_lineedit.setObjectName(u"select_judge_lineedit")
        self.select_judge_lineedit.setMinimumSize(QSize(0, 25))
        self.select_judge_lineedit.setMaximumSize(QSize(16777215, 25))
        self.select_judge_lineedit.setStyleSheet(u"border:1px solid rgb(107, 114, 120);\n"
"border-radius: 10px;\n"
"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"border-radius: 5px;	")

        self.verticalLayout_8.addWidget(self.select_judge_lineedit)

        self.judge_listWidget = QListWidget(self.slicer_setting_frame)
        self.judge_listWidget.setObjectName(u"judge_listWidget")
        self.judge_listWidget.setMinimumSize(QSize(200, 80))
        self.judge_listWidget.setMaximumSize(QSize(16777215, 9999))
        self.judge_listWidget.setAcceptDrops(False)
        self.judge_listWidget.setStyleSheet(u"QListWidget\n"
"{\n"
"	border:1px solid rgb(107, 114, 120);\n"
"	border-radius: 10px;\n"
"	font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	border-radius: 10px;	\n"
"}\n"
"QListWidget::item:selected\n"
"{\n"
"	background-color:rgb(38,71,99);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.judge_listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.judge_listWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.judge_listWidget.setProperty("showDropIndicator", False)
        self.judge_listWidget.setDragEnabled(False)
        self.judge_listWidget.setDragDropOverwriteMode(False)
        self.judge_listWidget.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.judge_listWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.judge_listWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)

        self.verticalLayout_8.addWidget(self.judge_listWidget)

        self.select_slicer_frame_4 = QFrame(self.slicer_setting_frame)
        self.select_slicer_frame_4.setObjectName(u"select_slicer_frame_4")
        self.select_slicer_frame_4.setStyleSheet(u"border:none;")
        self.select_slicer_frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.select_slicer_frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.select_slicer_frame_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.change_judge_btn = QPushButton(self.select_slicer_frame_4)
        self.change_judge_btn.setObjectName(u"change_judge_btn")
        self.change_judge_btn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(42, 62, 80);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(110, 119, 138);\n"
"   	color: rgb(221, 221, 221);\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	border-radius: 7px;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.change_judge_btn)

        self.add_judge_btn = QPushButton(self.select_slicer_frame_4)
        self.add_judge_btn.setObjectName(u"add_judge_btn")
        self.add_judge_btn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(42, 62, 80);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(110, 119, 138);\n"
"   	color: rgb(221, 221, 221);\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	border-radius: 7px;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.add_judge_btn)

        self.delect_judge_btn = QPushButton(self.select_slicer_frame_4)
        self.delect_judge_btn.setObjectName(u"delect_judge_btn")
        self.delect_judge_btn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(42, 62, 80);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(110, 119, 138);\n"
"   	color: rgb(221, 221, 221);\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	border-radius: 7px;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.delect_judge_btn)


        self.verticalLayout_8.addWidget(self.select_slicer_frame_4)


        self.horizontalLayout_17.addWidget(self.slicer_setting_frame)

        self.slicer_setting_frame_2 = QFrame(self.slicer_para_frame)
        self.slicer_setting_frame_2.setObjectName(u"slicer_setting_frame_2")
        self.slicer_setting_frame_2.setStyleSheet(u"QFrame{\n"
"border:1px solid rgb(107, 114, 120);\n"
"border-radius: 10px;\n"
"border-radius: 10px;\n"
"}")
        self.slicer_setting_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.slicer_setting_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.slicer_setting_frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.slicer_setting_label_2 = QLabel(self.slicer_setting_frame_2)
        self.slicer_setting_label_2.setObjectName(u"slicer_setting_label_2")
        self.slicer_setting_label_2.setStyleSheet(u"border:none;\n"
"")

        self.verticalLayout_9.addWidget(self.slicer_setting_label_2)

        self.slicer_para_frame1_2 = QFrame(self.slicer_setting_frame_2)
        self.slicer_para_frame1_2.setObjectName(u"slicer_para_frame1_2")
        self.slicer_para_frame1_2.setMinimumSize(QSize(0, 40))
        self.slicer_para_frame1_2.setMaximumSize(QSize(16777215, 40))
        self.slicer_para_frame1_2.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.slicer_para_frame1_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.slicer_para_frame1_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.slicer_para_frame1_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slicer_setting_label1_2 = QLabel(self.slicer_para_frame1_2)
        self.slicer_setting_label1_2.setObjectName(u"slicer_setting_label1_2")
        self.slicer_setting_label1_2.setMinimumSize(QSize(150, 0))
        self.slicer_setting_label1_2.setMaximumSize(QSize(150, 16777215))
        self.slicer_setting_label1_2.setFont(font1)
        self.slicer_setting_label1_2.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.slicer_setting_label1_2)

        self.pattem_comboBox = QComboBox(self.slicer_para_frame1_2)
        self.pattem_comboBox.setObjectName(u"pattem_comboBox")

        self.horizontalLayout_5.addWidget(self.pattem_comboBox)


        self.verticalLayout_9.addWidget(self.slicer_para_frame1_2)

        self.slicer_para_frame2_3 = QFrame(self.slicer_setting_frame_2)
        self.slicer_para_frame2_3.setObjectName(u"slicer_para_frame2_3")
        self.slicer_para_frame2_3.setMinimumSize(QSize(0, 40))
        self.slicer_para_frame2_3.setMaximumSize(QSize(16777215, 40))
        self.slicer_para_frame2_3.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.slicer_para_frame2_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.slicer_para_frame2_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.slicer_para_frame2_3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.slicer_setting_label2_2 = QLabel(self.slicer_para_frame2_3)
        self.slicer_setting_label2_2.setObjectName(u"slicer_setting_label2_2")
        self.slicer_setting_label2_2.setMinimumSize(QSize(150, 0))
        self.slicer_setting_label2_2.setMaximumSize(QSize(150, 16777215))
        self.slicer_setting_label2_2.setFont(font1)
        self.slicer_setting_label2_2.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.slicer_setting_label2_2)

        self.channel_comboBox = QComboBox(self.slicer_para_frame2_3)
        self.channel_comboBox.addItem("")
        self.channel_comboBox.addItem("")
        self.channel_comboBox.setObjectName(u"channel_comboBox")

        self.horizontalLayout_19.addWidget(self.channel_comboBox)


        self.verticalLayout_9.addWidget(self.slicer_para_frame2_3)

        self.slicer_para_frame2_4 = QFrame(self.slicer_setting_frame_2)
        self.slicer_para_frame2_4.setObjectName(u"slicer_para_frame2_4")
        self.slicer_para_frame2_4.setMinimumSize(QSize(0, 40))
        self.slicer_para_frame2_4.setMaximumSize(QSize(16777215, 16777215))
        self.slicer_para_frame2_4.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.slicer_para_frame2_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.slicer_para_frame2_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.slicer_para_frame2_4)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.frame = QFrame(self.slicer_para_frame2_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.slicer_setting_label3_3 = QLabel(self.frame)
        self.slicer_setting_label3_3.setObjectName(u"slicer_setting_label3_3")
        self.slicer_setting_label3_3.setMinimumSize(QSize(150, 0))
        self.slicer_setting_label3_3.setMaximumSize(QSize(150, 16777215))
        self.slicer_setting_label3_3.setFont(font1)
        self.slicer_setting_label3_3.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.slicer_setting_label3_3)

        self.intensity = QLineEdit(self.frame)
        self.intensity.setObjectName(u"intensity")
        self.intensity.setStyleSheet(u"border-radius: 8px;")
        self.intensity.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.intensity)


        self.verticalLayout_3.addWidget(self.frame)

        self.intensity_slider = QSlider(self.slicer_para_frame2_4)
        self.intensity_slider.setObjectName(u"intensity_slider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.intensity_slider.sizePolicy().hasHeightForWidth())
        self.intensity_slider.setSizePolicy(sizePolicy2)
        self.intensity_slider.setMaximumSize(QSize(16777215, 10))
        self.intensity_slider.setStyleSheet(u"QSlider{\n"
"	margin-top:0px;\n"
"	margin-bottom:0px;\n"
"	background-color: rgb(40, 47, 56);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 3px;\n"
"    height: 7px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 3px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}")
        self.intensity_slider.setMaximum(100)
        self.intensity_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.intensity_slider)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)

        self.verticalLayout_9.addWidget(self.slicer_para_frame2_4)

        self.slicer_para_frame2_5 = QFrame(self.slicer_setting_frame_2)
        self.slicer_para_frame2_5.setObjectName(u"slicer_para_frame2_5")
        self.slicer_para_frame2_5.setMinimumSize(QSize(0, 40))
        self.slicer_para_frame2_5.setMaximumSize(QSize(16777215, 16777215))
        self.slicer_para_frame2_5.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.slicer_para_frame2_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.slicer_para_frame2_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.slicer_para_frame2_5)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.frame_2 = QFrame(self.slicer_para_frame2_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.slicer_setting_label3_4 = QLabel(self.frame_2)
        self.slicer_setting_label3_4.setObjectName(u"slicer_setting_label3_4")
        self.slicer_setting_label3_4.setMinimumSize(QSize(150, 0))
        self.slicer_setting_label3_4.setMaximumSize(QSize(150, 16777215))
        self.slicer_setting_label3_4.setFont(font1)
        self.slicer_setting_label3_4.setStyleSheet(u"")

        self.horizontalLayout_28.addWidget(self.slicer_setting_label3_4)

        self.Ticks = QLineEdit(self.frame_2)
        self.Ticks.setObjectName(u"Ticks")
        self.Ticks.setStyleSheet(u"border-radius: 8px;")
        self.Ticks.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.Ticks)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.Ticks_slider = QSlider(self.slicer_para_frame2_5)
        self.Ticks_slider.setObjectName(u"Ticks_slider")
        sizePolicy2.setHeightForWidth(self.Ticks_slider.sizePolicy().hasHeightForWidth())
        self.Ticks_slider.setSizePolicy(sizePolicy2)
        self.Ticks_slider.setMaximumSize(QSize(16777215, 10))
        self.Ticks_slider.setStyleSheet(u"QSlider{\n"
"	margin-top:0px;\n"
"	margin-bottom:0px;\n"
"	background-color: rgb(40, 47, 56);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 3px;\n"
"    height: 7px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 3px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}")
        self.Ticks_slider.setMinimum(0)
        self.Ticks_slider.setMaximum(1000)
        self.Ticks_slider.setValue(1)
        self.Ticks_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_6.addWidget(self.Ticks_slider)

        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 1)

        self.verticalLayout_9.addWidget(self.slicer_para_frame2_5)


        self.horizontalLayout_17.addWidget(self.slicer_setting_frame_2)


        self.verticalLayout_15.addWidget(self.slicer_para_frame)


        self.verticalLayout_11.addWidget(self.setting_frame)

        self.dataset_frame = QFrame(self.scrollAreaWidgetContents)
        self.dataset_frame.setObjectName(u"dataset_frame")
        self.dataset_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.dataset_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.dataset_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.dataset_label = QLabel(self.dataset_frame)
        self.dataset_label.setObjectName(u"dataset_label")
        self.dataset_label.setMinimumSize(QSize(0, 60))
        self.dataset_label.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_16.addWidget(self.dataset_label)

        self.mark_para_frame = QFrame(self.dataset_frame)
        self.mark_para_frame.setObjectName(u"mark_para_frame")
        self.mark_para_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mark_para_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.mark_para_frame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 6)
        self.frame_9 = QFrame(self.mark_para_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.qrcode = QLabel(self.frame_9)
        self.qrcode.setObjectName(u"qrcode")
        self.qrcode.setMinimumSize(QSize(200, 200))
        self.qrcode.setMaximumSize(QSize(200, 200))
        self.qrcode.setScaledContents(True)
        self.qrcode.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.qrcode)


        self.verticalLayout_17.addWidget(self.frame_9)

        self.dglink_label = QLabel(self.mark_para_frame)
        self.dglink_label.setObjectName(u"dglink_label")
        self.dglink_label.setStyleSheet(u"color: rgb(221, 221, 221);\n"
"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.dglink_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.dglink_label)


        self.verticalLayout_16.addWidget(self.mark_para_frame)


        self.verticalLayout_11.addWidget(self.dataset_frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_home)
        self.page_console = QWidget()
        self.page_console.setObjectName(u"page_console")
        self.verticalLayout_13 = QVBoxLayout(self.page_console)
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 6, 6, 0)
        self.frame_8 = QFrame(self.page_console)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 60))
        self.label.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_8.addWidget(self.label)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.console = QPlainTextEdit(self.page_console)
        self.console.setObjectName(u"console")
        self.console.setStyleSheet(u"color: rgb(221, 221, 221);\n"
"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"background-color:rgb(27,34,40);\n"
"border-radius: 8px;")
        self.console.setReadOnly(False)
        self.console.setTextInteractionFlags(Qt.TextInteractionFlag.TextEditorInteraction)

        self.verticalLayout_13.addWidget(self.console)

        self.stackedWidget.addWidget(self.page_console)
        self.page_write = QWidget()
        self.page_write.setObjectName(u"page_write")
        self.horizontalLayout_115 = QHBoxLayout(self.page_write)
        self.horizontalLayout_115.setSpacing(10)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(9, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.page_write)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -72, 813, 670))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(800, 0))
        self.scrollAreaWidgetContents_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_38 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_38.setSpacing(10)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(700, 500))
        self.frame_35.setMaximumSize(QSize(16777215, 500))
        self.frame_35.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 37, 46);\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_35)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.avatarParameter_setting_7 = QLabel(self.frame_35)
        self.avatarParameter_setting_7.setObjectName(u"avatarParameter_setting_7")
        self.avatarParameter_setting_7.setMinimumSize(QSize(0, 20))
        self.avatarParameter_setting_7.setMaximumSize(QSize(16777215, 20))
        self.avatarParameter_setting_7.setStyleSheet(u"border:none;\n"
"")

        self.verticalLayout_81.addWidget(self.avatarParameter_setting_7)

        self.frame_108 = QFrame(self.frame_35)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(0, 120))
        self.frame_108.setMaximumSize(QSize(16777215, 120))
        self.frame_108.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 37, 46);\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.frame_108.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_108)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.frame_152 = QFrame(self.frame_108)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_152)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.intensity_label = QLabel(self.frame_152)
        self.intensity_label.setObjectName(u"intensity_label")
        self.intensity_label.setMinimumSize(QSize(120, 60))
        self.intensity_label.setMaximumSize(QSize(120, 60))
        self.intensity_label.setStyleSheet(u"font:50pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(212, 148, 249);")
        self.intensity_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_91.addWidget(self.intensity_label)


        self.verticalLayout_82.addWidget(self.frame_152)

        self.intensity_Slider = QSlider(self.frame_108)
        self.intensity_Slider.setObjectName(u"intensity_Slider")
        self.intensity_Slider.setMinimumSize(QSize(0, 10))
        self.intensity_Slider.setMaximumSize(QSize(16777215, 10))
        self.intensity_Slider.setStyleSheet(u"QSlider{\n"
"	margin-top:0px;\n"
"	margin-bottom:0px;\n"
"	background-color: rgb(30, 37, 46);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 3px;\n"
"    height: 7px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 3px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}")
        self.intensity_Slider.setMaximum(100)
        self.intensity_Slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_82.addWidget(self.intensity_Slider)


        self.verticalLayout_81.addWidget(self.frame_108)

        self.frame_153 = QFrame(self.frame_35)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setMinimumSize(QSize(0, 70))
        self.frame_153.setMaximumSize(QSize(16777215, 70))
        self.frame_153.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 37, 46);\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.frame_153.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_153)
        self.horizontalLayout_92.setSpacing(30)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(-1, 0, -1, 0)
        self.frame_154 = QFrame(self.frame_153)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 37, 46);\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.frame_154.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_154)
        self.horizontalLayout_93.setSpacing(30)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(-1, 0, -1, 0)
        self.frame_155 = QFrame(self.frame_154)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_93.addWidget(self.frame_155)

        self.A_btn = QPushButton(self.frame_154)
        self.A_btn.setObjectName(u"A_btn")
        self.A_btn.setMinimumSize(QSize(150, 40))
        self.A_btn.setMaximumSize(QSize(150, 40))
        self.A_btn.setStyleSheet(u"QPushButton {\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 34, 71);\n"
"	font: 15pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color: rgb(225, 225, 225);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_93.addWidget(self.A_btn)

        self.frame_156 = QFrame(self.frame_154)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setMinimumSize(QSize(120, 0))
        self.frame_156.setMaximumSize(QSize(120, 16777215))
        self.frame_156.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_156)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.frame_157 = QFrame(self.frame_156)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_157)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.mode_combox = QComboBox(self.frame_157)
        self.mode_combox.addItem("")
        self.mode_combox.addItem("")
        self.mode_combox.addItem("")
        self.mode_combox.setObjectName(u"mode_combox")
        self.mode_combox.setMinimumSize(QSize(100, 0))
        self.mode_combox.setMaximumSize(QSize(100, 16777215))
        self.mode_combox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.mode_combox.setStyleSheet(u"font:10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(225, 255, 255);\n"
"background-color: rgb(30, 37, 46);")

        self.horizontalLayout_94.addWidget(self.mode_combox)


        self.verticalLayout_83.addWidget(self.frame_157)

        self.frame_158 = QFrame(self.frame_156)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setMinimumSize(QSize(120, 0))
        self.frame_158.setMaximumSize(QSize(120, 16777215))
        self.frame_158.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_158)
        self.horizontalLayout_95.setSpacing(3)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, -1, -1)
        self.ticks_add_btn = QPushButton(self.frame_158)
        self.ticks_add_btn.setObjectName(u"ticks_add_btn")
        sizePolicy.setHeightForWidth(self.ticks_add_btn.sizePolicy().hasHeightForWidth())
        self.ticks_add_btn.setSizePolicy(sizePolicy)
        self.ticks_add_btn.setMinimumSize(QSize(20, 20))
        self.ticks_add_btn.setMaximumSize(QSize(20, 20))
        self.ticks_add_btn.setFont(font1)
        self.ticks_add_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ticks_add_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ticks_add_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;  \n"
"	background-image: url(:/forms/icons/add1.png);\n"
"	background-color: rgb(30, 37, 46);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: none;\n"
"}")

        self.horizontalLayout_95.addWidget(self.ticks_add_btn)

        self.Tick_label = QLabel(self.frame_158)
        self.Tick_label.setObjectName(u"Tick_label")
        self.Tick_label.setMinimumSize(QSize(35, 0))
        self.Tick_label.setMaximumSize(QSize(35, 16777215))
        self.Tick_label.setFont(font1)
        self.Tick_label.setStyleSheet(u"")

        self.horizontalLayout_95.addWidget(self.Tick_label)

        self.tick_label = QLabel(self.frame_158)
        self.tick_label.setObjectName(u"tick_label")
        self.tick_label.setMinimumSize(QSize(20, 0))
        self.tick_label.setMaximumSize(QSize(20, 16777215))
        self.tick_label.setStyleSheet(u"font:10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221,221, 221);")

        self.horizontalLayout_95.addWidget(self.tick_label)

        self.ticks_decrease_btn = QPushButton(self.frame_158)
        self.ticks_decrease_btn.setObjectName(u"ticks_decrease_btn")
        sizePolicy.setHeightForWidth(self.ticks_decrease_btn.sizePolicy().hasHeightForWidth())
        self.ticks_decrease_btn.setSizePolicy(sizePolicy)
        self.ticks_decrease_btn.setMinimumSize(QSize(20, 20))
        self.ticks_decrease_btn.setMaximumSize(QSize(20, 20))
        self.ticks_decrease_btn.setFont(font1)
        self.ticks_decrease_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ticks_decrease_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ticks_decrease_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;  \n"
"	background-image: url(:/forms/icons/decreaed2.png);\n"
"	background-color: rgb(30, 37, 46);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: none;\n"
"}")

        self.horizontalLayout_95.addWidget(self.ticks_decrease_btn)


        self.verticalLayout_83.addWidget(self.frame_158)


        self.horizontalLayout_93.addWidget(self.frame_156)

        self.B_btn = QPushButton(self.frame_154)
        self.B_btn.setObjectName(u"B_btn")
        self.B_btn.setMinimumSize(QSize(150, 40))
        self.B_btn.setMaximumSize(QSize(150, 40))
        self.B_btn.setStyleSheet(u"QPushButton {\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 34, 71);\n"
"	font: 15pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color: rgb(225, 225, 225);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_93.addWidget(self.B_btn)

        self.frame_159 = QFrame(self.frame_154)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_93.addWidget(self.frame_159)


        self.horizontalLayout_92.addWidget(self.frame_154)


        self.verticalLayout_81.addWidget(self.frame_153)

        self.frame_160 = QFrame(self.frame_35)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setMaximumSize(QSize(16777215, 14))
        self.frame_160.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_160)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(-1, 0, -1, 0)
        self.line_7 = QFrame(self.frame_160)
        self.line_7.setObjectName(u"line_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy3)
        self.line_7.setMinimumSize(QSize(0, 4))
        self.line_7.setMaximumSize(QSize(16777215, 4))
        self.line_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(30, 37, 46), stop:1 rgb(212, 148, 249));\n"
"")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_96.addWidget(self.line_7)

        self.label_67 = QLabel(self.frame_160)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(80, 0))
        self.label_67.setMaximumSize(QSize(80, 16777215))
        self.label_67.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);")
        self.label_67.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_96.addWidget(self.label_67)

        self.line_8 = QFrame(self.frame_160)
        self.line_8.setObjectName(u"line_8")
        sizePolicy3.setHeightForWidth(self.line_8.sizePolicy().hasHeightForWidth())
        self.line_8.setSizePolicy(sizePolicy3)
        self.line_8.setMinimumSize(QSize(0, 4))
        self.line_8.setMaximumSize(QSize(16777215, 4))
        self.line_8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgb(30, 37, 46), stop:0 rgb(212, 148, 249));\n"
"")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_96.addWidget(self.line_8)


        self.verticalLayout_81.addWidget(self.frame_160)

        self.frame_204 = QFrame(self.frame_35)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setMinimumSize(QSize(0, 130))
        self.frame_204.setMaximumSize(QSize(16777215, 130))
        self.frame_204.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 37, 46);\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.frame_204.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.frame_204)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.frame_205 = QFrame(self.frame_204)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_205.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_205)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.frame_206 = QFrame(self.frame_205)
        self.frame_206.setObjectName(u"frame_206")
        self.frame_206.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_206.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.frame_206)
        self.horizontalLayout_125.setSpacing(0)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, -1)
        self.btn1 = QPushButton(self.frame_206)
        self.btn1.setObjectName(u"btn1")
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setMinimumSize(QSize(60, 60))
        self.btn1.setMaximumSize(QSize(60, 60))
        self.btn1.setFont(font1)
        self.btn1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn1.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_125.addWidget(self.btn1)


        self.verticalLayout_103.addWidget(self.frame_206)

        self.frame_207 = QFrame(self.frame_205)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.frame_207)
        self.horizontalLayout_126.setSpacing(0)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.label_80 = QLabel(self.frame_207)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_80.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_126.addWidget(self.label_80)


        self.verticalLayout_103.addWidget(self.frame_207)


        self.horizontalLayout_124.addWidget(self.frame_205)

        self.frame_208 = QFrame(self.frame_204)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_208)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.frame_209 = QFrame(self.frame_208)
        self.frame_209.setObjectName(u"frame_209")
        self.frame_209.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_209.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_127 = QHBoxLayout(self.frame_209)
        self.horizontalLayout_127.setSpacing(0)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, -1)
        self.btn2 = QPushButton(self.frame_209)
        self.btn2.setObjectName(u"btn2")
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setMinimumSize(QSize(60, 60))
        self.btn2.setMaximumSize(QSize(60, 60))
        self.btn2.setFont(font1)
        self.btn2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn2.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_127.addWidget(self.btn2)


        self.verticalLayout_104.addWidget(self.frame_209)

        self.frame_210 = QFrame(self.frame_208)
        self.frame_210.setObjectName(u"frame_210")
        self.frame_210.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_210.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.frame_210)
        self.horizontalLayout_128.setSpacing(0)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.label_81 = QLabel(self.frame_210)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_81.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_128.addWidget(self.label_81)


        self.verticalLayout_104.addWidget(self.frame_210)


        self.horizontalLayout_124.addWidget(self.frame_208)

        self.frame_211 = QFrame(self.frame_204)
        self.frame_211.setObjectName(u"frame_211")
        self.frame_211.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_211.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_211)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.frame_212 = QFrame(self.frame_211)
        self.frame_212.setObjectName(u"frame_212")
        self.frame_212.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.frame_212)
        self.horizontalLayout_129.setSpacing(0)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(0, 0, 0, -1)
        self.btn3 = QPushButton(self.frame_212)
        self.btn3.setObjectName(u"btn3")
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        self.btn3.setMinimumSize(QSize(60, 60))
        self.btn3.setMaximumSize(QSize(60, 60))
        self.btn3.setFont(font1)
        self.btn3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn3.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_129.addWidget(self.btn3)


        self.verticalLayout_105.addWidget(self.frame_212)

        self.frame_213 = QFrame(self.frame_211)
        self.frame_213.setObjectName(u"frame_213")
        self.frame_213.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_213.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.frame_213)
        self.horizontalLayout_130.setSpacing(0)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.label_82 = QLabel(self.frame_213)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_82.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_130.addWidget(self.label_82)


        self.verticalLayout_105.addWidget(self.frame_213)


        self.horizontalLayout_124.addWidget(self.frame_211)

        self.frame_214 = QFrame(self.frame_204)
        self.frame_214.setObjectName(u"frame_214")
        self.frame_214.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_214)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.frame_215 = QFrame(self.frame_214)
        self.frame_215.setObjectName(u"frame_215")
        self.frame_215.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_215.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_131 = QHBoxLayout(self.frame_215)
        self.horizontalLayout_131.setSpacing(0)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.btn4 = QPushButton(self.frame_215)
        self.btn4.setObjectName(u"btn4")
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn4.setMinimumSize(QSize(60, 60))
        self.btn4.setMaximumSize(QSize(60, 60))
        self.btn4.setFont(font1)
        self.btn4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn4.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_131.addWidget(self.btn4)


        self.verticalLayout_106.addWidget(self.frame_215)

        self.frame_216 = QFrame(self.frame_214)
        self.frame_216.setObjectName(u"frame_216")
        self.frame_216.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_216.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.frame_216)
        self.horizontalLayout_132.setSpacing(0)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.label_83 = QLabel(self.frame_216)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_83.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_132.addWidget(self.label_83)


        self.verticalLayout_106.addWidget(self.frame_216)


        self.horizontalLayout_124.addWidget(self.frame_214)

        self.frame_217 = QFrame(self.frame_204)
        self.frame_217.setObjectName(u"frame_217")
        self.frame_217.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_217.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_217)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.frame_218 = QFrame(self.frame_217)
        self.frame_218.setObjectName(u"frame_218")
        self.frame_218.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_218.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.frame_218)
        self.horizontalLayout_133.setSpacing(0)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.btn5 = QPushButton(self.frame_218)
        self.btn5.setObjectName(u"btn5")
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        self.btn5.setMinimumSize(QSize(60, 60))
        self.btn5.setMaximumSize(QSize(60, 60))
        self.btn5.setFont(font1)
        self.btn5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn5.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_133.addWidget(self.btn5)


        self.verticalLayout_107.addWidget(self.frame_218)

        self.frame_219 = QFrame(self.frame_217)
        self.frame_219.setObjectName(u"frame_219")
        self.frame_219.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_219.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.frame_219)
        self.horizontalLayout_134.setSpacing(0)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.label_84 = QLabel(self.frame_219)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_84.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_134.addWidget(self.label_84)


        self.verticalLayout_107.addWidget(self.frame_219)


        self.horizontalLayout_124.addWidget(self.frame_217)

        self.frame_220 = QFrame(self.frame_204)
        self.frame_220.setObjectName(u"frame_220")
        self.frame_220.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_220.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_220)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.frame_221 = QFrame(self.frame_220)
        self.frame_221.setObjectName(u"frame_221")
        self.frame_221.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_221.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.frame_221)
        self.horizontalLayout_135.setSpacing(0)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.btn6 = QPushButton(self.frame_221)
        self.btn6.setObjectName(u"btn6")
        sizePolicy.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy)
        self.btn6.setMinimumSize(QSize(60, 60))
        self.btn6.setMaximumSize(QSize(60, 60))
        self.btn6.setFont(font1)
        self.btn6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn6.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_135.addWidget(self.btn6)


        self.verticalLayout_108.addWidget(self.frame_221)

        self.frame_222 = QFrame(self.frame_220)
        self.frame_222.setObjectName(u"frame_222")
        self.frame_222.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_222.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.frame_222)
        self.horizontalLayout_136.setSpacing(0)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.label_85 = QLabel(self.frame_222)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_85.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_136.addWidget(self.label_85)


        self.verticalLayout_108.addWidget(self.frame_222)


        self.horizontalLayout_124.addWidget(self.frame_220)

        self.frame_223 = QFrame(self.frame_204)
        self.frame_223.setObjectName(u"frame_223")
        self.frame_223.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_223.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_223)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.frame_224 = QFrame(self.frame_223)
        self.frame_224.setObjectName(u"frame_224")
        self.frame_224.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_224.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.frame_224)
        self.horizontalLayout_137.setSpacing(0)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.btn7 = QPushButton(self.frame_224)
        self.btn7.setObjectName(u"btn7")
        sizePolicy.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy)
        self.btn7.setMinimumSize(QSize(60, 60))
        self.btn7.setMaximumSize(QSize(60, 60))
        self.btn7.setFont(font1)
        self.btn7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn7.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_137.addWidget(self.btn7)


        self.verticalLayout_109.addWidget(self.frame_224)

        self.frame_225 = QFrame(self.frame_223)
        self.frame_225.setObjectName(u"frame_225")
        self.frame_225.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_225.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.frame_225)
        self.horizontalLayout_138.setSpacing(0)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.label_86 = QLabel(self.frame_225)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_86.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_138.addWidget(self.label_86)


        self.verticalLayout_109.addWidget(self.frame_225)


        self.horizontalLayout_124.addWidget(self.frame_223)

        self.frame_226 = QFrame(self.frame_204)
        self.frame_226.setObjectName(u"frame_226")
        self.frame_226.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_226.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_226)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.frame_227 = QFrame(self.frame_226)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.frame_227)
        self.horizontalLayout_139.setSpacing(0)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.btn8 = QPushButton(self.frame_227)
        self.btn8.setObjectName(u"btn8")
        sizePolicy.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy)
        self.btn8.setMinimumSize(QSize(60, 60))
        self.btn8.setMaximumSize(QSize(60, 60))
        self.btn8.setFont(font1)
        self.btn8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn8.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_139.addWidget(self.btn8)


        self.verticalLayout_110.addWidget(self.frame_227)

        self.frame_228 = QFrame(self.frame_226)
        self.frame_228.setObjectName(u"frame_228")
        self.frame_228.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.frame_228)
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.label_87 = QLabel(self.frame_228)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_87.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_140.addWidget(self.label_87)


        self.verticalLayout_110.addWidget(self.frame_228)


        self.horizontalLayout_124.addWidget(self.frame_226)


        self.verticalLayout_81.addWidget(self.frame_204)

        self.frame_178 = QFrame(self.frame_35)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setMinimumSize(QSize(0, 130))
        self.frame_178.setMaximumSize(QSize(16777215, 130))
        self.frame_178.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 37, 46);\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.frame_178.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.frame_178)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.frame_179 = QFrame(self.frame_178)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_179)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.frame_42 = QFrame(self.frame_179)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_116.setSpacing(0)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.btn9 = QPushButton(self.frame_42)
        self.btn9.setObjectName(u"btn9")
        sizePolicy.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy)
        self.btn9.setMinimumSize(QSize(60, 60))
        self.btn9.setMaximumSize(QSize(60, 60))
        self.btn9.setFont(font1)
        self.btn9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn9.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_116.addWidget(self.btn9)


        self.verticalLayout_92.addWidget(self.frame_42)

        self.frame_180 = QFrame(self.frame_179)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_180)
        self.horizontalLayout_107.setSpacing(0)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_180)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_107.addWidget(self.label_17)


        self.verticalLayout_92.addWidget(self.frame_180)


        self.horizontalLayout_106.addWidget(self.frame_179)

        self.frame_181 = QFrame(self.frame_178)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_181)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.frame_43 = QFrame(self.frame_181)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_117.setSpacing(0)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.btn10 = QPushButton(self.frame_43)
        self.btn10.setObjectName(u"btn10")
        sizePolicy.setHeightForWidth(self.btn10.sizePolicy().hasHeightForWidth())
        self.btn10.setSizePolicy(sizePolicy)
        self.btn10.setMinimumSize(QSize(60, 60))
        self.btn10.setMaximumSize(QSize(60, 60))
        self.btn10.setFont(font1)
        self.btn10.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn10.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_117.addWidget(self.btn10)


        self.verticalLayout_93.addWidget(self.frame_43)

        self.frame_182 = QFrame(self.frame_181)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_108 = QHBoxLayout(self.frame_182)
        self.horizontalLayout_108.setSpacing(0)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_182)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_108.addWidget(self.label_18)


        self.verticalLayout_93.addWidget(self.frame_182)


        self.horizontalLayout_106.addWidget(self.frame_181)

        self.frame_183 = QFrame(self.frame_178)
        self.frame_183.setObjectName(u"frame_183")
        self.frame_183.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_183.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_183)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.frame_184 = QFrame(self.frame_183)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.frame_184)
        self.horizontalLayout_118.setSpacing(0)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.btn11 = QPushButton(self.frame_184)
        self.btn11.setObjectName(u"btn11")
        sizePolicy.setHeightForWidth(self.btn11.sizePolicy().hasHeightForWidth())
        self.btn11.setSizePolicy(sizePolicy)
        self.btn11.setMinimumSize(QSize(60, 60))
        self.btn11.setMaximumSize(QSize(60, 60))
        self.btn11.setFont(font1)
        self.btn11.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn11.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_118.addWidget(self.btn11)


        self.verticalLayout_94.addWidget(self.frame_184)

        self.frame_185 = QFrame(self.frame_183)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.frame_185)
        self.horizontalLayout_109.setSpacing(0)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.label_74 = QLabel(self.frame_185)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_74.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_109.addWidget(self.label_74)


        self.verticalLayout_94.addWidget(self.frame_185)


        self.horizontalLayout_106.addWidget(self.frame_183)

        self.frame_186 = QFrame(self.frame_178)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_186)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.frame_187 = QFrame(self.frame_186)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.frame_187)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.btn12 = QPushButton(self.frame_187)
        self.btn12.setObjectName(u"btn12")
        sizePolicy.setHeightForWidth(self.btn12.sizePolicy().hasHeightForWidth())
        self.btn12.setSizePolicy(sizePolicy)
        self.btn12.setMinimumSize(QSize(60, 60))
        self.btn12.setMaximumSize(QSize(60, 60))
        self.btn12.setFont(font1)
        self.btn12.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn12.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_119.addWidget(self.btn12)


        self.verticalLayout_95.addWidget(self.frame_187)

        self.frame_188 = QFrame(self.frame_186)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.frame_188)
        self.horizontalLayout_110.setSpacing(0)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.label_75 = QLabel(self.frame_188)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_75.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_110.addWidget(self.label_75)


        self.verticalLayout_95.addWidget(self.frame_188)


        self.horizontalLayout_106.addWidget(self.frame_186)

        self.frame_189 = QFrame(self.frame_178)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_189)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.frame_190 = QFrame(self.frame_189)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.frame_190)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.btn13 = QPushButton(self.frame_190)
        self.btn13.setObjectName(u"btn13")
        sizePolicy.setHeightForWidth(self.btn13.sizePolicy().hasHeightForWidth())
        self.btn13.setSizePolicy(sizePolicy)
        self.btn13.setMinimumSize(QSize(60, 60))
        self.btn13.setMaximumSize(QSize(60, 60))
        self.btn13.setFont(font1)
        self.btn13.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn13.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_120.addWidget(self.btn13)


        self.verticalLayout_96.addWidget(self.frame_190)

        self.frame_191 = QFrame(self.frame_189)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.frame_191)
        self.horizontalLayout_111.setSpacing(0)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.label_76 = QLabel(self.frame_191)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_76.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_111.addWidget(self.label_76)


        self.verticalLayout_96.addWidget(self.frame_191)


        self.horizontalLayout_106.addWidget(self.frame_189)

        self.frame_192 = QFrame(self.frame_178)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_192)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.frame_193 = QFrame(self.frame_192)
        self.frame_193.setObjectName(u"frame_193")
        self.frame_193.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.frame_193)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.btn14 = QPushButton(self.frame_193)
        self.btn14.setObjectName(u"btn14")
        sizePolicy.setHeightForWidth(self.btn14.sizePolicy().hasHeightForWidth())
        self.btn14.setSizePolicy(sizePolicy)
        self.btn14.setMinimumSize(QSize(60, 60))
        self.btn14.setMaximumSize(QSize(60, 60))
        self.btn14.setFont(font1)
        self.btn14.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn14.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn14.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_121.addWidget(self.btn14)


        self.verticalLayout_97.addWidget(self.frame_193)

        self.frame_194 = QFrame(self.frame_192)
        self.frame_194.setObjectName(u"frame_194")
        self.frame_194.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.frame_194)
        self.horizontalLayout_112.setSpacing(0)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.frame_194)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_77.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_112.addWidget(self.label_77)


        self.verticalLayout_97.addWidget(self.frame_194)


        self.horizontalLayout_106.addWidget(self.frame_192)

        self.frame_198 = QFrame(self.frame_178)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_198)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.frame_199 = QFrame(self.frame_198)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_122 = QHBoxLayout(self.frame_199)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.btn15 = QPushButton(self.frame_199)
        self.btn15.setObjectName(u"btn15")
        sizePolicy.setHeightForWidth(self.btn15.sizePolicy().hasHeightForWidth())
        self.btn15.setSizePolicy(sizePolicy)
        self.btn15.setMinimumSize(QSize(60, 60))
        self.btn15.setMaximumSize(QSize(60, 60))
        self.btn15.setFont(font1)
        self.btn15.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn15.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn15.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_122.addWidget(self.btn15)


        self.verticalLayout_98.addWidget(self.frame_199)

        self.frame_200 = QFrame(self.frame_198)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_113 = QHBoxLayout(self.frame_200)
        self.horizontalLayout_113.setSpacing(0)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.label_78 = QLabel(self.frame_200)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_78.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_113.addWidget(self.label_78)


        self.verticalLayout_98.addWidget(self.frame_200)


        self.horizontalLayout_106.addWidget(self.frame_198)

        self.frame_201 = QFrame(self.frame_178)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_201)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.frame_202 = QFrame(self.frame_201)
        self.frame_202.setObjectName(u"frame_202")
        self.frame_202.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.frame_202)
        self.horizontalLayout_123.setSpacing(0)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.btn16 = QPushButton(self.frame_202)
        self.btn16.setObjectName(u"btn16")
        sizePolicy.setHeightForWidth(self.btn16.sizePolicy().hasHeightForWidth())
        self.btn16.setSizePolicy(sizePolicy)
        self.btn16.setMinimumSize(QSize(60, 60))
        self.btn16.setMaximumSize(QSize(60, 60))
        self.btn16.setFont(font1)
        self.btn16.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn16.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn16.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/forms/icons/heart_rate.png);\n"
"	border: no;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat; \n"
"	border-radius: 10px;\n"
"	background-color: rgba(82, 28, 129,0.3);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(162, 98, 199);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_123.addWidget(self.btn16)


        self.verticalLayout_99.addWidget(self.frame_202)

        self.frame_203 = QFrame(self.frame_201)
        self.frame_203.setObjectName(u"frame_203")
        self.frame_203.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_114 = QHBoxLayout(self.frame_203)
        self.horizontalLayout_114.setSpacing(0)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.label_79 = QLabel(self.frame_203)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(221, 221, 221);\n"
"")
        self.label_79.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_114.addWidget(self.label_79)


        self.verticalLayout_99.addWidget(self.frame_203)


        self.horizontalLayout_106.addWidget(self.frame_201)


        self.verticalLayout_81.addWidget(self.frame_178)


        self.verticalLayout_38.addWidget(self.frame_35)

        self.frame_195 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setMinimumSize(QSize(0, 160))
        self.frame_195.setMaximumSize(QSize(16777215, 16777215))
        self.frame_195.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 37, 46);\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.frame_195.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_195)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_196 = QFrame(self.frame_195)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setMinimumSize(QSize(0, 120))
        self.frame_196.setMaximumSize(QSize(16777215, 120))
        self.frame_196.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 37, 46);\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.frame_196.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_196)
        self.verticalLayout_101.setSpacing(0)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.judevalue_label = QLabel(self.frame_196)
        self.judevalue_label.setObjectName(u"judevalue_label")
        self.judevalue_label.setStyleSheet(u"border:none;\n"
"")

        self.verticalLayout_101.addWidget(self.judevalue_label)

        self.timeline_widget = QWidget(self.frame_196)
        self.timeline_widget.setObjectName(u"timeline_widget")
        self.timeline_widget.setMinimumSize(QSize(0, 120))
        self.timeline_widget.setMaximumSize(QSize(16777215, 120))
        self.timeline_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(30, 37, 46);\n"
"}")

        self.verticalLayout_101.addWidget(self.timeline_widget)


        self.verticalLayout_18.addWidget(self.frame_196)


        self.verticalLayout_38.addWidget(self.frame_195)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_115.addWidget(self.scrollArea_2)

        self.avatar_widget = QWidget(self.page_write)
        self.avatar_widget.setObjectName(u"avatar_widget")
        self.avatar_widget.setMinimumSize(QSize(100, 0))
        self.avatar_widget.setMaximumSize(QSize(100, 16777215))
        self.avatar_widget.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.verticalLayout_20 = QVBoxLayout(self.avatar_widget)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_21 = QLabel(self.avatar_widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 20))
        self.label_21.setMaximumSize(QSize(16777215, 20))
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_21)

        self.avatars_add_btn = QPushButton(self.avatar_widget)
        self.avatars_add_btn.setObjectName(u"avatars_add_btn")
        sizePolicy.setHeightForWidth(self.avatars_add_btn.sizePolicy().hasHeightForWidth())
        self.avatars_add_btn.setSizePolicy(sizePolicy)
        self.avatars_add_btn.setMinimumSize(QSize(90, 20))
        self.avatars_add_btn.setMaximumSize(QSize(90, 20))
        self.avatars_add_btn.setFont(font1)
        self.avatars_add_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.avatars_add_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.avatars_add_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	background-image: url(:/forms/icons/cross or add.png);    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.verticalLayout_20.addWidget(self.avatars_add_btn)

        self.avatar_scrollArea = QScrollArea(self.avatar_widget)
        self.avatar_scrollArea.setObjectName(u"avatar_scrollArea")
        self.avatar_scrollArea.setWidgetResizable(True)
        self.avatar_scrollAreaWidgetContents = QWidget()
        self.avatar_scrollAreaWidgetContents.setObjectName(u"avatar_scrollAreaWidgetContents")
        self.avatar_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 82, 501))
        self.verticalLayout_19 = QVBoxLayout(self.avatar_scrollAreaWidgetContents)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.avatar_scrollArea.setWidget(self.avatar_scrollAreaWidgetContents)

        self.verticalLayout_20.addWidget(self.avatar_scrollArea)

        self.save_btn = QPushButton(self.avatar_widget)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setMinimumSize(QSize(90, 20))
        self.save_btn.setMaximumSize(QSize(90, 20))
        self.save_btn.setFont(font1)
        self.save_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.save_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	background-image: url(:/forms/icons/cil-save.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.verticalLayout_20.addWidget(self.save_btn)


        self.horizontalLayout_115.addWidget(self.avatar_widget)

        self.stackedWidget.addWidget(self.page_write)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.verticalLayout_14 = QVBoxLayout(self.page_setting)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.Server_link_frame = QFrame(self.page_setting)
        self.Server_link_frame.setObjectName(u"Server_link_frame")
        self.Server_link_frame.setMinimumSize(QSize(0, 120))
        self.Server_link_frame.setMaximumSize(QSize(16777215, 120))
        self.Server_link_frame.setStyleSheet(u"QFrame{border: none;}")
        self.Server_link_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Server_link_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Server_link_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.MDX23_label = QLabel(self.Server_link_frame)
        self.MDX23_label.setObjectName(u"MDX23_label")
        self.MDX23_label.setMinimumSize(QSize(0, 60))
        self.MDX23_label.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_7.addWidget(self.MDX23_label)

        self.frame_3 = QFrame(self.Server_link_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.train_setting_frame6_2 = QFrame(self.frame_3)
        self.train_setting_frame6_2.setObjectName(u"train_setting_frame6_2")
        self.train_setting_frame6_2.setMinimumSize(QSize(0, 40))
        self.train_setting_frame6_2.setMaximumSize(QSize(16777215, 40))
        self.train_setting_frame6_2.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.train_setting_frame6_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.train_setting_frame6_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.train_setting_frame6_2)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.save_num_label_2 = QLabel(self.train_setting_frame6_2)
        self.save_num_label_2.setObjectName(u"save_num_label_2")
        self.save_num_label_2.setMinimumSize(QSize(190, 20))
        self.save_num_label_2.setMaximumSize(QSize(190, 20))
        self.save_num_label_2.setStyleSheet(u"border:none;")

        self.horizontalLayout_44.addWidget(self.save_num_label_2)

        self.server_ip = QLineEdit(self.train_setting_frame6_2)
        self.server_ip.setObjectName(u"server_ip")
        self.server_ip.setStyleSheet(u"border-radius: 8px;")
        self.server_ip.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.server_ip)


        self.horizontalLayout_3.addWidget(self.train_setting_frame6_2)

        self.train_setting_frame6_3 = QFrame(self.frame_3)
        self.train_setting_frame6_3.setObjectName(u"train_setting_frame6_3")
        self.train_setting_frame6_3.setMinimumSize(QSize(0, 40))
        self.train_setting_frame6_3.setMaximumSize(QSize(16777215, 40))
        self.train_setting_frame6_3.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.train_setting_frame6_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.train_setting_frame6_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.train_setting_frame6_3)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.save_num_label_3 = QLabel(self.train_setting_frame6_3)
        self.save_num_label_3.setObjectName(u"save_num_label_3")
        self.save_num_label_3.setMinimumSize(QSize(0, 20))
        self.save_num_label_3.setMaximumSize(QSize(16777215, 20))
        self.save_num_label_3.setStyleSheet(u"border:none;")

        self.horizontalLayout_45.addWidget(self.save_num_label_3)

        self.sleep_time = QLineEdit(self.train_setting_frame6_3)
        self.sleep_time.setObjectName(u"sleep_time")
        self.sleep_time.setStyleSheet(u"border-radius: 8px;")
        self.sleep_time.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_45.addWidget(self.sleep_time)


        self.horizontalLayout_3.addWidget(self.train_setting_frame6_3)


        self.verticalLayout_7.addWidget(self.frame_3)


        self.verticalLayout_14.addWidget(self.Server_link_frame)

        self.frame_7 = QFrame(self.page_setting)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.range_frame = QFrame(self.frame_7)
        self.range_frame.setObjectName(u"range_frame")
        self.range_frame.setGeometry(QRect(0, 10, 901, 160))
        self.range_frame.setMinimumSize(QSize(0, 160))
        self.range_frame.setMaximumSize(QSize(16777215, 160))
        self.range_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(30, 37, 46);\n"
"    border-radius: 10px;\n"
"	border:none;\n"
"}\n"
"")
        self.range_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.range_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.range_frame)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.range_label = QLabel(self.range_frame)
        self.range_label.setObjectName(u"range_label")
        self.range_label.setStyleSheet(u"border:none;\n"
"border-radius: 0px;\n"
"background-color: rgb(47, 54, 60);\n"
"")

        self.verticalLayout_102.addWidget(self.range_label)

        self.range_widget = QWidget(self.range_frame)
        self.range_widget.setObjectName(u"range_widget")
        self.range_widget.setMinimumSize(QSize(0, 120))
        self.range_widget.setMaximumSize(QSize(16777215, 120))
        self.range_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(40, 47, 56);\n"
"border-radius: 10px;\n"
"}")

        self.verticalLayout_102.addWidget(self.range_widget)


        self.verticalLayout_14.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_setting)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.mian)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(940, 45))
        self.bottomBar.setMaximumSize(QSize(16777215, 45))
        self.bottomBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_50.addWidget(self.creditsLabel)

        self.frame_40 = QFrame(self.bottomBar)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(40, 16777215))
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_50.addWidget(self.frame_40)

        self.stateshow = QLabel(self.bottomBar)
        self.stateshow.setObjectName(u"stateshow")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(False)
        font2.setItalic(False)
        self.stateshow.setFont(font2)
        self.stateshow.setStyleSheet(u"font-size: 11px; \n"
"color: rgb(113, 126, 149);")
        self.stateshow.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_50.addWidget(self.stateshow)

        self.frame_41 = QFrame(self.bottomBar)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(40, 16777215))
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_50.addWidget(self.frame_41)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(0, 0))
        self.version.setMaximumSize(QSize(100, 16777215))
        self.version.setTextFormat(Qt.TextFormat.PlainText)
        self.version.setScaledContents(False)
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.version.setWordWrap(False)
        self.version.setMargin(0)

        self.horizontalLayout_50.addWidget(self.version)


        self.verticalLayout_4.addWidget(self.bottomBar)


        self.horizontalLayout_2.addWidget(self.contentBottom)


        self.horizontalLayout_4.addWidget(self.contentBox)

        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.avatar_listWidget.setCurrentRow(-1)
        self.judge_listWidget.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VRCHATosc To DGLAB", None))
        self.run_btn.setText("")
        self.home.setText("")
        self.console_btn.setText("")
        self.equalizer_btn.setText("")
        self.setting_btn.setText("")
        self.audio_slicer_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Vrchat setting()</span></p></body></html>", None))
        self.avatarParameter_setting.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">avatarParameter(\u6a21\u578b\u53c2\u6570)</span></p></body></html>", None))
        self.select_avatarParameter_lineedit.setText("")
        self.change_avater_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u53c2\u6570", None))
        self.add_avatar_btn.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u53c2\u6570", None))
        self.delect_avatar_btn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u53c2\u6570", None))
        self.slicer_setting_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">judgevalue(\u5224\u65ad\u503c)</span></p></body></html>", None))
        self.slicer_setting_label1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">judgeMode(\u5224\u65ad\u6a21\u5f0f)</span></p></body></html>", None))
        self.judgemode_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7b49\u4e8e", None))
        self.judgemode_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5927\u4e8e", None))
        self.judgemode_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5c0f\u4e8e", None))

        self.select_judge_lineedit.setText("")
        self.change_judge_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u53c2\u6570", None))
        self.add_judge_btn.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u53c2\u6570", None))
        self.delect_judge_btn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u53c2\u6570", None))
        self.slicer_setting_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">judgeSetting(\u5224\u65ad\u6761\u4ef6)</span></p></body></html>", None))
        self.slicer_setting_label1_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">pattern(\u6ce2\u5f62)</span></p></body></html>", None))
        self.slicer_setting_label2_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">channel(\u901a\u9053)</span></p></body></html>", None))
        self.channel_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.channel_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))

        self.slicer_setting_label3_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">intensity(\u901a\u9053\u5f3a\u5ea6)</span></p></body></html>", None))
        self.intensity.setText("")
        self.slicer_setting_label3_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Ticks(\u5355\u6b21\u8f93\u51fa\u65f6\u95f41s)</span></p></body></html>", None))
        self.Ticks.setText("")
        self.dataset_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Dalab socket(\u90ca\u72fc\u4e8c\u7ef4\u7801)</span></p></body></html>", None))
        self.qrcode.setText("")
        self.dglink_label.setText(QCoreApplication.translate("MainWindow", u"\u7b49\u5f85\u8fde\u63a5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">console\u63a7\u5236\u53f0</span></p></body></html>", None))
        self.console.setPlainText("")
        self.avatarParameter_setting_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">DGLAB\u53c2\u6570\u8bbe\u7f6e</span></p></body></html>", None))
        self.intensity_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.A_btn.setText(QCoreApplication.translate("MainWindow", u"\u901a\u9053A", None))
        self.mode_combox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7b49\u4e8e", None))
        self.mode_combox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5927\u4e8e", None))
        self.mode_combox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5c0f\u4e8e", None))

        self.ticks_add_btn.setText("")
        self.Tick_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Ticks:</span></p></body></html>", None))
        self.tick_label.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.ticks_decrease_btn.setText("")
        self.B_btn.setText(QCoreApplication.translate("MainWindow", u"\u901a\u9053B", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u5f62", None))
        self.btn1.setText("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\u547c\u5438", None))
        self.btn2.setText("")
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"\u6f6e\u6c50", None))
        self.btn3.setText("")
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u51fb", None))
        self.btn4.setText("")
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u6309\u634f", None))
        self.btn5.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"\u6309\u634f\u5f3a\u52b2", None))
        self.btn6.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"\u5fc3\u8df3\u8282\u594f", None))
        self.btn7.setText("")
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"\u538b\u7f29", None))
        self.btn8.setText("")
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"\u8282\u594f\u6b65\u4f10", None))
        self.btn9.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u9897\u7c92\u6469\u64e6", None))
        self.btn10.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u6e10\u53d8\u5f39\u8df3", None))
        self.btn11.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u6d6a\u6d9f\u6f2a", None))
        self.btn12.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u96e8\u6c34\u51b2\u5237", None))
        self.btn13.setText("")
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u901f\u6572\u6253", None))
        self.btn14.setText("")
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u53f7\u706f", None))
        self.btn15.setText("")
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"\u6311\u90171", None))
        self.btn16.setText("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"\u6311\u90172", None))
        self.judevalue_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u6a21\u578b\u89e6\u53d1\u503c\u8bbe\u7f6e(\u5224\u65ad\u503c)</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">avatar</span></p><p><br/></p></body></html>", None))
        self.avatars_add_btn.setText("")
        self.save_btn.setText("")
        self.MDX23_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Server link</span></p></body></html>", None))
        self.save_num_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">server ip(\u670d\u52a1\u5668ip \u9ed8\u8ba4\u4e3a\u7a7a)</span></p></body></html>", None))
        self.server_ip.setText("")
        self.save_num_label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">package interval time(\u6570\u636e\u5305\u95f4\u9694\u65f6\u95f4)</span></p></body></html>", None))
        self.sleep_time.setText("")
        self.range_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u6ed1\u6761\u6700\u5927\u503c\u6700\u5c0f\u503c\u8bbe\u7f6e</span></p></body></html>", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"by ", None))
        self.stateshow.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"version: ", None))
    # retranslateUi

