import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):
  im = Image.fromarray(X)
  im1 = im.resize(resize)
  plt.figure()
  plt.imshow(im1)
  plt.show()
  return 0

@interact(X=fixed('Image') , resize =widgets.IntSlider(min=10, max=1250))
