
import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
import model

class Exam1(QMainWindow):
    
    def __init__(self, parent=None):
        super(Exam1, self).__init__()
        
        self.setWindowTitle("Exam1 template")
        
        self.initUI()
    
    def initUI(self):
        """This method is called when the application first runs
            The method initializes all the gui """
        pass
        
    def run(self):
        self.show()
        sys.exit(app.exec_())


        
        
        
app = QApplication(sys.argv)

# Start the program by calling the run method. 
# When the run method is called the Exam1.__init__ is run too
Exam1().run()




