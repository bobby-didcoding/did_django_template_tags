from django.shortcuts import render
from django.utils import timezone


'''
Basic index view
'''
def index(request):

	regroup_list = [
	    {'name': 'John', 'age': '19', 'country': 'UK'},
	    {'name': 'Mark', 'age': '22', 'country': 'USA'},
	    {'name': 'Frank', 'age': '55', 'country': 'France'},
	    {'name': 'Lewis', 'age': '27', 'country': 'USA'},
	    
	    {'name': 'Matt', 'age': '38', 'country': 'Germany'},
	    ]

	#template tag does not sort the dict
	#This is sorting a list of dics by key["family"]
	reset_cycle_list = sorted([

	    {'name': 'Jojen Reed', 'family': 'Reed'},
	    {'name': 'Daenerys Targaryen', 'family': 'Targaryen'},
	    {'name': 'Sansa Stark', 'family': 'Stark'},
	    {'name': 'Joffrey Baratheon', 'family': 'Lannister'},
	    {'name': 'Eddard Stark', 'family': 'Stark'},
	    {'name': 'Tyrion Lannister', 'family': 'Lannister'},
	    {'name': 'Arya Stark', 'family': 'Stark'},
	    {'name': 'Stannis Baratheon', 'family': 'Baratheon'},
    ], key=lambda k: k['family'])

    
	# reset_cycle_list = sorted(reset_cycle_list, key=lambda k: k['family'])
	
	context = {
		"cycle_list": ["This", "Is", "Cycle"],
		"firstof_1": False,
		"firstof_2": False,
		"firstof_3": "This will be displayed",
		"for_list": ["123 Winterfell,", "Kings Road", "The North", "PO BOX - 5N0W"],
		"for_dict": {
			"first_line": "123 Winterfell,",
			"second_line": "Kings Road,",
			"town": "The North,",
			"postcode": "PO BOX - 5N0W"},
		"if_list": [],
		"regroup_list": regroup_list,
		"reset_cycle_list": reset_cycle_list,
	}
	return render(request, 'main/index.html', context)



'''
Basic filter view 
'''
def filter(request):

	dictsort = [
	    {'name': 'John', 'age': '19', 'country': 'UK'},
	    {'name': 'Mark', 'age': '22', 'country': 'USA'},
	    {'name': 'Frank', 'age': '55', 'country': 'France'},
	    {'name': 'Lewis', 'age': '27', 'country': 'USA'},
	    {'name': 'Matt', 'age': '38', 'country': 'Germany'},
	    ]

	context = {
		"add": 3,
		"addslashes": "I'm building a demo",
		"capfirst": "winterfell",
		"center": "Kings Landing",
		"cut": "Kings Landing",
		"date": timezone.now(),
		"default": "",
		"default_if_none": None,
		"dictsort": dictsort,
		"dictsortreversed": dictsort,
		"divisibleby": 21,
		"filesizeformat": 123456789,
		"first": ["This", "Is", "First"],
		"floatformat": 39.4564765,
		"get_digit": 132456789,
		"join": ["This", "Is", "First"],
		"last": ["This", "Is", "Last"],
		"length": ["This", "Is", "First"],
		"length_is": ["This", "Is", "First"],
		"lower": "HELLO",
		"apnumber":321,
		"intcomma":987654321,
		"naturalday": timezone.now()	
	}
	return render(request, 'main/filter.html', context)



'''
Basic filter view 
'''
def bespoke_filter(request):

	context = {
		"price1": 2,
		"price2": 23.4567687,
		"price3": 24.1,		
	}
	return render(request, 'main/bespoke_filter.html', context)
