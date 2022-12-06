from data.config import LOG_FILE


def print_to_log(text: str) -> None:
    print(text)
    try:
        with open(LOG_FILE, 'a') as file:
            file.write(text + '\n')

    except:
        pass