from django.shortcuts import render

# Create your views here.
def mi_function(request):
	HW = "Hello World!"
	context = { 
	"msg" : HW,
	}
	return render(request, "index.html", context)