echo "taking pics start at $stills_start"

stills_start="$1"
echo "Starting taking pictures"
python ./take_pictures.py $TO_TIME $STILLS_DIRECTORY -p "$stills_start" -a
echo "Taking pictures complete"