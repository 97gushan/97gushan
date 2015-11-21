
import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
import model

class Exam1(QMainWindow):
    
    def __init__(self, parent=None):
        super(Exam1, self).__init__()
        
        self.setWindowTitle("Exam1 template")
        self.resize(500,500)

        
        self.model = model.Model()
        
        self.model.read_from_file()
    
        # hold the chosen object, if nothing else has been chosen, be the first object in the list
        if(len(self.model.get_vehicle_list()) > 0):
            self.chosen_vehicle = self.model.get_vehicle_list()[0]
    
        self.initUI()

    
    def initUI(self):
        """This method is called when the application first runs
            The method initializes all the gui """
        
        # crates a QMainWindow and sets it as central widget
        self.frame = QWidget(self)
        self.setCentralWidget(self.frame)
        
        
        # create the main layout as a horizontal box layout
        self.main_layout = QHBoxLayout(self.frame)
        
        
        """ Left Column"""
        ############################################################
        # create the layout for the left column
        self.left_column_layout = QFormLayout()
        
   
        # create the add_vehicle button and connect it to the open_add_vehicle_window method
        self.btn_add_vehicle = QPushButton("Add vehicle", self)
        self.btn_add_vehicle.clicked.connect(self.open_add_vehicle_window)
        
        # create the chose_vehicle button 
        self.btn_chose_vehicle = QPushButton("Chose vehicle", self)
        self.btn_chose_vehicle.clicked.connect(self.chose_vehicle)
        
        # create the change_values button
        self.btn_change_vehicle_values = QPushButton("Change values", self)
        self.btn_change_vehicle_values.clicked.connect(self.change_values)
        
        
        
        # create the scroll bar that the rb_layout is goind to use
        left_column_scrollbar = QScrollArea()
        left_column_scrollbar.setWidget(QWidget())
        left_column_scrollbar.setWidgetResizable(True)
        left_column_scrollbar.setFixedHeight(300)
        
        # create the layout for the QRadioButton 
        self.rb_layout = QFormLayout(left_column_scrollbar.widget())
        self.rb_objects = []
        
        # create a list of radiobuttons so the user can se and use the objects that he have
        self.create_vehicle_radio_button()

        
        
        
        # add the widgets to the layouts
        if(len(self.rb_objects) > 0):
            for n in range(len(self.rb_objects)):
                self.rb_layout.addWidget(self.rb_objects[n])
        
        self.left_column_layout.addRow("",left_column_scrollbar)
        self.left_column_layout.addRow("", self.btn_chose_vehicle)
        self.left_column_layout.addRow("",self.btn_add_vehicle)
        
        ##########################################################
        
        """ Main column"""
        ##########################################################
        
        self.main_column_layout = QFormLayout()
        
        self.main_column_layout.addRow("Choose a vehicle", QWidget())
        

        
        # add the layouts to the main_layout
        self.main_layout.addLayout(self.left_column_layout)
        self.main_layout.addLayout(self.main_column_layout)
        
    
    def create_vehicle_radio_button(self):
        """ this method will create radiobuttons of each and every
            object that the user have crated"""
        
        # remove all the radiobutton widgets that the rb_layout have
        for i in range(len(self.rb_layout)-1, -1, -1):
            item = self.rb_layout.itemAt(i)
            
            item.widget().close()
            self.rb_layout.removeItem(item)

        # empty the rb_objects list
        self.rb_objects = []

        # add the vehicles to the list 
        for n in range(len(self.model.get_vehicle_list())):
            vehicle = self.model.get_vehicle_list()[n]
            self.rb_objects.append(QRadioButton(vehicle.get_type() + " " + vehicle.get_maker() + " " + vehicle.get_model()))
        
        # add the new rbs to the layout 
        for n in range(len(self.rb_objects)):
                self.rb_layout.addRow("",self.rb_objects[n])
            
    def chose_vehicle(self):
        """ this method changes the layout of the self.main_column_layout
        to the way the chosen vehicle in the radiobuttons wants it to be"""
        
        # remove all the widgets from the layout
        for i in range(len(self.main_column_layout)-1, -1, -1):
            item = self.main_column_layout.itemAt(i)
            
            item.widget().close()
            self.main_column_layout.removeItem(item)    
        
        # get the chosen vehicle
        for n in range(len(self.rb_objects)):
            if(self.rb_objects[n].isChecked()):
                self.chosen_vehicle = self.model.get_vehicle_list()[n]
        
        # create the QLineEdits
        self.le_maker = QLineEdit(self.chosen_vehicle.get_maker())
        self.le_model = QLineEdit(self.chosen_vehicle.get_model())
        self.le_price = QLineEdit(self.chosen_vehicle.get_price())
        self.le_year = QLineEdit(self.chosen_vehicle.get_year())
        
        # if it is a car that the user chose
        if(self.chosen_vehicle.get_type() == "car"):
            # create a QLineEdit with the text string returned from get_door_amount()
            self.le_door_amount = QLineEdit(self.chosen_vehicle.get_door_amount())
        
        elif(self.chosen_vehicle.get_type() == "snowmobile"):
            # create a QLineEdit with the text string returned from get_seat_amount()
            self.le_seat_amount = QLineEdit(self.chosen_vehicle.get_seat_amount())
            
            # create a QRadioButton
            self.rb_have_reverse = QRadioButton()
            
            # get the state of the radiobutton and check it or uncheck it depending on the value of get_reverse()
            if(self.chosen_vehicle.get_reverse() == "True"):
                self.rb_have_reverse.setChecked(True)
            else:  
                self.rb_have_reverse.setChecked(False)
        
        
        # add the standard rows
        self.main_column_layout.addRow(self.chosen_vehicle.get_type() +", " + self.chosen_vehicle.get_maker() +", " + self.chosen_vehicle.get_model(), QWidget())
        self.main_column_layout.addRow("Change maker", self.le_maker)
        self.main_column_layout.addRow("Change model", self.le_model)
        self.main_column_layout.addRow("Change price", self.le_price)
        self.main_column_layout.addRow("Change manufacturing year", self.le_year)
        
        
        # add the rows that is vehicle specific
        if(self.chosen_vehicle.get_type() == "car"):
            self.main_column_layout.addRow("Change amount of doors", self.le_door_amount)
        elif(self.chosen_vehicle.get_type() == "snowmobile"):
            self.main_column_layout.addRow("Change amount of seats", self.le_seat_amount)
            self.main_column_layout.addRow("Reverse", self.rb_have_reverse)
   
    
    def change_values(self):
        """ this method takes the values writen in the QLineEdits of the main_column_layout
        and sets the values to the chosen vehicle"""
        
        # sets the user entered values to the chosen vehicle
        # for the shared attributes
        self.chosen_vehicle.set_maker(self.le_maker.text())
        self.chosen_vehicle.set_model(self.le_model.text())
        self.chosen_vehicle.set_price(self.le_price.text())
        self.chosen_vehicle.set_year(self.le_year.text())
        
        
        
        # if it is a car
        if(self.chosen_vehicle.get_type() == "car"):
            #call the set_door_amount method
            self.chosen_vehicle.set_door_amount(self.le_door_amount.text())
        
        # if it is a snowmobile
        elif(self.chosen_vehicle.get_type() == "snowmobile"):
            
            # call the set_seat_amount method
            self.chosen_vehicle.set_seat_amount(self.le_seat_amount.text())
            
            # check if the user clicked in the radiobutton
            if(self.rb_have_reverse.isChecked()):
                have_reverse = "True"
            else:
                have_reverse = "False"
            
            # call the set_reverse method
            self.chosen_vehicle.set_reverse(have_reverse)
        
        # update the radiobuttons
        self.create_vehicle_radio_button()       
            
   
    def open_add_vehicle_window(self):
        """ this method creates a QDialog window that can take 
        input from the user and then create a object with those values"""
        print("open a new window")
        
        self.dialog_window = QDialog(self)
        self.dialog_window.setWindowTitle("Add new object")
        
        # buttons
        self.btn_add = QPushButton("Add", self)
        self.btn_add.clicked.connect(self.add_vehicle)
        
        # create the cancel button and if it is pressed: close the window
        btn_cancel = QPushButton("Cancel", self)
        btn_cancel.clicked.connect(self.dialog_window.close)
        
        
        
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
        self.vertical_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        layouts = [QHBoxLayout(),QHBoxLayout(),QHBoxLayout(),QHBoxLayout(),QHBoxLayout()]
        
        
        
        # adding widgets to layouts
        
        for n in range(len(layouts)):
            layouts[n].addWidget(lbl_list[n])

            if(n == 0):
                layouts[n].addWidget(self.cbox_vehicle_type)
            else:
                layouts[n].addWidget(self.le_list[n])
        
        # button layout
        button_layout.addWidget(self.btn_add)
        button_layout.addWidget(btn_cancel)
        
        # add widgets and layouts to main layout

        for n in range(len(layouts)):
            self.vertical_layout.addLayout(layouts[n])
        
        #self.vertical_layout.addLayout(button_layout)
        
        main_layout = QVBoxLayout()
        
        main_layout.addLayout(self.vertical_layout)
        main_layout.addLayout(button_layout)
        
        #set the layout to the dialog_window
        self.dialog_window.setLayout(main_layout)
        
        
        # show the dialog_window
        
        self.dialog_window.show()
    
    def add_vehicle_spesific_layouts(self, vehicle_type):
        """ this method takes a string as an argument
        it then checks if it is a car or a snowmobile and
        depending on which one, it ads a new label and lineedit"""
        
        if(vehicle_type == "Car"):
        
            # create a new layout
            new_layout = QHBoxLayout()
            
            # create the new widgets that will be in the layout
            lbl_door_amount = QLabel("Amount of doors: ")
            self.le_add_vehicle_door_amount = QLineEdit()
            
            # add the new widgets to the layout
            new_layout.addWidget(lbl_door_amount)
            new_layout.addWidget(self.le_add_vehicle_door_amount)
            
            # add the layout to the main_layout
            self.vertical_layout.addLayout(new_layout)
            
            # disable the combobox
            self.cbox_vehicle_type.setEnabled(False)

        
        elif(vehicle_type == "Snowmobile"):
            # create a list of layouts
            new_layouts = [QHBoxLayout(), QHBoxLayout()]
            
            # creates the new widgets
            lbl_seat_amount = QLabel("Amount of seats: ")
            self.le_add_vehicle_seat_ammount = QLineEdit()
            
            lbl_have_reverse = QLabel("Reverse: ")
            self.rb_add_vehicle_have_reverse = QRadioButton()
            
            
            # add the widgets to the two layouts
            new_layouts[0].addWidget(lbl_seat_amount)
            new_layouts[0].addWidget(self.le_add_vehicle_seat_ammount)
            
            new_layouts[1].addWidget(lbl_have_reverse)
            new_layouts[1].addWidget(self.rb_add_vehicle_have_reverse)
            
            
            # add the layouts to the main layout
            self.vertical_layout.addLayout(new_layouts[0])
            self.vertical_layout.addLayout(new_layouts[1])
            
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
        
        # if the user wants a car
        if(user_inputs[0] == "Car"):
            user_inputs.append(self.le_add_vehicle_door_amount.text())
            
            # call the add_car method with the users values
            if(self.model.add_car(user_inputs[1],
                               user_inputs[2],
                               user_inputs[3],
                               user_inputs[4],
                               user_inputs[5],)):
                self.create_vehicle_radio_button()
                self.dialog_window.close()
            
            
        # if the user wants a snowmobile
        elif(user_inputs[0] == "Snowmobile"):
            user_inputs.append(self.le_add_vehicle_seat_ammount.text())


            # check if the user clicked in the radiobutton
            if(self.rb_add_vehicle_have_reverse.isChecked()):
                user_inputs.append("True")
            else:
                user_inputs.append("False")
            
            # call the add_sm method with the user values
            if(self.model.add_sm(user_inputs[1],
                               user_inputs[2],
                               user_inputs[3],
                               user_inputs[4],
                               user_inputs[5],
                               user_inputs[6])):
                               
                self.create_vehicle_radio_button()                
                self.dialog_window.close()
                
        


            
    
        
    
    def run(self):
        self.show()
        sys.exit(app.exec_())


        
        
        
app = QApplication(sys.argv)

# Start the program by calling the run method. 
# When the run method is called the Exam1.__init__ is run too
Exam1().run()




