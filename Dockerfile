FROM python:3.6-slim
WORKDIR = /
COPY load_model.py .
COPY model.pkl .
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "app.py"]