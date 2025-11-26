import os
import shutil

dir = "concepts"
input_file = 'input.txt'  # Correct filename


try:
    with open(os.path.join(dir, input_file), 'r') as file: # with statement ensures file is closed after its suite finishes
        content = file.read()
        print(content)


except FileNotFoundError:
    print(f"Error: The file {input_file} was not found in the directory {dir}.")
except IOError:
    print(f"Error: An I/O error occurred while handling the file {input_file}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")




# Writing to a file
output_file = 'output.txt'
try:
    with open(os.path.join(dir, output_file), 'w') as file: # 'w' mode for writing, creates file if it doesn't exist
        file.write("This is a sample output file.\n")
        file.write("File handling in Python is straightforward and efficient.\n")
    print(f"Data written to {output_file} successfully.")
except IOError:
    print(f"Error: An I/O error occurred while writing to the file {output_file}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")




# Appending to a file
try:
    with open(os.path.join(dir, output_file), 'a') as file: # 'a' mode for appending
        file.write("Appending a new line to the output file.\n")
    print(f"Data appended to {output_file} successfully.")
except IOError:
    print(f"Error: An I/O error occurred while appending to the file {output_file}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



# Reading file line by line
try:
    with open(os.path.join(dir, output_file), 'r') as file: # 'r' mode for reading
        print("Reading file line by line:")
        for line in file:
            print(line.strip())  # strip() removes leading/trailing whitespace including newline characters
except IOError:
    print(f"Error: An I/O error occurred while reading the file {output_file}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



# Using context manager to handle files
try:
    with open(os.path.join(dir, input_file), 'r') as file:
        lines = file.readlines()  # readlines() reads all lines into a list
        print("Lines read using context manager:")
        for line in lines:
            print(line.strip())
except IOError:
    print(f"Error: An I/O error occurred while handling the file {input_file}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


#clean up - remove created output file
try:
    os.remove(os.path.join(dir, output_file))
    print(f"Cleaned up: {output_file} removed.")
except OSError as e:
    print(f"Error: {e.strerror} - {e.filename}")




#using shutil to copy files
copied_file = 'copied_input.txt'
try:
    shutil.copy(os.path.join(dir, input_file), os.path.join(dir, copied_file)) # copies content and permissions
    # shutil.copyfile(os.path.join(dir, input_file), os.path.join(dir, copied_file)) # copies only content
    print(f"File copied to {copied_file} successfully.")
except IOError:
    print(f"Error: An I/O error occurred while copying the file to {copied_file}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}") 
finally:
   cleanup = True


#clean up - remove copied file
try:
    if cleanup:
        os.remove(os.path.join(dir, copied_file))
        print(f"Cleaned up: {copied_file} removed.")
    else:
        print(f"Cleanup not performed for {copied_file}.")
except OSError as e:
    print(f"Error: {e.strerror} - {e.filename}")




# Moving/Renaming files
input_moving_file = 'input2.txt'
moved_dst_file = 'moved_input.txt'
try:
    if(os.path.exists(os.path.join(dir, input_moving_file))):
        shutil.move(os.path.join(dir, input_moving_file), os.path.join(dir, moved_dst_file)) # moves or renames file
        # os.rename(os.path.join(dir, moved_dst_file), os.path.join(dir, 'renamed_input.txt')) # renames file
        # os.replace(os.path.join(dir, moved_dst_file), os.path.join(dir, 'renamed_input.txt')) # renames file, replacing if destination exists
        print(f"File moved/renamed to {moved_dst_file} successfully.")
except FileNotFoundError:
    print(f"Error: The file {input_moving_file} was not found in the directory {dir}.")
except IOError:
    print(f"Error: An I/O error occurred while moving/renaming the file to {moved_dst_file}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")




# delete file

try:
    os.remove(os.path.join(dir, moved_dst_file))
    # shutil.rmtree(os.path.join(dir, 'directory_name'))  # for removing directories
    #os.rmdir(os.path.join(dir, 'empty_directory_name'))  # for removing empty directories
    print(f"Cleaned up: {moved_dst_file} removed.")
except FileNotFoundError:
    print(f"Error: The file {moved_dst_file} was not found in the directory {dir}.")
except PermissionError:
    print(f"Error: Permission denied while trying to delete the file {moved_dst_file}.")
except OSError as e:
    print(f"Error: {e.strerror} - {e.filename}")


