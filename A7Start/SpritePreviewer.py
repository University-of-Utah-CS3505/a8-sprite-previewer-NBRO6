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
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        self.setGeometry(100, 100, 400, 300)
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)
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


        # Add any other instance variables needed to track information as the program
        # runs here

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 120)
        self.slider.setValue(60)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        # self.slider.valueChanged.connect(self.update_fps)
        self.layout.addWidget(self.slider)

        self.fps_label = QLabel("Frames per second 60")
        self.fps_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.fps_label)

        self.frames = load_sprite("sprites", 6)
        self.current_frame = 0

        if self.frames:
            self.label.setPixmap(self.frames[0])

       #############




# You will need methods in the class to act as slots to connect to signals
    def change_fps(self, fps_speed):
        print(fps_speed)

# get new speed


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
