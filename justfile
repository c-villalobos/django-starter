manage_base := 'uv run manage.py'

# Python manage.py commands
manage *ARGS:
	{{ manage_base }} {{ ARGS }}

run *ARGS:
	{{ manage_base }} runserver {{ ARGS }}

makemig *ARGS:
	{{ manage_base }} makemigrations {{ ARGS }}

mig *ARGS:
	{{ manage_base }} migrate {{ ARGS }}

shell *ARGS:
	{{ manage_base }} shell {{ ARGS }}

# Tools
ruff *ARGS:
  uv tool run ruff {{ ARGS }}

