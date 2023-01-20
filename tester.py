from shillelagh.adapters.registry import registry
from shillelagh.backends.apsw.db import connect
from shillelagh.adapters.file.adapter import JsonPlaceHolderAPI
from adapter import JsonPlaceHolderAPI

#registry.register('jsonplaceholderapi', "/Users/pawankumar/sup-analysis/jsonplaceholders/adapter.py","JsonPlaceHolderAPI")
registry.add('jsonplaceholderapi', JsonPlaceHolderAPI)
print(registry.loaders.keys())
print(registry.loaders.values())
from shillelagh.backends.apsw.db import connect

if __name__ == "__main__":
    connection = connect(":memory:", adapters=['jsonplaceholderapi'])
    cursor = connection.cursor()

    SQL = 'SELECT * from "https://jsonplaceholder.typicode.com/comments?postId=2"'
    for row in cursor.execute(SQL):
        print(row)

