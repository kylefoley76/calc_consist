from django.shortcuts import render
from logiccalculator.utils import logic_func

def calculate_logic(request):
    if request.POST:
        input_from_user = request.POST.get('sentence')
        result = logic_func(input_from_user)
        context = {
            'result':result,
        }
        return render(request,'logiccalculator/home.html',context)
    else:
        return render(request,'logiccalculator/home.html')