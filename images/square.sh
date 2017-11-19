ls *.png | xargs -I _ convert _ -trim +repage _
ls *.png | xargs -I _ convert _ \( +clone -rotate 90 +clone -mosaic +level-colors grey -transparent grey \)       +swap -gravity center -composite  _