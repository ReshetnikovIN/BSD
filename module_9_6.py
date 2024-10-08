
def all_variants(text):
    lenth = len(text)
    for k in range(lenth):
        for j in range(0, lenth-k):
            yield text[j:j+k+1]

a = all_variants("abc")
for i in a:
    print(i)