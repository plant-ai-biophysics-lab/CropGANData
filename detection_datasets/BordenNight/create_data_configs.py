import os, sys, glob
## Data configs

data_save_path = os.getcwd()
print("data save path: ", data_save_path)
all_train_image = glob.glob(data_save_path + "/train/images/*")
all_train_image.sort()
all_val_image = glob.glob(data_save_path + "/valid/images/*")
all_val_image.sort()
all_test_image = glob.glob(data_save_path + "/test/images/*")
all_test_image.sort()


def create_data_config(dataset_name, num_train, num_val):
    data_config_path = data_save_path + "/data_configs/" + dataset_name + "/"

    if not os.path.exists(data_config_path):
        os.makedirs(data_config_path)

    # Save data.data for yolo v3
    with open(data_config_path + "/data.data", 'w') as file:
        file.write("classes=1 \n")
        file.write("train=" + data_config_path + "train.txt" + "\n")
        file.write("valid=" + data_config_path + "valid.txt" + "\n")
        file.write("test=" + data_config_path + "test.txt" + "\n")
        file.write("names=" + data_config_path + "classes.names" + "\n")
    with open(data_config_path + "classes.names", 'w') as file:
        file.write("grapes\n")

    with open(data_config_path + "train.txt", 'w') as file:
        for i in range(num_train):
            file.write(all_train_image[i]+"\n")
    with open(data_config_path + "valid.txt", 'w') as file:
        for i in range(num_val):
            file.write(all_val_image[i]+"\n")
    with open(data_config_path + "test.txt", 'w') as file:
        for i in range(len(all_test_image)):
            file.write(all_test_image[i]+"\n")

dataset_name = "all"
num_train = len(all_train_image)
num_val = len(all_val_image)
print("All: num train = ", num_train, "num_val = ", num_val)
create_data_config(dataset_name, num_train, num_val)

dataset_name = "train1_val1"
num_train = 1
num_val = 1
create_data_config(dataset_name, num_train, num_val)

dataset_name = "train1_val14"
num_train = 1
num_val = 14
create_data_config(dataset_name, num_train, num_val)

dataset_name = "train10_val5"
num_train = 10
num_val = 5
create_data_config(dataset_name, num_train, num_val)
