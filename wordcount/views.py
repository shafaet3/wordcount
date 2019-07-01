from django.http import HttpResponse
from  django.shortcuts import render
import operator

def homepage(request):
	return render(request, 'home.html')

def count(request):
	data = request.GET['textarea']
	words_list = data.split()
	words_list_count = len(words_list)

	word_dict = {}

	for word in words_list:
		if word in word_dict:
			word_dict[word] += 1
		else:
			word_dict[word] = 1

	sorted_list = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'text' : data, 'word_count' : words_list_count, 'word_dictionary' : sorted_list})