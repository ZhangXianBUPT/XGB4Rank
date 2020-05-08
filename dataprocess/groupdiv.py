#train id:0-42622
#valid id:42623-47957
#test id:47958-53285
def transdata(group_file_path,out_feature_path_train,out_feature_path_vaild,out_feature_path_test):
    output_feature_train = open(out_feature_path_train,"w")
    output_feature_valid = open(out_feature_path_vaild, "w")
    output_feature_test = open(out_feature_path_test, "w")
    groups = open(group_file_path)
    for line in groups:
        if not line:
            break
        splits_x = line.strip().split("	")
        if int(splits_x[1]) < 42623:
            output_feature_train.write(line)
        if int(splits_x[1]) > 42622 and int(splits_x[1]) < 47958:
            output_feature_valid.write(line)
        if int(splits_x[1]) > 47957:
            output_feature_test.write(line)

    output_feature_train.close()
    output_feature_valid.close()
    output_feature_test.close()

if __name__ =="__main__":
    transdata("gt.txt","gt.train.txt","gt.valid.txt","gt.test.txt")