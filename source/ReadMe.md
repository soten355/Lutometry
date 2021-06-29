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
I highly recommend using this python app in a <a href = "https://realpython.com/python-virtual-environments-a-primer/">virtual environment</a> with Python 3.9 and Pyenv. Additionally, if you're attempting to build from source, you'll need to have the python framework in your Pyenv (<a href = "https://www.froehlichundfrei.de/blog/2014-11-30-my-transition-to-python3-and-pyenv-goodby-virtualenvwrapper/">how to here</a>).

<br>Installation requirements:
<ul>
  <li>
    Python 3.9
  </li>
  <li>
    Homebrew
  </li>
  <li>
    Pip
  </li>
  <li>
    Pyenv
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
    Install Homebrew
  </li>
  <li>
    Install Pyenv via Homebrew
  </li>
  <li>
    Install Python 3.9 via Pyenv (also the framework if building from source)
  </li>
  <li>
    Create a virtual environment
  </li>
  <li>
    In the virtual environment, use Pip install the necessary modules (listed above). The program will send an error message and quit if a module is missing. Check the command line interface for which ones are missing
  </li>
  <li>
    In the virtual environment, run the program
  </li>
</ol>
