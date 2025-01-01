FROM python:3.9.19-slim
RUN pip install streamlit
RUN mkdir /abhilashrepo
COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "Etl.py"]