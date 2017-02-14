#!/usr/bin/env bash

#upload k8s images in gcr.io to private registry.

images=`docker images | awk '{print $1}'`
version=`docker images | awk '{print $2}'`
prefix="gcr.io/"
prefixLen=${#prefix}

arrayImages=($images)
arrayVersion=($version)
len=${#arrayImages[@]}

registry="yourRegistry"
docker login -u ${username} -p ${password} -m {email} ${registry}

for((i=1;i<=len;i++));do
    image=${arrayImages[$i]}
    echo $i
    if [[ ${image:0:${prefixLen}} == ${prefix} ]]
    then
        version=${arrayVersion[$i]}
        docker tag ${image}:${version} ${registry}/${image##*${prefix}}:${version}
        docker push ${registry}/${image##*${prefix}}:${version}
    fi
done
