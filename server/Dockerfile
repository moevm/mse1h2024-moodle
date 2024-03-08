FROM python:3.12.2-alpine3.19 as builder
COPY ./requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.12.2-alpine3.19
WORKDIR /code
COPY --from=builder /root/.local /root/.local
COPY ./src .
ENV PATH=/root/.local:$PATH

CMD ["python", "-u", "./main.py"]