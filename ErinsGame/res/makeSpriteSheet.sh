mkdir frames
convert -coalesce $1.gif frames/*.png
montage -background transparent -tile 4x ./frames/*.png $1.png
rm -rf frames

