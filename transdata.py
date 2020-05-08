#train id:0-42622
#valid id:42623-47957
#test id:47958-53285
def transdata(feature_file_path,group_file_path,out_feature_path_train,out_feature_path_vaild,out_feature_path_test):
    output_feature_train = open(out_feature_path_train,"w")
    output_feature_valid = open(out_feature_path_vaild, "w")
    output_feature_test = open(out_feature_path_test, "w")
    with open (feature_file_path) as features, open(group_file_path) as groups:
        for x,y in zip(features,groups):
            splits_x = x.strip().split("	")
            splits_y = y.strip().split("	")
            if int(splits_x[0])<42623:
                output_feature_train.write(splits_y[0]+" "+splits_x[1]+"\n")
            if int(splits_x[0])>42622 and int(splits_x[0])<47958:
                output_feature_valid.write(splits_y[0]+" "+splits_x[1]+"\n")
            if int(splits_x[0])>47957:
                output_feature_test.write(splits_y[0]+" "+splits_x[1]+"\n")
    output_feature_train.close()
    output_feature_valid.close()
    output_feature_test.close()

if __name__ =="__main__":
    transdata("topic_features.txt","gt.txt","libsvm_format.train.txt","libsvm_format.valid.txt","libsvm_format.test.txt")