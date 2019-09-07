data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 100000 == 0:
			print(len(data))
print('總共', len(data), '筆資料')
sum_data = 0
for d in data:
	sum_data = sum_data + len(d)
print('每筆留言平均長度為', sum_data / len(data))
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '筆長度大於100')
print(new[0])
