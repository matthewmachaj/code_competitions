#!/bin/bash

#-------------------------------------------------------------------------------
# The script requires you to manually grab the cookie named `session` for
# the `adventofcode.com` domain from a currently logged-in browser (or CLI)
# session and store it in a file called `session.cookie` in the same directory
# as this script.
#-------------------------------------------------------------------------------
SESSION_COOKIE_NAME=session
SESSION_COOKIE_FILE=./session.cookie

NUM=${1:-0}

if [ "${NUM}" -lt 1 -o "${NUM}" -gt 31 ]; then
  echo -e "You must provide a day number from 1-31."
  exit 1
fi

if [ ! -f ${SESSION_COOKIE_FILE} ]; then
  echo "You must store you session cookie at -> [${SESSION_COOKIE_FILE}]"
  exit 1
fi

URL=https://adventofcode.com/2020/day/${NUM}/input

OUTPUT_DIR=day${NUM}
if [ ! -d $OUTPUT_DIR} ]; then
  mkdir $OUTPUT_DIR
fi
OUTPUT_FILE=$OUTPUT_DIR/unique.in
SESSION_COOKIE_HEADER="Cookie: ${SESSION_COOKIE_NAME}=$(cat ${SESSION_COOKIE_FILE})"

#-------------------------------------------------------------------------------
# Verify we can GET file
#-------------------------------------------------------------------------------
IS_VALID=( curl -I -s -H "${SESSION_COOKIE_HEADER}" "${URL}")
echo -e "Running curl:\n  ${IS_VALID[@]}"
echo
"${IS_VALID[@]}" | head -n1 | grep -q 200

if [ $? != 0 ]; then
  echo -e "Error: likely an invalid session cookie when getting input file"
fi

#-------------------------------------------------------------------------------
# Now GET the file
#-------------------------------------------------------------------------------
GET_INPUT_FILE=( curl -o "${OUTPUT_FILE}" -H "${SESSION_COOKIE_HEADER}" "${URL}" )
echo -e "Running curl:\n  ${GET_INPUT_FILE[@]}"
echo
"${GET_INPUT_FILE[@]}"
