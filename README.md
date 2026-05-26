# High-Performance Async Stress Test Tool

**GitHub:** https://github.com/Mikaeil297

---

## 🚀 Overview

A high-speed, optimized network stress testing tool built with Python. Unlike traditional synchronous scripts, this tool utilizes **`asyncio`** and **`aiohttp`** to handle thousands of concurrent requests with minimal resource consumption.

### Key Features:
- ⚡ **Async Architecture:** Non-blocking I/O for maximum speed and stability
- 📱 **Mobile Optimized:** Low memory footprint, safe for running on smartphones
- 📂 **File-Based Payload:** Generates large payloads once and reuses them efficiently
- 🛡️ **Robust Error Handling:** Gracefully handles timeouts and connection errors
- 🔍 **Detailed Reporting:** Real-time statistics and performance metrics
- 🎯 **Flexible HTTP Methods:** Supports GET, POST, PUT, and DELETE requests

---

## 👤 Author

**Created by:** Mikaeil297

---

## ⚠️ Disclaimer & Liability

**This tool is intended for educational purposes, authorized security testing, and load testing of your own servers ONLY.**

### Important Legal Notice:
- ❌ Do **NOT** use this tool against servers or websites you do not own or have explicit permission to test
- ❌ Unauthorized stress testing is **illegal** in many jurisdictions and can result in severe legal consequences
- ❌ The author assumes **no responsibility** for any misuse of this code
- ❌ Users are solely responsible for their actions and any damages caused by using this tool

By using this software, you agree to use it only for legitimate, authorized purposes.

---

## 📖 How to Use

### Prerequisites

You need **Python 3.7+** installed on your device. 

#### Install Required Libraries:

```bash
pip install aiohttp pyfiglet colorama
```

**For Mobile Users (Pydroid 3, Termux, etc.):**
- Ensure Python is installed
- Run the pip install command above within your Python environment

---

### Getting Started

1. **Copy the Code:**
   - Clone or download the `main.py` file from this repository

2. **Run the Script:**
   ```bash
   python main.py
   ```

3. **Follow the Interactive Prompts:**

   - **Enter Target URL:** 
     - Example: `http://127.0.0.1:8000/api/test`
     - Example: `https://example.com/endpoint`

   - **Enter Payload Size (in KB):**
     - Specify the size of data to send with each request
     - Example: `10` for 10KB
     - **Note:** Large sizes (1000KB+) may cause issues with GET requests due to URL length limits

   - **Enter Requests per Thread:**
     - How many times each async task should send a request
     - Example: `100` means 100 requests per thread

   - **Select HTTP Method:**
     - **1. POST:** Send payload in request body
     - **2. GET:** Append payload to URL as query parameter
     - **3. PUT:** Send payload in request body
     - **4. DELETE:** Send DELETE request with payload

   - **Automatic Test Execution:**
     - The tool will automatically create 100 concurrent async tasks
     - Each task sends the specified number of requests
     - Real-time results are displayed

4. **Review Results:**
   - The tool displays:
     - Total successful requests
     - Total timeouts
     - Total errors
     - Execution time
     - Requests Per Second (RPS)

---

## ⚙️ Configuration

### Default Settings:

```python
num_threads = 100          # Number of concurrent async tasks
timeout = 0.5 seconds      # Request timeout
payload_file = payload.txt # Generated file name
```

To modify these settings, edit the `main.py` file before running:

- **Reduce Memory Usage:** Lower `num_threads` (e.g., `50`)
- **Increase Timeout:** Change `timeout = aiohttp.ClientTimeout(total=1.0)` to higher value
- **Change Payload Size:** Adjust when prompted during execution

---

## 🔧 Troubleshooting

### Issue: Many Timeout Errors
**Solution:**
- The target server may be slow or blocking requests
- Increase the `timeout` value in the code (change `0.5` to `1.0` or higher)
- Reduce the number of `num_threads` to decrease load
- Add delays between requests if needed

### Issue: Memory Errors or App Crashes
**Solution:**
- Reduce `num_threads` from 100 to 50 or lower
- Reduce `requests_per_thread` 
- Reduce `payload_size`
- Run on a device with more available RAM

### Issue: "Connection Refused" Errors
**Solution:**
- Verify the target URL is correct and accessible
- Ensure the target server is running
- Check firewall settings
- Try connecting manually with a browser first

### Issue: "File Not Found" Error
**Solution:**
- Ensure the script has permission to write files in the current directory
- Run the script from a directory where you have write permissions
- Try running with elevated privileges if necessary

### Issue: Large Payloads in GET Requests
**Solution:**
- Avoid using GET method with payloads larger than 1000KB
- Use POST or PUT instead for large payloads
- Reduce the `payload_size` when using GET

---

## 📊 Performance Tips

1. **For Maximum Throughput:**
   - Use POST or PUT methods instead of GET
   - Reduce timeout value (if network is stable)
   - Increase `num_threads` (monitor memory usage)

2. **For Stability:**
   - Increase timeout value
   - Reduce `num_threads`
   - Use smaller payload sizes

3. **For Mobile Devices:**
   - Keep `num_threads` under 50
   - Use smaller payloads (10-50KB)
   - Increase timeout to 1-2 seconds

---

## 📝 Example Usage Scenarios

### Test Local API (Development):
```
Target URL: http://127.0.0.1:8000/api/users
Payload Size: 5 KB
Requests Per Thread: 50
Method: POST
```

### Load Test Public Endpoint:
```
Target URL: https://api.example.com/data
Payload Size: 20 KB
Requests Per Thread: 100
Method: POST
```

### Mobile Stress Testing:
```
Target URL: http://192.168.1.100:5000/test
Payload Size: 10 KB
Requests Per Thread: 25
Method: GET
```

---

## 🛡️ Safety Recommendations

1. **Always Test Authorized Systems Only**
   - Only test servers/APIs you own or have written permission to test

2. **Monitor Server Health**
   - Ensure your test doesn't crash the target server
   - Start with small loads and gradually increase

3. **Use in Controlled Environments**
   - Test during off-peak hours
   - Notify system administrators before testing

4. **Keep Logs**
   - Document your test parameters
   - Save results for analysis

---

## 📄 License

This project is provided as-is for educational purposes. Users assume all responsibility for their use of this tool.

---

## 🐛 Reporting Issues

If you encounter bugs or have suggestions, please open an issue on GitHub:
https://github.com/Mikaeil297/High-Performance-Async-Stress-Test-Tool/issues

---

🌈 **Access Confirmed!** - This file has been successfully updated by Mikaeil297
