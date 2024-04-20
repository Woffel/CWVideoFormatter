# WebM Files Collector and Combiner

This script is used to collect and combine `.webm` files from a directory structure. It provides two modes of operation: `long` and `short`.

## Dependencies

- Python 3
- ffmpeg-python

## How it works

The script walks through the directory structure and collects paths of `output.webm` files along with their creation times. It then combines these `.webm` files in the order of their creation times and saves the combined file as `output.mp4`.

The `long` mode collects `.webm` files that are nested two times in the directory structure. The `short` mode collects `.webm` files from the directory specified as an argument.

## Usage

Run the script with one of the following commands:

- For `long` mode: `python start.py long`
- For `short` mode: `python start.py short directory_path`

Replace `script_name.py` with the name of this script and `directory_path` with the path of the directory from which you want to collect `.webm` files.

## Example Directory Structure
