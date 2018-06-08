# !/usr/bin/env python

import psycopg2

DBNAME = "news"

# Query 1 "three_most_popular_articles"
question_1 = "What are the most popular three articles of all time?"
query_1 = (
    """select articles.title, count(*) as views 
    from articles inner join log on log.path 
    like concat('%', articles.slug, '%') 
    where log.status like '%200%' 
    group by articles.title 
    order by views desc limit 3""")

# Query 2 "most_popular_authors"
question_2 = "Who are the most popular article authors of all time?"
query_2 = (
    """select authors.name, count(*) as views from articles 
    inner join authors on articles.author = authors.id 
    inner join log on log.path like concat('%', articles.slug, '%') 
    where log.status like '%200%' 
    group by authors.name 
    order by views desc""")

# Query 3 "days_errors_exceed_one_percent"
question_3 = "On which days did more than 1% of requests lead to errors?"
query_3 = (
    """select * from perc_error where \"Error Percent\" >1""")

# Connect to the Database
def connect(dbname="news"):
    try:
        db = psycopg2.connect("dbname={}".format(dbname))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable to connect to the database")

# Run the query itself
def run_query(query):
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

# Define printing of queries relating to views
def print_results(query_results):
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print "\t", results[0]," - ", str(results[1]), "views"

# Define printing of queries relating to errors
def print_errors(query_results):
    print (query_results[1])
    for results in query_results[0]:
        print "\t", results[0], " - ", str(results[1]), "% errors"


if __name__ == '__main__':
    # Store results
    three_most_popular_articles = run_query(query_1), question_1
    most_popular_authors = run_query(query_2), question_2
    days_errors_exceed_one_percent = run_query(query_3), question_3
    
    # Print results
    print_results(three_most_popular_articles)
    print_results(most_popular_authors)
    print_errors(days_errors_exceed_one_percent)
