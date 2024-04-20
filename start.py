import datetime
import os
import ffmpeg
import sys

def extract_webm_creation_time(file_path):
    creation_time_epoch = os.path.getctime(file_path)
    creation_time = datetime.datetime.fromtimestamp(creation_time_epoch)
    return creation_time

def collect_webm_paths_and_creation_times(directory_path):
    webms_and_creation_times = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file == "output.webm":
                full_path = os.path.join(root, file)
                creation_time = extract_webm_creation_time(full_path)
                webms_and_creation_times.append((full_path, creation_time))
    return webms_and_creation_times

def combine_webms_in_order_and_save(webms_and_creation_times, output_path):

    webms_and_creation_times.sort(key=lambda x: x[1]) 
    
    with open('temp.txt', 'w') as f:
        for path, _ in webms_and_creation_times:
            f.write(f"file '{path}'\n")

    with open('temp2.txt', 'w') as f:
        for path, creation_time in webms_and_creation_times:
            f.write(f"File: {path}, Creation Time: {creation_time}\n")

    ffmpeg.input('temp.txt', format='concat', safe=0, ).output(output_path, vcodec='libx264').global_args('-hwaccel', 'auto', '-threads', '12').run()

    os.remove('temp.txt')  # clean up temporary file

def long_movie_collector():
    webms_and_creation_times = []
    for root, dirs, files in os.walk("."):
        if root.count(os.sep) == 2:  # Only collect if nested 2 times
            for file in files:
                if file == "output.webm":
                    full_path = os.path.join(root, file)
                    creation_time = extract_webm_creation_time(full_path)
                    webms_and_creation_times.append((full_path, creation_time))
    return webms_and_creation_times

def main():
    option = str(sys.argv[1])
    if option == "long":
        webms_and_creation_times = long_movie_collector()
        for path, creation_time in webms_and_creation_times:
            print(f"File: {path}, Creation Time: {creation_time}")

        combine_webms_in_order_and_save(webms_and_creation_times, "output.mp4")
    elif option == "short":
        pathss = str(sys.argv[2])
        webms_and_creation_times = collect_webm_paths_and_creation_times(pathss)
        for path, creation_time in webms_and_creation_times:
            print(f"File: {path}, Creation Time: {creation_time}")
        
        combine_webms_in_order_and_save(webms_and_creation_times, pathss + "/output.mp4")
    else:
        print("Invalid option. Please use 'long' or 'short'.")

if __name__ == '__main__':
    main()


# example dir structure
# Main Dir
#   Long id
#       Long id
#           output.webm
#       Long id
#           output.webm
#   Long id
#       Long id
#           output.webm
#       Long id
#           output.webm
#   Long id
#       Long id
#           output.webm
#       Long id
#           output.webm
#   Long id
#       Long id
#           output.webm
#       Long id
#           output.webm
#   Long id
#       Long id
#           output.webm
#       Long id
#           output.webm