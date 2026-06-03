def requires_login(func):
    def wrapper(*args,**kwargs):
        if not user_logged_in:
            raise PermissionError("User must be logged in to access this function.")
        return func(*args, **kwargs)
    return wrapper

user_logged_in = True

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")
view_profile() 





