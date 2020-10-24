from cv2 import imread,imwrite,flip,imshow
from os import path
#load the image file
filename=' '
#Check if filename exists
if path.isfile(filename):
    image=imread(filename)

    #flip the image
    image=flip(image,1)
    #Store the image
    imwrite(f'py{path.basename(filename)}',image)
else:
    print('No file found')

