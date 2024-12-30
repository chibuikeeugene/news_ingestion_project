import psycopg2
from psycopg2.extras import execute_values

# save process data to our database
def store_in_postgres(record: list[dict], db_config):
    """save transformed data to our postgres database"""

    # establishing a connection
    conn = psycopg2.connect(**db_config)

    # creating a cursor object
    with conn.cursor() as cursor:
        query = """
                CREATE TABLE IF NOT EXISTS news (title varchar, link varchar, published_date timestamp);                
                """
        insert_data_query =  """
                INSERT INTO news (title, link, published_date) VALUES (%s, %s, %s)
                """
        value = [(r["title"], r["link"], r["published"]) for r in record]
        cursor.execute(query)
        execute_values(cursor, insert_data_query,value)

        # making the changes to the database persistent
        conn.commit()

        cursor.close()
        conn.close()