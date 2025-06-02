#!/bin/bash

echo "🔁 Starting Legenie Dev Stack..."

# Start FastAPI backend
echo "🚀 Launching FastAPI..."
cd "$(dirname "$0")/backend"
source gptsqlenv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Start React frontend
echo "🎨 Launching Frontend..."
cd ~/legend_platform/frontend/legenie-fullstack-v2 || exit
npm run start &

# Start Ollama (if you're using it)
echo "🧠 Starting Ollama..."
ollama serve &

# Optional: Start Cloudflare Tunnel (if used)
# cloudflared tunnel run your-tunnel-name &

echo "✅ All systems launched."
