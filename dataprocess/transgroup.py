#train id:0-42622
#valid id:42623-47957
#test id:47958-53285
def transgroup(group_file_path,save_path):
    group_output = open(save_path,"w")
    group_file = open(group_file_path)
    group = ""
    group_data = []
    for line in group_file:
        if not line:
            break
        splits = line.strip().split("	")
        if splits[2]!=group:
            group_output.write(str(len(group_data))+"\n")
            group_data = []
        group = splits[2]
        group_data.append(splits[0])

    group_output.write(str(len(group_data)) + "\n")
    group_output.close()
    group_file.close()
if __name__ =="__main__":
    transgroup("gt.valid.txt","group.valid.txt")
