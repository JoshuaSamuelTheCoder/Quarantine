#!/usr/bin/env bash
docker run --user nobody -di --name my-container busybox
docker exec -i my-container whoami
exit 0
