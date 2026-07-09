import os 
from pathlib import Path
from dotenv import load_dotenv  # A tool that secretly reads your API keys from a private file

load_dotenv()  # This command "opens" your .env file and makes the keys inside available to your code

def main(): 
    # Figures out where the script is saved on your hard drive, it doesn't matter if it's 
    # C:\Users\... or /Users/...; this command finds the absolute location.
    base_dir = Path(__file__).resolve().parent
    
    # This creates a path to a file called 'logs.txt' inside a folder called 'data'.
    data_path = base_dir / "data" / "logs.txt"
    
    # This checks if the 'data' folder exists. If not, it creates it so the program doesn't crash.
    data_path.parent.mkdir(exist_ok=True)
    
    print(f"Project initialized successfully!")
    print(f"Working directory: {base_dir}") 
    print(f"Data file will be saved at: {data_path}")

    # This looks for the secret key you put in the .env file.
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Warning: OPENAI_API_KEY not found in environment variables.")

# This is the "Safety Switch". It ensures that if you ever import this file into another project,
# the code inside 'main()' doesn't run automatically unless you tell it to.
if __name__ == "__main__":
    main()