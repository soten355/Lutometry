import sys

#Import the modified and updated pyLUT
from pyLUT import *

#Import PyQt5 for creating the GUI
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Import matplotlib for PyQt5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

#Import this module for the random graph Lutometry generates
import random

"""
Main App
"""

class App(QMainWindow):
    #initial variables
    def __init__(self):
        super().__init__()
        #Main App Window Title
        self.title = 'Lutometry'

        #Main App Window Dimensions
        self.left = 10
        self.top = 10
        self.width = 896
        self.height = 896

        #Global System Settings
        ##Global LUT Settings
        self.userLUT = ["NO LUT LOADED", "NO LUT LOCATION", "graph"]
        self.LUTResolution = 33
        self.storedLUT = None
        ##Global Graph/Cube Settings
        self.graphKind = "2D Graph"
        self.graphWidth = 5.12
        self.graphHeight = 5.12
        self.graphDPI = 100

        #Initialize the UI/Window
        self.initUI()

    #initialize the UI/Window
    def initUI(self):
        #Build the main window
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMinimumSize(self.width, self.height)

        #Build the main layout
        self.createMainLayout()
        
        self.show()
    
    #Main Layout
    def createMainLayout(self):
        #Build the grid layout
        self.horizontalGroupBox = QGroupBox()
        self.MainLayout = QGridLayout()
        mainWindow = QWidget(self)
        self.setCentralWidget(mainWindow)
        
        #LUT Name at top of screen
        self.LUTName = QLabel("Lut loaded: " + self.userLUT[0], self)
        self.LUTName.setFont(QFont(None, 18))
        self.LUTName.setAlignment(Qt.AlignCenter)
        self.MainLayout.addWidget(self.LUTName, 0, 0, 1, 4)

        #Build the Load LUT button
        buttonLoadLUT = QPushButton('Load LUT', self)
        buttonLoadLUT.clicked.connect(self.onClickLoadLUT)
        buttonLoadLUT.setIcon(QIcon("images/folder.png"))
        buttonLoadLUT.resize(64,128)
        self.MainLayout.addWidget(buttonLoadLUT, 1, 0, 2, 2)

        #Build the LUT Resolution ComboBox
        #First, the label
        self.comboBoxLUTResLabel = QLabel("Cube Size:")
        self.MainLayout.addWidget(self.comboBoxLUTResLabel, 1, 2)
        #Then, the ComboBox
        self.comboBoxLUTRes = QComboBox()
        self.comboBoxLUTRes.addItem("9")
        self.comboBoxLUTRes.addItem("17")
        self.comboBoxLUTRes.addItem("33")
        self.comboBoxLUTRes.addItem("65")
        self.comboBoxLUTRes.setCurrentIndex(2)
        self.comboBoxLUTRes.activated[str].connect(self.resolutionSelectionChange)
        self.MainLayout.addWidget(self.comboBoxLUTRes, 2, 2)

        #Build the Graph Kind ComboBox
        #First, the label
        self.comboBoxLUTResLabel = QLabel("Graph Kind:")
        self.MainLayout.addWidget(self.comboBoxLUTResLabel, 1, 3)
        #Then, the ComboBox
        comboBoxGraphKind = QComboBox()
        comboBoxGraphKind.addItem("2D Graph")
        comboBoxGraphKind.addItem("3D Cube")
        comboBoxGraphKind.activated[str].connect(self.graphSelectionChange)
        self.MainLayout.addWidget(comboBoxGraphKind, 2, 3)

        #Build the MatPlotLib Graph
        self.canvas = PlotCanvas(self, width = self.graphWidth, height = self.graphHeight, dpi = self.graphDPI)
        self.graphToolBar = NavigationToolbar(self.canvas, self)
        self.Plot()
        self.MainLayout.addWidget(self.canvas, 3, 0, 1, 4)
        self.MainLayout.addWidget(self.graphToolBar, 4, 0, 1, 4)

        #Final layout settings
        self.horizontalGroupBox.setLayout(self.MainLayout)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        mainWindow.setLayout(windowLayout)

        #Build the Menu Bar
        self.MenuBar = QMenuBar()

        #File>
        fileMenu = self.MenuBar.addMenu("&File")
        #File>About Lutometry
        about = QAction("&About", self)
        about.triggered.connect(self.aboutBox)
        fileMenu.addAction(about)


    """
    Key Functions, alphabetical
    """
    
    #The ever so important about box. File/LUTOMETRY(mac version) > About Lutometry
    def aboutBox(self):
        print("User selected File>About Lutometry") #Log Info
        self.NewWindow = aboutWindow()
        self.NewWindow.show()

    #When the "Load LUT" button is clicked
    def onClickLoadLUT(self):
        newLUTLocation = None
        print("The User is attempting to load a LUT. Where is it?") #Log info
        newLUTLocation = self.openFileNameDialog() #Get the file location of the LUT
        print("Program about to load LUT. Global settings currently are:") #Log info
        self.printGlobalSettings() #Log info
        if newLUTLocation:
            try:
                self.storedLUT = LUT.FromCubeFile(newLUTLocation) #Load the LUT from source, via pyLUT
            except NameError:
                print("Wrong file selected. Need .CUBE file") #Log info
            self.userLUT[0] = self.storedLUT.name #Update global setting of LUT name
            self.userLUT[1] = newLUTLocation #Update global setting of LUT location
            self.updateSystemResolution(self.storedLUT.resolution) #Update global setting & GUI
            self.storedLUT.Plot(self.userLUT[2], self.LUTResolution) #Set the data from the LUT, via the pyLUT class that was just generated
            self.LUTName.setText("LUT Loaded: " + self.userLUT[0]) #Update the LUT Name label widget
            print("Program loaded the user's LUT. New global settings are:") #Log info
            print(self.storedLUT.cubeSize)
            self.printGlobalSettings() #Log info
        else:
            print("User aborted. No LUT loaded") #Log info
        self.Plot() #Update the graph/cube

    #When the user selects a different graph, this function is called.
    def graphSelectionChange(self, newGraph):
        self.graphKind = newGraph #Make the program record which kind of graph
        if newGraph == "2D Graph":
            self.userLUT[2] = "graph"
        elif newGraph == "3D Cube":
            self.userLUT[2] = "cube"
        self.refreshLUT() #refresh the stored LUT to match the needs of the graph

    #Open a file
    def openFileNameDialog(self):
        print("User is opening a file") #Log Info
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print("User selected a file") #Log Info
            return fileName
    
    #Open files
    def openFileNamesDialog(self):
        print("User is opening files") #Log Info
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print("User selected files") #Log Info
            return files

    #Plot either a 2D graph or 3D cube.
    def Plot(self):
        if self.storedLUT: #If there's a stored LUT, then determine which kind of graph/cube
            if self.graphKind == "2D Graph":
                print("Updating graph to 2D") #Log info
                self.canvas.axes.clear()
                self.plotGraph()
            elif self.graphKind == "3D Cube":
                print("Updating graph to 3D Cube") #Log info
                self.canvas.axes.clear()
                self.plotCube()

            self.canvas.axes.set_title(self.graphKind)
            self.canvas.draw()

        else: #If there's no stored LUT, then generate a random 2D graph
            graphGenerator = np.random.default_rng()
            datax = range(0, 33)
            datay = graphGenerator.exponential(1, 33)
            self.canvas.axes.clear()
            self.canvas.axes.plot(datax, datay, '#000000')
            self.canvas.axes.set_title(self.graphKind)
            self.canvas.draw()
    
    #Plots the 2D Graph
    def plotGraph(self):
        if self.canvas.cubeORgraph == "3d": #Does a 2d graph exist? If not, create a new PlotCanvas
            print("No 2D graph exists. Erasing all graphs and creating a new one") #Log Info
            self.MainLayout.removeWidget(self.canvas) #Remove old PlotCanvas
            self.MainLayout.removeWidget(self.graphToolBar) #Remove old matplotlib Tool Bar
            self.canvas = PlotCanvas(self, width = self.graphWidth, height = self.graphHeight, dpi = self.graphDPI)
            self.graphToolBar = self.graphToolBar = NavigationToolbar(self.canvas, self)
            self.MainLayout.addWidget(self.canvas, 3, 0, 1, 4)
            self.MainLayout.addWidget(self.graphToolBar, 4, 0, 1, 4)
        elif self.canvas.cubeORgraph is None: #Check if Class PlotCanvas is set to 2D or 3D. None = 2D
            print("2D graph already in use") #Log info
        remappedRange = np.linspace(0, 100, self.LUTResolution) #Remap the range from 0 - LUTResolution to -9 -> 9 with the number of intervals at the resolution
        gridXticks = np.arange(0, 110, 10) #Set x axis ticks at -9 to 9 at 1 step each
        gridYticks = np.arange(0, 110, 10) #Set y axis ticks at 0 to 1.0 at 0.05 steps each
        self.canvas.axes.plot(remappedRange, self.storedLUT.red_values, color = "red", linewidth = 1, marker = "o", markersize = 2)
        self.canvas.axes.plot(remappedRange, self.storedLUT.green_values, color = "green", linewidth = 1, marker = "o", markersize = 2)
        self.canvas.axes.plot(remappedRange, self.storedLUT.blue_values, color = "blue", linewidth = 1, marker = "o", markersize = 2)

        #Set updated tick markers and add a grid
        self.canvas.axes.set_xticks(gridXticks)
        self.canvas.axes.set_yticks(gridYticks)
        self.canvas.axes.grid()
    
    
    #Plots the 3D Cube
    def plotCube(self):
        if self.canvas.cubeORgraph is None: #Does a 3D cube exist? If not, create a new PlotCanvas
            print("No 3D cube exits. Erasing all graphs and creating a new one") #Log Info
            self.MainLayout.removeWidget(self.canvas) #Remove old PlotCanvas
            self.MainLayout.removeWidget(self.graphToolBar) #Remove old matplotlib Tool Bar
            self.canvas = PlotCanvas(self, width = self.graphWidth, height = self.graphHeight, dpi = self.graphDPI, cube = "3d")
            self.graphToolBar = self.graphToolBar = NavigationToolbar(self.canvas, self)
            self.MainLayout.addWidget(self.canvas, 3, 0, 1, 4)
            self.MainLayout.addWidget(self.graphToolBar, 4, 0, 1, 4)
        elif self.canvas.cubeORgraph == "3d": #If a 3D cube exists, then update the cube
            print("3D graph already in use") #Log info
        self.canvas.axes.set_xlabel('Red')
        self.canvas.axes.set_ylabel('Green')
        self.canvas.axes.set_zlabel('Blue')
        self.canvas.axes.set_xlim(min(self.storedLUT.red_values), max(self.storedLUT.red_values))
        self.canvas.axes.set_ylim(min(self.storedLUT.green_values), max(self.storedLUT.green_values))
        self.canvas.axes.set_zlim(min(self.storedLUT.blue_values), max(self.storedLUT.blue_values))
        self.canvas.axes.scatter(self.storedLUT.red_values, self.storedLUT.green_values, self.storedLUT.blue_values, c=self.storedLUT.colors, marker="o")

    #For log purposes
    def printGlobalSettings(self):
        print("LUT Name: " + self.userLUT[0]) #Log info
        print("LUT Location: " + self.userLUT[1]) #Log info
        print("LUT stored as graph or cube: " + self.userLUT[2]) #Log info
        print("LUT Resolution: " + str(self.LUTResolution)) #Log info
        print("Current graph kind: " + self.graphKind) #Log info
        print("Stored LUT: " + str(self.storedLUT)) #Log info

    #Refresh the luts - This function is called a lot.
        #Updates and resizes, if necessary, the stored LUT
    def refreshLUT(self):
        if self.storedLUT:
            print("Refreshing LUT info based on updated global settings:") #Log info
            self.printGlobalSettings() #Log info
            self.storedLUT = LUT.FromCubeFile(self.userLUT[1]) #Refresh the LUT from source, via pyLUT
            if (self.storedLUT.resolution > self.LUTResolution):
                print("Resizing LUT to smaller size")
                self.storedLUT = self.storedLUT.Resize(self.LUTResolution)
            elif (self.storedLUT.resolution > self.LUTResolution):
                print("Upscaling LUT.")
                self.storedLUT = self.storedLUT.Resize(self.LUTResolution)
            else:
                print("No LUT resize performed because LUT is proper resolution")
            self.storedLUT.Plot(self.userLUT[2], self.LUTResolution) #Refresh the data from the LUT, via pyLUT
            self.userLUT[0] = self.storedLUT.name #Return the refreshed name from pyLUT
            self.LUTName.setText("LUT Loaded: " + self.userLUT[0]) #Update the LUT Name label widget
            self.Plot() #Update the graph/cube
    
    #When user selects a different resolution
    def resolutionSelectionChange(self, userResolution):
        self.LUTResolution = int(userResolution) #change LUT Resolution to new selection
        print("User changed program resolution to: " + str(userResolution)) #Log info
        self.refreshLUT() #Refresh the stored LUT to match the needs of the resolution

    #Save a file
    def saveFileDialog(self):
        print("User is saving a file")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print("User has selected a location and file name to save file")
            return fileName
    
    #Update Global Resolution setting AND update the GUI to reflect the selected resolution
    def updateSystemResolution(self, newResolution):
        self.LUTResolution = newResolution
        if self.LUTResolution == 9:
            self.comboBoxLUTRes.setCurrentIndex(0)
        if self.LUTResolution == 17:
            self.comboBoxLUTRes.setCurrentIndex(1)
        if self.LUTResolution == 33:
            self.comboBoxLUTRes.setCurrentIndex(2)
        if self.LUTResolution == 65:
            self.comboBoxLUTRes.setCurrentIndex(3)

"""
Additional Windows and Widgets
    These methods are for additional windows and widgets that need to be generated
    on an as-needed basis
"""

class aboutWindow(QWidget):
    """
    This "About Window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """
    def __init__(self):
        super().__init__()

        #Create Main Horizontal Layout
        layout = QHBoxLayout()

        #Window Title
        self.setWindowTitle("About Lutometry")

        #About Logo
        Logo = QLabel(self)
        logoImage = QPixmap("images/LUTometryIcon.png")
        logoImage = logoImage.scaled(256,256)
        Logo.setPixmap(logoImage)
        layout.addWidget(Logo)

        #About Text
        self.aboutText = QLabel("<b>Lutometry</b><br>Version 0.1<br><br>MIT License<br><br>Developed by AJ Young<br>Built on <a href='https://github.com/gregcotten/pylut'>pyLut</a> by Greg Cotten<br><br><a href='http://www.AJYoungDP.com'>www.AJYoungDP.com</a>")
        self.aboutText.setOpenExternalLinks(True) #Allow for hyperlinks to open the system browser
        layout.addWidget(self.aboutText)
        self.setLayout(layout)

class PlotCanvas(FigureCanvas):
    """
    This is what creates the graph/cube. It will be used to replace self.canvas in the
    'App' method when the graph/cube needs to be updated
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100, cube=None):
        self.cubeORgraph = cube #important variable for the program to determine the graph's current state
        
        #Create the figure
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111, projection=cube) #If cube = 3d, then the projection will be a 3D graph

        FigureCanvas.__init__(self, fig)
        
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        
        FigureCanvas.updateGeometry(self)

"""
This runs the entire app
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())