from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Akshata Laxman Pawar"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown"
    
    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

    # Run 'top' command and get output
    try:
        top_output = subprocess.getoutput("top -b -n 1")
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    # Create response HTML
    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
