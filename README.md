# agentic-ai-crash-course

A Streamlit-based blood work analysis app that uses Anthropic to extract lab test values from blood reports and generate a health summary plus an Indian diet recommendation.

## Features

- Upload or paste a blood report
- Extract test values and classify them as HIGH, LOW, or NORMAL
- Generate a concise health summary
- Produce a practical Indian diet plan
- Built with Anthropic via `langchain_anthropic`

## Setup

1. Create a Python virtual environment in the project root:

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```powershell
   uv sync
   ```

3. Create a `.env` file in the project root with your Anthropic API key:

   ```ini
   ANTHROPIC_API_KEY=your_api_key_here
   ```

4. Make sure `.env` is ignored in Git. The project already includes `.env` in `.gitignore`.

## Run the app

From the project root:

```powershell
cd 2_heath_analysis\streamlit_app
streamlit run app.py
```

Then open the local URL shown in the terminal.

## GitHub Push Instructions

1. Confirm `.env` is ignored:

   ```powershell
   git status
   ```

   If `.env` is listed, remove it from tracking:

   ```powershell
   git rm --cached .env
   ```

2. Initialize Git if needed:

   ```powershell
   git init
   ```

3. Add files and commit:

   ```powershell
   git add .
   git commit -m "Initial project commit"
   ```

4. Add your GitHub remote and push:

   ```powershell
   git remote add origin https://github.com/your-username/your-repo.git
   git branch -M main
   git push -u origin main
   ```

## Notes

- Do not commit `.env` because it contains your private Anthropic API key.
- Keep `.gitignore` updated for local artifacts such as `.venv/`, `__pycache__/`, and `*.pyc`.
