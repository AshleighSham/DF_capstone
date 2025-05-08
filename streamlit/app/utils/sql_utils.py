def import_sql_query(_filename):
    try:
        with open(_filename, 'r') as file:
            imported_query = file.read().replace('\n', ' ').strip()
            print(f"Successfully imported query from {_filename}")
            return imported_query
    except FileNotFoundError as e:
        raise (f"Failed to import query in {_filename}: {e}")
