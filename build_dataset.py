out = open("data.txt", "w", encoding="utf-8")
for f in ["wiki.txt", "namu.txt"]:
    with open(f, encoding="utf-8") as inp:
        for line in inp:
            out.write(line.strip() + "\n")
out.close()
print("dataset ready")
