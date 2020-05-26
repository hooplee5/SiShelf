# -*- coding: utf-8 -*-

from ..vendor import Qt
from ..vendor.Qt import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(283, 349)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_6.setSpacing(3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.spinbox_xpop_separator_height = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinbox_xpop_separator_height.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_xpop_separator_height.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinbox_xpop_separator_height.setMaximum(9999)
        self.spinbox_xpop_separator_height.setObjectName("spinbox_xpop_separator_height")
        self.horizontalLayout_9.addWidget(self.spinbox_xpop_separator_height)
        self.button_xpop_separator_color = QtWidgets.QPushButton(self.groupBox_5)
        self.button_xpop_separator_color.setObjectName("button_xpop_separator_color")
        self.horizontalLayout_9.addWidget(self.button_xpop_separator_color)
        self.gridLayout_6.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_5, 8, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.spinbox_xpop_label_size = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinbox_xpop_label_size.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_xpop_label_size.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinbox_xpop_label_size.setMaximum(9999)
        self.spinbox_xpop_label_size.setObjectName("spinbox_xpop_label_size")
        self.horizontalLayout_7.addWidget(self.spinbox_xpop_label_size)
        self.button_xpop_fontcolor = QtWidgets.QPushButton(self.groupBox_3)
        self.button_xpop_fontcolor.setObjectName("button_xpop_fontcolor")
        self.horizontalLayout_7.addWidget(self.button_xpop_fontcolor)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_7.setSpacing(3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.button_xpop_bgtopcolor = QtWidgets.QPushButton(self.groupBox_6)
        self.button_xpop_bgtopcolor.setObjectName("button_xpop_bgtopcolor")
        self.horizontalLayout_8.addWidget(self.button_xpop_bgtopcolor)
        self.button_xpop_bgbottomcolor = QtWidgets.QPushButton(self.groupBox_6)
        self.button_xpop_bgbottomcolor.setObjectName("button_xpop_bgbottomcolor")
        self.horizontalLayout_8.addWidget(self.button_xpop_bgbottomcolor)
        self.button_xpop_selectedcolor = QtWidgets.QPushButton(self.groupBox_6)
        self.button_xpop_selectedcolor.setObjectName("button_xpop_selectedcolor")
        self.horizontalLayout_8.addWidget(self.button_xpop_selectedcolor)
        self.gridLayout_7.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_6, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.checkbox_xpop_customize = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkbox_xpop_customize.setChecked(False)
        self.checkbox_xpop_customize.setObjectName("checkbox_xpop_customize")
        self.horizontalLayout.addWidget(self.checkbox_xpop_customize)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.buttonbox = QtWidgets.QDialogButtonBox(Form)
        self.buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonbox.setObjectName("buttonbox")
        self.gridLayout.addWidget(self.buttonbox, 3, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.spinbox_snap_width = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinbox_snap_width.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_snap_width.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinbox_snap_width.setMaximum(9999)
        self.spinbox_snap_width.setObjectName("spinbox_snap_width")
        self.horizontalLayout_5.addWidget(self.spinbox_snap_width)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.spinbox_snap_height = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinbox_snap_height.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_snap_height.setMaximum(9999)
        self.spinbox_snap_height.setObjectName("spinbox_snap_height")
        self.horizontalLayout_5.addWidget(self.spinbox_snap_height)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.checkbox_snap_active = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_snap_active.setChecked(False)
        self.checkbox_snap_active.setObjectName("checkbox_snap_active")
        self.horizontalLayout_4.addWidget(self.checkbox_snap_active)
        self.checkbox_snap_grid = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_snap_grid.setChecked(True)
        self.checkbox_snap_grid.setObjectName("checkbox_snap_grid")
        self.horizontalLayout_4.addWidget(self.checkbox_snap_grid)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.spinbox_tab_label_size = QtWidgets.QSpinBox(self.groupBox)
        self.spinbox_tab_label_size.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_tab_label_size.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinbox_tab_label_size.setMaximum(9999)
        self.spinbox_tab_label_size.setObjectName("spinbox_tab_label_size")
        self.horizontalLayout_6.addWidget(self.spinbox_tab_label_size)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.spinbox_tab_height = QtWidgets.QSpinBox(self.groupBox)
        self.spinbox_tab_height.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_tab_height.setMaximum(9999)
        self.spinbox_tab_height.setObjectName("spinbox_tab_height")
        self.horizontalLayout_6.addWidget(self.spinbox_tab_height)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(Qt.QtCompat.translate("Form", "Form", None, -1))
        self.groupBox_3.setTitle(Qt.QtCompat.translate("Form", "XPOP", None, -1))
        self.groupBox_5.setTitle(Qt.QtCompat.translate("Form", "Separator", None, -1))
        self.label_11.setText(Qt.QtCompat.translate("Form", "height", None, -1))
        self.button_xpop_separator_color.setText(Qt.QtCompat.translate("Form", "Color", None, -1))
        self.label_10.setText(Qt.QtCompat.translate("Form", "FontSize", None, -1))
        self.button_xpop_fontcolor.setText(Qt.QtCompat.translate("Form", "FontColor", None, -1))
        self.groupBox_6.setTitle(Qt.QtCompat.translate("Form", "Background", None, -1))
        self.button_xpop_bgtopcolor.setText(Qt.QtCompat.translate("Form", "TopColor", None, -1))
        self.button_xpop_bgbottomcolor.setText(Qt.QtCompat.translate("Form", "BottomColor", None, -1))
        self.button_xpop_selectedcolor.setText(Qt.QtCompat.translate("Form", "SelectedColor", None, -1))
        self.checkbox_xpop_customize.setText(Qt.QtCompat.translate("Form", "Customize", None, -1))
        self.groupBox_4.setTitle(Qt.QtCompat.translate("Form", "Shelf", None, -1))
        self.groupBox_2.setTitle(Qt.QtCompat.translate("Form", "Snap", None, -1))
        self.label_7.setText(Qt.QtCompat.translate("Form", "Width", None, -1))
        self.label_6.setText(Qt.QtCompat.translate("Form", "Height", None, -1))
        self.checkbox_snap_active.setText(Qt.QtCompat.translate("Form", "Active", None, -1))
        self.checkbox_snap_grid.setText(Qt.QtCompat.translate("Form", "Guide grid", None, -1))
        self.groupBox.setTitle(Qt.QtCompat.translate("Form", "Tab", None, -1))
        self.label_8.setText(Qt.QtCompat.translate("Form", "FontSize", None, -1))
        self.label_9.setText(Qt.QtCompat.translate("Form", "Height", None, -1))
