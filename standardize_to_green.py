import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

replacements = {
    r'\btext-primary\b': 'text-success',
    r'\btext-info\b': 'text-success',
    r'\btext-warning\b': 'text-success',
    r'\bbg-primary\b': 'bg-success',
    r'\bbg-info\b': 'bg-success',
    r'\bbg-warning\b': 'bg-success',
    r'\bbg-soft-blue\b': 'bg-soft-green',
    r'\bbg-soft-blue-gradient\b': 'bg-soft-green',
    r'\bbtn-primary\b': 'btn-success',
    r'\bbtn-outline-primary\b': 'btn-outline-success',
    r'\bborder-primary\b': 'border-success',
    r'\bborder-info\b': 'border-success',
    r'\bborder-warning\b': 'border-success',
    # Specific attribute patterns
    r'rgba\(13, 202, 240, 0\.1\)': 'rgba(38, 185, 119, 0.1)',
    r'rgba\(255, 193, 7, 0\.1\)': 'rgba(38, 185, 119, 0.1)',
}

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for pattern, replacement in replacements.items():
        new_content = re.sub(pattern, replacement, new_content)
    
    # Custom fix for the gradient text if needed, but usually text-gradient is fine
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes in {filename}")
