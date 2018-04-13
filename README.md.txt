Introduction

I have created a code using Python and SQL programming languages to extract data from a database.
The 3 questions that are answered are the following:

1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

How to Run

1. Must install VAGRANT, VIRTUALBOX, and PYTHON 3. 

2. Clone the following : git clone https://github.com/visheshbanga/Log-Analysis-Udacity-Project

3.'Vagrant Up' within the folder you've clone the above URL via computer terminal, then 'Vagrant SSH' to log into VM.

4. To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.

5. Connect to your database using psql -d news and explore the tables using the \dt and \d table commands and select statements.

6.Run python3 LogAnalysis.