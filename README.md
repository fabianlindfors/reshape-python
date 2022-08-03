# Reshape Python helper

[![Tests](https://github.com/fabianlindfors/reshape-python/actions/workflows/test.yaml/badge.svg)](https://github.com/fabianlindfors/reshape-python/actions/workflows/test.yaml)

This is a Python helper library for the automated, zero-downtime schema migration tool [Reshape](https://github.com/fabianlindfors/reshape). To achieve zero-downtime migrations, Reshape requires that your application runs a simple query when it opens a connection to the database to select the right schema. This library automates that process with a simple method which will return the correct query for your application. It also [works great with Django](#usage-with-django)!

## Installation

```
pip install reshape_helper
```

## Usage

The library includes a `schema_query` method which will find all your Reshape migration files and determine the right schema query to run. Here's an example of how to use it:

```python
import schema_query from reshape_helper

# Run the schema query against your database when you open a new connection
db.execute(schema_query())
```

By default, `schema_query` will look for migrations files in `migrations/`, but you can specify your own directories as well:

```python
import schema_query from reshape_helper

query = schema_query(
	"src/users/migrations",
	"src/todos/migrations",
)
```

## Usage with Django

Using Reshape for zero-downtime migrations with Django is really simple. After installing `reshape_helper`, update your `app.py` and add a handler for the `connection_created` signal. This handler will run the schema query whenever a new database connection is opened:

```python
from django.db.backends.signals import connection_created
import schema_query from reshape_helper

class YourAppConfig(AppConfig):
	def ready(self):
		connection_created.connect(new_connection_handler)

def new_connection_handler(sender, connection, **kwargs):
	connection.cursor().execute(schema_query())
```

Now your Rails app is ready for use with Reshape. Rather than creating standard Django migrations, you should create [Reshape migration files](https://github.com/fabianlindfors/reshape) in `migrations/`. If you'd prefer to use other folders for your migrations, you can pass them to `schema_query()`:

```python
def new_connection_handler(sender, connection, **kwargs):
	connection.cursor().execute(schema_query("yourapp/users/migrations", "yourapp/todo/migrations"))
```

## License

Released under the [MIT license](https://choosealicense.com/licenses/mit/).