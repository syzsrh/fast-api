FROM python:3.10
WORKDIR /fast-api
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["fastapi", "run", "app/main.py", "--port", "8080"]
