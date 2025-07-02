# Recovery AI

A web app that analyzes user symptoms using an AI backend and displays possible conditions and medications with a modern glassmorphism UI and animated star background.

## Features

- **AI-powered symptom analysis** (Flask backend)
- **Modern glass (frosted) UI** with responsive design
- **Animated shooting stars** and starfield background
- **Easy to run locally or on your network**

---

## Getting Started

### 1. Clone or Download

Download or clone this repository to your computer.

### 2. Install Python Dependencies

Navigate to the project folder and install Flask and Flask-CORS:

```bash
pip install flask flask-cors
```

### 3. Run the Backend

Edit `app.py` if you want to allow network access:

```python
# app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

Start the backend:

```bash
python app.py
```

### 4. Serve the Frontend

In the same folder, start a simple HTTP server (Python 3):

```bash
python -m http.server 8000
```

### 5. Access the App

- On your computer:  
  Open [http://localhost:8000/Recovery.html](http://localhost:8000/Recovery.html)
- On another device (same network):  
  Find your computer's IP (e.g., `192.168.1.5`) and open  
  [http://192.168.1.5:8000/Recovery.html](http://192.168.1.5:8000/Recovery.html)

**Note:**  
In `Recovery.html`, update the fetch URL to use your computer's IP if accessing from another device:

```js
fetch('http://192.168.1.5:5000/check', { ... })
```

---

## File Structure

- `app.py` - Flask backend for AI analysis
- `ai_helper.py` - AI logic (implement your own or mock)
- `Recovery.html` - Main frontend file
- (Optional) `requirements.txt` - Python dependencies

---

## Troubleshooting

- **CORS errors:** Make sure Flask-CORS is enabled in `app.py`.
- **Firewall issues:** Allow Python through your firewall.
- **Backend not connecting:** Double-check IP addresses and that both servers are running.

---

## License

MIT License

---

**Enjoy your futuristic Recovery AI experience!**

