BASEDIR=$(dirname "$0")

cd $BASEDIR/game_svc_tests
docker-compose build
docker-compose -f up --abort-on-container-exit --exit-code-from swa_game_service_test
docker-compose down -v

exit $?
