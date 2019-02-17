from PIL import Image, ImageOps, ImageDraw
from PIL.ExifTags import TAGS
import os
from os import listdir
from os.path import isfile, join

def isImage(file_to_square):
  try: 
    og = Image.open(file_to_square)
    if 'exif' in og.info:
      setup_square(og, file_to_square)
  except OSError:
    print(f"{os.path.basename(file_to_square)}  No EXIF data - skipping")
    return False

def setup_square(og, file_to_square):
  og.show()
  correct = input('Is this is the correct image?')
  if correct is 'n':
    print("Sorry about that, skipping...")
    return False

  if og.width == og.height:
    print("This image is already a square")
    save_cropped_file(og, file_to_square)

  if og.width != og.height:
    orientation = input('Is this image in the correct orientation? ')
    if orientation is 'n':
      rotate_image(og, file_to_square)
    else: 
      make_square(og, file_to_square)

def make_square(og, file_to_square):
  width, height = og.size
  long_side = max(width, height)
  short_side = min(width, height)
  calc_border = int((long_side - short_side) / 2)

  im = Image.new('RGB', (long_side, long_side), (0,0,0))

  full_path = save_drawn_area(im, file_to_square)
  new_image = Image.open(full_path)
  if width < height:
    new_image.paste(og,box=(calc_border, 0, (short_side + calc_border), height ))
    new_image.show()
  else:
    new_image.paste(og,box=(0, calc_border, width, (short_side+ calc_border)))
    new_image.show()
  save_squared_file(new_image, file_to_square, full_path)


def save_drawn_area(im, file_to_square):
  file_path = os.path.dirname(os.path.abspath(file_to_square))
  file_name = 'temp.jpg'
  full_path = file_path + '/' + file_name
  im.save(full_path)
  return full_path

def save_squared_file(new_image, file_to_square, full_path):
  file_path = os.path.dirname(os.path.abspath(file_to_square))
  file_name = os.path.basename(file_to_square)
  os.makedirs(file_path + '/squared', exist_ok=True)
  new_image.save(f'{file_path}/squared/{file_name}')
  print("File save complete. You may need to refresh your directory to see the changes.")

def rotate_image(og, file_to_square):
  dir = input('Does this need to be rotated right, left, or flipped? ') or 'none'
  if dir is 'r' or dir is 'right':
    new_og = og.transpose(Image.ROTATE_270)
  elif dir is  'l' or dir is 'left':
    new_og = og.transpose(Image.ROTATE_90)
  elif dir is 'f' or dir is 'flipped':
    new_og = og.transpose(Image.ROTATE_180)
  else:
    make_square(og, file_to_square)
  new_og.show()
  correct = input('Does this look correct?')
  if correct is 'n':
    rotate_image(og, file_to_square)
  else:
    og = new_og
    make_square(og, file_to_square)

def batch_process(dir_to_suqare):
  only_photos = [f for f in listdir(dir_to_suqare) if isfile(join(dir_to_suqare, f))]
  for photo in only_photos:
    to_square = dir_to_suqare + "/" + photo
    isImage(to_square)
  print("Batch processing is complete")

if __name__ == '__main__':
  batch_or_single = input('Are you processing a -directory- or a -single- file? ') or 'single'
  if batch_or_single is 'directory' or batch_or_single is 'd' or batch_or_single is 'D':
    dir_to_suqare = input('Full directory path: ')
    print("All square files will be skipped.\nAll output files will be added to this directory in the 'squared' subdirectory\n\n\n")
    batch_process(dir_to_suqare)
  else:
    to_square = input('Which photo needs cropping? Include extension: ')
    isImage(to_square)