FROM gitpod/workspace-base
RUN sudo apt update
RUN sudo apt install python3-pip
USER gitpod
