echo "taking pics start at $stills_start"

stills_start="$1"
upsert_dir "$STILLS_DIRECTORY"
echo "Starting taking pictures"
./take_pictures.py $TO_TIME $STILLS_DIRECTORY -p "$stills_start"
echo "Taking pictures complete"