# run.py
"""
Quick launcher script for the LDA Topic Modelling Dashboard app.
"""

import os
import subprocess
import sys

def main():
    try:
        # Navigate to app folder where you have placed lda_streamlit_app.py
        app_dir = os.path.join(os.path.dirname(__file__), "app")
        app_script = os.path.join(app_dir, "lda_streamlit_app.py")

        if not os.path.exists(app_script):
            print("❌ Could not find the app script at:", app_script)
            sys.exit(1)

        # Run the Streamlit app
        print("🚀 Launching the LDA Topic Modelling Dashboard...")
        subprocess.run(["streamlit", "run", app_script], check=True)

    except KeyboardInterrupt:
        print("\n🛑 App terminated by user.")

if __name__ == "__main__":
    main()
