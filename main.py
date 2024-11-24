import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from Ui import MainUi, DialogUi
import sys
import sqlite3


class MainWindow(MainUi, QMainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.setWindowTitle("Планировщик R. edition")
        self.pushButton.clicked.connect(self.create_task)
        self.update_tasks()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_C:
            self.create_task()

    def update_tasks(self):
        self.arr_btn = []
        self.arr_label = []
        self.listWidget.clear()
        with sqlite3.connect("tasks.db") as conn:
            c = conn.cursor()
            res = c.execute("SELECT id,text,time FROM tasks").fetchall()
            res = sorted(res, key=lambda x: int("".join(x[2].split(":"))))
            for i in res:
                itemN = QListWidgetItem()
                widget = QWidget()
                widgetText = QLabel(f"{i[1]} ;;; {i[2]}")
                widgetButton = QPushButton("Удалить")
                widgetButton.clicked.connect(self.delete_task)
                self.arr_btn.append(widgetButton)
                self.arr_label.append(widgetText)
                widgetLayout = QHBoxLayout()
                widgetLayout.addWidget(widgetText)
                widgetLayout.addWidget(widgetButton)
                widgetLayout.addStretch()

                widget.setLayout(widgetLayout)
                itemN.setSizeHint(widget.sizeHint())
                self.listWidget.addItem(itemN)
                self.listWidget.setItemWidget(itemN, widget)

    def create_task(self):
        self.hide()
        dlg = DialogUi()
        text = ""
        if dlg.exec():
            text = dlg.lineEdit.text()
            time = dlg.timeEdit.text()
        self.show()
        if text:
            with sqlite3.connect("tasks.db") as conn:
                c = conn.cursor()
                c.execute(f"INSERT INTO tasks (text,time) VALUES ('{text}','{time}')").fetchall()
            self.update_tasks()

    def delete_task(self):
        labl = self.arr_label[self.arr_btn.index(self.sender())]
        task = labl.text().split(" ;;; ")
        text = task[0]
        time = task[1]
        with sqlite3.connect("tasks.db") as conn:
            c = conn.cursor()
            c.execute(f"DELETE FROM tasks WHERE text='{text}' AND time='{time}'")
            conn.commit()
        self.arr_btn.remove(self.sender())
        self.arr_label.remove(labl)
        self.update_tasks()


if __name__ == '__main__':
    if not os.path.exists('tasks.db'):
        with sqlite3.connect('tasks.db') as conn:
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, text TEXT,time TEXT)")
            conn.commit()
    app = QApplication(sys.argv)
    plan = MainWindow()
    plan.show()
    sys.exit(app.exec())
