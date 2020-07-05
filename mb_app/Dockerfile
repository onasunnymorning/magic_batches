FROM python:3.8.3-alpine
# Keeping this high up for now to save my local bandwidth, it may make more sense to move it down later?
COPY ./requirements.txt /app/requirements.txt
WORKDIR app
RUN pip install -r requirements.txt
RUN apk update && apk add bash
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]