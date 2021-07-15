# Base image including R/Shiny
FROM rocker/shiny:4.1.0

# Add additional packages to enable debugging and monitoring
RUN apt-get update \
    && apt-get install --yes --no-install-recommends openssh-server curl vim less \
    && apt-get clean

# Set the root password to a standard value, to enable SSH from Azure
RUN echo "root:Docker!" | chpasswd

# Copy setup files for SSH
COPY sshd_config /etc/ssh/sshd_config
COPY run-sshd.sh /etc/services.d/sshd/run

# Expose SSH and Shiny ports
EXPOSE 2222 3838
