import os

folder_path = "C:/Users/DELL/Downloads/math"

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

       
        name = lines[0].strip()
        number = lines[1].strip()

      
        full_text = "".join(lines[2:]).strip()

        
        example = ""
        description = full_text

        if "Example" in full_text:
            parts = full_text.split("Example", 1)
            description = parts[0].strip()
            example = "Example" + parts[1].strip()

        
        print("File:", filename)
        print("Name:", name)
        print("Number:", number)
        print("Description:", description[:200], "...")  
        print("Example:", example[:200], "...")
        print("-" * 50)