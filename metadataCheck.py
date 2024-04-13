# Helper to check missing metadata in an audio library, correcting them and updating the library with correct metadata

import sys
import os
from mutagen.id3 import ID3

def missingMetadata(filePath):
    audio = ID3(filePath)
    if not audio:
        return True
    else:
        return False
    
def checkAudio(filePath):
    audioExtensions = [
        ".mp3", ".wav", ".flac", ".m4a", ".wma", ".aac", 
        ".ogg", ".aiff", ".alac", ".ape", ".opus", ".mpc", 
        ".wv", ".tta", ".dsf", ".dff", ".webm", ".mp4"
    ]
    if any(filePath.endswith(ext) for ext in audioExtensions):
        return True
    else:
        return False

def updateMetadata(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filePath = os.path.join(root, file)
            if not checkAudio(filePath):
                continue
            if missingMetadata(filePath):
                with open("missing_metadata.txt", "a") as f:
                    f.write(filePath + "\n")
            else:
                audio = ID3(filePath)
                missing_fields = []
                if "TCON" not in audio:
                    missing_fields.append("Genre")
                if "TPE2" not in audio:
                    missing_fields.append("Album Artist")
                if "TPE1" not in audio:
                    missing_fields.append("Artist")
                if "TDRC" not in audio:
                    missing_fields.append("Year")
                if "TIT2" not in audio:
                    missing_fields.append("Title")
                if "TALB" not in audio:
                    missing_fields.append("Album")
                if "APIC:" not in audio:
                    missing_fields.append("Cover")
                
                # This write missing fields in a file to be corrected manually
                for field in missing_fields:
                    with open(f"missing_{field.lower()}.txt", "a") as f:
                        f.write(filePath + "\n")
            

if len(sys.argv) < 2:
    directory_path = os.getcwd()
else:
    directory_path = sys.argv[1]


updateMetadata(directory_path)

