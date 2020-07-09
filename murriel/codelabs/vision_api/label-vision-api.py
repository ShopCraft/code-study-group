from google.cloud import vision

imagelist=[
    "gs://murriel-generic-bucket/codelabs/labels/cat02.jpeg",
    "gs://cloud-samples-data/vision/using_curl/shanghai.jpeg",
    "gs://murriel-generic-bucket/longbeach.jpg",
    "gs://cloud-samples-data/vision/label/setagaya.jpeg",
    "https://www.dw.com/image/42582511_401.jpg"
]
for i in imagelist:
  print(i)

# TODO: Get from bucket and add to array 
# use Python API 

image_uri = imagelist[0]
print(image_uri)
# value = input("Please enter a string:\n")
# print(f'You entered {value}')

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = image_uri

response = client.label_detection(image=image)

print('Labels (and confidence score):')
print('=' * 79)
for label in response.label_annotations:
    print(f'{label.description} ({label.score*100.:.2f}%)')