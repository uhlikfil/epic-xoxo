BASEDIR=$(dirname "$0")
cd $BASEDIR/test

docker volume rm test_db_data
docker-compose build
docker-compose up --abort-on-container-exit --exit-code-from sut

exit $?
