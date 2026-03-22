# Use a lightweight Python image
FROM python:3.9-slim

# Set the directory where our app will live inside the container
WORKDIR /app

# Copy the requirements file first (this helps with build caching)
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all our code (app.py and test_app.py) into the container
COPY . .

# Tell Docker that the app listens on port 5000
EXPOSE 5000

# The command to start our Flask app
CMD ["python", "app.py"]