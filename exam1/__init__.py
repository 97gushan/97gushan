
import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
import model

class Exam1(QMainWindow):
    
    def __init__(self, parent=None):
        super(Exam1, self).__init__()
        
        self.setWindowTitle("Exam1 template")
        
        
        self.model = model.Model()
    
        self.initUI()

    
    def initUI(self):
        """This method is called when the application first runs
            The method initializes all the gui """
        
        # crates a QMainWindow and sets it as central widget
        self.frame = QMainWindow(self)
        self.setCentralWidget(self.frame)
        
        # create the main layout as a horizontal box layout
        self.main_layout = QHBoxLayout()
        
        # create the add_vehicle button and connect it to the open_add_vehicle_window method
        self.btn_add_vehicle = QPushButton("Add vehicle", self)
        self.btn_add_vehicle.clicked.connect(self.open_add_vehicle_window)


        # add the widgets to the main_layout
        self.main_layout.addWidget(self.btn_add_vehicle)
        
    
    def open_add_vehicle_window(self):
        """ this method creates a QDialog window that can take 
        input from the user and then create a object with those values"""
        print("open a new window")
        
        dialog_window = QDialog(self)
        dialog_window.setWindowTitle("Add new object")
        
        # buttons
        btn_add = QPushButton("Add", self)
        btn_add.clicked.connect(self.add_vehicle_spesific_layouts)
        
        btn_cancel = QPushButton("Cancel", self)
        
        
        
        # labels
        lbl_list = [QLabel("Vehicle type: "),QLabel("Maker: "),QLabel("Model: "),\
                    QLabel("Price: "),QLabel("Manufacturing year: ")]
        
        
        # Combobox
        cbox_vehicle_type = QComboBox()
        cbox_vehicle_type.addItems("Car Snowmobile".split())
        cbox_vehicle_type.activated["QString"].connect(self.add_vehicle_spesific_layouts)
        
        # line edits
        le_list = [QLineEdit("", self),QLineEdit("", self),QLineEdit("", self),QLineEdit("", self),QLineEdit("", self)]
       
        # layouts
        self.main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.layouts = [QHBoxLayout(),QHBoxLayout(),QHBoxLayout(),QHBoxLayout(),QHBoxLayout()]
        
        
        
        # adding widgets to layouts
        
        for n in range(len(self.layouts)):
            self.layouts[n].addWidget(lbl_list[n])

            if(n == 0):
                self.layouts[n].addWidget(cbox_vehicle_type)
            else:
                self.layouts[n].addWidget(le_list[n])
        
        # button layout
        button_layout.addWidget(btn_add)
        button_layout.addWidget(btn_cancel)
        
        # add widgets and layouts to main layout

        for n in range(len(self.layouts)):
            self.main_layout.addLayout(self.layouts[n])
        
        #self.main_layout.addLayout(button_layout)
        
        test_layout = QVBoxLayout()
        
        test_layout.addLayout(self.main_layout)
        test_layout.addLayout(button_layout)
        
        #set the layout to the dialog_window
        dialog_window.setLayout(test_layout)
        
        
        # show the dialog_window
        
        dialog_window.show()
    
    def add_vehicle_spesific_layouts(self, vehicle_type):
        
    
    def run(self):
        self.show()
        sys.exit(app.exec_())


        
        
        
app = QApplication(sys.argv)

# Start the program by calling the run method. 
# When the run method is called the Exam1.__init__ is run too
Exam1().run()




