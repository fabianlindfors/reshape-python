# Reshape Python helper

This is a Python helper library for the automated, zero-downtime schema migration tool [Reshape](https://github.com/fabianlindfors/reshape). To achieve zero-downtime migrations, Reshape requires that your application runs a simple query when it opens a connection to the database to select the right schema. This library automates that process with a simple method which will return the correct query for your application.

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

## License

Released under the [MIT license](https://choosealicense.com/licenses/mit/).