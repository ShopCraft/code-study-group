# Code Snippets from the Python Vision API Codelab here: 
# https://codelabs.developers.google.com/codelabs/cloud-vision-api-python/index.html?index=..%2F..index#4

export PROJECT_ID=$(gcloud config get-value core/project)
gcloud iam service-accounts create vision-api-sa --display-name "CodeLabs Vision API Service Account"
gcloud iam service-accounts keys create auth/key.json --iam-account vision-api-sa@${PROJECT_ID}.iam.gserviceaccount.com
pip3 install -U pip google-cloud-vision
python3 -c "import google.cloud.vision"

