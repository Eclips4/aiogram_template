FROM python:3.8

RUN mkdir -p /usr/src/aiogram_app/
WORKDIR /usr/src/aiogram_app/

COPY . /usr/src/aiogram_app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]