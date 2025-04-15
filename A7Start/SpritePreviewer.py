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
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        # setup Qtimer
        # everytime it times out, the frame should change
        # updating FPS should reset the timer
        # setInterval
        # update_fps = setInterval for timer
        # set interval will set the FPS
        # FPS variable to be shown as the value of the slider
        # whatever you're using the slider to set the interval of the timer
        #updating FPS changes timer interval
        # change frame gets called when the timer times out, FPS change is called when the slider changes
        # one method that updates FPS, another that actually changes the frame




        # Add any other instance variables needed to track information as the program
        # runs here

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()
        layout = QVBoxLayout(frame)
        slider_layout = QHBoxLayout(frame)
        sprite_image_label = QLabel("sprite image")
        fps_label = QLabel("Frames per second: " + str(self.num_frames))
        layout.addWidget(sprite_image_label)
        timer = QTimer(self)



        label = QLabel()
        pixmap = QPixmap('spriteImages/sprite_00.png')
        label.setPixmap(pixmap)
        layout.addWidget(label)



        # this would go with the start button
        timer.start()

        sprite_image_label.show()
        fps_label.show()

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.

        self.scale_slider = QSlider()
        self.scale_slider.setMinimum(0)
        self.scale_slider.setMaximum(100)
        layout.addWidget(self.scale_slider)
        self.scale_slider.valueChanged.connect(self.change_fps)

        frame.setLayout(slider_layout)
        self.setCentralWidget(frame)


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
