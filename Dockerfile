# Use a lightweight Python image as the base
FROM python:3.10-slim

# Set environment variables for better logging and no bytecode generation
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Add a non-root user for security
RUN adduser --disabled-password --gecos "" appuser
# Switch to the new user before copying app files
USER appuser

# Copy only the requirements file first to leverage Docker layer caching
COPY --chown=appuser:appuser requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY --chown=appuser:appuser . .

# Expose the port the application will run on
EXPOSE 8000

# Set the command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "appli_ticketing.wsgi"]