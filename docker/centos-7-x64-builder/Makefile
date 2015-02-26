TAG :=		local/centos-7-x64-suricata-builder
VOLUMES :=	-v $(shell pwd)/../..:/work
VOLUMES +=	-v $(shell pwd)/var/cache/yum:/var/cache/yum

all:

build:
	docker build --rm --tag $(TAG) - < Dockerfile

run:
	docker run --privileged $(VOLUMES) -i -t $(TAG) \
		/bin/bash -c "cd /work && su builder"

start:
	docker start -a -i \
		`docker ps -a | grep $(TAG) | head -n1 | awk '{ print $$1 }'`
