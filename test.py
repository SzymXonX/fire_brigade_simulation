import logging
import colorlog
import threading
import random
import time

# Lista kolorów
COLORS = ["red", "green", "yellow", "blue", "cyan"]

# Funkcja wykonywana przez wątki
def thread_task(color, thread_name):
    logger = logging.getLogger(thread_name)
    logger.setLevel(logging.INFO)
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        f"%(log_color)s%(asctime)s - {thread_name} - %(message)s",
        log_colors={"INFO": color}
    ))
    logger.addHandler(handler)

    for _ in range(5):
        logger.info(f"To jest wiadomość z wątku {thread_name}.")
        time.sleep(random.uniform(0.5, 1.5))

# Główny program
if __name__ == "__main__":
    threads = []
    for i, color in enumerate(COLORS):
        thread_name = f"Thread-{i+1}"
        thread = threading.Thread(target=thread_task, args=(color, thread_name), name=thread_name)
        threads.append(thread)

    # Uruchamianie wątków
    for thread in threads:
        thread.start()

    # Oczekiwanie na zakończenie wątków
    for thread in threads:
        thread.join()
