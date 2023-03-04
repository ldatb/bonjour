FROM python:3.8

RUN pip3 install Flask

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]
