#!/bin/bash

# Run at startup
cd ~/PiLapse

# reads all required env variables and functions
source bash-scripts/utils.sh

# check if slides exists and are not empty
if [ "$(ls -A $STILLS_DIRECTORY)" ]; then
    echo "$STILLS_DIRECTORY not empty."
    # if within time limits
    if withinTimeLimits; then
        # continue where left off
        stills="$(getStillsCount)"
        echo "Within time limits. Continueing from still: $stills"
        source bash-scripts/take_pictures.sh "$stills"
        source bash-scripts/render.sh
        source bash-scripts/upload.sh
    else 
        echo "Outside of time limits, make and upload video from current amount of slides"
        source bash-scripts/render.sh
        source bash-scripts/upload.sh
    fi
# if empty:
else
    echo "No stills in the folder"
    # if withing time and weekday limits
    if withinTimeLimits && isWeekday ; then
        echo starting new timelapse process
        source . timelapse.sh
    else # weekend or outside of filming hours
        echo No action, closing.
        exit
    fi
fi

