
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
        self.btn_add = QPushButton("Add", self)
        self.btn_add.clicked.connect(self.add_vehicle)
        
        btn_cancel = QPushButton("Cancel", self)
        
        
        
        # labels
        lbl_list = [QLabel("Vehicle type: "),QLabel("Maker: "),QLabel("Model: "),\
                    QLabel("Price: "),QLabel("Manufacturing year: ")]
        
        
        # Combobox
        self.cbox_vehicle_type = QComboBox()
        self.cbox_vehicle_type.addItems("Vehicle Car Snowmobile".split())
        self.cbox_vehicle_type.activated["QString"].connect(self.add_vehicle_spesific_layouts)
        
        # line edits
        self.le_list = [QLineEdit("", self),QLineEdit("", self),QLineEdit("", self),QLineEdit("", self),QLineEdit("", self)]
       
        # layouts
        self.main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.layouts = [QHBoxLayout(),QHBoxLayout(),QHBoxLayout(),QHBoxLayout(),QHBoxLayout()]
        
        
        
        # adding widgets to layouts
        
        for n in range(len(self.layouts)):
            self.layouts[n].addWidget(lbl_list[n])

            if(n == 0):
                self.layouts[n].addWidget(self.cbox_vehicle_type)
            else:
                self.layouts[n].addWidget(self.le_list[n])
        
        # button layout
        button_layout.addWidget(self.btn_add)
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
        """ this method takes a string as an argument
        it then checks if it is a car or a snowmobile and
        depending on which one, it ads a new label and lineedit"""
        
        if(vehicle_type == "Car"):
        
            # create a new layout
            new_layout = QHBoxLayout()
            
            # create the new widgets that will be in the layout
            lbl_door_amount = QLabel("Amount of doors: ")
            self.le_door_amount = QLineEdit()
            
            # add the new widgets to the layout
            new_layout.addWidget(lbl_door_amount)
            new_layout.addWidget(self.le_door_amount)
            
            # add the layout to the main_layout
            self.main_layout.addLayout(new_layout)
            
            # disable the combobox
            self.cbox_vehicle_type.setEnabled(False)

        
        elif(vehicle_type == "Snowmobile"):
            # create a list of layouts
            new_layouts = [QHBoxLayout(), QHBoxLayout()]
            
            # creates the new widgets
            lbl_seat_amount = QLabel("Amount of seats: ")
            self.le_seat_ammount = QLineEdit()
            
            lbl_have_reverse = QLabel("Reverse: ")
            self.rb_have_reverse = QRadioButton()
            
            
            # add the widgets to the two layouts
            new_layouts[0].addWidget(lbl_seat_amount)
            new_layouts[0].addWidget(self.le_seat_ammount)
            
            new_layouts[1].addWidget(lbl_have_reverse)
            new_layouts[1].addWidget(self.rb_have_reverse)
            
            
            # add the layouts to the main layout
            self.main_layout.addLayout(new_layouts[0])
            self.main_layout.addLayout(new_layouts[1])
            
            # disable the combobox
            self.cbox_vehicle_type.setEnabled(False)

        
    def add_vehicle(self):
        """ this method takes the values the user inputs and adds a vehicle with these values"""
        
        user_inputs = []
        
        # add the type of the vehicle to the list
        user_inputs.append(self.cbox_vehicle_type.itemText(self.cbox_vehicle_type.currentIndex()))
        
        # add the maker to the list
        user_inputs.append(self.le_list[1].text())
        
        # add the model to the list
        user_inputs.append(self.le_list[2].text())
        
        # add the price to the list
        user_inputs.append(self.le_list[3].text())
        
        # add the manufacturing year to the list
        user_inputs.append(self.le_list[4].text())
        
        if(user_inputs[0] == "Car"):
            user_inputs.append(self.le_door_amount.text())
        elif(user_inputs[0] == "Snowmobile"):
            user_inputs.append(self.le_seat_ammount.text())
            
            if(self.rb_have_reverse.isChecked()):
                user_inputs.append("True")
            else:
                user_inputs.append("False")
        
        print(user_inputs)
            
        
    
    
        
    
    def run(self):
        self.show()
        sys.exit(app.exec_())


        
        
        
app = QApplication(sys.argv)

# Start the program by calling the run method. 
# When the run method is called the Exam1.__init__ is run too
Exam1().run()




