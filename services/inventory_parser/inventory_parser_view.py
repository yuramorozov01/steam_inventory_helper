# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'services/inventory_parser/inventory_parser_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_inventory_parser(object):
    def setupUi(self, form_inventory_parser):
        form_inventory_parser.setObjectName("form_inventory_parser")
        form_inventory_parser.resize(1000, 660)
        form_inventory_parser.setMinimumSize(QtCore.QSize(700, 660))
        form_inventory_parser.setMaximumSize(QtCore.QSize(1000, 660))
        self.le_steam_id = QtWidgets.QLineEdit(form_inventory_parser)
        self.le_steam_id.setGeometry(QtCore.QRect(110, 20, 250, 21))
        self.le_steam_id.setReadOnly(True)
        self.le_steam_id.setObjectName("le_steam_id")
        self.cb_app_id = QtWidgets.QComboBox(form_inventory_parser)
        self.cb_app_id.setGeometry(QtCore.QRect(110, 60, 250, 26))
        self.cb_app_id.setObjectName("cb_app_id")
        self.cb_app_id.addItem("")
        self.lb_steam_id = QtWidgets.QLabel(form_inventory_parser)
        self.lb_steam_id.setGeometry(QtCore.QRect(20, 23, 121, 16))
        self.lb_steam_id.setObjectName("lb_steam_id")
        self.lb_add_id = QtWidgets.QLabel(form_inventory_parser)
        self.lb_add_id.setGeometry(QtCore.QRect(20, 63, 121, 16))
        self.lb_add_id.setObjectName("lb_add_id")
        self.tw_inventory = QtWidgets.QTableWidget(form_inventory_parser)
        self.tw_inventory.setGeometry(QtCore.QRect(10, 140, 980, 461))
        self.tw_inventory.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_inventory.setObjectName("tw_inventory")
        self.tw_inventory.setColumnCount(0)
        self.tw_inventory.setRowCount(0)
        self.pb_load = QtWidgets.QPushButton(form_inventory_parser)
        self.pb_load.setGeometry(QtCore.QRect(330, 610, 160, 41))
        self.pb_load.setObjectName("pb_load")
        self.lb_inventory = QtWidgets.QLabel(form_inventory_parser)
        self.lb_inventory.setGeometry(QtCore.QRect(20, 110, 71, 21))
        self.lb_inventory.setObjectName("lb_inventory")
        self.lb_inventory_price = QtWidgets.QLabel(form_inventory_parser)
        self.lb_inventory_price.setGeometry(QtCore.QRect(740, 110, 101, 16))
        self.lb_inventory_price.setObjectName("lb_inventory_price")
        self.le_inventory_price = QtWidgets.QLineEdit(form_inventory_parser)
        self.le_inventory_price.setGeometry(QtCore.QRect(842, 108, 141, 21))
        self.le_inventory_price.setReadOnly(True)
        self.le_inventory_price.setObjectName("le_inventory_price")
        self.lb_status = QtWidgets.QLabel(form_inventory_parser)
        self.lb_status.setGeometry(QtCore.QRect(10, 621, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_status.setFont(font)
        self.lb_status.setObjectName("lb_status")
        self.le_status = QtWidgets.QLineEdit(form_inventory_parser)
        self.le_status.setGeometry(QtCore.QRect(56, 620, 185, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_status.setFont(font)
        self.le_status.setReadOnly(True)
        self.le_status.setObjectName("le_status")
        self.pb_progress = QtWidgets.QProgressBar(form_inventory_parser)
        self.pb_progress.setGeometry(QtCore.QRect(770, 620, 211, 21))
        self.pb_progress.setProperty("value", 0)
        self.pb_progress.setObjectName("pb_progress")
        self.pb_sell = QtWidgets.QPushButton(form_inventory_parser)
        self.pb_sell.setGeometry(QtCore.QRect(510, 610, 160, 41))
        self.pb_sell.setObjectName("pb_sell")

        self.retranslateUi(form_inventory_parser)
        QtCore.QMetaObject.connectSlotsByName(form_inventory_parser)

    def retranslateUi(self, form_inventory_parser):
        _translate = QtCore.QCoreApplication.translate
        form_inventory_parser.setWindowTitle(_translate("form_inventory_parser", "Inventory parser"))
        self.cb_app_id.setItemText(0, _translate("form_inventory_parser", "Counter-Strike: Global Offensive"))
        self.lb_steam_id.setText(_translate("form_inventory_parser", "SteamID64:"))
        self.lb_add_id.setText(_translate("form_inventory_parser", "Game:"))
        self.pb_load.setText(_translate("form_inventory_parser", "Load"))
        self.lb_inventory.setText(_translate("form_inventory_parser", "Inventory:"))
        self.lb_inventory_price.setText(_translate("form_inventory_parser", "Inventory Price:"))
        self.lb_status.setText(_translate("form_inventory_parser", "Status:"))
        self.le_status.setText(_translate("form_inventory_parser", "OK"))
        self.pb_sell.setText(_translate("form_inventory_parser", "Sell items"))