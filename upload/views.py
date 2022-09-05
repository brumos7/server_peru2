from django.shortcuts import render

from .models import Document
from .forms import DocumentForm

# Create your views here.
def list(request):
    print(f"Pipipi")
    message = 'Upload as many files as you want!'
    
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            
            # Redirect to the document list after POST
            return redirect('my-view')
    else:
        form = DocumentForm() # A empty, unbound form
    
    # Load documents for the list page
    documents = Document.objects.all()
    
    # Render list page with the documents and the form
    context = {'documents':documents, 'form':form, 'message':message}
    return render(request, 'list.html', context)    