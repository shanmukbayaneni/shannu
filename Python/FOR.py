from loguru import logger

logger.info("This is an info message")

labour_name = ["mashe", "john", "doe"]

# for name in labour_name:
#     logger.info(f"Processing labour name: {name}")

# for i in range(5):
#     logger.info(i) \

for i in range(len(labour_name)):
    # print(i)
    # print(labour_name[i])
    logger.info(f"labour {i+1} name is {labour_name[i]}")


