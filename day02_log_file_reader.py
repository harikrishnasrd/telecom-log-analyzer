# Day 2 - Log File Reader and Keyword Hunter
# Opens a real log file, searches for keywords, counts pass/fail
# Part of Apple Modem System Test Engineer prep

search_word = "error"  # change this to any keyword in your log

total_lines = 0
matched_lines = 0

with open(r"C:\Users\sre78973\Desktop\console.log", "r") as file:
    for line in file:
        # count every line we read
        total_lines += 1

        # check if our keyword exists in this line (case insensitive)
        if search_word.lower() in line.lower():
            matched_lines += 1
            print(line.strip())

print(f"\n=== SUMMARY ===")
print(f"Total lines   : {total_lines}")
print(f"Matched lines : {matched_lines}")
