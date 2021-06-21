from django.shortcuts import render

def showCalc(request):
    if request.method=="POST":
        fno = int(request.POST.get("f1"))
        sno = int(request.POST.get("s1"))
        opr = request.POST.get("opr")
        print(fno)
        print(sno)
        print(opr)

        if(opr == "add"):
            result = fno + sno
            print(result)
            return render(request, "index.html", {"opr": result})
        elif(opr == "sub"):
            result = fno - sno
            return render(request, "index.html", {"opr": result})
        elif(opr == "mul"):
            result = fno * sno
            return render(request, "index.html", {"opr": result})
        elif(opr == "div"):
            result = fno/sno
            return render(request, "index.html", {"opr": result})



    if request.method=="GET":
        return render(request,"index.html")
