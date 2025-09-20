#!/bin/bash
#========================================================================#
# Safe Multi-Directory, Multi-Pattern Deletion Script                    #
#------------------------------------------------------------------------#
# Author: Narender Kumar                                                 #
#------------------------------------------------------------------------#
# This script deletes multiple files/patterns from multiple directories  #
# in one go, after a single final confirmation.                          #
#========================================================================#

start=$(date +%s)

echo "Current directory: $(pwd)"

# Get directories
read -p "Enter directories (separated by space): " -a directories

# Check directories
for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        echo "Directory '$dir' does not exist! Exiting."
        exit 1
    fi
done

# Show size and largest files for each directory
for dir in "${directories[@]}"; do
    echo ""
    echo "-----------------------------"
    echo "Directory: $dir"
    du -sh "$dir"
    echo "Top 5 largest files in $dir:"
    find "$dir" -type f -exec du -h {} + | sort -hr | head -5
    echo "-----------------------------"
done

# Get patterns
read -p "Enter file names or patterns to delete (separated by space, e.g., '*.tmp' '*.bak' 'test.txt'): " -a patterns

# Recursive?
read -p "Do you want to search subdirectories as well? [y/n]: " recurse
if [[ "${recurse,,}" == "y" ]]; then
    depth_arg=""
else
    depth_arg="-maxdepth 1"
fi

# Collect files to be deleted
declare -a all_matches
echo ""
echo "Files that will be deleted:"
for dir in "${directories[@]}"; do
    for pat in "${patterns[@]}"; do
        matches=$(find "$dir" $depth_arg -type f -name "$pat")
        if [ -n "$matches" ]; then
            echo "$matches"
            while IFS= read -r file; do
                all_matches+=("$file")
            done <<< "$matches"
        fi
    done
done

if [ ${#all_matches[@]} -eq 0 ]; then
    echo "No files found matching your patterns."
    exit 0
fi

# Single last confirmation, no further prompts after this!
echo ""
read -p "Type 'delete' (exactly) to PERMANENTLY delete ALL the above files: " confirm
if [ "$confirm" != "delete" ]; then
    echo "Aborted. No files deleted."
    exit 0
fi

# Perform deletion
for file in "${all_matches[@]}"; do
    echo "Deleting: $file"
    rm -f -- "$file"
done

echo "All matching files deleted."
end=$(date +%s)
echo "Execution time: $((end - start)) seconds."
