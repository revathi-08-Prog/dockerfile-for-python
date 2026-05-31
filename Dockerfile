FROM python:slim
MAINTAINER "revathi"
LABEL app="pythonapp" description="image of grocerries"
WORKDIR /Grocery
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 123
CMD ["python" , "app.py"]
