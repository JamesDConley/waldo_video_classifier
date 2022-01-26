parentdir=$(dirname `pwd`)
uid=$(id -u ${USER})
gid=$(id -g ${USER})
# Include --no-cache if needing to rebuild for a test
docker build -t "waldo" .

docker run --gpus all -it --rm --name waldo  -p 8862:8862 -v $parentdir:/module waldo /bin/bash