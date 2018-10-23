FROM andrebriggs/mypythonimage:v1.0.0

RUN mkdir -p /home/site/wwwroot/

COPY . /home/site/wwwroot

RUN cd /home/site/wwwroot && \
    pip install -r requirements.txt

#UN apt-get install zip -y
#RUN zip --symlinks -r /app.zip .
