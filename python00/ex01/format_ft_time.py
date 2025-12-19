import time

seconds = time.time()
notation = "{:.2e}".format(seconds)
start_date = time.strftime("%B %d, %Y", time.gmtime(0))

print(f"Seconds since {start_date}: {format(seconds, ',')} or {notation} in scientific notation")

print(time.strftime("%b %d %Y"))