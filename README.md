# TEF Spot Notifier 🔔

A Python-based website monitor built to reduce the need to repeatedly check for exam registration openings. It checks a registration page for availability changes and sends an email notification when a spot becomes available.

## Why I built it

A family member kept missing exam registration openings because available spots could appear unexpectedly. I wanted to make the process less manual by building a monitor that could check the page regularly and send a notification when the relevant status changed.

## Features

- **Automated availability monitoring:** Checks the target registration page for openings.
- **Email notifications:** Sends alerts using Gmail SMTP when an opening is detected.
- **Reliability improvements:** Accounts for failed requests, page-content changes, and false alerts.
- **Scheduled execution:** Uses GitHub Actions to run without manual checks.

## Tech stack

- **Python** — monitoring and notification logic
- **Requests** — fetching page content
- **BeautifulSoup4** — parsing HTML
- **Gmail SMTP** — email notifications
- **GitHub Actions** — recurring execution
- **HTML/CSS** — supporting web interface files in the repository

## How it works

```text
Scheduled GitHub Actions run
            |
            v
    Request registration page
            |
            v
   Parse page for availability
            |
            v
    Determine whether a spot
         is available
            |
         If yes
            v
     Send an email alert
```

The monitoring logic also includes handling for failed requests and unexpected page changes to reduce unreliable results.

## Project structure

```text
tef_spot_notifier/
├── .github/workflows/     # Automated workflow configuration
├── index.html             # Supporting web page
├── style.css              # Web page styling
├── requirements.txt       # Python dependencies
└── tef-Notifier.py        # Python monitoring script
```

## Running locally

The exact setup depends on the configuration used by `tef-Notifier.py`. Before publishing or running the project, review the script for its required configuration and environment variables.

1. Clone the repository.
2. Create a Python virtual environment and activate it.
3. Install the listed dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Configure the target site and email credentials **without committing secrets**.
5. Run the Python script after confirming its configuration:

   ```bash
   python tef-Notifier.py
   ```

> **Security:** Never commit SMTP passwords, app passwords, access tokens, or personal email credentials. For GitHub Actions, store secrets in repository **Settings → Secrets and variables → Actions** and reference them through the workflow. Check the entire Git history before making this repository public.

## What I learned

This project helped me work through the difference between a script that works once and an automation that can run repeatedly. I practiced HTML parsing, troubleshooting changing page content, handling failed requests, reducing false alerts, and setting up scheduled execution with GitHub Actions.

## Author

**Ansh Taparia** — Computer Science, University of British Columbia  
[GitHub](https://github.com/anshtaparia20689) · [LinkedIn](https://www.linkedin.com/in/ansh-taparia-719900247)

---

*This project is an independent utility and is not affiliated with the exam registration provider.*
