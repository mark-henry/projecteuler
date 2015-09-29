
def rects_count(width, height):
	count = 0
	for sub_width in range(1, width+1):
		for sub_height in range(1, height+1):
			count += (width - sub_width + 1) * (height - sub_height + 1)
	return count

target = 2000000
closest = (999999, 0)
for width in range(1000):
	for height in range(1000):
		count = rects_count(width, height)
		closest = min(closest, (abs(target-count), width*height))
		print(closest, width, height, rects_count(width, height))
		if count > target:
			break