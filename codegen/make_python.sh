java -jar swagger-codegen-cli-3.0.25.jar generate \
-i ./../docs/swagger/$1_api.yaml \
-l python-flask \
-o ./../microservices/$1/src/ -DpackageName=$1