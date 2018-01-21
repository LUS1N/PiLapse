echo "Rendering video"
avconv -r 25 -i "$STILLS_DIRECTORY"/%06d.png -vcodec libx264 -vf scale=1920:1080 "$OUT_DIRECTORY"/"$current_date".h264
echo "Rendering complete.".


