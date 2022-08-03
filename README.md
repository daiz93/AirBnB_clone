# Description of the project

The AirBnB clone project is last project of firspart of my python learning year with [Holberton](https://www.holbertonschool.com/). The goal of the project is to deploy on my server a simple copy of the [AirBnB website](https://fr.airbnb.com/?_set_bev_on_new_domain=1659504441_ZGM1MzFmYjBiYTYy).
During 4 month we will build:


    * A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
    * A website (the front-end) that shows the final product to everybody: static and dynamic
    * A database or files that store data (data = objects)
    * An API that provides a communication interface between the front-end and data (retrieve, create, delete, update them)


# Description of the command interpreter:

## how to start it
        Command interpreter is a Shell that we will use in this case to manage the objects of our project. It will be build to recognized and execute some commande we use in this project as a shell command.

## how to use it
The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.

## example

**Work like this in interactive mode:**

'''
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
'''
**Non-interactive mode**

'''
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
'''
