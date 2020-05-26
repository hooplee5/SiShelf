# -*- coding: utf-8 -*-

from ..vendor import Qt
from ..vendor.Qt import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(556, 258)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonbox = QtWidgets.QDialogButtonBox(Form)
        self.buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonbox.setObjectName("buttonbox")
        self.gridLayout.addWidget(self.buttonbox, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.button_preview = QtWidgets.QHBoxLayout()
        self.button_preview.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.button_preview.setObjectName("button_preview")
        self.horizontalLayout_9.addLayout(self.button_preview)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.spinbox_btn_position_x = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinbox_btn_position_x.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_btn_position_x.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinbox_btn_position_x.setMaximum(9999)
        self.spinbox_btn_position_x.setObjectName("spinbox_btn_position_x")
        self.horizontalLayout_5.addWidget(self.spinbox_btn_position_x)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.spinbox_btn_position_y = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinbox_btn_position_y.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_btn_position_y.setMaximum(9999)
        self.spinbox_btn_position_y.setObjectName("spinbox_btn_position_y")
        self.horizontalLayout_5.addWidget(self.spinbox_btn_position_y)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spinbox_line_length = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinbox_line_length.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_line_length.setMaximum(9999)
        self.spinbox_line_length.setObjectName("spinbox_line_length")
        self.horizontalLayout_2.addWidget(self.spinbox_line_length)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.spinbox_line_width = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinbox_line_width.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_line_width.setMaximum(9999)
        self.spinbox_line_width.setObjectName("spinbox_line_width")
        self.horizontalLayout_8.addWidget(self.spinbox_line_width)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.combo_style = QtWidgets.QComboBox(self.groupBox_2)
        self.combo_style.setObjectName("combo_style")
        self.combo_style.addItem("")
        self.combo_style.addItem("")
        self.horizontalLayout_11.addWidget(self.combo_style)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spinbox_label_font_size = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinbox_label_font_size.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_label_font_size.setObjectName("spinbox_label_font_size")
        self.horizontalLayout_3.addWidget(self.spinbox_label_font_size)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.checkbox_use_label = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_use_label.setText("")
        self.checkbox_use_label.setChecked(True)
        self.checkbox_use_label.setObjectName("checkbox_use_label")
        self.horizontalLayout_4.addWidget(self.checkbox_use_label)
        self.label_label = QtWidgets.QLabel(self.groupBox_2)
        self.label_label.setObjectName("label_label")
        self.horizontalLayout_4.addWidget(self.label_label)
        self.line_label = QtWidgets.QLineEdit(self.groupBox_2)
        self.line_label.setObjectName("line_label")
        self.horizontalLayout_4.addWidget(self.line_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_12.addWidget(self.label_2)
        self.button_color = QtWidgets.QPushButton(self.groupBox_2)
        self.button_color.setObjectName("button_color")
        self.horizontalLayout_12.addWidget(self.button_color)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(Qt.QtCompat.translate("Form", "Form", None, -1))
        self.groupBox_2.setTitle(Qt.QtCompat.translate("Form", "partition", None, -1))
        self.label_7.setText(Qt.QtCompat.translate("Form", "Position ", None, -1))
        self.label_6.setText(Qt.QtCompat.translate("Form", "×", None, -1))
        self.label.setText(Qt.QtCompat.translate("Form", "LineLength ", None, -1))
        self.label_8.setText(Qt.QtCompat.translate("Form", "LineWidth ", None, -1))
        self.label_5.setText(Qt.QtCompat.translate("Form", "Style ", None, -1))
        self.combo_style.setItemText(0, Qt.QtCompat.translate("Form", "Horizontal", None, -1))
        self.combo_style.setItemText(1, Qt.QtCompat.translate("Form", "Vertical", None, -1))
        self.label_4.setText(Qt.QtCompat.translate("Form", "Label Font Size ", None, -1))
        self.label_label.setText(Qt.QtCompat.translate("Form", "Label ", None, -1))
        self.label_2.setText(Qt.QtCompat.translate("Form", "Color", None, -1))
        self.button_color.setText(Qt.QtCompat.translate("Form", "SelectColor", None, -1))
