#election
n = int(input("Enter number of voters:"))
vote = []
for i in range(n):
    ch = int(input("Enter choice for voter:"))
    if ch in [1, 2, 3, 4]:
        vote.append(ch)
    else:
        print("Invalid choice")
        break

print("Votes:", vote)
count = [0] * 4
for i in vote:
    count[i - 1] =count[i-1]+1
print("Vote counts:", count)
max_votes = max(count)
winner = count.index(max_votes) + 1  # Adding 1 to match candidate number (1-4)
print("The winner is candidate number:", winner)


