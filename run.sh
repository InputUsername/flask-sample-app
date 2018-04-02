docker run --detach \
	--restart=always \
	--volume flask-sample-app-volume:/data \
	--publish 127.0.0.1:9001:5000 \
	--name flask_sample_app \
	flask-sample-app