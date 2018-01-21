echo "cleaning up"

delete_dir "$STILLS_DIRECTORY"
delete_dir "$OUT_DIRECTORY"

echo Emptying trash

trash-empty

echo Trash emptied.


upsert_dir "$OUT_DIRECTORY"
upsert_dir "$STILLS_DIRECTORY"


