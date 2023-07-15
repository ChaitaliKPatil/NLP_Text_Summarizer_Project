import os
import sys
# implementing custom log using inbuilt logging module.
import logging 

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# In log, it will save timestamp first.
# then will give a level name (kinds of log/ information logging).
# which module are you running.
# then log a message you wanted to give.
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # it will log into a file after creation
        logging.StreamHandler(sys.stdout)  # it will log inside the terminal.
    ]
)

logger = logging.getLogger("textSummarizerLogger")