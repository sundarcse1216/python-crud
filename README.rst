Python CRUD Operation
=====================
In this Project I have done CRUD (Create Read Update and Delete) operation using Python-3 and MySQL-5.5.53
(SQL). This is the beginners level application. In this project I have used class, interfaces, calss methods, abstract method, static method, properties(getter and setter), command-line argument(s), logger and read data from .ini file concepts.

Prerequisites
=============
First of all install Pycharm IDE ( https://itsfoss.com/install-pycharm-ubuntu/ ). It Will make easy for development.
The Pycharm required Java-8. So, before that install java-8 JDK
$ sudo apt-get install oracle-java8-installer

Install the following packages one by one Or else install the setup.py

"Configparser" package is used to read data from .ini file

$ sudo pip install configparser==3.5.0

"PyMySQL" package is used to interact with MySQLDB

$ sudo pip install PyMySQL==0.7.11

"python-interface" package is used to create interface in our project

$ sudo pip install python-interface==1.2.0

Below mentioned packages are dependencies

funcsigs: $sudo pip install funcsigs==1.0.2

typing: $sudo pip install typing==3.6.2

six: $sudo pip install six==1.5.2

To install setup.py
===================
go to setup.py file path and run following command, it will install all the dependencies

$ sudo python setup.py install

Running
=======
__main__.py is the main class of this project, just go __main__.py file path and run this file with command-line argument(s). The command-line argument should be atleast one argument atmost four argument
The argument minimum value is 1 maximum value is 4

1 for Create

2 for Read

3 for Update

4 for Delete

For Example: 
	$ python __main__.py 1
Authors
=======
 * Sundararajan S ( @sundar815 )
