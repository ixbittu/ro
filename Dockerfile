FROM nikolaik/python-nodejs:python3.11-nodejs19

# Fix Debian archive + install system deps
RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i '/security.debian.org/d' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        ffmpeg \
        aria2 \
        build-essential \
        libssl-dev \
        rustc \
        cargo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app/

# Pip upgrade
RUN python -m pip install --no-cache-dir --upgrade pip setuptools wheel

# 🔥 CRITICAL FIX (Rust panic avoid)
RUN pip uninstall -y cryptography pymongo motor || true

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

CMD bash start