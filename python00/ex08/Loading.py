from time import sleep
from tqdm import tqdm
# # from Loading import ft_tqdm

import os


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    term_width = os.get_terminal_size().columns
    bar_width = max(term_width - 30, 20)
    
    for i, item in enumerate(lst):
        current = i + 1
        percent = (current * 100) // total
        filled = (current * bar_width) // total
        if filled > 0:
            bar = '=' * (filled - 1) + '>'
        else:
            bar = ''
        bar += ' ' * (bar_width - filled)
        
        print(f"\r{percent:3d}%|[{bar}]| {current}/{total}", 
              end='', flush=True)
        
        yield item
    
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()
