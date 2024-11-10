import os

from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QHBoxLayout, QPushButton, QLabel, \
    QTextEdit, QDialogButtonBox, QInputDialog
from main_Ui import MainUi
import sys
import sqlite3


class DialogUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)
        self.buttons = QDialogButtonBox(self)
        self.buttons.clicked.connect(self.btn_event)

    def btn_event(self):
        print(self.sender())


class MainWindow(MainUi, QMainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.setWindowTitle("Планировщик R. edition")
        self.pushButton.clicked.connect(self.create_task)
        self.update_tasks()

    def update_tasks(self):
        self.arr_btn = []
        self.arr_label = []
        self.listWidget.clear()
        with sqlite3.connect("tasks.db") as conn:
            c = conn.cursor()
            res = c.execute("SELECT id,text FROM tasks").fetchall()
            for i in res:
                itemN = QListWidgetItem()
                widget = QWidget()
                widgetText = QLabel(i[1])
                widgetButton = QPushButton("Удалить")
                widgetButton.clicked.connect(self.delete_task)
                self.arr_btn.append(widgetButton)
                self.arr_label.append(widgetText)
                widgetLayout = QHBoxLayout()
                widgetLayout.addWidget(widgetText)
                widgetLayout.addWidget(widgetButton)
                widgetLayout.addStretch()

                # widgetLayout.setSizeConstraint(QtWidgets.QLayout.sets)
                widget.setLayout(widgetLayout)
                itemN.setSizeHint(widget.sizeHint())
                self.listWidget.addItem(itemN)
                self.listWidget.setItemWidget(itemN, widget)

    def create_task(self):
        text, state = QInputDialog.getText(self, "", "Введите текст задачи:", )
        if text and state:
            with sqlite3.connect("tasks.db") as conn:
                c = conn.cursor()
                c.execute(f"INSERT INTO tasks (text) VALUES ('{text}')").fetchall()
            self.update_tasks()

    def delete_task(self):
        item = self.listWidget.currentItem()
        labl = self.arr_label[self.arr_btn.index(self.sender())]
        with sqlite3.connect("tasks.db") as conn:
            c = conn.cursor()
            c.execute(f"DELETE FROM tasks WHERE text='{labl.text()}'")
            conn.commit()
        # self.listWidget.insertItem(self.arr_btn.index(self.sender()))
        self.arr_btn.remove(self.sender())
        self.arr_label.remove(labl)
        self.update_tasks()


if __name__ == '__main__':
    if not os.path.exists('tasks.db'):
        with sqlite3.connect('tasks.db') as conn:
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, text TEXT)")
            conn.commit()
    app = QApplication(sys.argv)
    plan = MainWindow()
    plan.show()
    sys.exit(app.exec())
