import os

count = 0

for filename in os.listdir("C:/Users/Adit/code/PERSONAL/piton/bot-discord/prefix_command"):
    if (filename.endswith(".py")) and (filename != "__init__.py"):
        count += 1

print(f"Loaded {count} prefix commands")