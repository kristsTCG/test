#!/usr/bin/env python3
"""
GitHub Action script to generate documentation when ClickUp tasks are completed.
"""

import os
import re
import json
import subprocess
import requests
from datetime import datetime
from typing import Optional, Dict, Any, List

class DocumentationGenerator:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.clickup_api_key = os.getenv('CLICKUP_API_KEY')
        self.task_id = os.getenv('TASK_ID')
        self.task_name = os.getenv('TASK_NAME')
        self.task_url = os.getenv('TASK_URL')
        self.space_id = os.getenv('SPACE_ID')
        self.repo_name = os.getenv('GITHUB_REPOSITORY')
        
        if not all([self.openai_api_key, self.clickup_api_key, self.task_id]):
            raise ValueError("Missing required environment variables")
    
    def get_task_details(self) -> Optional[Dict]:
        """Get detailed task information from ClickUp."""
        try:
            url = f"https://api.clickup.com/api/v2/task/{self.task_id}"
            headers = {
                'Authorization': self.clickup_api_key,
                'Content-Type': 'application/json'
            }
            
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error getting task details: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Error fetching task details: {e}")
            return None
    
    def get_task_comments(self) -> List[Dict]:
        """Get all comments for the task."""
        try:
            url = f"https://api.clickup.com/api/v2/task/{self.task_id}/comment"
            headers = {
                'Authorization': self.clickup_api_key,
                'Content-Type': 'application/json'
            }
            
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json().get('comments', [])
            else:
                print(f"Error getting comments: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"Error fetching comments: {e}")
            return []
    
    def get_related_commits(self) -> List[Dict]:
        """Find all commits related to this task."""
        try:
            # Get all commits from the repository
            result = subprocess.run([
                'git', 'log', '--oneline', '--grep', f'CU-{self.task_id}', '--all'
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                print("No related commits found")
                return []
            
            commits = []
            for line in result.stdout.strip().split('\n'):
                if line.strip():
                    parts = line.split(' ', 1)
                    if len(parts) == 2:
                        sha = parts[0]
                        message = parts[1]
                        
                        # Get commit details
                        commit_info = subprocess.run([
                            'git', 'show', '--name-only', '--format=%an|%ad|%s', sha
                        ], capture_output=True, text=True)
                        
                        if commit_info.returncode == 0:
                            lines = commit_info.stdout.strip().split('\n')
                            if lines:
                                author_date_subject = lines[0].split('|')
                                if len(author_date_subject) >= 3:
                                    commits.append({
                                        'sha': sha,
                                        'message': message,
                                        'author': author_date_subject[0],
                                        'date': author_date_subject[1],
                                        'files': [f for f in lines[1:] if f.strip()]
                                    })
            
            return commits
                
        except Exception as e:
            print(f"Error getting commits: {e}")
            return []
    
    def generate_documentation_content(self, task_details: Dict, comments: List[Dict], commits: List[Dict]) -> str:
        """Generate comprehensive documentation using AI."""
        try:
            # Prepare data for AI analysis
            task_description = task_details.get('description', 'No description provided')
            task_status = task_details.get('status', {}).get('status', 'Unknown')
            
            # Extract code update comments (from our automation)
            code_updates = []
            for comment in comments:
                if comment.get('comment_text', '').startswith('🔧 **Code Update**'):
                    code_updates.append(comment['comment_text'])
            
            # Prepare commit summary
            commit_summary = []
            for commit in commits:
                commit_summary.append(f"- {commit['message']} ({commit['author']} - {commit['date']})")
            
            prompt = f"""
Create comprehensive technical documentation for a completed software development task.

**Task Information:**
- Title: {self.task_name}
- ID: {self.task_id}
- Status: {task_status}
- Description: {task_description}

**Code Updates and AI Analysis:**
{chr(10).join(code_updates) if code_updates else 'No automated code analysis available'}

**Related Commits:**
{chr(10).join(commit_summary) if commit_summary else 'No related commits found'}

**Requirements:**
Create a well-structured technical document that includes:
1. Executive summary of what was accomplished
2. Technical implementation details
3. Code changes summary
4. Key features or fixes implemented
5. Testing considerations
6. Future considerations or maintenance notes

Format the output as a professional technical document suitable for team reference.
"""

            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers={
                    'Authorization': f"Bearer {self.openai_api_key}",
                    'Content-Type': 'application/json'
                },
                json={
                    'model': 'gpt-4',  # Using GPT-4 for better documentation quality
                    'messages': [
                        {
                            'role': 'system',
                            'content': 'You are a senior technical writer creating comprehensive software documentation. Write clear, detailed, and well-structured technical documentation.'
                        },
                        {
                            'role': 'user',
                            'content': prompt
                        }
                    ],
                    'max_tokens': 2000,
                    'temperature': 0.3
                }
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            else:
                print(f"AI documentation generation failed: {response.status_code}")
                return self.generate_fallback_documentation(task_details, comments, commits)
                
        except Exception as e:
            print(f"Error generating AI documentation: {e}")
            return self.generate_fallback_documentation(task_details, comments, commits)
    
    def generate_fallback_documentation(self, task_details: Dict, comments: List[Dict], commits: List[Dict]) -> str:
        """Generate basic documentation without AI."""
        doc = f"""# {self.task_name}

## Task Summary
- **Task ID:** {self.task_id}
- **Status:** {task_details.get('status', {}).get('status', 'Completed')}
- **Completed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Description
{task_details.get('description', 'No description provided')}

## Code Changes
"""
        
        if commits:
            doc += "### Commits:\n"
            for commit in commits:
                doc += f"- **{commit['sha'][:8]}**: {commit['message']}\n"
                doc += f"  - Author: {commit['author']}\n"
                doc += f"  - Date: {commit['date']}\n"
                if commit['files']:
                    doc += f"  - Files: {', '.join(commit['files'])}\n"
                doc += "\n"
        else:
            doc += "No related commits found.\n"
        
        if comments:
            doc += "\n## Development Notes\n"
            for comment in comments:
                if comment.get('comment_text', '').startswith('🔧 **Code Update**'):
                    doc += f"{comment['comment_text']}\n\n"
        
        doc += f"\n## Links\n- [ClickUp Task]({self.task_url})\n"
        if self.repo_name:
            doc += f"- [Repository](https://github.com/{self.repo_name})\n"
        
        return doc
    
    def create_clickup_doc(self, content: str) -> bool:
        """Create a document in ClickUp Docs."""
        try:
            url = f"https://api.clickup.com/api/v2/space/{self.space_id}/doc"
            headers = {
                'Authorization': self.clickup_api_key,
                'Content-Type': 'application/json'
            }
            
            data = {
                'name': f"Documentation: {self.task_name}",
                'content': content,
                'parent': None  # Creates in root of docs
            }
            
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 200:
                doc_data = response.json()
                print(f"✅ Documentation created successfully!")
                print(f"📄 Document ID: {doc_data.get('id')}")
                return True
            else:
                print(f"❌ Failed to create ClickUp document: {response.status_code}")
                print(f"Response: {response.text}")
                return False
                
        except Exception as e:
            print(f"Error creating ClickUp document: {e}")
            return False
    
    def run(self):
        """Main execution function."""
        print(f"🚀 Generating documentation for task: {self.task_id}")
        
        # Get task details
        task_details = self.get_task_details()
        if not task_details:
            print("❌ Could not fetch task details")
            return
        
        # Get comments
        print("📝 Fetching task comments...")
        comments = self.get_task_comments()
        
        # Get related commits
        print("🔍 Finding related commits...")
        commits = self.get_related_commits()
        
        # Generate documentation
        print("🤖 Generating comprehensive documentation...")
        documentation = self.generate_documentation_content(task_details, comments, commits)
        
        # Create ClickUp document
        print("📄 Creating ClickUp document...")
        success = self.create_clickup_doc(documentation)
        
        if success:
            print("✅ Documentation generation completed successfully!")
        else:
            print("❌ Documentation generation failed")
            # Optionally save to repository as fallback
            with open(f"docs/task-{self.task_id}.md", "w") as f:
                f.write(documentation)
            print(f"💾 Documentation saved to docs/task-{self.task_id}.md as fallback")

if __name__ == "__main__":
    generator = DocumentationGenerator()
    generator.run()