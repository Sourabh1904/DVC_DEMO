import os

dir=[
  os.path.join("data","raw"),
  os.path.join("data","processed"),
  "notebooks",
  "saved_models",
  "src"
]

files_=[
"dvc.yaml",
"params.yaml",
".gitignore",
os.path.join("src","__init__.py"),


]
for i in dir:
    os.makedirs(i,exist_ok=True)
    with open(os.path.join(i,".gitkeep"),"w") as f:
        pass 

for j in files_:
    with open(j,"w") as f:
        pass