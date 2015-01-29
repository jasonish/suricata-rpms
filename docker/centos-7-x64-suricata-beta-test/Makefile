TAG :=		local/centos-7-x64-suricata-beta-test
VOLUMES :=	-v $(shell pwd)/../..:/work

all:

build:
	docker build --rm --tag $(TAG) .

run:
	docker run $(VOLUMES) -i -t $(TAG) /bin/bash

start:
	docker start -a -i \
		`docker ps -a | grep $(TAG) | head -n1 | awk '{ print $$1 }'`
