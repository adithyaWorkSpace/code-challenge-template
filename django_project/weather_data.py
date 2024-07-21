import os
import logging
import multiprocessing as mp
from datetime import datetime
from connect_database import get_db_connection

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_sql_file(filepath: str) -> str:
    """
    Reads an SQL file and returns its content.

    Args:
        filepath (str): The path to the SQL file.

    Returns:
        str: The content of the SQL file.
    """
    with open(filepath, 'r') as file:
        return file.read()

def handle_missing_value(value: str) -> str:
    """
    Replaces missing values with None.

    Args:
        value (str): The value to check.

    Returns:
        str: None if the value is '-9999', otherwise the original value.
    """
    return None if value == '-9999' else value

def process_file(filepath: str) -> int:
    """
    Processes a weather data file and inserts data into the database.

    Args:
        filepath (str): The path to the weather data file.

    Returns:
        int: 1 if processing is successful, 0 otherwise.
    """
    try:
        with get_db_connection() as connection:
            cursor = connection.cursor()
            sql_file_path = os.path.join(os.path.dirname(__file__), 'queries.sql')
            sql_queries = read_sql_file(sql_file_path).split(';')

            filename = os.path.basename(filepath)
            filename_str = os.path.splitext(filename)[0]

            with open(filepath, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split()

                    if len(data) != 4:
                        logging.warning(f"Skipping malformed line in file {filename}: {line.strip()}")
                        continue

                    date_str, max_temp_str, min_temp_str, precipitation_str = data

                    max_temp_str = handle_missing_value(max_temp_str)
                    min_temp_str = handle_missing_value(min_temp_str)
                    precipitation_str = handle_missing_value(precipitation_str)

                    try:
                        cursor.execute(sql_queries[1].strip(), (filename_str, date_str))
                        existing_record = cursor.fetchone()

                        if not existing_record:
                            cursor.execute(sql_queries[2].strip(), (filename_str, date_str, max_temp_str, min_temp_str, precipitation_str))
                            connection.commit()
                    except Exception as e:
                        logging.error(f"Error processing line in file {filename}: {line.strip()} - {str(e)}")

            cursor.close()
        return 1  
    except Exception as e:
        logging.error(f"Error processing file {filepath}: {str(e)}")
        return 0  

def main():
    """
    Main function to handle the data ingestion process.
    """
    try:
        with get_db_connection() as connection:
            cursor = connection.cursor()

            sql_file_path = os.path.join(os.path.dirname(__file__), 'queries.sql')
            sql_queries = read_sql_file(sql_file_path).split(';')

            cursor.execute(sql_queries[0].strip())
            connection.commit()

            directory = os.path.join(os.path.dirname(__file__), '..', 'wx_data')
            directory = os.path.abspath(directory)

            if not os.path.exists(directory):
                logging.error(f"The directory {directory} does not exist.")
                return

            files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]
            if not files:
                logging.error(f"No .txt files found in the directory {directory}.")
                return

            # Log the start time of data ingestion process
            start_time = datetime.now()
            logging.info("Data ingestion started")

            with mp.Pool(processes=5) as pool:
                results = pool.map(process_file, files)

            # Calculate total files successfully ingested into the database
            total_files = sum(results)

            # Log the end time of data ingestion process and the number of records ingested
            end_time = datetime.now()
            logging.info(f"Data ingestion completed. Start time: {start_time}, End time: {end_time}, Total files ingested: {total_files}")

            cursor.close()

    except Exception as error:
        logging.error(f"Error connecting to the database or processing data: {error}")

if __name__ == '__main__':
    main()
