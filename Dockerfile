FROM python:3.9

# Create non-root user and set up environment
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Create and set working directory
RUN mkdir /app
WORKDIR /app

# Copy and install requirements
COPY --chown=user:user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy application code
COPY --chown=user:user . /app

# Run Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]