# !/usr/bin/env python

import psycopg2

DBNAME = "news"

question_1 = "What are the most popular three articles of all time?"
query_1 = (
    "select articles.title, count(*) as views "
    "from articles join log on log.path "
    "like concat('%', articles.slug, '%') "
    "group by articles.title, log.path order by views desc limit 3")

question_2 = "Who are the most popular article authors of all time?"
query_2 = (
    "")

question_3 = "On which days did more than 1% of requests lead to errors?"

def runQuery(sql_query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close
    return results

result_1 = runQuery(query_1)
#result_2 = runQuery(query_2)
#result_3 = runQuery(query_3)

def printResult():

print(question_1)
printResult(result_1)
    
# print(question_2)
# printResult(result_2)
    
# print(question_3)
# printResult(result_3)
