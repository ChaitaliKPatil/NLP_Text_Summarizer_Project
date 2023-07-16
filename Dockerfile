# we built program in Python 3.7 Environment.
FROM python:3.8-slim-buster



# Update apt and also AWS CLI
RUN apt update -y && apt install awscli -y
# create folder"app" where we will copy all the cource code.
WORKDIR /app

COPY . /app


# install requirements.txt which involves the requirements of environments
RUN pip install -r requirements.txt
# following commands we ran in order to avoid updating errors.
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate


# Launch app.py
CMD ["python3", "app.py"]