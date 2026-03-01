import glob
import os

files = glob.glob("*.html")
count = 0
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Update navigation
    if '<footer class="site-footer">\n        <div class="container">' in content:
        new_content = content.replace('<footer class="site-footer">\n        <div class="container">', '<footer class="site-footer">\n        <div class="container text-center">')
        if new_content != content:
            with open(f, "w", encoding="utf-8") as file:
                file.write(new_content)
            count += 1
            
print(f"Alignment updated in {count} HTML files.")
