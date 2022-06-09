from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.POST.get('text', 'default').lstrip()
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    removenewline = request.POST.get('removenewline', 'off')

    analyzedtext = ''
    purpose = ''
    punctuations='''<>,./?;:-'"{[]}!@#$%^&*()~'''
    if removepunc == 'on':
        for char in text:
            if char not in punctuations:
                analyzedtext = analyzedtext + char
        purpose = 'Remove Punctuations'
        params = {'analyzedtext': analyzedtext, 'purpose': purpose}
    
    if capitalize == 'on':
        if analyzedtext == '':
            analyzedtext = text.upper()
            purpose = 'Capitalize'
        else:
            analyzedtext = analyzedtext.upper()
            purpose = purpose + ', Capitalize'
        params = {'analyzedtext': analyzedtext, 'purpose':purpose}
        
    if extraspace == 'on':
        newtext = ''
        if analyzedtext == '':
            purpose = 'Remove Extra Spaces'
            for i in range(0, len(text)-1):
                if text[i] == ' ' and text[i+1] == ' ':
                    pass
                else:
                    newtext = newtext + text[i]
        else:
            purpose = purpose + ', Remove extra spaces'
            for i in range(0, len(analyzedtext)-1):
                if analyzedtext[i] == ' ' and analyzedtext[i+1] == ' ':
                    pass
                else:
                    newtext = newtext + analyzedtext[i]
        
        analyzedtext = newtext
        params = {'analyzedtext': analyzedtext, 'purpose':purpose}
        
    if removenewline == 'on':
        newtext = ''
        if analyzedtext == '':
            purpose = purpose + 'Remove Newline'
            for char in text:
                if char != "\n":
                    newtext = newtext + char
        else:
            purpose = purpose + ', Remove Newline'
            for char in analyzedtext:
                if char != "\n":
                    newtext = newtext + char
        analyzedtext = newtext
        
        params = {'analyzedtext': analyzedtext, 'purpose':purpose}

    if (removepunc == 'off' and capitalize == 'off' and extraspace == 'off' and removenewline == 'off'):
        return HttpResponse('Please select some checkbox to analyze content')

    return render(request, 'analyze.html', params)
