FROM python:latest
COPY . /paysistem46
WORKDIR /paysistem46
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--reload","---host=0.0.0.0","--port=2525"]