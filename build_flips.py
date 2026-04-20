import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the 8 projects structured data
projects = [
    {
        "id": "1",
        "name": "Type 2 Diabetes Risk (PIMA)",
        "file": "diabetes_pima.py",
        "img": "diabetes.png",
        "tech": ['<span class="badge bright">Python</span>', '<span class="badge">Scikit-learn</span>', '<span class="badge">XGBoost</span>'],
        "desc": "Machine learning-based diabetes risk prediction system using real-world dataset with multiple models and evaluation.",
        "status": "deployed",
        "link": '<a href="https://github.com/Abuthwahir/type2-diabetes-using-PIMA_Dataset-and-Lifestyle-Factor" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    },
    {
        "id": "2",
        "name": "YouTube Video Analyzer",
        "file": "yt_analyzer.js",
        "img": "Youtube-Video-Analyser.png",
        "tech": ['<span class="badge bright">React</span>', '<span class="badge">Node.js</span>', '<span class="badge">AI APIs</span>', '<span class="badge">Chrome Extension</span>'],
        "desc": "Chrome extension to analyze YouTube videos and generate insights directly on the video page.",
        "status": "production",
        "link": '<a href="https://github.com/Abuthwahir/Youtube-Video-Analyzer" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    },
    {
        "id": "3",
        "name": "AI Interview Coach",
        "file": "ai_coach.py",
        "img": "Ai_interview_coach.png",
        "tech": ['<span class="badge bright">Python</span>', '<span class="badge">LangChain</span>', '<span class="badge">Groq API</span>', '<span class="badge">Streamlit</span>', '<span class="badge">RAG</span>', '<span class="badge">LLM</span>', '<span class="badge">NLP</span>'],
        "desc": "Adaptive multi-turn interview simulation platform using LangChain, Groq, and Streamlit to simulate real technical interviews with memory, structured evaluation, and adaptive difficulty.<br><br>- Multi-turn interview flow with conversational memory<br>- Structured evaluation (score, strengths, improvements)<br>- Adaptive difficulty progression<br>- RAG-based job-aware question generation<br>- CLI + Streamlit interface<br>- Final performance report with transcript",
        "status": "deployed",
        "link": '<a href="https://github.com/Abuthwahir/ai-interview-coach-using-rag" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    },
    {
        "id": "4",
        "name": "Theatre Management",
        "file": "theatre_sys.sql",
        "img": "Theatre-Management-system.png",
        "tech": ['<span class="badge bright">Flask</span>', '<span class="badge">SQLAlchemy</span>'],
        "desc": "Full-stack theatre booking system with real-time seat management and admin controls.",
        "status": "stable",
        "link": '<a href="https://github.com/Abuthwahir/theatre-management-system-using-SQL" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    },
    {
        "id": "5",
        "name": "Task Management System using SpringBoot",
        "file": "task_mgr.java",
        "img": "Task-Management-System.png",
        "tech": ['<span class="badge bright">Spring Boot</span>', '<span class="badge">Java</span>'],
        "desc": "Backend-driven task management system with structured APIs and workflow handling.",
        "status": "stable",
        "link": '<a href="https://github.com/Abuthwahir/task-management-system-using-springboot" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    },
    {
        "id": "6",
        "name": "Top Level Domain Predictor Game",
        "file": "domain_svc.py",
        "img": "Domain Guesser.png",
        "tech": ['<span class="badge bright">Flask</span>', '<span class="badge">Machine Learning</span>'],
        "desc": "Machine learning application to predict domain extensions using text-based features.",
        "status": "optimized",
        "link": '<a href="https://github.com/Abuthwahir/TLD-Predictor" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    },
    {
        "id": "7",
        "name": "Type 2 Diabetes (T2DM) Risk Assessment (NHANES+XAI)",
        "file": "nhanes_xai.py",
        "img": "Type2-NHANES.png",
        "tech": ['<span class="badge bright">Python</span>', '<span class="badge">SHAP</span>', '<span class="badge">XGBoost</span>'],
        "desc": 'Advanced ML project using NHANES dataset with Explainable AI for model interpretation.<br><span class="text-xs dim">(Will be made public soon)</span>',
        "status": "private",
        "link": '<span class="btn-private" title="Repository is Private">PRIVATE_REPO_🔐</span>'
    },
    {
        "id": "8",
        "name": "Multimodal Stock Market Analysis Dashboard (Capstone)",
        "file": "finance_dashboard.py",
        "img": "Stock-Analysis.png",
        "tech": ['<span class="badge bright">Data Analysis</span>', '<span class="badge">Visualization</span>'],
        "desc": 'Capstone project focused on financial data analysis and visualization.<br><span class="text-xs dim">(Pending publication)</span>',
        "status": "private",
        "link": '<span class="btn-private" title="Repository is Private">PRIVATE_REPO_🔐</span>'
    },
    {
        "id": "9",
        "name": "GTG Perfumes frontend design using Figma",
        "file": "gtg_perfumes.html",
        "img": "GTG-perfumes.png",
        "tech": ['<span class="badge bright">HTML</span>', '<span class="badge">CSS</span>', '<span class="badge">JavaScript</span>'],
        "desc": "Frontend project replicating a Figma design into a responsive website.",
        "status": "deployed",
        "link": '<a href="https://github.com/Abuthwahir/gtg-perfumes" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    }
]

html_chunks = ['            <div class="grid">']

for p in projects:
    techs = "".join(p["tech"])
    s = f"""                <!-- {p['id']}. {p['name']} -->
                <div class="flip-card vault-card focus-card group project-flip">
                    <div class="flip-card-inner">
                        <!-- FRONT -->
                        <div class="flip-card-front">
                            <div class="term-header">
                                <div class="dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div><span class="filename">{p['file']}</span>
                            </div>
                            <div class="project-preview">
                                <img src="assets/project/{p['img']}" alt="{p['name']}">
                            </div>
                            <div class="front-content">
                                <h3>{p['name']}</h3>
                                <div class="tech" style="flex-wrap: wrap;">{techs}</div>
                            </div>
                        </div>
                        <!-- BACK -->
                        <div class="flip-card-back">
                            <div class="term-header">
                                <div class="dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div><span class="filename">{p['file']}</span>
                            </div>
                            <div class="back-content">
                                <p class="desc scroll-text" style="line-height:1.5;">{p['desc']}</p>
                                <div class="card-ftr">
                                    <span class="status">{p['status']}</span>
                                    <div class="links">{p['link']}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>"""
    html_chunks.append(s)

html_chunks.append('            </div>')
new_grid = "\n".join(html_chunks)

# Regex to safely replace just the grid inside projects
pattern = re.compile(r'(\<section id="projects" class="projects reveal"\>.*?\<h2 class="sec-title"\>Deployment_Vault \<span class="line"\>\<\/span\>\<\/h2\>\s*)\<div class="grid"\>.*?\<\/div\>(\s+\<\/section\>)', re.DOTALL)

def repl(match):
    return match.group(1) + new_grid + match.group(2)

new_content = pattern.sub(repl, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated successfully.")
