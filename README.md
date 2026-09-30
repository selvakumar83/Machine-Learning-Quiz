# Bank-Exam-Style Memory Management Test

## Features

- 10 scenario-based MCQs
- 10-minute examination
- Bank-exam-style question palette
- One question at a time
- Previous / Save & Next
- Answered / Not Answered status
- Submit confirmation
- No score during the examination
- Score displayed only after submission
- Automatic result storage
- SRN + Section + Name
- Submission timestamp
- Timeout status
- Faculty/Admin result dashboard
- CSV download
- Supabase persistent database
- No streamlit-autorefresh dependency

## Run on Windows

Open Command Prompt:

```cmd
cd "C:\Users\ASUS\Desktop\New folder\bank_style_memory_test"
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Then open:

http://localhost:8501

## Supabase

Create a Supabase project.

Open SQL Editor and run:

`supabase_schema.sql`

## Streamlit Secrets

In Streamlit Community Cloud:

App -> Settings -> Secrets

Add:

```toml
SUPABASE_URL = "https://YOUR-PROJECT.supabase.co"
SUPABASE_KEY = "YOUR_SERVER_SIDE_KEY"
ADMIN_PASSWORD = "YOUR_ADMIN_PASSWORD"
```

Do NOT upload these secrets to GitHub.

## GitHub files

Upload:

- app.py
- requirements.txt
- supabase_schema.sql
- README.md

## Important

The application uses browser-side countdown display. The server still calculates the result only when the exam is submitted.

A normal web application cannot completely prevent students from using another device, screenshots, or external resources. For high-stakes exams, additional proctoring controls are required.


## Updated Timer
The exam timer is displayed in **HH:MM:SS** format and starts only when the student clicks **START EXAM**. The timer is enforced using the recorded server-side start time and the exam is automatically submitted when the 10-minute duration expires.


## Timer
The exam timer is a true Streamlit server-side countdown and refreshes every second in HH:MM:SS format. It starts only after START EXAM and automatically submits when the time reaches 00:00:00.

Install dependencies with `python -m pip install -r requirements.txt`.
