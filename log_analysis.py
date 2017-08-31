#! /usr/bin/env python3

import psycopg2

# Query for question number 1 (What are the most popular
# three articles of all time?)
query1 = "select title,views from article limit 3"

# Query for question number 2 (Who are the most popular
# article authors of all time?)
query2 = """select authors.name,sum(article.views) as views from
article,authors where authors.id = article.author
group by authors.name order by views desc"""

# Query for question number 3 (On which days did more
# than 1% of requests lead to errors?)
query3 = "select * from error where \"Percent Error\" > 1"

# defining and formatting output
query_1_result = dict()
query_1_result['title'] = (
    """\n1. The three most popular articles of all time are:\n"""
    )

query_2_result = dict()
query_2_result['title'] = (
    """\n2. The most popular article authors of all time are:\n"""
    )

query_3_result = dict()
query_3_result['title'] = (
    """\n3. Days with more than 1% of requests that lead to errors:\n"""
    )

# obtaining and printing query results


def get_query_result(query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' --- ' + str(result[1]) + ' views')


def print_error(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' --- ' + str(result[1]) + ' %')


# defining query results
query_1_result['results'] = get_query_result(query1)
query_2_result['results'] = get_query_result(query2)
query_3_result['results'] = get_query_result(query3)

# printing final output
print_query_results(query_1_result)
print_query_results(query_2_result)
print_error(query_3_result)
