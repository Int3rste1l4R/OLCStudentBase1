members = ""
with open("members.csv","r") as f:
    members = f.readlines()
    for s in members:
        s_list = s.split(",")
        print(s_list[1])