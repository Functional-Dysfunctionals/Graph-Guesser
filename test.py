import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication, Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 300)  # Set initial geometry (x, y, width, height)

        # Create a button to trigger window size change
        self.button = QPushButton('Toggle Size', self)
        self.button.clicked.connect(self.toggle_size)

        # Disable window maximize button
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)

        self.show()

        self.expanded = False  # Track the current state

    def toggle_size(self):
        if self.expanded:
            self.animate_resize(400, 300)  # Retract size
        else:
            self.animate_resize(600, 400)  # Expand size

        self.expanded = not self.expanded

    def animate_resize(self, target_width, target_height):
        current_width, current_height = self.width(), self.height()
        num_steps = 30  # Adjust the number of steps as needed

        width_step = (target_width - current_width) / num_steps
        height_step = (target_height - current_height) / num_steps

        for _ in range(num_steps):
            current_width += width_step
            current_height += height_step
            self.resize(int(current_width), int(current_height))
            QCoreApplication.processEvents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())