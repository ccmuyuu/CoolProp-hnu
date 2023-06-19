from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGroupBox, QFormLayout, QPushButton
from PyQt5.QtCore import Qt
from calc import SaturationResultWindow

def handle_lables(vary, units):
    if vary == 0:
        return "温度", units[0]
    elif vary == 1:
        return "压力", units[1]

def handle_type(type):
    if type == 0:
        return "饱和气液"
    elif type == 1:
        return "熔化线"
    elif type == 2:
        return "升华线"

def create_input_layout(line_edit, unit):
    input_layout = QHBoxLayout()
    input_layout.addWidget(line_edit)
    input_layout.addWidget(QLabel(unit))
    return input_layout

class input_T_or_P(QWidget):
    def __init__(self, type, vary, units):
        super().__init__()
        self.type, self.vary, self.units = type, vary, units 
        self.input_lables, self.input_units = handle_lables(self.vary, self.units)
        
        self.setWindowTitle("输入属性范围")
        self.setGeometry(1000, 400, 300, 190)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 创建方框1
        group_box1 = QGroupBox("")
        layout.addWidget(group_box1)
        group_box1.setFixedSize(250, 100)

        group_box1_layout = QVBoxLayout()
        group_box1.setLayout(group_box1_layout)

        # 使用QFormLayout来放置标签和字段
        form_layout = QFormLayout()
        group_box1_layout.addLayout(form_layout)

        self.line_edit1 = QLineEdit() # 添加输入框
        input_layout1 = create_input_layout(self.line_edit1, self.input_units)
        self.line_edit2 = QLineEdit() # 添加输入框
        input_layout2 = create_input_layout(self.line_edit2, self.input_units)
        self.line_edit3 = QLineEdit() # 添加输入框
        input_layout3 = create_input_layout(self.line_edit3, self.input_units)

        form_layout.addRow(f"起始{self.input_lables}", input_layout1)
        form_layout.addRow(f"最终{self.input_lables}", input_layout2)
        form_layout.addRow("增量", input_layout3)

        self.setWindowModality(Qt.ApplicationModal)

        button_layout = QHBoxLayout()
        ok_button = QPushButton("确定")
        cancel_button = QPushButton("取消")

        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)

        cancel_button.clicked.connect(self.close)
        ok_button.clicked.connect(self.handle_ok_button_clicked)

    def handle_ok_button_clicked(self):
        # 处理确认按钮的点击事件    
        start_value = float(self.line_edit1.text())
        end_value = float(self.line_edit2.text())
        increment = float(self.line_edit3.text())

        self.saturationresultwindow = SaturationResultWindow("R410A", handle_type(self.type), self.input_lables, self.input_units, start_value, end_value, increment, self.units)
        self.saturationresultwindow.show()
        self.close()

