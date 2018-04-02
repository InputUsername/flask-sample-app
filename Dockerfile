FROM python:3.6

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP app.py
ENV DATABASE_URL sqlite:///flask_app.db

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]