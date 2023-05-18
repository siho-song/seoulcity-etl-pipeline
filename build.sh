IMAGE_NAME=gkdldhdl/spark
IMAGE_TAG=0.04

IMAGE_NAME_TAG=$IMAGE_NAME:$IMAGE_TAG

docker build -f ./Dockerfile -t $IMAGE_NAME_TAG .