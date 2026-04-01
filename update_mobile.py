import codecs
import re

with codecs.open('style.css', 'r', 'utf-8') as f:
    css = f.read()

# 1. name font-size: 4rem;
css = css.replace("font-size: 4rem;", "font-size: clamp(2.5rem, 8vw, 4rem);")

# 2. sec-title font-size: 2.5rem;
css = css.replace("font-size: 2.5rem;", "font-size: clamp(1.8rem, 5vw, 2.5rem);")

# 3. title font-size: 1.5rem;
css = css.replace("font-size: 1.5rem;", "font-size: clamp(1.1rem, 3vw, 1.5rem);")

# 4. desc font-size: 1.25rem;
css = css.replace("font-size: 1.25rem;", "font-size: clamp(1rem, 2.5vw, 1.25rem);")

# 5. .term-window structural width fix
css = css.replace("""
.term-window {
  background: linear-gradient(135deg, rgba(26, 26, 39, 0.7), rgba(13, 13, 25, 0.5));
  border: 1px solid var(--border);
  border-radius: 8px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(10px);
}""", """
.term-window {
  width: 100%;
  box-sizing: border-box;
  background: linear-gradient(135deg, rgba(26, 26, 39, 0.7), rgba(13, 13, 25, 0.5));
  border: 1px solid var(--border);
  border-radius: 8px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(10px);
}""")

# 6. Hero image scaling constraints
css = css.replace('width: 240px;\n  height: 240px;', 'width: clamp(160px, 40vw, 240px);\n  height: clamp(160px, 40vw, 240px);')

# 7. Media query replacement
new_query = """@media (max-width: 768px) {
  body {
    overflow-x: hidden;
  }
  .sidebar {
    transform: translateX(-100%);
  }
  .sidebar.show {
    transform: translateX(0);
  }
  .mobile-btn {
    display: block;
  }
  .topbar {
    display: none;
  }
  .content {
    margin-left: 0;
    padding: 1.5rem;
    padding-top: 5rem;
    width: 100%;
    box-sizing: border-box;
    overflow-x: hidden;
  }
  .hero-content {
    flex-direction: column-reverse;
    text-align: center;
    gap: 2rem;
  }
  .hero-btns {
    justify-content: center;
  }
  /* Reduce Visual Noise */
  .term-window {
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(4px);
  }
  /* Fix vertical constraint */
  .v-line {
    left: 10px;
  }
  .t-item {
    padding-left: 1rem;
    margin-left: 0.5rem;
  }
  /* Grid Constraints */
  .grid {
    grid-template-columns: 1fr !important;
    gap: 1.5rem;
  }
  /* Optimal Flip Card on Mobile */
  .flip-card {
    min-height: 500px;
    max-width: 450px;
    margin: 0 auto;
    width: 100%;
  }
  .project-preview {
    height: 160px;
  }
  .front-content {
    padding: 1.2rem;
    gap: 0.8rem;
  }
  .front-content h3 {
    font-size: 1.15rem !important;
  }
  .back-content {
    padding: 1.5rem 1.25rem;
  }
  .scroll-text {
    max-height: 200px;
  }
}
"""

css = re.sub(r'(?s)@media \(max-width: 768px\) \{.*?\}(?=\n/\* Floating)', new_query, css)

with codecs.open('style.css', 'w', 'utf-8') as f:
    f.write(css)
print("Mobile Resizing Rebuilt!")
