from PIL import Image
import os
from os import listdir

input_dir="Images/"
outptdir='Output_dir/'

for i in os.listdir(input_dir):
 if i != ".DS_Store":
 
    img= Image.open(os.path.join(input_dir, i))
    img=img.rotate(-90).resize((128,128)).convert('RGB')
    img.save(os.path.join(outptdir,i+".RGB"))