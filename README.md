# MoodSync Notifier

A tiny Python utility that sends a desktop notification with a random uplifting quote every hour (or a custom interval). Great for keeping the mood high while you code.

## Features

- Runs in the background.
- Works on macOS, Linux (with `notify-send`), and Windows (with `win10toast`).
- Customizable interval via a command‑line argument.

## Installation

```bash
pip install -r requirements.txt  # only needed on Windows for win10toast
``` 

*(On macOS and most Linux distros the notification tools are built‑in.)*

## Usage

```bash
python mood_sync.py                # default: every 3600 seconds (1 hour)
python mood_sync.py -i 600         # every 10 minutes
```

## How it works

The script picks a random quote from a short list and calls the appropriate system command to display a notification.

## License

MIT (see the LICENSE file if you add one).
