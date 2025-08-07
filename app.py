from flask import Flask, render_template, request, redirect, url_for, session, jsonify

import random

import os

app = Flask(__name__)
app.secret_key = "your_secret_key_here"


WORDS = [
    'apple.jpg',
    'elephant.jpg',
    'aeroplane.jpg',
    'cap.avif',
    'peach.png',
    'beach.webp',
    'giraffe.avif',
    'horse.avif',
    'kite.avif',
    'pumpkin.jpg'
]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('profile'))
    return render_template('login.html')

@app.route('/profile')
def profile():
    user_data = {
        'name': 'Jane Doe',
        'role': 'Student',
        'email': 'jane@example.com',
        'progress': '70%'
    }
    return render_template('profile.html', user=user_data)



@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    if 'messages' not in session:
        session['messages'] = []

    if request.method == "POST":
        user_input = request.form["user_input"]
        session['messages'].append({"sender": "You", "text": user_input})

        emoji_responses = {
            "😊": "I'm happy to see your smile!",
            "😢": "I'm here for you. Want to talk about it?",
            "❤️": "Sending love and support your way ❤️",
            "🍎": "Yummy! Apples are healthy and sweet.",
            "🍌": "Bananas give you energy! 🍌",
            "🍇": "Grapes are great! Are you having some fruit?",
            "🐶": "Dogs are lovely friends! 🐾 Do you like dogs?",
            "🐱": "Meow~ Cats are cute and cuddly 🐱",
            "🐘": "Wow! Elephants are wise and strong. 🐘",
            "✍️": "Do you want to write something? I'm here to help.",
            "👍": "Awesome! Keep going, you're doing great! 👍",
            "😎": "Looking cool! 😎 What would you like to do today?",
            "😴": "Feeling sleepy? Don’t forget to rest well. 😴",
            "🌈": "Rainbows are beautiful, just like your thoughts 🌈",
            "🚀": "To the stars! You can achieve anything 🚀"
        }

        # Text responses for simple words
        text_responses = {
            "hi": "Hello! 👋 How can I help you today?",
            "hello": "Hi there! 😊",
            "help": "I'm here to help. You can talk to me or use emojis too!",
            "thanks": "You're welcome! 💖",
            "bye": "Goodbye! Hope to see you again soon 👋",
        }

        cleaned_input = user_input.lower().strip()
        reply = emoji_responses.get(user_input.strip()) or text_responses.get(cleaned_input) or "Tell me more 😊 You can use words or emojis!"

        session['messages'].append({"sender": "Mira", "text": reply})

    return render_template("chatbot.html", messages=session['messages'])

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        user_input = request.form.get('user_input', '').strip().lower()
        correct_word = request.form.get('correct_word', '').strip().lower()
        
        if user_input == correct_word:
            message = '✅ Correct!'
        else:
            message = f'❌ Wrong! The correct word was \"{correct_word}\"'
        
        return render_template(
            'game.html',
            message=message,
            image_filename=request.form.get('image_filename'),
            jumbled_word=request.form.get('jumbled_word'),
            correct_word=correct_word
        )

    # GET request: new round
    image_filename = random.choice(WORDS)
    correct_word = os.path.splitext(image_filename)[0].lower()
    jumbled_word = ''.join(random.sample(correct_word, len(correct_word)))

    return render_template('game.html', image_filename=image_filename, jumbled_word=jumbled_word, correct_word=correct_word)

# ----------------- RUN APP -----------------
if __name__ == '__main__':
    app.run(debug=True)
