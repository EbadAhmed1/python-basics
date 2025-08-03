
# multithreading ; used to perform multiple tasks concurrently

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

# walk_dog()
# take_out_trash()

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore1.join()
chore2.join()