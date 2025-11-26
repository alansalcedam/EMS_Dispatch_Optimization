import subprocess

print("Running supervised models...")
subprocess.run(["python", "src/supervised/supervised_models_drive.py"])

print("Running unsupervised models...")
subprocess.run(["python", "src/unsupervised/unsupervised_models_drive.py"])
