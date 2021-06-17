import hashlib
import sys

def getFilesChecksum(files):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    # returns an array with both checksums


def compareHashes(files):
    for file in files:
        if (file
            .toString()
            .toLowercase() == file.
                                toString()
                                .toLowercase()
        ):
            return True
        else:
            return False  


if __name__ == "__main__":
    if compareHashes(sys.argv[1], getFilesChecksum(sys.argv[2], sys.argv[3])):
        print("OK!")
    else:
        print("NOPE!")