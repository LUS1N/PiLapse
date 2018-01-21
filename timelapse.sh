#!/bin/bash

cd ~

source utils.sh

DIRECTORY="pilapse"
STILLS_DIRECTORY="stills"
OUT_DIRECTORY="out"

upsert_dir "$DIRECTORY"

cd $DIRECTORY

current_date=$(date +"%Y-%m-%d")

echo "Date: $current_date"

upsert_dir "$STILLS_DIRECTORY"

echo "Starting taking pictures"

./take_pictures.py $TO_TIME $STILLS_DIRECTORY -p 1

echo "Taking pictures complete"

upsert_dir "$OUT_DIRECTORY"

echo "Rendering video"

avconv -r 25 -i "$STILLS_DIRECTORY"/%06d.png -vcodec libx264 -vf scale=1920:1080 "$OUT_DIRECTORY"/"$current_date".h264

echo "Rendering complete. Starting youtube upload".

python google_upload.py PiLapse "$OUT_DIRECTORY/$current_date.h264" "$current_date" "Timelapse in Risskov, Aarhus on $current_date" --tags Timelapse, Denmark, Aarhus, Construction

echo Drive and Youtube upload complete. Deleting "$STILLS_DIRECTORY" and "$OUT_DIRECTORY".

delete_dir "$STILLS_DIRECTORY"
delete_dir "$OUT_DIRECTORY"

echo Emptying trash

trash-empty

echo Trash emptied.
