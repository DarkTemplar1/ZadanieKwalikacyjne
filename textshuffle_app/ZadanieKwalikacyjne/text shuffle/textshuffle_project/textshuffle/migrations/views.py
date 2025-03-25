import random
from django.http import JsonResponse

def shuffle_word(word):
    if len(word) > 3:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]
    return word

def process_text(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        words = text.split()
        shuffled_text = ' '.join(shuffle_word(word) for word in words)
        return JsonResponse({'processed_text': shuffled_text})
    return JsonResponse({'error': 'Invalid request'}, status=400)
