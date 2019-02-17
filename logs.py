import psycopg2

DBNAME = "news"


def run_query(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


def get_top_three_articles():
    """Will return back top 3 article of all time """

    # Build Query String
    query = """
        SELECT articles.title, COUNT(*) AS num
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;
    """

    # Run Query
    results = run_query(query)

    # Print Results
    print('\nWhat are the most popular three articles of all time?:')
    count = 1
    for i in results:
        number = '(' + str(count) + ') "'
        title = i[0]
        views = '" with ' + str(i[1]) + " views"
        print(number + title + views)
        count += 1


def get_top_article_authors():
    """returns Who are the most popular article authors of all time? """

    # Build Query String
    query = """
        SELECT authors.name, COUNT(*) AS num
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path like concat('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 3;
    """

    # Run Query
    results = run_query(query)

    # Print Results
    print('\nWho are the most popular article authors of all time? :')
    count = 1
    for i in results:
        print('(' + str(count) + ') ' + i[0] + ' with ' + str(i[1]) + " views")
        count += 1


def get_days_with_errors():
    """returns On which days did more than 1% of requests lead to errors? """

    # Build Query String
    query = """
        SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC;
    """

    # Run Query
    results = run_query(query)

    # Print Results
    print('\nOn which days did more than 1% of requests lead to errors? :')
    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print(date + " -- " + errors)

print('Please wait the results are being calculated Thank you...\n')
get_top_three_articles()
get_top_article_authors()
get_days_with_errors()
