import os
current_path = os.path.dirname(os.path.realpath(__file__))
path = (f"{current_path}\bin")
os.system(f"cd {path}")
print(path)
os.system("java -jar Lavalink.jar")