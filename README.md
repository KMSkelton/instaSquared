# instaSquared
Tool to modify an image's canvas so it is square

# Use
instaSquared was built for OSX and Python3. "yes" and 0 are the default values, please `return` your way though the prompts if you don't need to make changes.

Open finder.

Single-click the image or directory that needs to be prepped for Instagram.

`option + CMD + c` (this copies the path and the filename)

In terminal: 

`>>> python3 makeSquare.py`

You will be asked whether you want to process a directory or a single file. Directory can be selected by typing d, D, or directory. The default is a single file. 

`CMD + v` paste the path into the terminal.

If there are files without EXIF data in the directory, instaSquared will notify you and move on to the next file.

instaSquared will ask you to confirm that this is the correct photo. If it is not, instaSquared will apologize and move on.

You will be asked to confirm that this is the photo you'd like to modify each time.

Pillow does odd things with image orientation, typically rotating portrait images to the left. If the photo is not the in the orientation you expect, type n. You'll be asked which direction the image needs to be rotated. The default is 'right'. If you type anything other than r/right, l/left or f/flipped the function will take that to mean you don't need to change the orientation and will move on.


instaSquared calculates the size of the image to figure the dimensions of new canvas square. It creates a new canvas that uses the longest side of the image for all four of its sides.

instaSquared is desgined with bulk image modifying in mind (though a single image can be processed). To that end, there are no decisions that the user can make beyond image rotation. All files are saved to a "squared" directory and have `squared_` prefixed to the original file name. 