# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 765)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 765))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/chess.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(420, 0))
        self.widget.setObjectName("widget")
        self.original_source = QtWidgets.QLabel(self.widget)
        self.original_source.setGeometry(QtCore.QRect(10, 30, 400, 300))
        self.original_source.setStyleSheet("border-width:3px;\n"
"border: 1px solid black;")
        self.original_source.setText("")
        self.original_source.setObjectName("original_source")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 400, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("border-width:3px;\n"
"background-color: rgb(186, 189, 182);\n"
"border: 1px solid black;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(10, 350, 400, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-width:3px;\n"
"background-color: rgb(186, 189, 182);\n"
"border: 1px solid black;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setGeometry(QtCore.QRect(180, 550, 210, 70))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.edit_max = QtWidgets.QLineEdit(self.groupBox_4)
        self.edit_max.setGeometry(QtCore.QRect(70, 10, 60, 25))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(11)
        self.edit_max.setFont(font)
        self.edit_max.setText("")
        self.edit_max.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edit_max.setObjectName("edit_max")
        self.edit_min = QtWidgets.QLineEdit(self.groupBox_4)
        self.edit_min.setGeometry(QtCore.QRect(70, 40, 60, 25))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(11)
        self.edit_min.setFont(font)
        self.edit_min.setText("")
        self.edit_min.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edit_min.setObjectName("edit_min")
        self.set_panorama = QtWidgets.QPushButton(self.groupBox_4)
        self.set_panorama.setGeometry(QtCore.QRect(150, 15, 50, 40))
        self.set_panorama.setStyleSheet("")
        self.set_panorama.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.set_panorama.setIcon(icon1)
        self.set_panorama.setObjectName("set_panorama")
        self.anypoint_view = QtWidgets.QRadioButton(self.widget)
        self.anypoint_view.setGeometry(QtCore.QRect(20, 420, 201, 23))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(14)
        self.anypoint_view.setFont(font)
        self.anypoint_view.setObjectName("anypoint_view")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 380, 400, 250))
        self.groupBox_2.setStyleSheet("border-width:3px;\n"
"border: 1px solid black;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.normal_view = QtWidgets.QRadioButton(self.widget)
        self.normal_view.setGeometry(QtCore.QRect(20, 390, 200, 23))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(14)
        self.normal_view.setFont(font)
        self.normal_view.setObjectName("normal_view")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setGeometry(QtCore.QRect(179, 430, 210, 100))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.edit_alpha = QtWidgets.QLineEdit(self.groupBox_3)
        self.edit_alpha.setGeometry(QtCore.QRect(70, 10, 60, 25))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(11)
        self.edit_alpha.setFont(font)
        self.edit_alpha.setText("")
        self.edit_alpha.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edit_alpha.setDragEnabled(True)
        self.edit_alpha.setObjectName("edit_alpha")
        self.edit_beta = QtWidgets.QLineEdit(self.groupBox_3)
        self.edit_beta.setGeometry(QtCore.QRect(70, 40, 60, 25))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(11)
        self.edit_beta.setFont(font)
        self.edit_beta.setText("")
        self.edit_beta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edit_beta.setDragEnabled(True)
        self.edit_beta.setObjectName("edit_beta")
        self.edit_zoom = QtWidgets.QLineEdit(self.groupBox_3)
        self.edit_zoom.setGeometry(QtCore.QRect(70, 70, 60, 25))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(11)
        self.edit_zoom.setFont(font)
        self.edit_zoom.setText("")
        self.edit_zoom.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edit_zoom.setObjectName("edit_zoom")
        self.set_anypoint = QtWidgets.QPushButton(self.groupBox_3)
        self.set_anypoint.setGeometry(QtCore.QRect(150, 30, 50, 40))
        self.set_anypoint.setStyleSheet("")
        self.set_anypoint.setText("")
        self.set_anypoint.setIcon(icon1)
        self.set_anypoint.setIconSize(QtCore.QSize(25, 25))
        self.set_anypoint.setObjectName("set_anypoint")
        self.panorama_view = QtWidgets.QRadioButton(self.widget)
        self.panorama_view.setGeometry(QtCore.QRect(20, 550, 201, 23))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(14)
        self.panorama_view.setFont(font)
        self.panorama_view.setObjectName("panorama_view")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(40, 450, 120, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.any_mode_1 = QtWidgets.QRadioButton(self.groupBox)
        self.any_mode_1.setGeometry(QtCore.QRect(10, 10, 90, 25))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.any_mode_1.setFont(font)
        self.any_mode_1.setObjectName("any_mode_1")
        self.any_mode_2 = QtWidgets.QRadioButton(self.groupBox)
        self.any_mode_2.setGeometry(QtCore.QRect(10, 45, 90, 25))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.any_mode_2.setFont(font)
        self.any_mode_2.setObjectName("any_mode_2")
        self.panoX_view = QtWidgets.QRadioButton(self.widget)
        self.panoX_view.setGeometry(QtCore.QRect(20, 585, 141, 23))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(14)
        self.panoX_view.setFont(font)
        self.panoX_view.setObjectName("panoX_view")
        self.groupBox_2.raise_()
        self.original_source.raise_()
        self.label_3.raise_()
        self.label_11.raise_()
        self.groupBox_4.raise_()
        self.anypoint_view.raise_()
        self.normal_view.raise_()
        self.groupBox_3.raise_()
        self.panorama_view.raise_()
        self.groupBox.raise_()
        self.panoX_view.raise_()
        self.horizontalLayout_2.addWidget(self.widget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 6, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, -1, 6, -1)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(756, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-width:3px;\n"
"background-color: rgb(186, 189, 182);\n"
"border: 1px solid black;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.rotate_left = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_left.sizePolicy().hasHeightForWidth())
        self.rotate_left.setSizePolicy(sizePolicy)
        self.rotate_left.setMinimumSize(QtCore.QSize(30, 30))
        self.rotate_left.setStyleSheet("border-width:3px;\n"
"border: 1px solid black;")
        self.rotate_left.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/left-rotation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_left.setIcon(icon2)
        self.rotate_left.setIconSize(QtCore.QSize(20, 20))
        self.rotate_left.setObjectName("rotate_left")
        self.horizontalLayout_5.addWidget(self.rotate_left)
        self.rotate_right = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_right.sizePolicy().hasHeightForWidth())
        self.rotate_right.setSizePolicy(sizePolicy)
        self.rotate_right.setMinimumSize(QtCore.QSize(30, 30))
        self.rotate_right.setStyleSheet("border-width:3px;\n"
"border: 1px solid black;")
        self.rotate_right.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/right_rotation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_right.setIcon(icon3)
        self.rotate_right.setIconSize(QtCore.QSize(20, 20))
        self.rotate_right.setObjectName("rotate_right")
        self.horizontalLayout_5.addWidget(self.rotate_right)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(816, 612))
        self.widget_2.setObjectName("widget_2")
        self.Main_window = QtWidgets.QLabel(self.widget_2)
        self.Main_window.setGeometry(QtCore.QRect(0, 0, 816, 612))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_window.sizePolicy().hasHeightForWidth())
        self.Main_window.setSizePolicy(sizePolicy)
        self.Main_window.setStyleSheet("")
        self.Main_window.setText("")
        self.Main_window.setScaledContents(True)
        self.Main_window.setAlignment(QtCore.Qt.AlignCenter)
        self.Main_window.setObjectName("Main_window")
        self.Plus_icon = QtWidgets.QLabel(self.widget_2)
        self.Plus_icon.setGeometry(QtCore.QRect(0, 0, 816, 612))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Plus_icon.sizePolicy().hasHeightForWidth())
        self.Plus_icon.setSizePolicy(sizePolicy)
        self.Plus_icon.setStyleSheet("border-width:3px;\n"
"border: 1px solid black;")
        self.Plus_icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Plus_icon.setText("")
        self.Plus_icon.setObjectName("Plus_icon")
        self.gridLayout_2.addWidget(self.widget_2, 1, 2, 2, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 25))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.MenuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MenuFile.setFont(font)
        self.MenuFile.setObjectName("MenuFile")
        self.menuAbout_Us = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuAbout_Us.setFont(font)
        self.menuAbout_Us.setObjectName("menuAbout_Us")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(1300, 0))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen_Image = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/in_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Image.setIcon(icon4)
        self.actionOpen_Image.setObjectName("actionOpen_Image")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelo = QtWidgets.QAction(MainWindow)
        self.actionHelo.setObjectName("actionHelo")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.actionCamera_Name = QtWidgets.QAction(MainWindow)
        self.actionCamera_Name.setObjectName("actionCamera_Name")
        self.actionLoad_Parameter = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/json.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionLoad_Parameter.setIcon(icon5)
        self.actionLoad_Parameter.setObjectName("actionLoad_Parameter")
        self.MenuFile.addAction(self.actionLoad_Parameter)
        self.MenuFile.addAction(self.actionOpen_Image)
        self.MenuFile.addAction(self.actionExit)
        self.menuAbout_Us.addAction(self.actionHelo)
        self.menuAbout_Us.addAction(self.actionAbout_Us)
        self.menubar.addAction(self.MenuFile.menuAction())
        self.menubar.addAction(self.menuAbout_Us.menuAction())
        self.toolBar.addAction(self.actionLoad_Parameter)
        self.toolBar.addAction(self.actionOpen_Image)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Moil Demo Apps"))
        self.label_3.setText(_translate("MainWindow", "Original Source"))
        self.label_11.setText(_translate("MainWindow", "Select Mode View"))
        self.label_9.setText(_translate("MainWindow", "Max :"))
        self.label_10.setText(_translate("MainWindow", "Min  :"))
        self.anypoint_view.setText(_translate("MainWindow", "AnyPoint"))
        self.normal_view.setText(_translate("MainWindow", "Normal"))
        self.label_6.setText(_translate("MainWindow", "Alpha :"))
        self.label_7.setText(_translate("MainWindow", "Beta   :"))
        self.label_8.setText(_translate("MainWindow", "Zoom :"))
        self.panorama_view.setText(_translate("MainWindow", "Panorama"))
        self.any_mode_1.setText(_translate("MainWindow", "Mode-1"))
        self.any_mode_2.setText(_translate("MainWindow", "Mode-2"))
        self.panoX_view.setText(_translate("MainWindow", "PanoramaX"))
        self.label_4.setText(_translate("MainWindow", "Main Window"))
        self.MenuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout_Us.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen_Image.setText(_translate("MainWindow", "Open Image"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHelo.setText(_translate("MainWindow", "Help"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
        self.actionCamera_Name.setText(_translate("MainWindow", "Camera Name:"))
        self.actionLoad_Parameter.setText(_translate("MainWindow", "Load Parameter"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
