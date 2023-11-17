from django.contrib.auth.models import Group, User

def add_user_group(username, group, email, password='abcde' ):
    user = User.objects.create_user(
        username=username,
        email = email,
        password=password,
    )
    
    try:
        g = Group.objects.get(name=group)
    except:
        g = Group.objects.create(name=group)
    
    user.groups.add(g)

    return user
