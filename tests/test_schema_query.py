from reshape_helper import schema_query

def test_default_directory():
	assert schema_query() == "SET search_path TO migration_2_test_migration"

def test_custom_directory():
	assert schema_query("tests/fixtures/migrations-1") == "SET search_path TO migration_10_test_migration"

def test_multiple_directories():
	assert schema_query("tests/fixtures/migrations-1", "tests/fixtures/migrations-2") == "SET search_path TO migration_10_test_migration"

def test_custom_migration_name():
	assert schema_query("tests/fixtures/custom-migration-name") == "SET search_path TO migration_custom_migration_name"

def test_non_existent_directory():
	assert schema_query("tests/fixtures/non-existens") == 'SET search_path TO "$user", public'
