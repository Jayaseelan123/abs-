import os
import re

dir_path = r'e:\demo abs'

navbar_html = '''    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg fixed-top navbar-light bg-glass py-3">
        <div class="container">
            <a class="navbar-brand text-decoration-none" href="index.html">
                <img src="logo23.png" alt="ABS Academy Logo" style="height: 80px; object-fit: contain;">
            </a>
            <button class="navbar-toggler border-0 shadow-none" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-center">
                    <li class="nav-item mx-2"><a class="nav-link fw-semibold text-muted" href="index.html">Home</a></li>
                    <li class="nav-item mx-2"><a class="nav-link fw-semibold text-muted" href="about.html">About</a></li>
                    <li class="nav-item dropdown mx-2">
                        <a class="nav-link dropdown-toggle fw-semibold text-muted" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Course
                        </a>
                        <ul class="dropdown-menu border-0 shadow-lg p-3 rounded-4" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item rounded-3 py-2 px-3 fw-medium small mb-1" href="ai-development.html">AI Development</a></li>
                            <li><a class="dropdown-item rounded-3 py-2 px-3 fw-medium small mb-1" href="ai-automations.html">AI Automations</a></li>
                            <li><a class="dropdown-item rounded-3 py-2 px-3 fw-medium small mb-1" href="digital-marketing-ai.html">Digital Marketing with AI</a></li>
                            <li><a class="dropdown-item rounded-3 py-2 px-3 fw-medium small mb-1" href="web-development.html">Web Development</a></li>
                            <li><a class="dropdown-item rounded-3 py-2 px-3 fw-medium small mb-1" href="full-stack-development.html">Full Stack Development</a></li>
                            <li><a class="dropdown-item rounded-3 py-2 px-3 fw-medium small mb-1" href="graphic-design.html">Graphic Design</a></li>
                            <li><hr class="dropdown-divider opacity-10"></li>
                            <li><a class="dropdown-item rounded-3 py-2 px-3 fw-bold small text-primary" href="courses.html">View All Courses</a></li>
                        </ul>
                    </li>
                    <li class="nav-item mx-2"><a class="nav-link fw-semibold text-muted" href="workshops.html">Workshops</a></li>
                    <li class="nav-item mx-2"><a class="nav-link fw-semibold text-muted" href="summer-camp.html">Summer Camp</a></li>
                    <li class="nav-item mx-2"><a class="nav-link fw-semibold text-muted" href="careers.html">Careers</a></li>
                    <li class="nav-item mx-2"><a class="nav-link fw-semibold text-muted" href="contact.html">Contact Us</a></li>
                </ul>
            </div>
        </div>
    </nav>'''

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find navbar start and end
        nav_start = content.find('<!-- Navbar -->')
        nav_end = content.find('</nav>') + 6
        
        if nav_start != -1 and nav_end != -1:
            content = content[:nav_start] + navbar_html + content[nav_end:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Standardized navbar in {filename}')

