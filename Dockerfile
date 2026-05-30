FROM python
MAINTAINER revathi
LABEL creating an image where python grocerries application should run
WORKDIR Groceryapp/
COPY app.py .
COPY .(all files which is there in our local path) (WorkDIR_image_path)/
RUN pip install -r requirements.txt
