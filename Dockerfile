FROM python:3.9

WORKDIR /app

COPY dependencies.txt .

RUN pip install --no-cache-dir -r dependencies.txt

COPY . .

EXPOSE 5000


CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]