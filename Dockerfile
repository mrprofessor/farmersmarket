FROM python:3.7

RUN mkdir farmersmarket

COPY . /farmersmarket/

WORKDIR /farmersmarket

RUN chmod +x entrypoint.sh

# Install the Python libraries
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir -r requirements-dev.txt

RUN pip3 install --editable .

CMD ["bash", "entrypoint.sh"]
