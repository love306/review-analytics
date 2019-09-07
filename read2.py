data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 100000 == 0:
			print(len(data))
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
# for word in wc:
# 	if wc[word] >= 1000000:
		# print(word, wc[word])
# print(len(wc))
# print(wc['Allen'])

while True:
	word = input('請輸入想查詢單字')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現了', wc[word])
	else:
		print('檔案無此單字')
print('感謝您的使用')