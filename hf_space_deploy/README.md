---
title: Blood Work Analyzer
emoji: 🩺
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: "1.57.0"
app_file: app.py
pinned: false
---

# Blood Work Analyzer

A Streamlit-based blood work analysis app that uses Anthropic to extract lab test values from blood reports and generate a health summary plus an Indian diet recommendation.

## Features

- Upload or paste a blood report
- Extract test values and classify them as HIGH, LOW, or NORMAL
- Generate a concise health summary
- Produce a practical Indian diet plan
- Built with Anthropic via `langchain_anthropic`

## Configuration

This Space requires an `ANTHROPIC_API_KEY` secret, set under Settings → Variables and secrets.
