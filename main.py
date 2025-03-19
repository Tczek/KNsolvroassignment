import data
import clustering
import visualisation
import subprocess
import webbrowser
import time
import requests
import importlib



def wait_for_jupyter():
    """Wait for the Jupyter Notebook server to start."""
    while True:
        try:
            response = requests.get("http://localhost:8888")
            if response.status_code == 200:
                break
        except requests.ConnectionError:
            time.sleep(1)

if __name__ == "__main__":
    # Reload modules to ensure the latest changes are picked up
    importlib.reload(data)
    importlib.reload(clustering)
    importlib.reload(visualisation)
    
    notebook_path = "Results.ipynb"
    
    # Start the Jupyter Notebook server
    process = subprocess.Popen(
        ["jupyter", "notebook", "--no-browser"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    
    # Wait for the Jupyter Notebook server to be ready
    wait_for_jupyter()
    
    # Open the specified notebook in the default web browser
    webbrowser.open(f"http://localhost:8888/notebooks/{notebook_path}")







