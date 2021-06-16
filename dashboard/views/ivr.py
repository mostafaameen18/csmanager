from .__init__ import *

@csrf_exempt
def answerCompanyPhone(request, companyName):
    vr = VoiceResponse()
    company = Company.objects.get(subdomain=companyName)

    if "is_first" in request.GET:
        answer = Answer.objects.get(company=company)
        if answer.message:
            vr.say(answer.message)

        branch = answer.redirect

    elif "branch" in request.GET:
        prevBranch = Branch.objects.get(id=request.GET.get('branch'))

        digit = request.POST.get('Digits')
        choice = Choice.objects.get(branch=prevBranch, number=digit).order_by('number')
        branch = choice.reference

    else:
        vr.say('Sorry, something went wrong')
        return HttpResponse(str(vr), content_type='text/xml')

    
    if branch.message:
        vr.say(branch.message)

    choices = Choice.objects.filter(branch=branch)

    with vr.gather(
        action=f'{reverse("answerCompanyPhone", args=[companyName])}?branch={branch.id}',
        finish_on_key='#',
        timeout=20,
    ) as gather:
        for choice in choices:
            gather.say(choice.message)

    vr.say('We did not receive your selection')

    if "is_first" in request.GET:
        vr.redirect(f'{reverse("answerCompanyPhone", args=[companyName])}?is_first=true')
    elif "branch" in request.GET:
        vr.redirect(f'{reverse("answerCompanyPhone", args=[companyName])}?branch={prevBranch.id}')


    return HttpResponse(str(vr), content_type='text/xml')