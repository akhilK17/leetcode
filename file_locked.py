import subprocess

def get_file_lock_count(file_path):
    try:
        # Run the lsof command piped to wc -l
        result = subprocess.run(f"lsof {file_path} | wc -l", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Check if the command ran successfully
        if result.returncode == 0:
            # Decode and strip the output to get the count
            count = int(result.stdout.decode('utf-8').strip())
            return count
        else:
            print(f"Error: {result.stderr.decode('utf-8').strip()}")
            return -1
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return -1

# Example usage:
file_path = '/Users/<UserName>/Downloads/*.pdf'
lock_count = get_file_lock_count(file_path)

if lock_count > 0:
    print(f"The file {file_path} is locked by {lock_count} processes.")
elif lock_count == 0:
    print(f"The file {file_path} is not locked by any processes.")
else:
    print("An error occurred while checking the file.")
