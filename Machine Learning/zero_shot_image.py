# -*- coding: utf-8 -*-
"""Zero_shot_image.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qoWBOSC0GFWrv2JRJSvDvaKqpD4ok1xR
"""

# !pip install git+https://github.com/PrithivirajDamodaran/ZSIC.git

from ZSIC import ZeroShotImageClassification

zsic = ZeroShotImageClassification()


#Predictions
# preds = zsic(image="http://images.cocodataset.org/val2017/000000039769.jpg",
#             candidate_labels=["birds", "lions", "cats","dogs"],
#             )
# print(preds)

# #Predictions
# preds = zsic(image="https://imgcdn.shortlyst.com/ondc?u=https%3A%2F%2Fcdn.shopify.com%2Fs%2Ffiles%2F1%2F0661%2F9732%2F4035%2Fproducts%2FSoulflower-Coffee-Soap.jpg%3Fv%3D1685470435",
#             candidate_labels=["birds", "lions", "cats","dogs", "sauce", "soap"],
#             )
# print(preds)

def zero_shot_image(img, labels):
  preds = zsic(
      image = img,
      candidate_labels = labels
      )
  print(preds)
  return preds

# image = "https://images.heb.com/is/image/HEBGrocery/000970730"
# labels=["birds", "lions", "cats","dogs", "sauce", "tea", "coffee", "drink"]

# zero_shot_image(image, labels)
