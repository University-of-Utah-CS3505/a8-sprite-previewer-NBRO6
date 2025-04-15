import math
import sys

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

#Nick Brault
#Martin Cheng
# https://github.com/University-of-Utah-CS3505/a8-sprite-previewer-NBRO6

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = os.path.join(sprite_folder_name, f"sprite_{str(frame).rjust(padding, '0')}.png")
        frames.append(QPixmap(folder_and_file_name))
    return frames

class SpritePreview(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        self.setGeometry(100, 100, 400, 300)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu("File")

        pause_action = QAction("Pause", self)
        pause-action.triggered.connect(self.pause_animation)
        file_menu.addAction(pause_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 120)
        self.slider.setValue(60)
        self.slider.valueChanged.connect(self.update_fps)
        self.layout.addWidget(self.slider)

        self.fps_label = QLabel("Frames per second 60")
        self.fps_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.fps_label)

        self.button = QPushButton("Play")
        self.button.clicked.connect(self.play_animation)
        self.layout.addWidget(self.button)

        self.frames = load_sprite("sprites", 6)
        self.current_frame = 0

        if self.frames:
            self.label.setPixmap(self.frames[0])

        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)

        self.fps = 60

    def next_frame(self)
        if self.frames:
            self.label.setPixmap(self.frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def pause_animation(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.update_fps()

    def play_animation(self):
        self.update_fps()

    def update_fps(self):
        fps = self.slider.value()
        self.fps_label.setText(f"Frames per second {fps}")
        if fps == 0:
            self.timer.stop()
        else:
            interval = int(1000 / fps)
            if self.timer.isActive():
                self.timer.stop()
            self.timer.start(interval)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpritePreviewer()
    window.show()
    sys.exit(app.exec())





