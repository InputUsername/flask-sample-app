docker run --detach \
	--rm \
	--volume flask-sample-app-volume:/data \
	--publish 9001:9001 \
	--name flask_sample_app \
	flask-sample-app
