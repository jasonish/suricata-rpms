TAG :=		local/centos-7-x64-suricata-builder
VOLUMES :=	-v $(shell pwd)/../..:/work
VOLUMES +=	-v $(shell pwd)/var/cache:/var/cache

all:

build:
	docker build --rm --tag $(TAG) - < Dockerfile

run:
	docker run --privileged $(VOLUMES) -i -t $(TAG) \
		/bin/bash -c "cd /work && su builder"
