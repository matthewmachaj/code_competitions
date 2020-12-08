#!/bin/bash

EXAMPLE_BASE_FILENAME=example
UNIQUE_BASE_FILENAME=unique
INPUT_FILE_SUFFIX=in
ANSWER_FILE_SUFFIX=ans

SCRIPT_DIR=$(dirname $(readlink -f $0))

usage() {
  cat<<EOF

NAME
	$0 - Run Advent 2020 daily script

SYNOPSIS
	$0 <day_num> <part_num> [-u]

OPTIONS
	-u
	    Run script against '$UNIQUE_INPUT_FILENAME'
EOF
}


DAY_NUM=$1
if [ -z "$DAY_NUM" ]; then
  echo "ERROR: You must provide a day num: [1-31]"
  echo
  usage
  exit 1
fi

PART_NUM=$2
if [[ -z "$PART_NUM" || ( "$PART_NUM" != "1" && "$PART_NUM" != "2" ) ]]; then
  echo "ERROR: You must provide a part num: [1|2]"
  echo
  usage
  exit 1
fi

BASE_FILENAME=${EXAMPLE_BASE_FILENAME}
if [ "$3" = "-u" ]; then
  BASE_FILENAME=${UNIQUE_BASE_FILENAME}
fi

INPUT_FILE=${BASE_FILENAME}.${INPUT_FILE_SUFFIX}
ANSWER_FILE=${BASE_FILENAME}.part${PART_NUM}.${ANSWER_FILE_SUFFIX}

WORKDIR=$SCRIPT_DIR/day${DAY_NUM}
cd $WORKDIR

export PYTHONPATH=../
./run.py $PART_NUM $INPUT_FILE
echo
echo "ANSWER File Contents: [$(cat $ANSWER_FILE)]"

