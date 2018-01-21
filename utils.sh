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