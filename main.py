### 👤 Author
#Created by: Mikaeil297

### ⚠️ Disclaimer & Liability
#**Mikaeil297** assumes **no responsibility** for any misuse of this code. This tool is intended for **educational purposes, authorized security testing, and load testing of your own servers only**.

#*   Do not use this tool against servers or websites you do not own or have explicit permission to test.
#*   Unauthorized stress testing is illegal in many jurisdictions and can result in severe legal consequences.
#*   The author is not liable for any damages, data loss, or legal issues arising from the use of this software.


################################################################################
#https://github.com/Mikaeil297


import aiohttp
import asyncio
import time
import random 
import os
import string
from pyfiglet import figlet_format
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_logo():
    text = "Mikaeil297"
    try:
        ascii_art = figlet_format(text, font='slant')
        print(f"\n{Fore.RED}{Style.BRIGHT}{ascii_art}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}🚀 HIGH-PERFORMANCE ASYNC STRESS TEST 🚀{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}✅ Using aiohttp for maximum speed & stability.{Style.RESET_ALL}\n")
    except Exception:
        print("\nMikaeil297 - HIGH-PERFORMANCE STRESS TEST\n")

def generate_and_save_payload(filename, size_kb=100):
    """
    Generates payload ONCE and saves it to a file.
    """
    print(f"{Fore.CYAN}Generating payload ({size_kb}KB) and saving to {filename}...{Style.RESET_ALL}")
    
    size_bytes = size_kb * 1024
    characters = string.ascii_letters + string.digits + string.punctuation + " " + "\n"
    
    # Generate data
    payload = ''.join(random.choice(characters) for _ in range(size_bytes))
    
    # Save to file
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(payload)
        print(f"{Fore.GREEN}✅ File saved successfully! Size: {size_kb}KB{Style.RESET_ALL}")
        return True
    except Exception as e:
        print(f"{Fore.RED}❌ Error saving file: {e}{Style.RESET_ALL}")
        return False

async def send_request(session, url, method, payload, results, thread_id, request_count):
    """
    Sends requests asynchronously using aiohttp.
    """
    for i in range(request_count):
        try:
    
            timeout = aiohttp.ClientTimeout(total=0.5) 
            
            if method.upper() == 'GET':
                #!
                full_url = f"{url}?data={payload}"
                async with session.get(full_url, timeout=timeout) as response:
                    results.append(f"[{Fore.GREEN}OK{Style.RESET_ALL}] T-{thread_id} Req-{i+1}: Status {response.status}")
                    
            elif method.upper() == 'POST':
                async with session.post(url, data=payload, timeout=timeout) as response:
                    results.append(f"[{Fore.GREEN}OK{Style.RESET_ALL}] T-{thread_id} Req-{i+1}: Status {response.status}")
                    
            elif method.upper() == 'PUT':
                async with session.put(url, data=payload, timeout=timeout) as response:
                    results.append(f"[{Fore.GREEN}OK{Style.RESET_ALL}] T-{thread_id} Req-{i+1}: Status {response.status}")
                    
            elif method.upper() == 'DELETE':
                async with session.delete(url, timeout=timeout) as response:
                    results.append(f"[{Fore.GREEN}OK{Style.RESET_ALL}] T-{thread_id} Req-{i+1}: Status {response.status}")
                    
            else:
                results.append(f"[{Fore.RED}INVALID{Style.RESET_ALL}] Method {method}")
                continue
                
        except asyncio.TimeoutError:
            results.append(f"[{Fore.YELLOW}TIMEOUT{Style.RESET_ALL}] T-{thread_id} Req-{i+1}")
        except aiohttp.ClientError as e:
            results.append(f"[{Fore.RED}CONN_ERR{Style.RESET_ALL}] T-{thread_id} Req-{i+1}: {str(e)}")
        except Exception as e:
            results.append(f"[{Fore.RED}ERR{Style.RESET_ALL}] T-{thread_id} Req-{i+1}: {str(e)}")

async def main_async(target_url, method, payload, num_threads, requests_per_thread):
    """
    Main async function to run the stress test.
    """
    print(f"\n{Fore.RED}Starting {num_threads} async tasks with {requests_per_thread} requests each...{Style.RESET_ALL}")
    print(f"{Fore.RED}Total Requests: {num_threads * requests_per_thread}{Style.RESET_ALL}\n")
    
    start_time = time.time()
    results = []
    
    #
    async with aiohttp.ClientSession() as session:
        #ا
        tasks = []
        for i in range(num_threads):
            task = asyncio.create_task(
                send_request(session, target_url, method, payload, results, i, requests_per_thread)
            )
            tasks.append(task)
        
        
        await asyncio.gather(*tasks)

    end_time = time.time()
    duration = end_time - start_time
    
    return results, duration

def get_user_input(prompt, is_exit_check=True):
    user_input = input(f"{Fore.YELLOW}{prompt}{Style.RESET_ALL}")
    if is_exit_check and user_input.strip().lower() in ['end', 'exit', 'q']:
        print(f"\n{Fore.RED}Operation cancelled by user.{Style.RESET_ALL}")
        exit()
    return user_input

def main():
    print_logo()
    
    # 1. Get URL
    target_url = get_user_input("Enter Target URL (e.g., https://github.com/Mikaeil297 ): ")
    if not target_url:
        print(f"{Fore.RED}URL cannot be empty! Exiting.{Style.RESET_ALL}")
        return

    # 2. Get Payload Size (KB)
    size_input = get_user_input("Enter Payload Size in KB (e.g., 10 for 10KB): ", is_exit_check=False)
    try:
        size_kb = int(size_input)
    except ValueError:
        print(f"{Fore.RED}Invalid size! Exiting.{Style.RESET_ALL}")
        return

    if size_kb <= 0:
        print(f"{Fore.RED}Size must be greater than 0! Exiting.{Style.RESET_ALL}")
        return

    # 3. Generate File ONCE
    filename = "payload.txt"
    if not generate_and_save_payload(filename, size_kb):
        return

    # 4. Get Count (Requests per thread)
    count_input = get_user_input("Enter Number of Requests PER THREAD: ")
    try:
        count = int(count_input)
    except ValueError:
        print(f"{Fore.RED}Invalid number! Exiting.{Style.RESET_ALL}")
        return

    if count <= 0:
        print(f"{Fore.RED}Count must be greater than 0! Exiting.{Style.RESET_ALL}")
        return

    # 5. Select Method
    print(f"\n{Fore.CYAN}Select Request Method:{Style.RESET_ALL}")
    print(f"1. POST (Send File Content)")
    print(f"2. GET (Append File Content to URL)")
    print(f"3. PUT (Send File Content)")
    print(f"4. DELETE (No Content)")
    
    choice = get_user_input("Your Choice (1-4): ")

    method = ''
    if choice == '1':
        method = 'POST'
    elif choice == '2':
        method = 'GET'
    elif choice == '3':
        method = 'PUT'
    elif choice == '4':
        method = 'DELETE'
    else:
        print(f"{Fore.RED}Invalid choice! Exiting.{Style.RESET_ALL}")
        return

    # 6. Set Number of Threads (Async tasks)
    num_threads = 100 
    print(f"\n{Fore.RED}Starting {num_threads} async tasks...{Style.RESET_ALL}")
    
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            payload = f.read()
    except Exception as e:
        print(f"{Fore.RED}❌ Error reading file: {e}{Style.RESET_ALL}")
        return

    
    try:
        results, duration = asyncio.run(main_async(target_url, method, payload, num_threads, count))
        
        # Print Results
        print(f"\n{Fore.CYAN}--- Final Results ---{Style.RESET_ALL}")
        ok_count = sum(1 for r in results if 'OK' in r)
        timeout_count = sum(1 for r in results if 'TIMEOUT' in r)
        error_count = sum(1 for r in results if 'ERR' in r or 'CONN_ERR' in r)
        
        print(f"{Fore.GREEN}Total Successful: {ok_count}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Total Timeouts: {timeout_count}{Style.RESET_ALL}")
        print(f"{Fore.RED}Total Errors: {error_count}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}Total Execution Time: {duration:.2f} seconds{Style.RESET_ALL}")
        
        if duration > 0:
            rps = (ok_count + timeout_count + error_count) / duration
            print(f"{Fore.CYAN}Requests Per Second (RPS): {rps:.2f}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}An error occurred during execution: {e}{Style.RESET_ALL}")

    # Optional: Clean up file
    cleanup = input(f"\n{Fore.YELLOW}Delete payload.txt after test? (y/n): {Style.RESET_ALL}")
    if cleanup.lower() == 'y':
        try:
            os.remove(filename)
            print(f"{Fore.GREEN}File deleted.{Style.RESET_ALL}")
        except:
            pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program interrupted by user (Ctrl+C). Exiting.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")
