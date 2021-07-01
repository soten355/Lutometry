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
</ul>
<hr>
<h2>How to install</h2>
I highly recommend using this python app in a <a href = "https://realpython.com/python-virtual-environments-a-primer/">virtual environment</a> with Python 3.9 and <a href = "https://realpython.com/intro-to-pyenv/">Pyenv</a>. Additionally, if you're attempting to build from source, you'll need to have the python framework in your Pyenv (<a href = "https://www.froehlichundfrei.de/blog/2014-11-30-my-transition-to-python3-and-pyenv-goodby-virtualenvwrapper/">how to here</a>).

<br>Installation requirements:
<ul>
  <li>
    Python 3.9
  </li>
  <li>
    Homebrew [Mac or Linux users]
  </li>
  <li>
    Pip
  </li>
  <li>
    Pyenv
  </li>
  <li>
    Xcode [Mac users]
  </li>
</ul>

Python modules needed via Pip:
<ul>
  <li>
    NumPy
  </li>
  <li>
    Progress
  </li>
  <li>
    matplotlib
  </li>
  <li>
    PyQt5
  </li>
  <li>
    KDTree
  </li>
</ul>

Here are the steps to install the program for use with Python and a command line interface:

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
    Install Python 3.9.0 via Pyenv (also the framework if building from source)
    <br>Without the framework:
    <br><code>pyenv install 3.9.0</code>
    <br>With the framework:
    <br><code>env PYTHON_CONFIGURE_OPTS="--enable-framework CC=clang" pyenv install 3.9.0</code>
    <br>(Further tutorial on using frameworks and pyenv can be found<a href = "https://www.froehlichundfrei.de/blog/2014-11-30-my-transition-to-python3-and-pyenv-goodby-virtualenvwrapper/">here</a>)
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
    In the virtual environment, use Pip install the necessary modules (listed above).The program will send an error message and quit if a module is missing. Check the command line interface for which ones are missing:
    <ul>
      <li>
        <code>pip install --only-binary :all: numpy</code>
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
  </li>
</ol>
