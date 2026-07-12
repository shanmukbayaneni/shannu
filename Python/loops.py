from loguru import logger
import time

logger.info("This is an info message")

labour_names=["shanu","cud","maj","sum"]

name_iter = len(labour_names)-1

while(name_iter >=0):
    print(labour_names[name_iter])
    time.sleep(5)
    name_iter-=1
    