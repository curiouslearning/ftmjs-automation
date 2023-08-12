gcloud functions deploy hello-world \
	--verbosity=info \
	--gen2 \
	--region=us-central1 \
	--runtime=python310 \
	--source=. \
	--entry-point=hello_http \
	--trigger-http
