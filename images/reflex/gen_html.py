from os import listdir
from os.path import isfile, join

files = [f for f in listdir(".") if f.endswith(".jpg")]
print(files)

counter = 0

with open('html.txt', 'w') as writer:
    for ff in files:
        html = f"<a href=\"images/reflex/{ff}\" data-lightbox=\"mygallery\" data-title=\"...\"><img src=\"images/reflex/resized/{ff[:-4]}.resized.jpg\" width=\"300\" height=\"300\"></a>\n"
        
        writer.write(html)
        
        counter += 1
        if counter % 3 == 0:
            writer.write('\n')

