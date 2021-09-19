# pyinstaller example
This repository contains a simple script which will create new folder under script location with folder name being equal to current time

# Instalation

* Once you have cloned the repository, create virtual environment by using this command: ***virtualenv venv***

* Then, you have to activate it: ***.\venv\Scripts\activate*** (assuming that you are under directory in which you created your virutal environment)

* Then you can run main file: ***python main.py***

* If everything is done successfully, you should see new folder created with current date and time

# Pyinstaller

* At this point, you need to install pyinstaller to be able to create executable files. You can do that with the following: ***pip install pyinstaller***

* To verify that you have installed pyinstaller successfully, you can run the following: ***pyinstaller --version***. In my case this command returns ***4.5.1***, so that means that package is installed correctly

* For the most basic example, run ***pyinstaller main.py*** which will build executable under ./dist directory

* If you want to build everything into single executable, you should use *--onefile* option.

* If you want to change executable name, you should specify it via *--name* option

* If you don't want for popup window to show up after launching executable, you can do that by specifying *--windowed* option