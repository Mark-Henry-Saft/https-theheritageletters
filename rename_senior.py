import glob
import os

files = glob.glob("story-*.html")
count = 0
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Update navigation
    new_content = content.replace("Nominate a Senior", "Nominate an Honored Elder")
    
    if new_content != content:
        with open(f, "w", encoding="utf-8") as file:
            file.write(new_content)
        count += 1

print(f"Terminology updated in {count} story files.")
