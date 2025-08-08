
# Mira – Flask Chatbot & Mini Game 

Mira is a fun and interactive Flask web application that works as:
- A **chatbot** that responds to emojis and simple text inputs.
- A **mini word game** where you guess the correct word from jumbled letters and matching images.
- A **student-friendly profile page** for a personalized touch.

---

**Live Deployment:** [Click here to view the live app on Render](https://miraa-rypf.onrender.com)
  
---

## Features
- **Emoji Chatbot** – Predefined emoji responses for a friendly, human-like experience.
- **Profile Page** – Displays user info like name, role, email, and progress.
- **Word Game** – Randomly jumbled words with images for users to guess.
- **Home & Login Pages** – Simple navigation and basic login form.

---

## Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Jinja2 Templates
- **Others**: Random module for game logic

---

## Project Structure
```

Mira/
│
├── static/                # Images, CSS, and JS files
│   ├── images/             # Game images
│   └── styles.css
│
├── templates/             # HTML templates
│   ├── home.html
│   ├── login.html
│   ├── profile.html
│   ├── chatbot.html
│   └── game.html
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

````

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/Mira.git
cd Mira
````

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

* Windows:

```bash
venv\Scripts\activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install flask python-dotenv
```

5. **Run the app**

```bash
python app.py
```

Visit: `http://127.0.0.1:5000`

---

## How to Play the Word Game

1. Go to the **Game** page.
2. Look at the image and jumbled letters.
3. Type your guess in the input box.
4. Submit to see if you’re correct!

---

## Screenshots

<img width="1920" height="977" alt="MIRAA" src="https://github.com/user-attachments/assets/1b000e05-4f71-4106-a65a-c7703f81cc10" />
<img width="1920" height="977" alt="LOGIN PAGE" src="https://github.com/user-attachments/assets/e5edee32-aa67-4527-bffd-ad79c188478b" />
<img width="1920" height="977" alt="CHATBOT" src="https://github.com/user-attachments/assets/22ca135c-09e0-43fb-a1d8-6be1b9633da1" />
<img width="1920" height="977" alt="GAME PAGE" src="https://github.com/user-attachments/assets/373241fc-11c4-4247-8f94-7f5b430a37d7" />


---

##  Contributing

Pull requests are welcome! If you want to add features or fix bugs:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a pull request

---

## License

This project is open-source and available under the [MIT License](LICENSE).

```

---

