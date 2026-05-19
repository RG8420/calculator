#!/bin/bash
# push.sh - Push calculator to GitHub
# Run this from the calculator directory

echo "Pushing to GitHub..."

cd "$(dirname "$0")"

# Add remote if not already added
git remote add origin https://github.com/RG8420/calculator.git 2>/dev/null || true

# Push
git push -u origin main

echo "Done!"