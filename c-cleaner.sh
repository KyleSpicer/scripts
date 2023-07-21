#!/bin/bash 

# About:
# This script will recursively check all .h and .c files using "indent -linux" when invoked with -i. When invoked with "-r", it will remove all .h~ and .c~ files generated from the "indent -linux" command.

# all commands will execute from current directory and sub directories
# -i : simply runs "indent -linux" on all .c and .h files
# -r : removes all .c~ and .h~ files

# Author: CW2 Kyle Spicer
# Published: April 30, 2023


if [ "$1" == "-i" ]; then
    echo "Running indent -linux on all .c and .h files"
    find . -name "*.c" -type f -exec indent -linux {} \;
    find . -name "*.h" -type f -exec indent -linux {} \;

elif [ "$1" == "-r" ]; then
    echo "Removing all .c~ and .h~ files"
    find . -name "*.c~" -type f -delete
    find . -name "*.h~" -type f -delete
    find . -name "*.sh~" -type f -delete

else    
    echo "Usage: $0 [-i/-r]"
    echo "       -i : Indent .c and .h files using the Linux coding style"
    echo "       -r : Remove all .c~ and .h~ backup files"
fi

