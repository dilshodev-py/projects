import subprocess


def restart_python_project():
    python_script = 'dilshod.py'
    command = ['python', python_script]
    try:
        process = subprocess.Popen(command, shell=False)
        print("Python project restarted successfully.")
        process.wait()
    except Exception as e:
        print("Error:", e)

restart_python_project()
