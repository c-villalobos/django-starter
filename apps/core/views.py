from django.shortcuts import render


def home(request):
  context = {}
  template = 'core/home.html'
  return render(
    request=request,
    template_name=template,
    context = context,
  )