from django.shortcuts import render
from django.views import View


class ClassBasedView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'second_task/class_template.html')


def function_based_view(request):
    return render(request, 'second_task/func_template.html')


from django.shortcuts import render

# Create your views here.
