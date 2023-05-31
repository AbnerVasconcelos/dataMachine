FROM python:3
WORKDIR /app
COPY . /app
RUN pip install openpyxl pyModbusTCP pandas
RUN ls
RUN pwd
EXPOSE 502
CMD [ "python", "main.py" ]
