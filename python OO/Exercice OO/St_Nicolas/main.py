from alive_progress import alive_bar
from time import sleep

with alive_bar(100) as bar:  # default setting
    for i in range(100):
        sleep(0.03)
        bar()  # call after consuming one item

# using bubble bar and notes spinner
with alive_bar(200, bar="bubbles", spinner="notes2") as bar:
    for i in range(200):
        sleep(0.03)
        bar()
