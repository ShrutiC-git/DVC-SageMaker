FROM python:3.6-slim
WORKDIR = deploy/
COPY load_model.py .
COPY model.pkl .
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "app.py"]