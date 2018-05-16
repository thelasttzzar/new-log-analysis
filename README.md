# Log Analysis Project

A project for the Udacity Full Stack Web Developer Nanodegree. As part of the section on backend: databases & applications, this is a test of how comfortable you are with working with databases and connecting them to Python code.

## The Purpose 

This code asks 3 questions about a newspaper blog site, and queries the database for answers, and displays those answers in plain text.  We want to know:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

## Prerequisites

In order to run this program you'll need Python 2.7 or newer. All files should be in the same directory. You'll also need access to the "news" database, and a Vagrant virtual machine configured.

## Project Contents

All of these files are required to run the program
* news-log-analysis.py
* (the database "news", but the course notes don't require it to be submitted here)

## How to run

* Download or clone the full repository to your machine
* Move the repository to a Vagrant virtual machine directory on your machine
* Open a terminal window
* Launch the VM using ```vagrant up``` and login using ```vagrant ssh```
* CD to the /vagrant directory (where you placed the news-log-analysis.py file)
* Run ```python news-log-analysis.py``` (you may need to use python3 if that's the version you're using)


## Built With

* [Python](https://www.python.org/) - The entirety of the programing (IDLE)
* [Sublime](https://www.sublimetext.com/) - The README
* [GitHub](https://github.com/) - Version control 
* [Udacity](https://www.udacity.com/) - Forums and rubric

## Considerations

* This is all effectively brand-new stuff for me.

## Authors

* **Nick Cassady** - *following the class* 

### Miscellaneous

I definitely got some help on this one from my Udacity mentor, as well as the community in general. And can't forget good ol' Googlin'