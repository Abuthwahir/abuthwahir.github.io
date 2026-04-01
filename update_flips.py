import re
import html

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

def mktec(techs):
    res = []
    for t in techs:
        cls = 'badge bright' if t in ['Python', 'Flask', 'React', 'Spring Boot', 'HTML', 'BiLSTM'] else 'badge'
        res.append(f'<span class="{cls}">{t}</span>')
    return "".join(res)

projects = [
    {
        "id": "1",
        "name": "Type 2 Diabetes Risk Prediction using PIMA Dataset (XAI + Lifestyle Modeling)",
        "file": "diabetes_pima.py",
        "img": "diabetes.png",
        "tech": mktec(['Python', 'Scikit-learn', 'XGBoost', 'SHAP', 'Pandas', 'RF']),
        "desc": "Machine learning-based diabetes risk prediction system built on the PIMA dataset, enhanced with lifestyle-based feature engineering (BMI, glucose levels, activity patterns).<br><br>Implemented multiple models and optimized using XGBoost. Integrated SHAP (Explainable AI) for model interpretability, enabling feature contribution analysis for individual predictions.<br><br>Designed an end-to-end ML pipeline including preprocessing, feature scaling, model training, evaluation, and explainability visualization.",
        "status": "deployed",
        "link": '<a href="https://github.com/Abuthwahir/type2-diabetes-using-PIMA_Dataset-and-Lifestyle-Factor" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    },
    {
        "id": "2",
        "name": "Taskie – Theatre Management System (Flask-Based Booking Engine)",
        "file": "theatre_sys.py",
        "img": "Theatre-Management-system.png",
        "tech": mktec(['Flask', 'SQLAlchemy', 'Python', 'SQLite']),
        "desc": "Developed a full-stack theatre booking system using Flask (NOT MERN), supporting real-time seat selection, booking workflows, and admin-level control.<br><br>Designed relational database schemas using SQLAlchemy and implemented dynamic seat allocation logic.<br><br>Features include user booking flows, admin dashboard, and efficient transaction handling.<br><br>Focused on backend architecture, database consistency, and scalable design patterns.",
        "status": "stable",
        "link": '<a href="https://github.com/Abuthwahir/theatre-management-system-using-SQL" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    },
    {
        "id": "3",
        "name": "YouTube Video Analyzer (Chrome Extension with AI Insights)",
        "file": "yt_analyzer.js",
        "img": "Youtube-Video-Analyser.png",
        "tech": mktec(['React', 'Node.js', 'Chrome Extension API', 'AI APIs']),
        "desc": "Built a Chrome extension that overlays directly on YouTube pages to analyze video content in real time.<br><br>Extracts metadata, captions, and engagement signals to generate AI-driven insights.<br><br>Implements browser extension architecture with content scripts, background scripts, and API integrations.<br><br>Designed for productivity enhancement, enabling users to quickly understand video content without full viewing.",
        "status": "production",
        "link": '<a href="https://github.com/Abuthwahir/Youtube-Video-Analyzer" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    },
    {
        "id": "4",
        "name": "Multimodal Financial Market Analysis using Deep Learning (Capstone)",
        "file": "finance_model.py",
        "img": "Stock-Analysis.png",
        "tech": mktec(['BiLSTM', 'CNN', 'BERT', 'VADER', 'Python']),
        "desc": "Capstone project focused on multimodal financial analysis combining time-series data and textual sentiment.<br><br>Implemented hybrid deep learning architecture:<br>• BiLSTM for temporal patterns<br>• CNN for feature extraction<br>• BERT for financial text understanding<br>• Fallback sentiment analysis using VADER<br><br>Designed a robust pipeline integrating numerical and textual signals for improved prediction accuracy.<br><br>Currently under research and paper writing phase; will be made public soon.",
        "status": "private",
        "link": '<span class="btn-private" title="Repository is Private">PRIVATE_REPO_🔐</span>'
    },
    {
        "id": "5",
        "name": "Task Management System using Spring Boot (REST API Architecture)",
        "file": "TaskController.java",
        "img": "Task-Management-System.png",
        "tech": mktec(['Spring Boot', 'Java', 'REST APIs']),
        "desc": "Developed a backend-centric task management system using Spring Boot.<br><br>Designed RESTful APIs for task creation, updates, prioritization, and workflow management.<br><br>Focused on clean architecture, modular design, and scalability.<br><br>Implements structured service layers and controller-based routing.",
        "status": "stable",
        "link": '<a href="https://github.com/Abuthwahir/task-management-system-using-springboot" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    },
    {
        "id": "6",
        "name": "Type 2 Diabetes Prediction using NHANES Dataset (XAI + Modeling)",
        "file": "nhanes_xai.py",
        "img": "Type2-NHANES.png",
        "tech": mktec(['Python', 'XGBoost', 'RF', 'LightGBM', 'LogReg', 'SHAP', 'Pandas']),
        "desc": "Advanced diabetes prediction system using NHANES dataset enriched with lifestyle and exercise-related features.<br><br>Applied XGBoost for high-performance prediction and SHAP for explainability.<br><br>Focused on real-world health analytics and interpretability of medical predictions.<br><br>Includes preprocessing of complex healthcare datasets and feature importance visualization.",
        "status": "private",
        "link": '<span class="btn-private" title="Repository is Private">PRIVATE_REPO_🔐</span>'
    },
    {
        "id": "7",
        "name": "Top-Level Domain Prediction using TF-IDF & Machine Learning Pipelines",
        "file": "domain_svc.py",
        "img": "Domain Guesser.png",
        "tech": mktec(['Python', 'TF-IDF', 'NLP', 'Scikit-learn']),
        "desc": "Developed an NLP-based system to predict domain extensions using textual patterns.<br><br>Implemented TF-IDF vectorization for feature extraction and trained classification models.<br><br>Includes two functional pipelines:<br>1. Prediction mode (input → domain classification)<br>2. Interactive mode (game-like guessing system for unknown domains)<br><br>Focuses on text-based feature engineering and lightweight ML deployment.",
        "status": "optimized",
        "link": '<a href="https://github.com/Abuthwahir/TLD-Predictor" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    },
    {
        "id": "8",
        "name": "GTG Perfumes – Figma-to-Code Frontend Implementation",
        "file": "gtg_perfumes.html",
        "img": "GTG-perfumes.png",
        "tech": mktec(['HTML', 'CSS', 'JavaScript']),
        "desc": "Frontend project focused on replicating a Figma design into a fully responsive website.<br><br>Implemented pixel-perfect layout, responsive design, and interactive UI elements.<br><br>Demonstrates strong fundamentals in HTML, CSS, and JavaScript without frameworks.",
        "status": "deployed",
        "link": '<a href="https://github.com/Abuthwahir/gtg-perfumes" target="_blank" class="btn-link hover-neon text-neon" style="display:flex;align-items:center;">VIEW_CODE &gt;&gt;</a>'
    }
]

html_chunks = ['            <div class="grid">']

for p in projects:
    techs = p["tech"]
    s = f"""                <!-- {p['id']}. {p['name']} -->
                <div class="flip-card vault-card focus-card group project-flip">
                    <div class="flip-card-inner">
                        <!-- FRONT -->
                        <div class="flip-card-front">
                            <div class="term-header">
                                <div class="dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div><span class="filename">{p['file']}</span>
                            </div>
                            <div class="project-preview">
                                <img src="assets/project/{p['img']}" alt="{html.escape(p['name'])}">
                            </div>
                            <div class="front-content">
                                <h3 style="font-size: 1.15rem;">{p['name']}</h3>
                                <div class="tech" style="flex-wrap: wrap;">{techs}</div>
                            </div>
                        </div>
                        <!-- BACK -->
                        <div class="flip-card-back">
                            <div class="term-header">
                                <div class="dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div><span class="filename">{p['file']}</span>
                            </div>
                            <div class="back-content">
                                <div class="scroll-wrap" style="flex:1; overflow-y:auto; padding-right:8px; margin-bottom:1rem;">
                                    <p class="desc scroll-text" style="line-height:1.6; font-size:0.9rem;">{p['desc']}</p>
                                </div>
                                <div class="card-ftr" style="margin-top:auto; padding-top:10px; border-top:1px solid rgba(180,255,0,0.1);">
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

pattern = re.compile(r'(\<section id="projects" class="projects reveal"\>.*?\<h2 class="sec-title"\>Deployment_Vault \<span class="line"\>\<\/span\>\<\/h2\>\s*)\<div class="grid"\>.*?\<\/div\>(\s+\<\/section\>)', re.DOTALL)

def repl(match):
    return match.group(1) + new_grid + match.group(2)

new_content = pattern.sub(repl, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated exactly!")
