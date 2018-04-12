FROM python:3.6

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_DEBUG 1
ENV FLASK_APP app.py
ENV DATABASE_URL sqlite:///data/flask_app.db
ENV DASHBOARD_DATABASE_URL sqlite:///data/flask_monitoringdashboard.db

EXPOSE 9001

CMD ["flask", "run", "--host=0.0.0.0", "--port=9001"]
