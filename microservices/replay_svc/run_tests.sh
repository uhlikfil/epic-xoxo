BASEDIR=$(dirname "$0")

cd $BASEDIR/docker_tests

docker-compose build
docker-compose up --abort-on-container-exit --exit-code-from swa_replays_test
docker-compose down

exit $?
