from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QToolBar,
    QPushButton, QGraphicsPixmapItem, QGraphicsPathItem, QHBoxLayout, QVBoxLayout, 
    QWidget, QSpacerItem, QSizePolicy, QTextBrowser, QLabel, QDialog
)
from PyQt5.QtGui import QPen, QPainterPath, QPixmap, QPainter, QColor, QImage, QImageWriter, QIcon
from PyQt5.QtCore import Qt, QSysInfo, pyqtSlot

class ResultWindow(QDialog):
    def __init__(self, result_text):
        super().__init__()

        self.setWindowTitle("Guess Result")
        self.setGeometry(75, 450, 400, 100)

        label = QLabel(result_text)
        label.setAlignment(Qt.AlignCenter)
        
        # Increase the font size for better readability
        font = label.font()
        font.setPointSize(16)
        label.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)

class InstructionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Instructions")
        self.setGeometry(60, 167, 100, 200)  # Set the initial position and size
        self.setWindowIcon(QIcon("icon.png"))

        instructions_text = """
        <html>
            <body style="font-family: Arial; font-size: 16px; font-weight: bold;">
                <p>Welcome to Graph Guesser!</p>
                <p>Instructions:</p>
                <ol>
                    <li>Use the left mouse button to draw on the canvas.</li>
                    <li>Click the 'Clear' button to clear the canvas.</li>
                    <li>Draw a simple function, for example: y = x²</li>
                    <li>Click the 'Guess' button to save and guess the drawn image.</li>
                </ol>
            </body>
        </html>
        """

        label = QLabel()
        label.setTextFormat(Qt.RichText)
        label.setText(instructions_text)
        label.setOpenExternalLinks(True)

        layout = QVBoxLayout()
        layout.addWidget(label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

class DrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.instruction_window = InstructionWindow()  # Keep a reference to the instruction window

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setSizePolicy(self.view.sizePolicy().horizontalPolicy(), self.view.sizePolicy().verticalPolicy())
        self.view.setSceneRect(0, 0, 730, 730)

        background_image = QPixmap("graph.png")
        if not background_image.isNull():
            background_item = QGraphicsPixmapItem(background_image)
            self.scene.addItem(background_item)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_canvas)
        self.guess_button = QPushButton("Guess")
        self.guess_button.clicked.connect(self.guess_image)
        self.setWindowIcon(QIcon("icon.png"))

        # Apply stylesheets for nicer button appearance
        button_stylesheet = (
            "QPushButton {"
            "   background-color: #2299e3;"
            "   color: white;"
            "   border-radius: 10px;"
            "   border: 2px solid #1775b0;" 
            "   padding: 10px 20px;"
            "   font-size: 16px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #135a87;" 
            "}"
        )

        self.clear_button.setStyleSheet(button_stylesheet)
        self.guess_button.setStyleSheet(button_stylesheet)

        # Create a widget to hold the buttons
        button_widget = QWidget()
        button_layout = QHBoxLayout(button_widget)

        # Add a stretchable space on the left
        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        button_layout.addSpacerItem(QSpacerItem(6, 20, QSizePolicy.Fixed, QSizePolicy.Minimum))

        # Add the "Clear" and "Guess" buttons
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.guess_button)

        # Add a stretchable space on the right
        button_layout.addSpacerItem(QSpacerItem(90, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  # Adjusted width to 90 pixels

        # Create the toolbar and add the button widget
        self.toolbar = QToolBar("Toolbar", movable=False)
        self.toolbar.addWidget(button_widget)
        
        # Set the allowed area for the toolbar
        self.toolbar.setAllowedAreas(Qt.BottomToolBarArea)
        
        self.addToolBar(Qt.BottomToolBarArea, self.toolbar)

        self.path = None
        self.pen = QPen(QColor(39, 118, 174), 3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.scene.mousePressEvent = self.start_drawing
        self.scene.mouseMoveEvent = self.draw
        self.setCentralWidget(self.view)
        self.setWindowTitle("Graph Guesser")
        self.centralWidget().setSizePolicy(self.centralWidget().sizePolicy().horizontalPolicy(), self.centralWidget().sizePolicy().verticalPolicy())
        self.setFixedSize(732, 801)

    def start_drawing(self, event):
        if event.button() == Qt.LeftButton:
            self.path = QPainterPath()
            pos = event.scenePos()
            self.path.moveTo(pos)

    def draw(self, event):
        if self.path is not None and event.buttons() == Qt.LeftButton:
            pos = event.scenePos()
            self.path.lineTo(pos)
            self.scene.addPath(self.path, self.pen)

    def clear_canvas(self):
        for item in self.scene.items():
            if isinstance(item, QGraphicsPathItem):
                self.scene.removeItem(item)

    def guess_image(self):
        # Get the visible rect in scene coordinates
        visible_rect = self.view.mapToScene(self.view.viewport().rect()).boundingRect()

        # Set the scene rect to the visible area
        self.scene.setSceneRect(visible_rect)

        # Render the scene into an image
        image = QImage(self.view.viewport().size(), QImage.Format_ARGB32)
        image.fill(Qt.transparent)
        painter = QPainter(image)
        self.scene.render(painter)
        painter.end()

        # Save the image to a file (e.g., PNG format)
        image_writer = QImageWriter("output_image.png")
        image_writer.write(image)

        # Placeholder for the actual function guessing logic
        guessed_function = "y = x^2"  # Replace this with your actual guessing logic

        # Display the result in a new window
        result_text = f"Your function is: {guessed_function}, 56% similar"  # Modify as needed
        result_window = ResultWindow(result_text)
        result_window.exec_()

        print("Guessing . . . Image saved as output_image.png")


    @pyqtSlot()
    def close_instruction_window(self):
        self.instruction_window.close()

if __name__ == "__main__":
    app = QApplication([])

    # Create and show the main window
    main_window = DrawingApp()
    main_window.show()

    # Connect the destroyed signal of the main window to the custom slot
    main_window.destroyed.connect(main_window.close_instruction_window)

    # Create and show the instruction window
    instruction_window = main_window.instruction_window
    instruction_window.show()

    app.exec_()