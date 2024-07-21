import os
import logging
from connect_database import get_db_connection

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_sql_file(filepath: str) -> str:
    """
    Reads an SQL file and returns its result.

    Args:
        filepath (str): The path to the SQL file.

    Returns:
        str: The content of the SQL file.
    """
    with open(filepath, 'r') as file:
        return file.read()

def execute_statistics_queries():
    """
    Executes the SQL statements to create and populate the weather_stats table.
    """
    sql_file_path = os.path.join(os.path.dirname(__file__), 'queries.sql')
    sql_queries = read_sql_file(sql_file_path).split(';')

    create_table_query = sql_queries[3].strip()
    insert_stats_query = sql_queries[4].strip()

    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(create_table_query)
                logging.info("Executed SQL: Create weather_stats table")

                cursor.execute(insert_stats_query)
                logging.info("Executed SQL: Insert statistics into weather_stats table")

                connection.commit()
                cursor.execute("SELECT COUNT(*) FROM weather_stats")
                total_count = cursor.fetchone()[0]
                logging.info(f"Total records ingested: {total_count}")
            except Exception as e:
                logging.error(f"Error executing statistics queries: {str(e)}")
                connection.rollback()

if __name__ == "__main__":
    execute_statistics_queries()
    logging.info("Statistics queries executed successfully.")
