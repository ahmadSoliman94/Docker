
### To create files in Linux
```
sudo nano file_name
```

>__NOTE:__ after i run the following command:
``` 
sudo docker run -it image_name
```

### I will not get the output of the container, because the container will run in the background, so to get the output of the container, i need to run  the following command:
```
sudo docker run -v /home/ahmed/Desktop/Docker_test:/home/ahmed/Desktop/Docker_test image_name # -v is used to mount the volume, the first path is the path of the host machine, and the second path is the path where you want to for example save the output of the container.
```
