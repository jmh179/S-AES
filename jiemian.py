# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jiemian.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(846, 627)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(450, 50, 361, 188))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_10.addWidget(self.label_3)

        self.key3 = QLineEdit(self.layoutWidget)
        self.key3.setObjectName(u"key3")
        self.key3.setMaxLength(48)

        self.horizontalLayout_10.addWidget(self.key3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.in_ming3 = QLineEdit(self.layoutWidget)
        self.in_ming3.setObjectName(u"in_ming3")
        self.in_ming3.setMaxLength(16)

        self.horizontalLayout_11.addWidget(self.in_ming3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.out_mi3 = QLabel(self.layoutWidget)
        self.out_mi3.setObjectName(u"out_mi3")
        self.out_mi3.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_5.addWidget(self.out_mi3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.in_mi3 = QLineEdit(self.layoutWidget)
        self.in_mi3.setObjectName(u"in_mi3")
        self.in_mi3.setMaxLength(16)

        self.horizontalLayout_12.addWidget(self.in_mi3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.out_ming3 = QLabel(self.layoutWidget)
        self.out_ming3.setObjectName(u"out_ming3")

        self.verticalLayout_5.addWidget(self.out_ming3)


        self.horizontalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_6.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_6.addWidget(self.pushButton_6)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)

        self.layoutWidget_2 = QWidget(Form)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(450, 250, 361, 166))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_13 = QLabel(self.layoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_7.addWidget(self.label_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.key4 = QLineEdit(self.layoutWidget_2)
        self.key4.setObjectName(u"key4")
        self.key4.setMaxLength(16)

        self.horizontalLayout_14.addWidget(self.key4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_15 = QLabel(self.layoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.in_ming4 = QLineEdit(self.layoutWidget_2)
        self.in_ming4.setObjectName(u"in_ming4")
        self.in_ming4.setMaxLength(2)

        self.horizontalLayout_15.addWidget(self.in_ming4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.out_mi4 = QLabel(self.layoutWidget_2)
        self.out_mi4.setObjectName(u"out_mi4")
        self.out_mi4.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_7.addWidget(self.out_mi4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_16 = QLabel(self.layoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_16.addWidget(self.label_16)

        self.in_mi4 = QLineEdit(self.layoutWidget_2)
        self.in_mi4.setObjectName(u"in_mi4")
        self.in_mi4.setMaxLength(16)

        self.horizontalLayout_16.addWidget(self.in_mi4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.out_ming4 = QLabel(self.layoutWidget_2)
        self.out_ming4.setObjectName(u"out_ming4")

        self.verticalLayout_7.addWidget(self.out_ming4)


        self.horizontalLayout_13.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_7 = QPushButton(self.layoutWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_8.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.layoutWidget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_8.addWidget(self.pushButton_8)


        self.horizontalLayout_13.addLayout(self.verticalLayout_8)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(33, 53, 361, 166))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.key1 = QLineEdit(self.layoutWidget1)
        self.key1.setObjectName(u"key1")
        self.key1.setMaxLength(16)

        self.horizontalLayout.addWidget(self.key1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.in_ming1 = QLineEdit(self.layoutWidget1)
        self.in_ming1.setObjectName(u"in_ming1")
        self.in_ming1.setMaxLength(16)

        self.horizontalLayout_2.addWidget(self.in_ming1)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.out_mi1 = QLabel(self.layoutWidget1)
        self.out_mi1.setObjectName(u"out_mi1")
        self.out_mi1.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.out_mi1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.in_mi1 = QLineEdit(self.layoutWidget1)
        self.in_mi1.setObjectName(u"in_mi1")
        self.in_mi1.setMaxLength(16)

        self.horizontalLayout_3.addWidget(self.in_mi1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.out_ming1 = QLabel(self.layoutWidget1)
        self.out_ming1.setObjectName(u"out_ming1")

        self.verticalLayout.addWidget(self.out_ming1)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.layoutWidget2 = QWidget(Form)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 250, 361, 166))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.key2 = QLineEdit(self.layoutWidget2)
        self.key2.setObjectName(u"key2")
        self.key2.setMaxLength(32)

        self.horizontalLayout_5.addWidget(self.key2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.in_ming2 = QLineEdit(self.layoutWidget2)
        self.in_ming2.setObjectName(u"in_ming2")
        self.in_ming2.setMaxLength(16)

        self.horizontalLayout_6.addWidget(self.in_ming2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.out_mi2 = QLabel(self.layoutWidget2)
        self.out_mi2.setObjectName(u"out_mi2")
        self.out_mi2.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.out_mi2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.layoutWidget2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.in_mi2 = QLineEdit(self.layoutWidget2)
        self.in_mi2.setObjectName(u"in_mi2")
        self.in_mi2.setMaxLength(16)

        self.horizontalLayout_7.addWidget(self.in_mi2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.out_ming2 = QLabel(self.layoutWidget2)
        self.out_ming2.setObjectName(u"out_ming2")

        self.verticalLayout_3.addWidget(self.out_ming2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_3 = QPushButton(self.layoutWidget2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCheckable(False)

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.layoutWidget2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCheckable(False)

        self.verticalLayout_4.addWidget(self.pushButton_4)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.layoutWidget_3 = QWidget(Form)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(30, 440, 361, 166))
        self.horizontalLayout_17 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_17 = QLabel(self.layoutWidget_3)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_9.addWidget(self.label_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_18 = QLabel(self.layoutWidget_3)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_18.addWidget(self.label_18)

        self.key5 = QLineEdit(self.layoutWidget_3)
        self.key5.setObjectName(u"key5")
        self.key5.setMaxLength(16)

        self.horizontalLayout_18.addWidget(self.key5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_19 = QLabel(self.layoutWidget_3)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_19.addWidget(self.label_19)

        self.in_ming5 = QLineEdit(self.layoutWidget_3)
        self.in_ming5.setObjectName(u"in_ming5")
        self.in_ming5.setMaxLength(16)

        self.horizontalLayout_19.addWidget(self.in_ming5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.out_mi5 = QLabel(self.layoutWidget_3)
        self.out_mi5.setObjectName(u"out_mi5")
        self.out_mi5.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_9.addWidget(self.out_mi5)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_20 = QLabel(self.layoutWidget_3)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_20.addWidget(self.label_20)

        self.in_mi5 = QLineEdit(self.layoutWidget_3)
        self.in_mi5.setObjectName(u"in_mi5")
        self.in_mi5.setMaxLength(16)

        self.horizontalLayout_20.addWidget(self.in_mi5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_20)

        self.out_ming5 = QLabel(self.layoutWidget_3)
        self.out_ming5.setObjectName(u"out_ming5")

        self.verticalLayout_9.addWidget(self.out_ming5)


        self.horizontalLayout_17.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_9 = QPushButton(self.layoutWidget_3)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_10.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.layoutWidget_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_10.addWidget(self.pushButton_10)


        self.horizontalLayout_17.addLayout(self.verticalLayout_10)

        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(471, 451, 150, 16))
        self.label_22 = QLabel(Form)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(471, 473, 174, 17))
        self.label_22.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(471, 497, 302, 17))
        self.label_23.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(471, 521, 246, 51))
        self.label_24.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"S-AES", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u4e09\u91cd\u52a0\u5bc6", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5bc6\u94a5\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u660e\u6587\uff1a", None))
        self.out_mi3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u5bc6\u6587</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5bc6\u6587\uff1a", None))
        self.out_ming3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u660e\u6587</p></body></html>", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u5bc6\u6587", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u89e3\u5bc6", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u5b57\u7b26\u4e32\u52a0\u5bc6", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5bc6\u94a5\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u660e\u6587\uff1a", None))
        self.out_mi4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u5bc6\u6587</p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5bc6\u6587\uff1a", None))
        self.out_ming4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u660e\u6587</p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u5bc6\u6587", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u89e3\u5bc6", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5355\u91cd\u52a0\u5bc6", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5bc6\u94a5\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u660e\u6587\uff1a", None))
        self.out_mi1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u5bc6\u6587</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5bc6\u6587\uff1a", None))
        self.out_ming1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u660e\u6587</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u5bc6\u6587", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u89e3\u5bc6", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u53cc\u91cd\u52a0\u5bc6", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5bc6\u94a5\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u660e\u6587\uff1a", None))
        self.out_mi2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u5bc6\u6587</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5bc6\u6587\uff1a", None))
        self.out_ming2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u660e\u6587</p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u5bc6\u6587", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u89e3\u5bc6", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"CBC\u52a0\u5bc6", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5bc6\u94a5\uff1a", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u660e\u6587\uff1a", None))
        self.out_mi5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u5bc6\u6587</p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5bc6\u6587\uff1a", None))
        self.out_ming5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u660e\u6587</p></body></html>", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u5bc6\u6587", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"\u89e3\u5bc6", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u53c2\u8003\u5bc6\u94a5\uff08\u53ef\u590d\u5236\u4f7f\u7528", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"16\u4f4d\uff1a1001001111100010", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>32\u4f4d\uff1a01010001001110100110110001001111</p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>48\u4f4d\uff1a110000110110101010110110</p><p>111100110001101010111100</p></body></html>", None))
    # retranslateUi
