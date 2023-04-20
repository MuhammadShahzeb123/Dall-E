import openai
import requests as r
import os

openai.api_key = "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"

Files = os.listdir()
images = [item for item in Files if item.endswith('.png')]

for image in images:
  response = openai.Image.create_variation(
    image=open(image, "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']

  Similar_image = r.get(image_url)

  with open(f"{image[:-4]}_Similar.png", 'wb') as f:
      f.write(Similar_image.content)