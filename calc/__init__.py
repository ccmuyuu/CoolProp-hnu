from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox
from . import calc_saturation

class SaturationResultWindow(QWidget):
    def __init__(self, working_fluid, type, vary, unit,start, end, range, units):
        super().__init__()

        results = calc_saturation.calc_saturation(working_fluid, type, vary, unit, start, end, range, units)
        print(results)
        if results[0]:        
            self.setWindowTitle(f"{working_fluid}: {type} {vary}={start} 到 {end} {unit}")
            self.setGeometry(400, 200, 1280, 720)

            layout = QVBoxLayout()
            self.setLayout(layout)
            # 创建表格
            self.table = QTableWidget(len(results), 9)
            layout.addWidget(self.table)
            self.table.setHorizontalHeaderLabels([f"温度 {units[0]}", f"饱和液态压力 {units[1]}", f"饱和气态压力 {units[1]}", "饱和液态密度 kg/m3", "饱和气态密度 kg/m3", "饱和液态比焓 kJ/kg", "饱和气态比焓 kJ/kg", "饱和液态比熵 kJ/(kg*K)", "饱和气态比熵 kJ/(kg*K)"])  # 设置表头
            for i, result in enumerate(results[1:]):
                print(i, result)
                for j, item in enumerate(result):
                    if item <= 1:
                        item = round(item,5)
                    elif 1 < item <= 10:
                        item = round(item,4)
                    else:
                        item = round(item,2)
                    self.table.setItem(i, j, QTableWidgetItem(str(item)))
                    self.table.setColumnWidth(j, 135)
        else:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setWindowTitle("错误")
            error_dialog.setText("发生错误！")
            error_dialog.setInformativeText("请检查输入的范围")
            error_dialog.exec_()