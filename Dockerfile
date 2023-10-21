# import python library
FROM python:3.8-slim

# install FLask library
RUN pip install Flask

# Create work directory
WORKDIR /app

# Copy python's file to work directory
COPY api_calc.py .

# Use 5000 port
EXPOSE 5000

# Start program
CMD ["python", "api_calc.py"]

USER 1000
