for f in `find . -name "*.jpg"`
do
    ff="${f%.jpg}"
    convert $f -resize 20% ./resized/$ff.resized.jpg
    echo $f
done
