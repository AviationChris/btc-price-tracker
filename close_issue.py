from github import Github
import os
from dotenv import load_dotenv

load_dotenv()

def close_issue(issue_number):
    try:
        # Initialize Github instance using token
        g = Github(os.getenv('GITHUB_TOKEN'))
        
        # Get repository
        repo = g.get_repo("AviationChris/btc-price-tracker")
        
        # Get issue
        issue = repo.get_issue(number=issue_number)
        
        # Close issue
        issue.edit(state='closed')
        print(f"Successfully closed issue #{issue_number}")
        
    except Exception as e:
        print(f"Error closing issue: {str(e)}")

if __name__ == "__main__":
    issue_number = int(input("Enter issue number to close: "))
    close_issue(issue_number)