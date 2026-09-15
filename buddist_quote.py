import datetime
import smtplib
from email.mime.text import MIMEText
import schedule
import time

# Structured content store with Pāḷi term etymologies and exegetical context
DAILY_WISDOM = [
    {
        "source": "Dhammapada, Verse 2",
        "quote": "If with a pure mind a person speaks or acts, happiness follows them like a never-departing shadow.",
        "term": "Manas (मनाः) & Sukha (सुख)",
        "etymology": (
            "• 'Manas' (Mind/Intellect) comes from PIE *men- ('to think').\n"
            "• 'Sukha' (Happiness) derives from 'su-' (good, ease) + 'kha' (axle-hole of a chariot).\n"
            "  Literally translates to 'a smooth-running wheel or axle.'"
        ),
        "exegesis": (
            "Exegesis: Early Buddhist philosophy places intention (Cetanā) as the primary motor of Karma. "
            "The metaphor of 'sukha' implies that mental cultivation aligns life so it runs smoothly, "
            "mirroring how an axle hole free of friction produces effortlessly stable motion."
        )
    },
    {
        "source": "Samyutta Nikaya 22.86",
        "quote": "Both formerly and now, it is only suffering that I describe, and the cessation of suffering.",
        "term": "Dukkha (दुक्ख)",
        "etymology": (
            "• 'Dukkha' (Suffering/Unsatisfactoriness) derives from 'du-' (bad, ill) + 'kha' (axle-hole).\n"
            "  Literally translates to 'an off-center, grinding axle'."
        ),
        "exegesis": (
            "Exegesis: 'Dukkha' is often oversimplified as 'pain,' but its root refers to structural friction. "
            "The Buddha's teaching targets the impermanence (Anicca) inherent in conditioned reality, which "
            "inevitably grinds against our desire for permanent stability."
        )
    }
]

def format_message(entry):
    return f"""
==================================================
BUDDHIST QUOTE & ETYMOLOGICAL EXEGESIS
==================================================

Source: {entry['source']}

"{entry['quote']}"

--------------------------------------------------
KEY TERM ETYMOLOGY:
{entry['term']}

{entry['etymology']}

--------------------------------------------------
EXEGETICAL COMMENTARY:
{entry['exegesis']}
==================================================
"""

def send_daily_quote():
    # Pick entry based on day index
    day_index = datetime.date.today().timetuple().tm_yday % len(DAILY_WISDOM)
    content = DAILY_WISDOM[day_index]
    message_body = format_message(content)

    print("--- Sending Daily Insight ---")
    print(message_body)

    # --- Optional Email Integration ---
    # SENDER_EMAIL = "your_email@gmail.com"
    # RECEIVER_EMAIL = "target_email@gmail.com"
    # APP_PASSWORD = "your_app_password"
    #
    # msg = MIMEText(message_body)
    # msg['Subject'] = f"Daily Buddhist Wisdom & Etymology - {datetime.date.today()}"
    # msg['From'] = SENDER_EMAIL
    # msg['To'] = RECEIVER_EMAIL
    #
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    #     server.login(SENDER_EMAIL, APP_PASSWORD)
    #     server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

# Schedule to run every day at 08:00 AM
schedule.every().day.at("08:00").do(send_daily_quote)

if __name__ == "__main__":
    print("Scheduler running. Press Ctrl+C to exit.")
    # Run once immediately on startup
    send_daily_quote()
    
    while True:
        schedule.run_pending()
        time.sleep(60)
