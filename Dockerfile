FROM python:3.7
MAINTAINER cao
COPY ./demo_20191126 ./demo
WORKDIR /demo
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
