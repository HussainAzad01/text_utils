# I have created this file - Hussain Azad
from django.http import HttpResponse
from django.shortcuts import render

puntuation = '''.?"',;-<>_!@#$%^*&~(){}[]/\:'''


def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def analyze(request):
    user_text = request.POST.get('text', 'No text was Given!')
    removepunc_checkbox = request.POST.get('removepunc', 'off')
    removespace_checkbox = request.POST.get('removespace', 'off')
    extraspace_checkbox = request.POST.get('removeextraspace', 'off')
    capitalize_checkbox = request.POST.get('capitalize', 'off')
    charcount_checkbox = request.POST.get('charcount', 'off')
    newlineremover_checkbox = request.POST.get('newlineremover', 'off')
    lower_checkbox = request.POST.get('lower', 'off')
    after_analyzed = user_text
    purpose = []

    if removepunc_checkbox == 'on':
        after_analyzed = remove_punc(after_analyzed)
        purpose.append("Remove Punctuations")

    if capitalize_checkbox == 'on':
        after_analyzed = capitalize(after_analyzed)
        purpose.append("CAPITALIZE")

    if removespace_checkbox == 'on':
        after_analyzed = removespace(after_analyzed)
        purpose.append("Remove Spaces")

    if extraspace_checkbox == 'on':
        after_analyzed = extraspace(after_analyzed)
        purpose.append("Extra Remove Spaces")

    if charcount_checkbox == 'on':
        count = charcount(after_analyzed)
        purpose.append("Char Counter")

    if newlineremover_checkbox == 'on':
        after_analyzed = newlineremover(after_analyzed)
        purpose.append("New Line Remover")

    if lower_checkbox == 'on':
        after_analyzed = lower(after_analyzed)
        purpose.append("lower")

    if len(purpose) == 0:
        return HttpResponse("Select which operation you want to do on your text!"
                            "<a href = '/'><p>Back</p></a>")

    else:
        operation = {'purpose': purpose, 'result': after_analyzed}
        return render(request, 'analyzed2.html', operation)


def remove_punc(text):
    no_punc = ""
    for char in text:
        if char not in puntuation:
            no_punc = no_punc + char
    return no_punc


def capitalize(text):
    text = text.upper()
    return text


def removespace(text):
    no_space = ""
    for spaces in text:
        no_space = no_space + spaces.replace(" ", '')
    return no_space


def extraspace(text):
    no_extra_space = text[0]
    for index in range(1, len(text)):
        if not (text[index] == " " and text[index - 1] == " "):
            no_extra_space = no_extra_space + text[index]
    return no_extra_space


def charcount(text):
    count = 0
    for char in text:
        if char != " ":
            count += 1
    return count


def newlineremover(text):
    no_line = ""
    for char in text:
        if char != "\n" and char != "\r":
            no_line = no_line + char
    return no_line


def lower(text):
    text = text.lower()
    return text

def remove():
    return