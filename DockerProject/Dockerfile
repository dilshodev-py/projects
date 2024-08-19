FROM python:3.11-alpine
WORKDIR apps/
COPY . .
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r req.txt
CMD python3 main.py