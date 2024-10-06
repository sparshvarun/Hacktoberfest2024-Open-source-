import sys
import random
from pyfiglet import Figlet

# A list of inspirational quotes
QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The best way to predict the future is to invent it. - Alan Kay"
]

def generate_banner(text, font='standard'):
    f = Figlet(font=font)
    return f.renderText(text)

def word_wrap(text, width=70):
    """Wrap text to fit within a certain width."""
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + 1 <= width:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)

    if current_line:
        lines.append(' '.join(current_line))

    return '\n'.join(lines)

def main():
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = random.choice(QUOTES)

    wrapped_text = word_wrap(text)
    banner = generate_banner(wrapped_text.split('\n')[0])  # Use first line for banner
    
    print("\n" + "=" * 80)
    print(banner)
    print(wrapped_text)
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
