#!/usr/bin/env python3
"""
GitHub Action script to update ClickUp tickets with commit information and AI analysis.
"""

import os
import re
import json
import subprocess
import requests
from typing import Optional, Dict, Any

class ClickUpUpdater:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.clickup_api_key = os.getenv('CLICKUP_API_KEY')
        self.clickup_team_id = os.getenv('CLICKUP_TEAM_ID')
        
        # GitHub environment variables
        self.commit_sha = os.getenv('GITHUB_SHA')
        self.repo_name = os.getenv('GITHUB_REPOSITORY')
        self.actor = os.getenv('GITHUB_ACTOR')
        
        if not all([self.openai_api_key, self.clickup_api_key]):
            raise ValueError("Missing required environment variables")
    
    def get_commit_info(self) -> Dict[str, Any]:
        """Get commit message and diff information."""
        try:
            # Get commit message
            commit_message = subprocess.check_output([
                'git', 'log', '-1', '--pretty=%B'
            ], text=True).strip()
            
            # Get changed files
            changed_files = subprocess.check_output([
                'git', 'diff', '--name-only', 'HEAD~1', 'HEAD'
            ], text=True).strip().split('\n')
            
            # Get diff content (limited for AI processing)
            diff_content = subprocess.check_output([
                'git', 'diff', 'HEAD~1', 'HEAD'
            ], text=True)
            
            # Limit diff content to avoid API limits
            if len(diff_content) > 2000:
                diff_content = diff_content[:2000] + "\n... (diff truncated)"
            
            return {
                'message': commit_message,
                'files': [f for f in changed_files if f],  # Remove empty strings
                'diff': diff_content,
                'sha': self.commit_sha,
                'author': self.actor
            }
        except subprocess.CalledProcessError as e:
            print(f"Error getting commit info: {e}")
            return None
    
    def extract_clickup_ticket_id(self, commit_message: str) -> Optional[str]:
        """Extract ClickUp ticket ID from commit message."""
        match = re.search(r'CU-([A-Za-z0-9]+)', commit_message)
        return match.group(1) if match else None
    
    def analyze_with_ai(self, commit_info: Dict[str, Any]) -> str:
        """Use OpenAI to analyze the commit and generate a summary."""
        try:
            prompt = f"""
Analyze this code commit and provide a concise technical summary:

Commit Message: {commit_info['message']}
Files Changed: {', '.join(commit_info['files'])}
Code Diff:
{commit_info['diff']}

Provide a clear explanation of what was implemented, fixed, or changed. Focus on the technical aspects and impact.
"""

            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers={
                    'Authorization': f"Bearer {self.openai_api_key}",
                    'Content-Type': 'application/json'
                },
                json={
                    'model': 'gpt-3.5-turbo',
                    'messages': [
                        {
                            'role': 'system', 
                            'content': 'You are a senior developer analyzing code commits. Provide clear, concise technical explanations.'
                        },
                        {
                            'role': 'user', 
                            'content': prompt
                        }
                    ],
                    'max_tokens': 300,
                    'temperature': 0.3
                }
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content'].strip()
            else:
                print(f"OpenAI API error: {response.status_code}")
                return f"📝 Code changes made to: {', '.join(commit_info['files'])}"
                
        except Exception as e:
            print(f"AI analysis error: {e}")
            return f"📝 Code update: {commit_info['message']}"
    
    def get_clickup_task_info(self, task_id: str) -> Optional[Dict]:
        """Get task information from ClickUp to verify it exists."""
        try:
            # ClickUp API endpoint for getting task
            url = f"https://api.clickup.com/api/v2/task/{task_id}"
            
            headers = {
                'Authorization': self.clickup_api_key,
                'Content-Type': 'application/json'
            }
            
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"ClickUp API error getting task: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Error getting ClickUp task: {e}")
            return None
    
    def post_to_clickup(self, task_id: str, commit_info: Dict[str, Any], ai_summary: str) -> bool:
        """Post a comment to the ClickUp task."""
        try:
            # First verify task exists
            task_info = self.get_clickup_task_info(task_id)
            if not task_info:
                print(f"Task {task_id} not found in ClickUp")
                return False
            
            # Format the comment
            comment_text = f"""🔧 **Code Update**

**AI Analysis:**
{ai_summary}

**Details:**
- **Commit:** {commit_info['message']}
- **Files:** {', '.join(commit_info['files']) if commit_info['files'] else 'No files changed'}
- **Author:** {commit_info['author']}
- **SHA:** {commit_info['sha'][:8]}

[View full commit](https://github.com/{self.repo_name}/commit/{commit_info['sha']})"""
            
            # ClickUp API endpoint for posting comments
            url = f"https://api.clickup.com/api/v2/task/{task_id}/comment"
            
            headers = {
                'Authorization': self.clickup_api_key,
                'Content-Type': 'application/json'
            }
            
            data = {
                'comment_text': comment_text,
                'notify_all': False
            }
            
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 200:
                print(f"✅ Successfully updated ClickUp task {task_id}")
                return True
            else:
                print(f"❌ ClickUp API error: {response.status_code}")
                print(f"Response: {response.text}")
                return False
                
        except Exception as e:
            print(f"Error posting to ClickUp: {e}")
            return False
    
    def run(self):
        """Main execution function."""
        print("🚀 Starting ClickUp update process...")
        
        # Get commit information
        commit_info = self.get_commit_info()
        if not commit_info:
            print("❌ Could not get commit information")
            return
        
        print(f"📝 Processing commit: {commit_info['message']}")
        
        # Extract ClickUp ticket ID
        ticket_id = self.extract_clickup_ticket_id(commit_info['message'])
        if not ticket_id:
            print("ℹ️  No ClickUp ticket ID found in commit message (format: CU-ticketid)")
            return
        
        print(f"🎫 Found ClickUp ticket: {ticket_id}")
        
        # Analyze with AI
        print("🤖 Generating AI analysis...")
        ai_summary = self.analyze_with_ai(commit_info)
        
        # Post to ClickUp
        success = self.post_to_clickup(ticket_id, commit_info, ai_summary)
        
        if success:
            print("✅ Process completed successfully!")
        else:
            print("❌ Process failed")

if __name__ == "__main__":
    updater = ClickUpUpdater()
    updater.run()