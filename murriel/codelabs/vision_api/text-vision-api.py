from google.cloud import vision 

imagelist=[
    "gs://cloud-vision-codelab/otter_crossing.jpg",
    "gs://murriel-generic-bucket/sharpedges.jpeg",
    "gs://murriel-generic-bucket/chainsaw.jpeg",
    "https://thumb1.zeppy.io/d/l400/pict/290103661246/-no-soliciting-warning-sign-metal-heavy-duty"
]

image_uri = imagelist[1]
print(image_uri)
# TODO Add Error Checking 


client = vision.ImageAnnotatorClient()
image = vision.types.Image() 
image.source.image_uri = image_uri 

response = client.text_detection(image=image)

for text in response.text_annotations:
    print('=' * 79)
    print(f'"{text.description}"')
    vertices = [f'({v.x},{v.y})' for v in text.bounding_poly.vertices]
    print(f'bounds: {",".join(vertices)}')