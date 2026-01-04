FROM ollama/ollama

WORKDIR /app

# Sistem + Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Python bağımlılıkları
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Backend
COPY backend ./backend
COPY start.sh .

RUN chmod +x start.sh

# Modeli önceden indir
RUN ollama pull llama3

EXPOSE 8000
EXPOSE 11434

CMD ["bash", "start.sh"]
