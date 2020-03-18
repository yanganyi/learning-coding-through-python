# ========= ===============================================================
# Character Meaning
# --------- ---------------------------------------------------------------
# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
# 'U'       universal newline mode (deprecated)
# ========= ===============================================================

with open("Hey_", "a+") as file:
    file.write("\nHey this is written in lesson 77!")
    file.seek(0)    # cursor is put back to 0 position
    content = file.read()

print(content)