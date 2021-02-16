#!/bin/bash

# Run all the shortest path tests in the sp_tests directory. See README.md
# for information on how to write tests.

# Set some strings to help us format our results.
green_format='\033[0;32m'
red_format='\033[0;31m'
reset_format='\033[0m'

# Specify that all the shortest path tests are in the shortest_path_tests directory.
sp_tests_dir="shortest_path_tests"

# Make sure that the test binary is available.
make test_shortest_path
if [ $? -ne 0 ]; then
	echo -e "${red_format}Error building the testing binary."
	exit 1;
fi

# Calculate the list of available tests in the test directory.
tests=$(for i in `ls ${sp_tests_dir}/*`; do echo `basename $i` | awk -F. '{print $1;}' ; done | sort -u);

total_tests=0
passing_tests=0
failing_tests=0

for i in $tests; do
	# Make sure that all three required files are present.
	if [ \! \( -f ${sp_tests_dir}/$i.environment \) -o \! \( -f ${sp_tests_dir}/$i.guards \) -o \! \( -f ${sp_tests_dir}/$i.result \) ]; then
		echo -e "${red_format}Cannot run ${i}: Missing file."
		failing_tests=$(( failing_tests + 1 ))
		continue
	fi

	# Run the test.
	./test_shortest_path ${sp_tests_dir}/$i.environment ${sp_tests_dir}/$i.guards ${sp_tests_dir}/$i.result

	# Handle the result.
	if [ $? -ne 0 ]; then
		echo "${red_format}Test Failure."
		failing_tests=$(( failing_tests + 1 ))
	else
		echo -e "${green_format}Test Passed."
		passing_tests=$(( passing_tests + 1 ))
	fi

	# No matter what, we ran a test so we have to add 1 to total_tests.
	total_tests=$(( total_tests + 1 ))
done

echo "==============================================="
echo "Results:"
echo -e "${green_format}Passing Tests: ${passing_tests}"
echo -e "${red_format}Failing Tests: ${failing_tests}"
echo -e "${reset_format}Total   Tests: ${total_tests}"

# The status code will be the number of failing tests.
exit ${failing_tests}
