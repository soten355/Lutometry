# Lutometry Source Code
This directory contains the source code for <b>Lutometry</b>

<h2>File break down</h2>
<ul>
  <li>
    images/ - necessary icons for the app
  </li>
  <li>
    lutometry.py - The main python app
  </li>
  <li>
    pylut.py - The updated and modified pyLUT module
  </li>
  <li>
    setup.py - The setup file used by py2app to build from source on Mac
  </li>
</ul>
<hr>
<h1>How to use the source code</h1>
I highly recommend using this python app in a <a href = "https://realpython.com/python-virtual-environments-a-primer/">virtual environment</a> with Python 3.9 and <a href = "https://realpython.com/intro-to-pyenv/">Pyenv</a>. Additionally, if you're attempting to build from source, you'll need to have the python framework in your Pyenv (<a href = "https://www.froehlichundfrei.de/blog/2014-11-30-my-transition-to-python3-and-pyenv-goodby-virtualenvwrapper/">how to here</a>).

<br>Installation requirements:
<ul>
  <li>
    <a href = "https://www.python.org/">Python 3.9+</a>
  </li>
  <li>
    <a href = "https://brew.sh/">Homebrew</a> [Mac or Linux users]
  </li>
  <li>
    <a href = "https://pypi.org/project/pip/">Pip</a>
  </li>
  <li>
    <a href = "https://github.com/pyenv/pyenv">Pyenv</a>
  </li>
  <li>
    <a href = "https://developer.apple.com/xcode/">Xcode</a> [Mac users]
  </li>
</ul>

Python modules needed via Pip:
<ul>
  <li>
    <a href = "https://numpy.org/">NumPy</a>
  </li>
  <li>
    <a href = "https://pypi.org/project/progress/">Progress</a>
  </li>
  <li>
    <a href = "https://matplotlib.org/">matplotlib</a>
  </li>
  <li>
    <a href = "https://pypi.org/project/PyQt5/">PyQt5</a>
  </li>
  <li>
    KDTree
  </li>
</ul>

<h2>How to use the source code on a Mac</h2>

<ol>
  <li>
    Install Homebrew [If not already installed]
    <br><code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code>
  </li>
  <li>
    Install Pyenv via Homebrew
    <br><code>brew install pyenv</code>
  </li>
  <li>
    Install Python 3.9.0 via Pyenv
    <br>Without the framework (if you want to develop/run the program through Terminal):
    <br><code>pyenv install 3.9.0</code>
    <br>With the framework (if you want to build a standalone app of this program):
    <br><code>env PYTHON_CONFIGURE_OPTS="--enable-framework CC=clang" pyenv install 3.9.0</code>
    <br>(Further tutorial on using frameworks and pyenv can be found <a href = "https://www.froehlichundfrei.de/blog/2014-11-30-my-transition-to-python3-and-pyenv-goodby-virtualenvwrapper/">here</a>)
  </li>
  <li>
    Create a virtual environment
    <br><code>python3 -m venv [desired_name_of_your_virtual_environment]</code>
    <br>[desired_name_of_your_virtual_environment] = whatever name you want to call the virtual environemnt. Shorter names are easier to type in the console. I recommend something like "lutenv" or "VirtLut".
  </li>
  <li>
    Run the newly created virtual environment
    <br><code>source [desired_name_of_your_virtual_environment]/bin/activate</code>
  <li>
    In the virtual environment, use Pip install the necessary modules (listed below).The program will send an error message and quit if a module is missing. Check the command line interface for which ones are missing.
    <ul>
      <li>
        <code>pip install --only-binary :all: numpy</code>
        <ul>
          <li>
            (installing NumPy like this is the only way for the program to work on other Mac's if you are building from source into a standalone app)
          </li>
        </ul>
      </li>
      <li>
        <code>pip install progress</code>
      </li>
      <li>
        <code>pip install matplotlib</code>
      </li>
      <li>
        <code>pip install pyqt5</code>
      </li>
      <li>
        <code>pip install kdtree</code>
      </li>
    </ul>
  </li>
  <li>
    In the virtual environment, run the program
    <br><code>python lutometry.py</code>
  </li>
</ol>

<h2>How to build from source on Mac</h2>

<ol>
  <li>
    Make sure you're running the virtual environment. If not, activate the virtual environment:
    <br><code>source [desired_name_of_your_virtual_environment]/bin/activate</code>
  </li>
  <li>
    Install py2app via pip:
    <br><code>pip install py2app</code>
  </li>
  <li>
    Make sure you have the setup.py from Lutometry's github file in the same folder as lutometry.py.
    <br>(If you've installed any additional modules beyond what Lutometry needs, you'll need to edit the setup.py file to include those additional modules)
  </li>
  <li>
    Build the app:
    <br><code>python setup.py py2app</code>
  </li>
  <li>
    The <b>Lutometry</b> app file will be in dist/Lutometry.app
  </li>
  <li>
    <b>Lutometry</b> is ready for use!
  </li>
</ol>
  
