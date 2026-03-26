def word_frequency(string):
    words = string.lower().split(" ")
    frequency={}
    for word in words :
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    sorted_dic = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return sorted_dic[0:5]

line =  "Hammad is learning Python and Hammad is practicing coding every day. Coding helps Hammad improve problem solving skills and Hammad is enjoying the process of learning and coding."
print(word_frequency(line))

