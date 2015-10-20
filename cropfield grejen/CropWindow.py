import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


from Wheat import *
from Potato import *
from RadioButtonWidget import * # provides the radiobutton class that was created

class CropWindow(QMainWindow):
    """ This class creates a main window to observe the growth of the simulation"""
    
    # constructor
    def __init__(self):
        super().__init__() # call the soper class constructor
        self.setWindowTitle("Crop simulator") # set window title
        self.create_select_crop_layout()        
        
        
    def create_select_crop_layout(self):
        # this is the initial lauout of the window
        # it lets us select a crop type
    
        self.crop_radio_buttons = RadioButtonWidget("Crop simulation", \
                                                    "Please select a crop",\
                                                    ("Wheat", "Potato"))
        self.instantiate_button = QPushButton("Create crop")
        
        # create the layout to hold the widgets
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)
        
        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)
        
        self.setCentralWidget(self.select_crop_widget)

        # connections
        self.instantiate_button.clicked.connect(self.instantiate_crop)
        
    def create_view_crop_layout(self, crop_type):
        """ this method create the second layout of the window
            it lets us view the crops grow"""
            
        self.growth_label = QLabel("Growth")
        self.days_label = QLabel("Days growing")
        self.status_label = QLabel("Crop status")
        
        self.growth_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()
        
        self.manual_grow_button = QPushButton("Manually grow")
        self.automatic_grow_button = QPushButton("Automatically grow")
        
        self.grow_grid = QGridLayout()
        self.status_grid = QGridLayout()
        
        #add label widgets to the status layout
        self.status_grid.addWidget(self.grow_grid, 0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)
        
        #add line edit widgets to the status layout
        self.status_grid.addWidget(self.growth_line_edit, 0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)
        
        # add widgets/ layout ot the grow layout
        self.grow_grid.addLayout(self.status_grid, 0, 1)
        self.grow_grid.addWidget(self.manual_grow_button, 1,0)
        self.grow_grid.addWidget(self.automatic_grow_button, 1,1)
        
        # create a widget to display the grow layout
        self.view_crop_widget = QWidget()
        self.view_crop_widget.setLayout(self.grow_grid)
    
    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button() # get the radio that was selected
        if crop_type == 1:
            self.simulated_crop = Wheat()
        elif(crop_type == 2):
            self.simulated_crop = Potato()
        print(self.simulated_crop)
        self.setCentralWidget(self.view_crop_widget)

def main():
    crop_simulation = QApplication(sys.argv) #create ta new application
    crop_window = CropWindow() # create new instance of main window
    crop_window.show() # make instance visible
    crop_window.raise_() # raise instance to top of window stack
    crop_simulation.exec_() # monitor application for events
    
    
if __name__ == "__main__":
    main()