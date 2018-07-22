#IVDM3Seg Challenge - MICCAI 2018 
## https://ivdm3seg.weebly.com/

Example docker containers for the IVD Segmentation Challenge. These example scripts simply threshold the /fat.nii.gz image at 20, but can be used to see how applications can be containerized and run within the challenge.

## Python example
A detailed description of the Python example is provided here: https://ivdm3seg.weebly.com/methods.html. 

In order to run matlab scripts in a container, the script has to be compiled with the matlab compiler. Within the container, we install the corresponding matlab runtime to execute the compiled script.

## Docker commands
Containers submitted to the challenge will be run with the following commands:

```
CONTAINERID=`docker run -dit -v [TEST-DIR]:/input:ro -v /output ivdm3seg/[TEAM-NAME]`
docker exec $CONTAINERID [YOUR-COMMAND]
docker cp $CONTAINERID:/output [RESULT-TEAM]
docker stop $CONTAINERID
docker rm -v $CONTAINERID
```
