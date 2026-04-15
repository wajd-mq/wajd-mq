import os

folder = "C:/Users/DELL/Downloads/math"

for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        
        path = folder + "/" + filename
        file = open(path, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        
        name = lines[0].strip()
        number = lines[1].strip()
        full_text = ""
        for line in lines[2:]:
            full_text = full_text + line
        full_text = full_text.strip()
        
        if "Example" in full_text:
            parts = full_text.split("Example", 1)
            description = parts[0].strip()
            example = "Example" + parts[1].strip()
        else:
            description = full_text
            example = "No example found"
        
        
        print("File:", filename)
        print("Name:", name)
        print("Number:", number)
        print("Description:", description)
        print("Example:", example)
        print("----------------------------")
            