import keyboard
import datetime

log_file = 'key_log.txt'

print("This program logs your keystrokes for legitimate purposes only. By continuing, you consent to the logging of your keystrokes.")
user_input = input("Do you consent to the logging of your keystrokes? (y/n)")

if user_input.lower() != 'y':
    exit()

def on_press(event):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as f:
        f.write(f'{timestamp} - {event.name}\n')

keyboard.on_press(on_press)

keyboard.wait()
