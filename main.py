import sys
from datetime import datetime

from PySide6.QtWidgets import QApplication, QFrame, QLabel, QWidget
from PySide6.QtCore import Qt, QTimer

class IslandFrame(QFrame):
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start = event.globalPosition()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            print("Dynamic Island left-clicked!")


    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("Dynamic Island double-clicked!")

    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.setCursor(Qt.CursorShape.OpenHandCursor)
            print("Dynamic Island left button released!")

   
    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            delta = event.globalPosition() - self.drag_start

            window = self.parentWidget()
            new_position = window.pos() + delta.toPoint()

            screen_rect = window.screen().availableGeometry()
            minimum_x = screen_rect.x()
            maximum_x = screen_rect.right() - window.width() + 1
            minimum_y = screen_rect.y()
            maximum_y = screen_rect.bottom() - window.height() + 1

            safe_x = max(minimum_x, min(new_position.x(), maximum_x))
            safe_y = max(minimum_y, min(new_position.y(), maximum_y))

            window.move(safe_x, safe_y)
            self.drag_start = event.globalPosition()

app = QApplication(sys.argv)

screen = app.primaryScreen()

window = QWidget()
window.setWindowFlag(Qt.WindowType.Tool)
window.setWindowFlag(Qt.WindowType.FramelessWindowHint)
window.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
window.setAttribute(Qt.WidgetAttribute.WA_QuitOnClose, True)
window.setWindowTitle("Windows Dynamic Island")
window.resize(400, 48)


window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

background = IslandFrame(window)
background.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
background.setGeometry(0, 0, 400, 48)
background.setStyleSheet("background-color: #202124; border-radius: 24px;")
background.setCursor(Qt.CursorShape.OpenHandCursor)

label = QLabel(datetime.now().strftime("%H:%M"), background)
label.setGeometry(24, 0, 352, 48)
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
label.setStyleSheet("color: white; background-color: transparent;")
label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)

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