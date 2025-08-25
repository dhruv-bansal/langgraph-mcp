import subprocess
import sys
import os

SERVERS = [
    "math.py",
    "tavily.py",
    "weather.py",
    "yt_transcript.py"
]

SERVERS_DIR = os.path.dirname(os.path.abspath(__file__))


def run_server(server_file):
    server_path = os.path.join(SERVERS_DIR, server_file)
    print(f"Starting {server_file}...")
    try:
        proc = subprocess.Popen([sys.executable, server_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Wait a short time to see if it starts
        try:
            outs, errs = proc.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            print(f"{server_file} started successfully.")
            return True
        if proc.returncode == 0:
            print(f"{server_file} started and exited immediately (unexpected). Output: {outs.decode()}")
            return False
        else:
            print(f"{server_file} failed to start. Error: {errs.decode()}")
            return False
    except Exception as e:
        print(f"Error starting {server_file}: {e}")
        return False


def main():
    all_started = True
    for server in SERVERS:
        started = run_server(server)
        if not started:
            all_started = False
    if all_started:
        print("All servers started successfully.")
    else:
        print("Some servers failed to start.")

if __name__ == "__main__":
    main()
