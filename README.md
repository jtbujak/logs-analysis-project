# Log Analysis Project
This is my log analysis project for Udacity.  When the program `log_analysis.py` is run, it sends three queries to a SQL database and produces a text output with answers to the three questions assigned: (1) What are the most popular three articles of all time? (2) Who are the most popular article authors of all time?

# Necessary Software
This program was written using Python 3.6.2.  You will need to have Python installed on your computer in order to run the _Movie Trailer Website_ program.

# How to Run the Program
These instructions assume that you have the `news` database installed per the Udacity instructions.  If so, then simply run the `log_analysis.py` program in the same folder as the database.

# Views
I created two views in order to complete this poject.  The two view commands are:

CREATE view article as
SELECT title, author, count(*) as views
FROM articles, log
WHERE log.path like concat('%', articles.slug)
GROUP by articles.title, articles.author order by views desc;

CREATE view error as
SEKECT date(time), round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)/count(log.status), 2) as "Percent Error"
FROM log 
GROUP by date(time) order by "Percent Error" desc;

# Licensing

MIT License

Copyright (c) [2017] [John T Bujak]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.