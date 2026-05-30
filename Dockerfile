FROM python
MAINTAINER revathi
LABEL creating an image where python grocerries application should run
WORKDIR Groceryapp/
COPY app.py .
COPY ..
RUN pip install -r requirements.txt
