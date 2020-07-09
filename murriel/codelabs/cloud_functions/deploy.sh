# Main Lab Commands
gcloud functions deploy hello_world --runtime python37 --trigger-http --allow-unauthenticated 

curl https://us-central1-decisive-plasma-260907.cloudfunctions.net/hello_world

gcloud functions deploy hello_name --runtime python37 --trigger-http --allow-unauthenticated

# Note - each function is deployed individually..... not all functions in the code. 
# TODO: read up on this more later! 
 
gcloud functions deploy get_cat --runtime python37 --trigger-http --allow-unauthenticated