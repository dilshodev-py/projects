with open("matn.txt", "r") as f:
    users = f.read().splitlines()

result = []
for user in users:
    result.append(" ".join(user.strip().split()))

result = "\n".join(result)
with open("matn.txt", "w") as f:
    f.write(result)