docker run --detach \
	--restart=always \
	--volume flask-sample-app-volume:/data \
	--publish 9001:5000 \
	--name flask_sample_app \
	flask-sample-app