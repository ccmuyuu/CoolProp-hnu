import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QToolBar, QToolButton, QMenu, QAction
from windows import SelectUnitsWindow, SaturationTablesWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.units = ["K", "MPa", "m3", "kg; kmol", "kJ", "m/s", "μPa-s", "mW/m-K", "mN/m"]
        self.setWindowTitle("压焓图计算工具")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        # 添加顶部按钮和子项
        button1 = QToolButton()
        button1.setText("文件")
        menu1 = QMenu(button1)
        b1_s1 = QAction("打开", self)
        menu1.addAction(b1_s1)
        b1_s2 = QAction("保存", self)
        menu1.addAction(b1_s2)
        b1_s3 = QAction("关闭", self)
        menu1.addAction(b1_s3)
        menu1.addSeparator()
        b1_s4 = QAction("退出", self)
        menu1.addAction(b1_s4)
        button1.setMenu(menu1)
        button1.setPopupMode(QToolButton.InstantPopup)
        self.toolbar.addWidget(button1)

        button2 = QToolButton()
        button2.setText("选项")
        menu2 = QMenu(button2)
        b2_s1 = QAction("单位", self)
        b2_s1.triggered.connect(self.open_select_units)
        menu2.addAction(b2_s1)
        b2_s2 = QAction("特性", self)
        menu2.addAction(b2_s2)
        button2.setMenu(menu2)
        button2.setPopupMode(QToolButton.InstantPopup)
        self.toolbar.addWidget(button2)

        button3 = QToolButton()
        button3.setText("工质")
        menu3 = QMenu(button3)
        b3_s1 = QAction("纯流体(单一化合物)", self)
        menu3.addAction(b3_s1)
        b3_s2 = QAction("伪纯流体", self)
        menu3.addAction(b3_s2)
        b3_s3 = QAction("预定义的混合物", self)
        menu3.addAction(b3_s3)
        b3_s4 = QAction("定义新的混合物", self)
        menu3.addAction(b3_s4)
        b3_s5 = QAction("特定流体组", self)
        menu3.addAction(b3_s5)
        button3.setMenu(menu3)
        button3.setPopupMode(QToolButton.InstantPopup)
        self.toolbar.addWidget(button3)

        button4 = QToolButton()
        button4.setText("计算")
        menu4 = QMenu(button4)
        b4_s1 = QAction("饱和状态", self)
        b4_s1.triggered.connect(self.open_saturation_calculation_window)
        menu4.addAction(b4_s1)
        b4_s2 = QAction("非饱和状态", self)
        menu4.addAction(b4_s2)
        b4_s3 = QAction("相位边界", self)
        menu4.addAction(b4_s3)
        menu4.addSeparator()
        b4_s4 = QAction("指定状态点", self)
        menu4.addAction(b4_s4)
        b4_s5 = QAction("饱和点(处于平衡状态)", self)
        menu4.addAction(b4_s5)
        button4.setMenu(menu4)
        button4.setPopupMode(QToolButton.InstantPopup)
        self.toolbar.addWidget(button4)

        self.sub_window = None  # 添加子窗口的成员变量
        self.saturation_window = None  # 添加饱和状态计算窗口的成员变量

    def enable_main_window(self):
        self.setDisabled(False)  # 启用主窗口

    def open_select_units(self):
        if not self.sub_window:
            self.sub_window = SelectUnitsWindow()
            self.sub_window.all_units.connect(self.handle_units_selected)
        self.sub_window.show()

    def handle_units_selected(self, selected_units):
        self.units = selected_units

    def open_saturation_calculation_window(self):
        if not self.saturation_window:
            self.saturation_window = SaturationTablesWindow(self.units)
        else:
            self.saturation_window.units = self.units
        self.saturation_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
