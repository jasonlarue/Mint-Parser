#Mint-Parser
I use the personal budgeting software [Mint](http://mint.com) (made by Intuit) and I wanted a way to access and download my net worth easily. This is a simple python script that can login to your Mint account for you, refresh and retrieve your net worth, and save it in a CSV file. 

#Requirements:
* This script uses Selenium WebDriver, you must have that module installed.
* I chose to use Firefox as the web driver, so by default you must have that installed. If you wish to change the web driver to something else you can do that manually. 
* In the working directory where you run this script, you must have a CSV file called "balance.csv" in order for the script to work properly.

#Steps:
1. Make sure you have fulfilled all the requirements
2. Edit webparser.py and change "your username here" and "your password here" to your username and password for Mint, make sure that you keep the quotes.
3. Run the script to retrieve your net worth once, or set the script to run on a time interval if you want to track your net worth over time. 