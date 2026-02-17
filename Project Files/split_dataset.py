import os
import random
import shutil

SOURCE_DIR = "dataset/all"
TRAIN_DIR = "dataset/train"
TEST_DIR = "dataset/test"

classes = ["fresh", "rotten"]
split_ratio = 0.8

for cls in classes:
    os.makedirs(os.path.join(TRAIN_DIR, cls), exist_ok=True)
    os.makedirs(os.path.join(TEST_DIR, cls), exist_ok=True)

    images = os.listdir(os.path.join(SOURCE_DIR, cls))
    random.shuffle(images)

    split_index = int(len(images) * split_ratio)

    train_imgs = images[:split_index]
    test_imgs = images[split_index:]

    for img in train_imgs:
        shutil.copy(os.path.join(SOURCE_DIR, cls, img),
                    os.path.join(TRAIN_DIR, cls, img))

    for img in test_imgs:
        shutil.copy(os.path.join(SOURCE_DIR, cls, img),
                    os.path.join(TEST_DIR, cls, img))

print("Dataset split completed")
