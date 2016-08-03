FROM briefy/python3
MAINTAINER RideLink <developers@ridelink.com>

# Add ssh key for read-only access on Github
ADD ./docker/id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa && \
    echo "    IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config && \
    echo "Host github.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config

# Add docker_entrypoint file
ADD ./docker/docker_entrypoint.sh /docker_entrypoint.sh
RUN chmod +x /docker_entrypoint.sh

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["/docker_entrypoint.sh"]

EXPOSE 8000