import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

@interact(X=fixed('Image') , resize = 10 )

def imshow(X, resize=None):
  im = Image.fromarray(X)
  im1 = im.resize((resize, resize))
  plt.figure()
  plt.imshow(im1)
  plt.show()
  return 0


