# from .views import get_category_act_view
# from .views import list_act_in_category
from .models import Count, Crash


def is_sha1(maybe_sha):
    if len(maybe_sha) != 40:
        return False
    try:
        sha_int = int(maybe_sha, 16)
    except ValueError:
        return False
    return True

# def decide_which_api(request,cat_name):
#     if len(request.GET)==0:
#         get_category_act_view(request,cat_name)
#     else:
#         list_act_in_category(request,cat_name)


def isValidB64(str):
    return True


def increment_count():
    if list(Count.objects.all()) == []:
        c = Count()
        c.api_count = 1
        c.save()
        print("Incremented count")
        return 1
    c = Count.objects.first()
    c.api_count = c.api_count + 1
    c.save()
    print("Count incremented")
    return 1

crash = False

def check_crash():
    # global crash
    k = Crash.objects.all()
    if list(k) == []:
            Crash().save()
    print(k)
    crash = Crash.objects.first().crash
    return crash
