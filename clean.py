import csv

filename = "all-agents"
name_list = []
with open(f"{filename}.csv") as old_file:
    line_list = old_file.readlines()
    with open(f"{filename}-cleaned.csv", 'a') as cleaned_file:
        fieldnames = ["zip", "name", "email", "phone", "facebook", "instagram", "url"] # linkedin
        writer = csv.DictWriter(cleaned_file, fieldnames=fieldnames)
        writer.writeheader()
        for agent_line in line_list:
            if agent_line == "\n":
                continue
            else:
                agent_zip, name, email, phone, facebook, insta, url = agent_line.split(",")
                name_list_copy = name_list.copy()
                if name in name_list_copy:
                    continue
                else:
                    cleaned_agent = {
                        "zip": agent_zip,
                        "name": name,
                        "email": email,
                        "phone": phone,
                        "facebook": facebook if "compass" not in facebook else "None",
                        "instagram": insta if "compass" not in insta else "None",
                        "url": url
                    }
                    writer.writerow(cleaned_agent)
                    name_list.append(name)

print(len(name_list))