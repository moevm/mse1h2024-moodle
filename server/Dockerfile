FROM python:3.12.2-alpine3.19
COPY ./requirements.txt .
RUN pip install --user -r requirements.txt
COPY . ./
CMD ["python", "-u", "main.py"]