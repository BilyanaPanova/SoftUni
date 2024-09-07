file_path = input().split("\\")

need_file_information = file_path[-1]
name, extension = need_file_information.split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")
