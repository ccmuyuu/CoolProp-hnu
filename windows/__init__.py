from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QComboBox, QGroupBox, QCheckBox, QHBoxLayout, QPushButton, QButtonGroup
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from functools import partial
from .saturation_window import input_T_or_P

class SelectUnitsWindow(QWidget):
    all_units = pyqtSignal(list)  # 创建一个信号

    def __init__(self):
        super().__init__()
        self.setWindowTitle("选择单位")
        self.setGeometry(685, 368, 550, 345)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.selected_units = ["K", "MPa", "m3", "kg; kmol", "kJ", "m/s", "μPa-s", "mW/m-K", "mN/m"]  # 保存当前各个单位名称对应的单位

        self.create_table()

    def create_table(self):
        table_widget = QTableWidget()
        table_widget.setColumnCount(2)
        table_widget.setHorizontalHeaderLabels(["单位名称", "单位"])
        table_widget.setShowGrid(False)  # 隐藏表格线
        table_widget.verticalHeader().setVisible(False)  # 隐藏垂直表头

        units_data = [
            ["温度", ["K", "°C", "°F", "°R", "T/Tc"]],
            ["压力", ["Pa", "kPa", "MPa", "bar", "atm", "mmHg", "inHg", "psia", "p/pc"]],
            ["体积", ["m3", "cm3", "dm3", "L", "in3", "ft3", "gal", "V/Vc"]],
            ["质量/摩尔", ["g; mol", "kg; kmol", "lbm; lbmol"]],
            ["能量", ["J", "kJ", "cal", "kcal", "Btu", "/RTc"]],
            ["声速", ["m/s", "cm/s", "in/s", "ft/s", "mph"]],
            ["粘度", ["Pa-s", "mPa-s", "μPa-s", "g/cm-s", "Poise", "cPoise", "lbm/ft-s", "lbm/ft-h"]],
            ["热导率", ["W/m-K", "mW/m-K", "g-cm/s3-K", "cal/s-cm-K", "lbm-ft/s3-°F", "lbf/s-°F", "Btu/h-ft-°F", "Btu-in/h-ft2-°F"]],
            ["表面张力", ["N/m", "mN/m", "dyn/cm", "lbf/ft"]],
        ]

        table_widget.setColumnCount(2)
        table_widget.setRowCount(len(units_data))
        for row, data in enumerate(units_data):
            name_item = QTableWidgetItem(data[0])
            table_widget.setItem(row, 0, name_item)

            unit_combo = QComboBox()
            unit_combo.addItems(data[1])
            unit_combo.setCurrentIndex(data[1].index(self.selected_units[row]))  # 设置默认选项的索引值
            table_widget.setCellWidget(row, 1, unit_combo)
            unit_combo.currentIndexChanged.connect(partial(self.handle_unit_selected, row, unit_combo))

        self.layout().addWidget(table_widget)

        # 设置模态窗口
        self.setWindowModality(Qt.ApplicationModal)

    def handle_unit_selected(self, row, combo):
        unit = combo.currentText()
        # 更新 selected_units 列表
        self.selected_units[row] = unit

        # # 发出信号，将 selected_units 作为参数传递
        self.all_units.emit(self.selected_units)

class SaturationTablesWindow(QWidget):
    def __init__(self,units):
        self.units = units
        super().__init__()
        self.setWindowTitle("特定饱和状态")
        self.setGeometry(400, 200, 500, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        hbox = QHBoxLayout()
        layout.addLayout(hbox)

        group_box1 = QGroupBox("类型")
        group_box2 = QGroupBox("变化量")

        hbox.addWidget(group_box1)
        hbox.addWidget(group_box2)

        # 设置方框1的固定大小
        group_box1.setFixedSize(200, 150)

        # 设置方框2的固定大小
        group_box2.setFixedSize(200, 150)

        # 添加勾选框到方框1
        self.checkbox1_1 = QCheckBox("饱和气液")
        self.checkbox1_2 = QCheckBox("饱和固液(熔化线)")
        self.checkbox1_3 = QCheckBox("饱和固气(升华线)")

        group_box1_layout = QVBoxLayout()
        group_box1.setLayout(group_box1_layout)
        group_box1_layout.addWidget(self.checkbox1_1)
        group_box1_layout.addWidget(self.checkbox1_2)
        group_box1_layout.addWidget(self.checkbox1_3)
        self.checkbox1_1.setChecked(True)  # 默认勾选第一个选项

        # 添加勾选框到方框2
        self.checkbox2_1 = QCheckBox("温度")
        self.checkbox2_2 = QCheckBox("压力")
        self.checkbox2_3 = QCheckBox("固定温度时的质量")
        self.checkbox2_4 = QCheckBox("固定压力时的质量")

        group_box2_layout = QVBoxLayout()
        group_box2.setLayout(group_box2_layout)
        group_box2_layout.addWidget(self.checkbox2_1)
        group_box2_layout.addWidget(self.checkbox2_2)
        group_box2_layout.addWidget(self.checkbox2_3)
        group_box2_layout.addWidget(self.checkbox2_4)
        self.checkbox2_1.setChecked(True)  # 默认勾选第一个选项

        # 添加按钮
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        ok_button = QPushButton("确定")
        cancel_button = QPushButton("取消")

        button_layout.addStretch()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        # 创建按钮组并设置互斥性
        button_group1 = QButtonGroup(self)
        button_group1.addButton(self.checkbox1_1)
        button_group1.addButton(self.checkbox1_2)
        button_group1.addButton(self.checkbox1_3)
        button_group1.setExclusive(True)  # 设置为互斥状态

        button_group2 = QButtonGroup(self)
        button_group2.addButton(self.checkbox2_1)
        button_group2.addButton(self.checkbox2_2)
        button_group2.addButton(self.checkbox2_3)
        button_group2.addButton(self.checkbox2_4)
        button_group2.setExclusive(True)  # 设置为互斥状态

        # 连接checkbox1_2的状态改变信号到槽函数
        self.checkbox1_2.stateChanged.connect(self.handle_checkbox1_2_state_changed)
        self.checkbox1_3.stateChanged.connect(self.handle_checkbox1_2_state_changed)

        cancel_button.clicked.connect(self.close)  # 将取消按钮的clicked信号连接到close方法
        ok_button.clicked.connect(self.open_input_saturation_window)# 连接确定按钮的点击事件到打开另一个子窗口的槽函数
        
        self.setLayout(layout)

        # 设置模态窗口
        self.setWindowModality(Qt.ApplicationModal)

    @pyqtSlot(int)
    def handle_checkbox1_2_state_changed(self, state):
        # 根据checkbox1_2的状态设置checkbox2_3的可用性
        self.checkbox2_3.setDisabled(state == Qt.Checked)
        self.checkbox2_4.setDisabled(state == Qt.Checked)
        self.checkbox2_1.setChecked(True) #重新勾选第一个选项

    def open_input_saturation_window(self):
        self.selected_type, self.selected_vary = None, None
         
        # 获取类型复选框的选中状态
        type_checkboxes = [self.checkbox1_1, self.checkbox1_2, self.checkbox1_3]
        for i, checkbox in enumerate(type_checkboxes):
            if checkbox.isChecked():
                self.selected_type = i

        # 获取变化量复选框的选中状态
        vary_checkboxes = [self.checkbox2_1, self.checkbox2_2, self.checkbox2_3, self.checkbox2_4]
        for i, checkbox in enumerate(vary_checkboxes):
            if checkbox.isChecked():
                self.selected_vary = i

        if self.selected_vary == 0 or self.selected_vary == 1:
            self.input_saturation_window = input_T_or_P(self.selected_type, self.selected_vary,self.units)
            self.input_saturation_window.show()
        self.close() # 关闭当前子窗口
        