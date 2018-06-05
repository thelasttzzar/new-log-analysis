# !/usr/bin/env python

import psycopg2

DBNAME = "news"

question_1 = "What are the most popular three articles of all time?"
query_1 = (
    "select articles.title, count(*) as views "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug, '%') "
    "where log.status like '%200%' "
    "group by articles.title, log.path "
    "order by views desc limit 3")

#question_2 = "Who are the most popular article authors of all time?"
#query_2 = (
    #"")

#question_3 = "On which days did more than 1% of requests lead to errors?"
#query_3 = (
    #"")


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable to connect to the database")


def run_query(query):
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def print_results(query_results):
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print "\t", index+1, "-", results[0],"\t - ", str(results[1]), "views"


if __name__ == '__main__':
    # define/store results
    three_most_popular_articles = run_query(query_1), question_1
    # most_popular_authors = run_query(query_2), question_2
    # days_errors_exceed_one-percent = run_query(query_3), question_3
    
    # print results
    print_results(three_most_popular_articles)
    # print_results(most_popular_authors)
    # print_results(days_errors_exceed_one-percent)
