# from .views import get_category_act_view
# from .views import list_act_in_category

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