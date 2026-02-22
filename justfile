manage_base := 'uv run manage.py'

# Python manage.py commands
manage *ARGS:
  {{ manage_base }} {{ ARGS }}

check *ARGS:
  {{ manage_base }} check {{ ARGS }}

run *ARGS:
  {{ manage_base }} runserver {{ ARGS }}

makemig *ARGS:
  {{ manage_base }} makemigrations {{ ARGS }}

mig *ARGS:
  {{ manage_base }} migrate {{ ARGS }}

shell *ARGS:
  {{ manage_base }} shell {{ ARGS }}

# Django - Tailwind
tw *ARGS:
  {{ manage_base }} tailwind start {{ ARGS }}

# Tools
ruff *ARGS:
  uv tool run ruff {{ ARGS }}

