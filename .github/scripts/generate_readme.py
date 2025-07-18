#!/usr/bin/env python3
"""
Auto-generate README.md files for folders and document code files.
"""

import os
import re
import json
import requests
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

class READMEGenerator:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.repo_root = Path('.')
        self.supported_extensions = {
            '.py': 'Python',
            '.js': 'JavaScript', 
            '.ts': 'TypeScript',
            '.java': 'Java',
            '.cpp': 'C++',
            '.c': 'C',
            '.cs': 'C#',
            '.php': 'PHP',
            '.rb': 'Ruby',
            '.go': 'Go',
            '.rs': 'Rust',
            '.sql': 'SQL',
            '.html': 'HTML',
            '.css': 'CSS',
            '.sh': 'Shell Script',
            '.yaml': 'YAML',
            '.yml': 'YAML',
            '.json': 'JSON'
        }
        
        # Folders to skip
        self.skip_folders = {
            '.git', '.github', 'node_modules', '__pycache__', 
            '.venv', 'venv', 'env', 'dist', 'build', '.pytest_cache',
            'coverage', '.coverage', 'htmlcov', '.mypy_cache'
        }
        
        if not self.openai_api_key:
            raise ValueError("Missing OPENAI_API_KEY environment variable")
    
    def is_code_file(self, file_path: Path) -> bool:
        """Check if file is a supported code file."""
        return file_path.suffix.lower() in self.supported_extensions
    
    def should_skip_folder(self, folder_path: Path) -> bool:
        """Check if folder should be skipped."""
        return folder_path.name in self.skip_folders or folder_path.name.startswith('.')
    
    def read_file_content(self, file_path: Path) -> Optional[str]:
        """Safely read file content."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Limit content size for AI processing
                if len(content) > 3000:
                    content = content[:3000] + "\n... (file truncated for analysis)"
                return content
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None
    
    def analyze_file_with_ai(self, file_path: Path, content: str) -> str:
        """Use AI to analyze a single file and generate documentation."""
        try:
            file_type = self.supported_extensions.get(file_path.suffix.lower(), 'Code')
            
            prompt = f"""
Analyze this {file_type} file and provide comprehensive enterprise-level documentation:

File: {file_path.name}
Content:
{content}

Provide detailed documentation in this format:

## {file_path.name}

### 📊 Business Context & Impact
**Business Problem Statement:**
- What specific business challenge this code solves
- Current pain points it addresses
- Value delivered to the organization

**Stakeholder Analysis:**
- Primary users and their needs
- Secondary stakeholders who benefit
- Business processes this integrates with

### 🏗️ Technical Architecture
**System Design:**
- Architecture pattern and design principles used
- Technology stack and dependencies
- Integration points with other systems

**Data Architecture:**
- Data models and structures used
- Database interactions and persistence
- Data validation and business rules

**Performance & Scalability:**
- Performance characteristics
- Scalability considerations
- Optimization strategies

### 💻 Code Implementation Details
**Function/Class Documentation:**
- Detailed breakdown of main components
- Input/output specifications with examples
- Error handling and exception management
- Side effects and external interactions

**Code Examples & Usage:**
- Basic usage examples
- Integration scenarios
- Common patterns and best practices

**Security & Compliance:**
- Security measures implemented
- Data protection considerations
- Compliance requirements addressed

### 🔧 Operations & Maintenance
**Deployment Considerations:**
- Environment requirements
- Configuration needs
- Monitoring and health checks

**Troubleshooting:**
- Common issues and solutions
- Performance tuning recommendations
- Maintenance requirements

Provide detailed, professional documentation suitable for enterprise environments.
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
                            'content': 'You are a technical documentation expert. Create clear, concise documentation for code files.'
                        },
                        {
                            'role': 'user',
                            'content': prompt
                        }
                    ],
                    'max_tokens': 500,
                    'temperature': 0.3
                }
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content'].strip()
            else:
                print(f"AI analysis failed for {file_path}: {response.status_code}")
                return self.generate_basic_file_doc(file_path, content)
                
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            return self.generate_basic_file_doc(file_path, content)
    
    def generate_basic_file_doc(self, file_path: Path, content: str) -> str:
        """Generate basic documentation without AI."""
        file_type = self.supported_extensions.get(file_path.suffix.lower(), 'Code')
        
        # Extract basic info from content
        lines = content.split('\n')
        functions = []
        classes = []
        
        for line in lines[:50]:  # Check first 50 lines
            line = line.strip()
            if line.startswith('def ') or line.startswith('function '):
                func_name = re.search(r'(def|function)\s+(\w+)', line)
                if func_name:
                    functions.append(func_name.group(2))
            elif line.startswith('class '):
                class_name = re.search(r'class\s+(\w+)', line)
                if class_name:
                    classes.append(class_name.group(1))
        
        doc = f"## {file_path.name}\n\n"
        doc += f"**Type:** {file_type} file\n\n"
        
        if classes:
            doc += f"**Classes:** {', '.join(classes[:5])}\n\n"
        
        if functions:
            doc += f"**Functions:** {', '.join(functions[:5])}\n\n"
        
        doc += f"**Size:** {len(content)} characters\n\n"
        
        return doc
    
    def analyze_folder_with_ai(self, folder_path: Path, files_info: List[Dict]) -> str:
        """Use AI to analyze a folder and generate overview documentation."""
        try:
            files_summary = "\n".join([
                f"- {info['name']} ({info['type']}): {info['size']} characters"
                for info in files_info[:10]  # Limit to first 10 files
            ])
            
            prompt = f"""
Analyze this code folder and provide comprehensive enterprise-level documentation:

Folder: {folder_path.name if folder_path.name != '.' else 'Root Directory'}
Path: {folder_path}

Files in this folder:
{files_summary}

Provide detailed documentation in this format:

# {folder_path.name if folder_path.name != '.' else folder_path.absolute().name}

## 📊 Business Context & Impact

### Business Problem Statement
Explain what business challenges this module/system solves, the value it delivers, and why it exists.

### Stakeholder Analysis  
- **Primary Users:** Who directly interacts with this functionality
- **Business Processes:** How this integrates into larger business workflows
- **Success Metrics:** How business value is measured

## 🏗️ Technical Architecture

### System Design
- **Architecture Pattern:** How the code is structured and organized
- **Technology Stack:** Languages, frameworks, libraries used
- **Design Principles:** SOLID, DRY, separation of concerns applied

### Data Architecture
- **Data Models:** How information is structured and managed
- **Integration Points:** Connections to databases, APIs, external systems
- **Data Flow:** How information moves through the system

### Performance & Scalability
- **Performance Characteristics:** Speed, throughput, resource usage
- **Scalability Considerations:** How it handles growth and load
- **Optimization Strategies:** Techniques used for efficiency

## 💻 Implementation Overview

### Key Components
Detailed breakdown of main files and their roles in the system.

### Code Organization
- **Directory Structure:** How files are organized and why
- **Naming Conventions:** Standards followed throughout
- **Common Patterns:** Reusable patterns and practices

### Integration & Usage
- **How to Use:** Getting started with this module
- **Dependencies:** What this code requires to function
- **API/Interface:** How other systems interact with this

## 🔧 Operations & Maintenance

### Deployment Considerations
- **Environment Requirements:** What's needed to run this code
- **Configuration:** Settings and parameters to configure
- **Monitoring:** What to watch for operational health

### Development Guidelines
- **Contributing:** How to modify and extend this code
- **Testing:** Testing strategies and requirements
- **Best Practices:** Standards to follow when working with this code

Provide professional, enterprise-grade documentation suitable for technical and business stakeholders.
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
                            'content': 'You are a technical documentation expert. Create clear folder documentation for software projects.'
                        },
                        {
                            'role': 'user',
                            'content': prompt
                        }
                    ],
                    'max_tokens': 800,
                    'temperature': 0.3
                }
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content'].strip()
            else:
                print(f"AI folder analysis failed for {folder_path}: {response.status_code}")
                return self.generate_basic_folder_doc(folder_path, files_info)
                
        except Exception as e:
            print(f"Error analyzing folder {folder_path}: {e}")
            return self.generate_basic_folder_doc(folder_path, files_info)
    
    def generate_basic_folder_doc(self, folder_path: Path, files_info: List[Dict]) -> str:
        """Generate basic folder documentation without AI."""
        folder_name = folder_path.name if folder_path.name != '.' else folder_path.absolute().name
        
        doc = f"# {folder_name}\n\n"
        doc += f"## Overview\n\nThis folder contains {len(files_info)} files.\n\n"
        
        # Group files by type
        file_types = {}
        for info in files_info:
            file_type = info['type']
            if file_type not in file_types:
                file_types[file_type] = []
            file_types[file_type].append(info['name'])
        
        doc += "## File Types\n\n"
        for file_type, files in file_types.items():
            doc += f"**{file_type}:** {len(files)} files\n"
        
        doc += "\n## Files\n\n"
        for info in files_info:
            doc += f"- **{info['name']}** - {info['type']} file ({info['size']} characters)\n"
        
        doc += f"\n*Documentation generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"
        
        return doc
    
    def generate_folder_readme(self, folder_path: Path):
        """Generate README.md for a specific folder."""
        print(f"📁 Processing folder: {folder_path}")
        
        # Get all code files in this folder (non-recursive)
        code_files = []
        files_info = []
        
        try:
            for file_path in folder_path.iterdir():
                if file_path.is_file() and self.is_code_file(file_path):
                    content = self.read_file_content(file_path)
                    if content:
                        code_files.append((file_path, content))
                        files_info.append({
                            'name': file_path.name,
                            'type': self.supported_extensions.get(file_path.suffix.lower(), 'Unknown'),
                            'size': len(content)
                        })
        except PermissionError:
            print(f"Permission denied accessing {folder_path}")
            return
        
        if not code_files:
            print(f"No code files found in {folder_path}")
            return
        
        # Generate folder overview
        folder_overview = self.analyze_folder_with_ai(folder_path, files_info)
        
        # Generate individual file documentation
        file_docs = []
        for file_path, content in code_files:
            print(f"  📄 Analyzing {file_path.name}...")
            file_doc = self.analyze_file_with_ai(file_path, content)
            file_docs.append(file_doc)
        
        # Combine into README
        readme_content = folder_overview + "\n\n"
        
        if file_docs:
            readme_content += "---\n\n# Files Documentation\n\n"
            readme_content += "\n\n".join(file_docs)
        
        readme_content += f"\n\n---\n*Auto-generated documentation - Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"
        
        # Write README.md
        readme_path = folder_path / 'README.md'
        try:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            print(f"✅ Generated {readme_path}")
        except Exception as e:
            print(f"Error writing {readme_path}: {e}")
    
    def run(self):
        """Main execution - scan repository and generate README files."""
        print("🚀 Starting README generation...")
        
        # Generate README for root directory
        self.generate_folder_readme(self.repo_root)
        
        # Find all subdirectories with code files
        for root, dirs, files in os.walk(self.repo_root):
            root_path = Path(root)
            
            # Skip certain folders
            dirs[:] = [d for d in dirs if not self.should_skip_folder(root_path / d)]
            
            # Skip root directory (already processed)
            if root_path == self.repo_root:
                continue
            
            # Check if this directory has code files
            has_code_files = any(
                Path(root, file).suffix.lower() in self.supported_extensions
                for file in files
            )
            
            if has_code_files:
                self.generate_folder_readme(root_path)
        
        print("✅ README generation completed!")

if __name__ == "__main__":
    generator = READMEGenerator()
    generator.run()