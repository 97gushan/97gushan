
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
        print("open a new window")
        
        dialog_window = QDialog(self)
        
        # buttons
        btn_add = QPushButton("test", self)
        
        # line edits
        text = QLineEdit("enter text", self)
        
        # layouts
        main_layout = QVBoxLayout()
        
        
        # adding widgets to layouts
        main_layout.addWidget(text)

        main_layout.addWidget(btn_add)
        
        #set the layout to the dialog_window
        dialog_window.setLayout(main_layout)
        
        
        # show the dialog_window
        dialog_window.show()
    
    def run(self):
        self.show()
        sys.exit(app.exec_())


        
        
        
app = QApplication(sys.argv)

# Start the program by calling the run method. 
# When the run method is called the Exam1.__init__ is run too
Exam1().run()




