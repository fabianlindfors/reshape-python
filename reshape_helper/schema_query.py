import glob, os
from pathlib import Path
from natsort import natsort_keygen
import toml
import json

DEFAULT_SEARCH_PATH = '"$user", public'

def schema_query(*dirs):
	path = search_path(*dirs) or DEFAULT_SEARCH_PATH
	return f"SET search_path TO {path}"

def search_path(*dirs):
	if len(dirs) == 0:
		dirs = ["migrations"]

	migrations = find_migrations(dirs)

	if len(migrations) == 0:
		return None
	else:
		last_migration = migrations[-1]
		return f"migration_{last_migration}"

def find_migrations(dirs):
	# Find all files across all specified directories
	files = [filename for dir in dirs for filename in glob.glob(f"{dir}/*")]

	# Sort files by their names in natural order
	natsort_key = natsort_keygen()
	sorted_files = sorted(files, key=lambda file: natsort_key(Path(file).name))

	migrations = [migration_name_for_file(file) for file in sorted_files]
	return migrations

def migration_name_for_file(file_path):
	contents = open(file_path, "r").read()
	migration = decode_migration(file_path, contents)

	if "name" in migration:
		return migration["name"]
	else:
		return Path(file_path).stem

def decode_migration(file_path, contents):
	if len(contents) == 0:
		return {}

	extension = Path(file_path).suffix
	if extension == ".toml":
		return toml.loads(contents)
	elif extension == ".json":
		return toml.loads(contents)
	else:
		raise Exception(f"Unrecognized migration file extension {extension}")