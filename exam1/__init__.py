
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
        self.model.sort_list("maker")
    
        # hold the chosen object, if nothing else has been chosen, be the first object in the list
        if(len(self.model.get_vehicle_list()) > 0):
            self.chosen_vehicle = self.model.get_vehicle_list()[0]
            self.chosen_vehicle_index = 0
    
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
        
        # create the save_list button and connect it to save_vehicle_list method
        self.btn_save_list = QPushButton("Save list", self)
        self.btn_save_list.clicked.connect(self.model.write_to_file)
        
        # create the search_for_object button and connect it to open_search_window
        self.btn_search_for_object = QPushButton("Search for vehicle", self)
        self.btn_search_for_object.clicked.connect(self.open_search_window)
        
        # create the sort list button
        self.btn_sort_list = QPushButton("Sort list", self)
        self.btn_sort_list.clicked.connect(self.open_sort_window)
        
        # create the chose_vehicle button 
        self.btn_chose_vehicle = QPushButton("Chose vehicle", self)
        
        if(len(self.model.get_vehicle_list()) == 0):
            self.btn_chose_vehicle.setEnabled(False)
        self.btn_chose_vehicle.clicked.connect(self.chose_vehicle)
        
        
        
        
        
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
        
        search_and_sort_layout = QHBoxLayout()
        search_and_sort_layout.addWidget(self.btn_search_for_object)
        search_and_sort_layout.addWidget(self.btn_sort_list)
        
        self.left_column_layout.addRow("",left_column_scrollbar)
        self.left_column_layout.addRow("", self.btn_chose_vehicle)
        self.left_column_layout.addRow("", search_and_sort_layout)
        self.left_column_layout.addRow("",self.btn_add_vehicle)
        self.left_column_layout.addRow("", self.btn_save_list)
        
        ##########################################################
        
        """ Main column"""
        ##########################################################
        
        # create the change_values button
        self.btn_change_vehicle_values = QPushButton("Change values", self)
        self.btn_change_vehicle_values.setEnabled(False)
        self.btn_change_vehicle_values.clicked.connect(self.change_values)
        
        # create the remove_vehicle button
        self.btn_remove_vehicle = QPushButton("Remove vehicle", self)
        self.btn_remove_vehicle.setEnabled(False)
        self.btn_remove_vehicle.clicked.connect(self.remove_vehicle)
        
        # create two layouts, one to hold all the vehicle values and one
        # to hold the value layout and buttons needed in the column
        self.main_column_layout = QFormLayout()
        self.vehicle_values_layout = QFormLayout()
        
        # add a row to the vehicle_values_layout
        self.vehicle_values_layout.addRow("Choose a vehicle", QWidget())
        
        # add the vehicle_values_layout and the btn_change_vehicle_values to the layout
        self.main_column_layout.addRow(self.vehicle_values_layout)
        self.main_column_layout.addRow(self.btn_change_vehicle_values)
        self.main_column_layout.addRow(self.btn_remove_vehicle)
        
        ##########################################################

        
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
        for i in range(len(self.vehicle_values_layout)-1, -1, -1):
            item = self.vehicle_values_layout.itemAt(i)
            
            item.widget().close()
            self.vehicle_values_layout.removeItem(item)    
        
        # get the chosen vehicle
        for n in range(len(self.rb_objects)):
            if(self.rb_objects[n].isChecked()):
                self.chosen_vehicle = self.model.get_vehicle_list()[n]
                self.chosen_vehicle_index = n
        
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
        self.vehicle_values_layout.addRow(self.chosen_vehicle.get_type() +", " + self.chosen_vehicle.get_maker() +", " + self.chosen_vehicle.get_model(), QWidget())
        self.vehicle_values_layout.addRow("Change maker", self.le_maker)
        self.vehicle_values_layout.addRow("Change model", self.le_model)
        self.vehicle_values_layout.addRow("Change price", self.le_price)
        self.vehicle_values_layout.addRow("Change manufacturing year", self.le_year)
        
        
        # add the rows that is vehicle specific
        if(self.chosen_vehicle.get_type() == "car"):
            self.vehicle_values_layout.addRow("Change amount of doors", self.le_door_amount)
        elif(self.chosen_vehicle.get_type() == "snowmobile"):
            self.vehicle_values_layout.addRow("Change amount of seats", self.le_seat_amount)
            self.vehicle_values_layout.addRow("Reverse", self.rb_have_reverse)
   
        
        self.btn_change_vehicle_values.setEnabled(True)
        self.btn_remove_vehicle.setEnabled(True)
   
    
    def change_values(self):
        """ this method takes the values writen in the QLineEdits of the main_column_layout
        and sets the values to the chosen vehicle"""
        
        
        # if it is a car
        if(self.chosen_vehicle.get_type() == "car"):
        
            # call the model.set_car_values method and if it returns true:
            if(self.model.set_car_values(self.chosen_vehicle_index,
                                         self.le_maker.text(),\
                                         self.le_model.text(),\
                                         self.le_price.text(),\
                                         self.le_year.text(),\
                                         self.le_door_amount.text())):
                
                # update the radiobuttons
                self.create_vehicle_radio_button()     
                
                # lock the buttons
                self.btn_remove_vehicle.setEnabled(False)
                self.btn_change_vehicle_values.setEnabled(False)
            else:
                # if it returns false, call the unaccepted_values_window with the string "car"
                self.unaccepted_values_window("car")
                
        
        # if it is a snowmobile
        elif(self.chosen_vehicle.get_type() == "snowmobile"):
            
            # check if the rb_have_reverse is checked or not
            if(self.rb_have_reverse.isChecked()):
                have_reverse = "True"
            else:
                have_reverse = "False"
                
            # call the model.set_sm_values method and if it returns true:
            if(self.model.set_sm_values(self.chosen_vehicle_index,
                                         self.le_maker.text(),\
                                         self.le_model.text(),\
                                         self.le_price.text(),\
                                         self.le_year.text(),\
                                         self.le_seat_amount.text(),\
                                         have_reverse)):
                
                # update the radiobuttons
                self.create_vehicle_radio_button()     
                
                # lock the buttons
                self.btn_remove_vehicle.setEnabled(False)
                self.btn_change_vehicle_values.setEnabled(False)
            else:
                # if it returns false, call the unaccepted_values_window with the string "snowmobile"
                self.unaccepted_values_window("snowmobile")
            
            
   
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
            else:
                self.unaccepted_values_window("car")
            
            
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
            else:
                self.unaccepted_values_window("snowmobile")
                
        self.btn_chose_vehicle.setEnabled(True)
        
    def unaccepted_values_window(self, vehicle_type):
        """ this method creates a QDialog window which tells 
        the user that a entered value is not accepted and which
        values that are acceptable"""
        
        # create the window
        window = QDialog(self)
        
        # create its layout
        layout = QFormLayout()
        
        
        # add the rows needed to display the text
        layout.addRow("Maker: String", QWidget())
        layout.addRow("Model: String", QWidget())
        layout.addRow("Price: Int - above 0", QWidget())
        layout.addRow("Manufacturing year: Int - between 1900 and 2015", QWidget())
        
        # add the vehicle specific rows
        if(vehicle_type == "car"):
            layout.addRow("Amount of doors: Int - between 1 and 10", QWidget())
        elif(vehicle_type == "snowmobile"):
            layout.addRow("Amount of seats: Int - between 1 and 3", QWidget())
            
        # create the closebutton
        btn_close = QPushButton("Close", self)
        btn_close.clicked.connect(window.close)
        
        # add the button to the layout
        layout.addRow(btn_close)
        
        # set the layout of the window
        window.setLayout(layout)
        
        # show the window
        window.show()

    
    def remove_vehicle(self):
        """ this method removes the chosen vehicle"""
        
        # get the chosen vehicle
        for n in range(len(self.rb_objects)):
            if(self.rb_objects[n].isChecked()):
                # remove the vehicle
                self.model.remove_vehicle(n)
    
        # update the radiobuttons
        self.create_vehicle_radio_button()  
        
        # lock the buttons
        self.btn_remove_vehicle.setEnabled(False)
        self.btn_change_vehicle_values.setEnabled(False)
    
    def open_search_window(self):
        """this method creates a QDialog window which is used to search for objects"""
        
        # create the window
        self.search_window = QDialog(self)
        self.search_window.setWindowTitle("Search for object")
        self.search_window.setMinimumWidth(300)
        
        # create the main layout for the window
        main_layout = QFormLayout()
        
        # create a QScrollArea to hold the object_layout
        search_window_scrollbar = QScrollArea()
        search_window_scrollbar.setWidget(QWidget())
        search_window_scrollbar.setWidgetResizable(True)
        search_window_scrollbar.setFixedHeight(100)
        
        
        # create a layout to hold the objects found in the search
        self.object_layout = QFormLayout(search_window_scrollbar.widget())

        # create the combobox 
        self.cbox_searchwindow_type = QComboBox()
        self.cbox_searchwindow_type.addItems("maker model price year".split())
        
        # create the QLineEdit where the user adds the searchword
        self.le_search_word = QLineEdit()
        
        
        # create the search button
        btn_search = QPushButton("Search")
        btn_search.clicked.connect(self.search_for_object)
        
        # create the chose_vehicle button
        btn_choose_vehicle = QPushButton("Choose")
        btn_choose_vehicle.clicked.connect(self.choose_searched_vehicle)
        
        main_layout.addRow("What to search for: ", self.cbox_searchwindow_type)
        main_layout.addRow("Search word: ", self.le_search_word)
        main_layout.addRow("", btn_search)
        main_layout.addRow("", search_window_scrollbar)
        main_layout.addRow("", btn_choose_vehicle)
        
        self.search_window.setLayout(main_layout)
        
        # show the window
        self.search_window.show()
        
    
    def search_for_object(self):
        """ this method takes the values the user added in the
        combobox and lineedit of the search_window and uses these
        Strings as arguments when calling the model.search_for_object method"""
        
        # get the user entered values
        type = str(self.cbox_searchwindow_type.currentText())
        searchword = self.le_search_word.text()
        
        # get the list of indexes that matches the search
        self.index_list = self.model.search_for_object(type, searchword)
        
        # remove all the radiobutton widgets that the rb_layout have
        for i in range(len(self.object_layout)-1, -1, -1):
            item = self.object_layout.itemAt(i)
            
            item.widget().close()
            self.object_layout.removeItem(item)
        
        # create a empty list
        self.found_objects = []
        
        for n in range(len(self.index_list)):
            # get the vehicle with the found index
            vehicle = self.model.get_vehicle_list()[self.index_list[n]]
            
            # create a QRadioButton and add it to the list
            self.found_objects.append(QRadioButton(vehicle.get_type() + " " + vehicle.get_maker() + " " + vehicle.get_model()))

            # add the radiobutton to the layout
            self.object_layout.addRow("",self.found_objects[n])
        
    
    def choose_searched_vehicle(self):
        """ this method sets the value of chosen_vehicle to the vehicle chosen
        after the search"""
        
        for n in range(len(self.found_objects)):
            if(self.found_objects[n].isChecked()):
                self.rb_objects[self.index_list[n]].setChecked(True)

        self.chose_vehicle()
        self.search_window.close()
    
    
    def open_sort_window(self):
        """ this method creates a window where the user can
        chose what to sort the vehicle_list after"""
        
        # create the window
        sort_window = QDialog(self)
        
        # create the layout
        sort_layout = QFormLayout()
 
        # create the combobox that will hold the different options
        self.cbox_sort_options = QComboBox()
        self.cbox_sort_options.addItems("maker model price year".split())
        
        # create close button
        btn_close = QPushButton("Close")
        btn_close.clicked.connect(sort_window.close)
        
        # create the sort button
        btn_sort = QPushButton("Sort list")
        btn_sort.clicked.connect(self.sort_the_list)
        
        # create a layout for the buttons
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_sort)
        btn_layout.addWidget(btn_close)
        
        # add to the sort_layout
        sort_layout.addRow("Choose what to sort by: ", self.cbox_sort_options)
        sort_layout.addRow(btn_layout)
        
        # set the layout of the sort_window
        sort_window.setLayout(sort_layout)
        
        # show the window
        sort_window.show()
    
    def sort_the_list(self):
        pass
    
    def run(self):
        self.show()
        sys.exit(app.exec_())


        
        
        
app = QApplication(sys.argv)

# Start the program by calling the run method. 
# When the run method is called the Exam1.__init__ is run too
Exam1().run()




