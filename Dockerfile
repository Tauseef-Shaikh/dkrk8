FROM python:3.8
WORKDIR /src
COPY requirements.txt .
ENV PYTHONUNBUFFERED=1
RUN pip install -r requirements.txt
COPY /src/dkr_k8s.py .
CMD [ "python", "./dkr_k8s.py" ] 