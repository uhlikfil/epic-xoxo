BASEDIR=$(dirname "$0")

docker-compose build
docker-compose -f docker-compose.tests.yml up --abort-on-container-exit --exit-code-from swa_game_service_test
docker-compose down -v

exit $?
