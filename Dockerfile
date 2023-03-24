FROM python:3.8
EXPOSE 8000  
WORKDIR /app
COPY . /app
RUN apt-get update
RUN pip install -r requirements.txt
RUN python manage.py migrate
ENTRYPOINT ["python"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]