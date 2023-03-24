FROM gitpod/workspace-base
RUN sudo apt update
RUN sudo apt -y install python3-pip
USER gitpod
RUN pip install pandas
RUN pip install seaborn
RUN pip install 
RUN pip install sklearn.cluster