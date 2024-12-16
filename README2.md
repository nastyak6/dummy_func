Set the environment variables SAMBA_USER and SAMBA_PASS on the host from which you run Docker Compose, or include them in an .env file that Docker Compose automatically reads when you run docker-compose up.

sudo apt install smbclient
run this command to get the contianer's IP:
docker inspect -f '{% raw %}{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}{% endraw %}' <container_name>
smbclient -U admin //<container_ip>/shared
