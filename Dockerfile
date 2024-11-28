# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 8000

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app 
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
#