# !/usr/bin/env python

import psycopg2

DBNAME = "news"

question_1 = "What are the most popular three articles of all time?"
query_1 = (
    "select articles.title, count(*) as views "
    "from articles join log on log.path "
    "like concat('%', articles.slug, '%') "
    "group by articles.title, log.path order by views desc limit 3")

#question_2 = "Who are the most popular article authors of all time?"
#query_2 = (
    #"")

#question_3 = "On which days did more than 1% of requests lead to errors?"
#query_3 = (
    #"")

def run_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    return results
    db.close

result_1 = run_query(query_1)
#result_2 = run_query(query_2)
#result_3 = run_query(query_3)

def print_query_results(results):
    print (results[1])
    for index, results in enumerate(results[0]):
        print (
            "\t", index+1, "-", str(results[0]),
            "\t - ", str(results[1]), "views")

print(question_1)
print_query_results(result_1)

# print(question_2)
# printResult(result_2)
        
# print(question_3)
# printResult(result_3)
