#!/bin/bash
cd ~/PiLapse
source bash-scripts/utils.sh
source bash-scripts/cleanup.sh

source bash-scripts/take_pictures.sh 1
source bash-scripts/render.sh
source bash-scripts/upload.sh