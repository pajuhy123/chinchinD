from django.shortcuts import render


def post_list(request):
    return render(request, 'main/post_list.html')

def estimate(request):
    return render(request, 'main/estimate.html')

#form
def test(request):
    form = RadioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print('form was valid')
    return render_to_response('estimate.html', {'form' : form})    

