from google.cloud import vision

imagelist=[
    "gs://cloud-vision-codelab/eiffel_tower.jpg"
]

for i in imagelist:
  print(i)

image_uri = imagelist[0]
print(image_uri)

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = image_uri

response = client.landmark_detection(image=image)

for landmark in response.landmark_annotations:
    print('=' * 79)
    print(landmark)