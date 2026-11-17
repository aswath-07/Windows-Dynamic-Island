import sys
from datetime import datetime

from PySide6.QtWidgets import QApplication, QFrame, QLabel, QWidget
from PySide6.QtCore import Qt, QTimer

app = QApplication(sys.argv)

screen = app.primaryScreen()

window = QWidget()
window.setWindowFlag(Qt.WindowType.FramelessWindowHint)
window.setWindowTitle("Windows Dynamic Island")
window.resize(400, 48)


window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

background = QFrame(window)
background.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
background.setGeometry(0, 0, 400, 48)
background.setStyleSheet("background-color: #202124; border-radius: 24px;")

label = QLabel(datetime.now().strftime("%H:%M"), background)
label.setGeometry(24, 0, 352, 48)
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
label.setStyleSheet("color: white; background-color: transparent;")


def update_clock():
    label.setText(datetime.now().strftime("%H:%M"))

update_clock()

timer = QTimer()
timer.timeout.connect(update_clock)
timer.start(1000)

center_x = screen.geometry().x() + (screen.geometry().width() - window.width()) // 2
window.move(center_x, 20)

window.show()

sys.exit(app.exec())