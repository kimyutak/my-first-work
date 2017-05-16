from django.http import JsonResponse

def keyboard(request):

	return JsonResponse({
		'type' : 'buttons',
		'buttons' : ['A','1','가']
		})