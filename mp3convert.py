# Converts all audio files in a directory containing an audio library to MP3 format for smaller file size

import os
import shutil
import sys

# Define the source directory
srcDir = sys.argv[1] if len(sys.argv) > 1 else "."

# Define the destination directory
outputDir = "_MP3"

audioExtensions = [
    ".mp3", ".wav", ".flac", ".m4a", ".wma", ".aac", 
    ".ogg", ".aiff", ".alac", ".ape", ".opus", ".mpc", 
    ".wv", ".tta", ".dsf", ".dff", ".webm", ".mp4"
]

# Create the destination directory if it doesn't exist
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

# Traverse through the directory and its subdirectories
for root, dirs, files in os.walk(srcDir):
    for file in files:
        # Check if the file is an audio file
        if any(file.endswith(ext) for ext in audioExtensions):
            # Create the same directory structure in the destination directory
            outputPath = os.path.join(outputDir, os.path.relpath(root, srcDir))
            if not os.path.exists(outputPath):
                os.makedirs(outputPath)
            
            if file.endswith(".mp3"):
                # Move the MP3 file to the destination directory
                print("Moving", file, "to", outputPath)
                shutil.move(os.path.join(root, file), os.path.join(outputPath, file))
                continue
            else:
                # Convert the audio file to MP3 using ffmpeg
                outputFile = os.path.splitext(file)[0] + ".mp3"
                print("Converting", file, "to", outputFile)
                inputPath = os.path.join(root, file)
                outputFilePath = os.path.join(outputPath, outputFile)
                ffmpeg_command = f'ffmpeg -i "{inputPath}" -ab 320k "{outputFilePath}"'
                if os.system(ffmpeg_command):
                    print("An error occurred while converting", file)
                else:
                    print("Successfully converted", file, "to", outputFile)
                # Remove the original audio file (?)
                # os.remove(os.path.join(root, file))