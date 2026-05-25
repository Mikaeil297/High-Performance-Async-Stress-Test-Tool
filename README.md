
# High-Performance-Async-Stress-Test-Tool
https://github.com/Mikaeil297


# 🚀 High-Performance Async Stress Test Tool

### 📝 Description
This is an optimized, high-speed network stress testing tool built with Python. Unlike traditional synchronous scripts, this tool utilizes **`asyncio`** and **`aiohttp`** to handle thousands of concurrent connections efficiently. It is designed to run smoothly on mobile devices (like Android via Pydroid 3) without consuming excessive RAM or CPU resources.

**Key Features:**
*   ⚡ **Async Architecture:** Uses non-blocking I/O for maximum speed and stability.
*   📱 **Mobile Optimized:** Low memory footprint, safe for running on smartphones.
*   📂 **File-Based Payload:** Generates large data payloads once and saves them to a file, then reads from the file during the test to save processing power.
*   🛡️ **Robust Error Handling:** Gracefully handles timeouts and connection errors without crashing.

### 👤 Author
**Created by:** Mikaeil297

### ⚠️ Disclaimer & Liability
**Mikaeil297** assumes **no responsibility** for any misuse of this code. This tool is intended for **educational purposes, authorized security testing, and load testing of your own servers only**.

*   Do not use this tool against servers or websites you do not own or have explicit permission to test.
*   Unauthorized stress testing is illegal in many jurisdictions and can result in severe legal consequences.
*   The author is not liable for any damages, data loss, or legal issues arising from the use of this software.

### 📖 How to Use (Guide)

#### 1. Prerequisites
You need Python installed on your device. If you are using a mobile app like **Pydroid 3**, ensure you have the following libraries installed:
```bash
pip install aiohttp pyfiglet colorama
```

#### 2. Running the Script
1.  Copy the code into a new Python file (e.g., `stress_test.py`).
2.  Run the script.
3.  **Enter Target URL:** Provide the URL you want to test (e.g., `http://127.0.0.1:8000/api/test`).
4.  **Enter Payload Size:** Specify the size in KB (e.g., `10` for 10KB). *Note: Large sizes (1000KB+) may cause URL length errors in GET requests.*
5.  **Enter Requests per Thread:** How many times each thread should send a request.
6.  **Select Method:** Choose between POST, GET, PUT, or DELETE.
7.  **Start Test:** The script will generate the payload file and begin the async stress test.

#### 3. Troubleshooting
*   **Timeouts:** If you see many timeouts, the server might be slow or blocking your IP. Try increasing the `timeout` value in the code or reducing the number of threads.
*   **Memory Errors:** If the app crashes, reduce the `num_threads` variable in the code (default is 100).
*   **File Not Found:** Ensure the script has permission to write to the directory where it is running.

---
