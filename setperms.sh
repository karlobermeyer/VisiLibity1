#!/bin/bash

# Recursively set permissions for website directories and files.

# r, w, x
# 4, 2, 1
# For directories, x => navigability
# chmod [ugoa][+-][rwx]

# Directories
# 7 = 4 + 2 + 1 => owner can r, w, x
# 5 = 4 + 1 => group can r, x
# 5 = 4 + 1 => others can r, x
find . -type d -exec chmod 755 {} \;

# Files
# 6 = 4 + 2 => owner can r, w
# 4 => group can r
# 4 => others can r
find . -type f -exec chmod 644 {} \;

# Restore owner-executability of script(s)
# chmod u+x ./setperms.sh
# chmod u+x ./use_notes/make_python_package.sh
find . -name "*.sh" -exec chmod u+x {} \;
