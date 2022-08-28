from datetime import datetime, timezone

def show_running():
    print("APScheduler still running at %s",datetime.now(timezone.tzname('Asia/Taipei')).strftime("%Y-%m-%d %H:%M:%S"))