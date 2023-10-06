FROM python:3.8-slim

RUN pip install Flask

WORKDIR /app

COPY api_calc.py .

EXPOSE 5000

CMD ["python", "api_calc.py"]

