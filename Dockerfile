FROM public.ecr.aws/lambda/python:3.10

RUN mkdir -p /app
COPY ./main.py /app/
COPY ./requirements.txt /app/requirements.txt
COPY mylib/ /app/mylib/

WORKDIR /app
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "/app/main.py" ]