FROM python:3.11

# Create non-root user and set up environment
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Create and set working directory
RUN mkdir -p /home/user/app
WORKDIR /home/user/app

# Copy and install requirements
COPY --chown=user:user ./requirements.txt /home/user/app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy application code
COPY --chown=user:user . /home/user/app

# Run Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]