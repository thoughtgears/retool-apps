import psycopg2
from dotenv import load_dotenv
import click
import os

# Load environment variables
load_dotenv()


def execute_sql_file(filename, connection):
    """Executes the SQL statements in the given file."""
    with open(filename, 'r') as sql_file:
        sql = sql_file.read()
    with connection.cursor() as cursor:
        cursor.execute(sql)
    connection.commit()


def create_table(file: str, password: str, host: str) -> None:
    """Creates a table in the database if it doesn't exist."""
    try:
        # Use 'with' to ensure proper cleanup of resources
        with psycopg2.connect(
                dbname="retool",
                user="retool",
                password=password,
                host=host,
                port="5432"
        ) as connection:
            print("Connection successful")
            execute_sql_file(file, connection)
            print("Table created successfully")

    except psycopg2.DatabaseError as error:
        print(f"Database error occurred: {error}")
    except Exception as error:
        print(f"Unexpected error occurred: {error}")


@click.command()
@click.option('--app-name', type=str, required=True, help='Retool app name')
def main(app_name: str):
    """CLI command to trigger the table creation process."""
    db_password = os.getenv("PG_PASSWORD")
    db_host = os.getenv("PG_HOST")

    # Ensure required environment variables are present
    if not db_password or not db_host:
        raise EnvironmentError("PG_PASSWORD and PG_HOST must be set in the environment variables.")

    file_path = f"db/{app_name}/db.sql"

    if not os.path.exists(file_path):
        print(f"SQL file {file_path} does not exist.")
        return

    create_table(file_path, db_password, db_host)


# Entry point for the CLI script
if __name__ == "__main__":
    main()
