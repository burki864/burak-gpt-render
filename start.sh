#!/usr/bin/env bash

echo "🧠 Ollama başlatılıyor..."
ollama serve &

sleep 3

echo "🚀 BurakGPT API ayağa kalkıyor..."
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
