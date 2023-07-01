from typing import Optional, Any

from data import config


def print_to_log(text: Any, color: Optional[str] = '') -> None:
    print(color + text + config.RESET_ALL)
    try:
        with open(file=config.LOG_FILE, mode='a', encoding='utf-8') as file:
            file.write(text + '\n')

    except:
        pass
