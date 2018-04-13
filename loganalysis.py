#importing psycopg2 library
#connecting to database named News

#the following is the step by step behaviors of the 3 queries:
#created cursor object to retrieve data from database
#created a command in sql to collect certain info
#informed cursor to fetch results within a certain way
#display results
#closed connection


import psycopg2

conndb = psycopg2.connect(DATABASE="news")


#question 1, top 3 articles
def top_three_articles():
    db = conndb
    cursor = db.cursor()
    cursor.execute(''''select path, count (*) as number
            from log where path like '%/article%'
            and status = '200 OK'group by path
            order by number desc limit 3;''')
    results = cursor.fetchall()
    print results
    conn.close()

#question 2, most popular authors
def most_popular_authors():
    db = conndb
    cursor = db.cursor()
    cursor.execute('''select authors.name, count(*) as num
            from articles, authors, log
            where log.status='200 OK'
            and authors.id = articles.author
            and articles.slug = substr(log.path, 10)
            group by authors.name
            order by num desc;''')
    results = cursor.fetchall()
    print results
    conn.close()


#qsuestion 3, On which days did more than 1% of requests lead to errors
def percentage_lead_to_errors():
    db = conndb
    cursor = db.cursor()
    cursor.execute('''select * from (
        select to_char(a.day,'Mon dd, yyyy'),
        round
        (cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2)
            as err_ratio from
        (select date(time) as day, count(*)
            as hits from log group by day) as a join
        (select date(time) as day, count(*)
            as hits from log where status
        like '%404%' group by day) as b
        on a.day = b.day) as c
        where err_ratio > 1.0;''')
    results = cursor.fetchall()
    print results
    conn.close()


if __name__ == "__main__":
    top_three_articles()
    most_popular_authors()
    percentage_lead_to_errors()

   

