from django.http import JsonResponse

def keyboard(request):

	return JsonResponse({
		'type' : 'buttons',
		'buttons' : ['A','1','가']
		})
def message(request):

	return JsonResponse({
		"user_key": "encryptedUserKey",
		"type": "text",
		"content": "차량번호등록"
	})
def friend(request):

	return JsonResponse({
		'type' : 'buttons',
		'buttons' : ['A','1','가']
		})