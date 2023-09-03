ENV_FILE="./env/.dev.env"
ENTRYPOINT="./docker/dev/entrypoint.sh"
CMD="python -Xfrozen_modules=off manage.py runserver 0.0.0.0:8000"

env $(cat $ENV_FILE | xargs) $ENTRYPOINT bash -c "$CMD"