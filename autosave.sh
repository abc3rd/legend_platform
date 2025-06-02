#!/bin/bash

cd "$(dirname "$0")"

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

echo "🔄 Auto-saving project at $timestamp..."

# Skip pushing temp/log/secret files
echo -e "\n# Auto-ignored files\n.env\n*.log\n__pycache__/" >> .gitignore

git add .
git commit -m "💾 Auto-backup: $timestamp"
git push origin main

echo "✅ Backup complete at $timestamp"
