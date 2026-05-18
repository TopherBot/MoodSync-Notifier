#!/usr/bin/env python3
import random, time, sys, os

quotes = [
    "Stay positive, work hard, make it happen.",
    "Every day is a new opportunity.",
    "You are capable of amazing things.",
    "Keep going, you're doing great!",
    "Believe you can and you're halfway there."
]

def notify(message):
    if sys.platform.startswith('darwin'):
        # macOS notification via AppleScript
        os.system(f'''osascript -e 'display notification "{message}" with title "MoodSync"' ''')
    elif sys.platform.startswith('linux'):
        # Linux notification via notify-send (must be installed)
        os.system(f'notify-send "MoodSync" "{message}"')
    elif sys.platform.startswith('win'):
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("MoodSync", message, duration=10)
        except Exception as e:
            print("Notification failed:", e)
    else:
        # Fallback: print to console
        print(message)

def main(interval=3600):
    while True:
        quote = random.choice(quotes)
        notify(quote)
        time.sleep(interval)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="MoodSync Notifier")
    parser.add_argument("-i", "--interval", type=int, default=3600,
                        help="Interval in seconds between notifications (default: 3600)")
    args = parser.parse_args()
    main(args.interval)
