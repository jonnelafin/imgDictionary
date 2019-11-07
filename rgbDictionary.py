import numpy
import random
#import hashlib
inputD = "have a nice day"
data = numpy.zeros((1, len(inputD), 3), dtype=numpy.uint8)
import time

def jpg_image_to_array(image_path):
  from PIL import Image
  """
  Loads JPEG image into 3D Numpy array of shape 
  (width, height, channels)
  """
  with Image.open(image_path) as image:         
    im_arr = numpy.fromstring(image.tobytes(), dtype=numpy.uint8)
    #im_arr = im_arr.reshape((image.size[1], image.size[0], 3))                                   
  return im_arr

dictionary = []

def initDict():
    for i in range(500):
        dictionary.append([])

def saveDict(prefix = ""):
    with open("dict.txt" + str(prefix), "w+") as f:
      f.write(dictionary)
def toF(name):
  print("Converting from text...")
  print(inputD)
  print("initializing dictionary...")
  initDict()
  print("conversion:")
  for x in range(len(inputD)):
      print(x)
      i = inputD[x]
      print(i)
      value = []
      if dictionary[ord(i)] == []:
          r = random.randint(0, 255)
          b = random.randint(0, 255)
          g = random.randint(0, 255)
          dictionary[ord(i)] = [r, b, g]
      value = dictionary[ord(i)]
      print("Value" + str(value))
      data[0][x] = value
      print("=====")
  print("Converting to image...")
  #data[25, 25] = [255, 0, 0]
  #data[25, 26] = [0, 255, 0]
  #data[25, 27] = [0, 0, 255]

  from PIL import Image

  image = Image.fromarray(data)
  image.save(name, "PNG")
  print("completed!")
def fromF(name):
    print("converting from image...")
for i in range(1):
    toF("conversion"+str(i)+".jpg")
    saveDict()
print("Have a nice day.")
