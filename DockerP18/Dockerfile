FROM python:3.11-alpine
WORKDIR app/
COPY . /app
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirement.txt

RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]











