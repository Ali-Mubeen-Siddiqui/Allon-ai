from datetime import datetime
import os
import subprocess

def get_current_time(format):
    time = datetime.now().strftime(format)
    return time

def write_to_file(text,filename):
    
    notes_dir = "../notes"
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)
    try:
        with open(os.path.join(notes_dir, filename),"w") as notefile:
            notefile.writelines(text)
            return "successfully written"
        
    except Exception as e:
        return e
    


def execute_system_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()