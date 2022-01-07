
def callviews(passw):
    import crud
    obj1 = crud.vicks(passw, link = 'https://home-automation-336c0-default-rtdb.firebaseio.com/')
    pageviews = obj1.pull(child = 'Views')
    pageviews += 1
    obj1.push(data = pageviews, child = 'Views')
    return pageviews

passw = '@Hey_Vicks'
# passw = input('Enter Password : ')
# g = callviews(passw)
# print(g)
