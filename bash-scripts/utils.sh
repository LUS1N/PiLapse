#!/bin/bash

function upsert_dir {
    if [ ! -d "$1" ]; then
        mkdir "$1"
        echo "$1"
    fi
}  

function delete_dir {
    rm -rf  "$1"
} 

function read_times {
    timesValue=`cat times`
    FROM_TIME="${timesValue%,*}"
    TO_TIME="${timesValue##*,}"
    export FROM_TIME
    export TO_TIME
}

function withinTimeLimits {
    H=$(date +%H)
    if (( $FROM_TIME <= 10#$H && 10#$H < $TO_TIME )); then 
        return 0
    else
        return 1
    fi
}

function isWeekday {
    if [[ $(date +%u) -gt 5 ]] ; then
       return 1
    else
        return 0
    fi
}

function getStillsCount {
    filename=$(ls -v $STILLS_DIRECTORY | tail -1)
    number="${filename%.*}"
    extracted_number=`echo $number|sed -e "s/^0*//g"`
    echo "$extracted_number"
}

export DIRECTORY="pilapse"
export STILLS_DIRECTORY="stills"
export OUT_DIRECTORY="out"
read_times

export current_date=$(date +"%Y-%m-%d")
echo "Date: $current_date"

export ROOT_DIR=$(pwd)
