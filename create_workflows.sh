# read the workflow template
WORKFLOW_TEMPLATE=$(cat .github/template.yml)
RUN_TESTS_TEMPLATE=$'echo "Javascripteri nemaj penis ale vaginu 8===D"\nexit 69'

# iterate each route in routes directory
for SVC in $(ls microservices); do
    if [[ $SVC == *_svc ]]; then
        echo "generating workflow for ${SVC}"

        # replace template route placeholder with route name
        WORKFLOW=$(echo "${WORKFLOW_TEMPLATE}" | sed "s/{{SERVICE}}/${SVC}/g")

        # save workflow to .github/workflows/{ROUTE}
        echo "${WORKFLOW}" > .github/workflows/${SVC}.yml

        # create run_tests.sh
        RUN_TESTS_FILE="microservices/${SVC}/run_tests.sh"
        if [[ ! -e ${RUN_TESTS_FILE} ]]; then
            echo "${RUN_TESTS_TEMPLATE}" > ${RUN_TESTS_FILE}
        fi
    else
        echo "skipping ${SVC} - not a service"
    fi
done