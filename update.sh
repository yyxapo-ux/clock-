#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "🕰️ Updating Clock..."

git add .

git commit -m "Update Clock bot" || {
    echo "ℹ️ Nothing new to commit."
}

git push origin main

echo "✅ Clock updated successfully!"
