from userprofiles.models import User


class EmailOrUsernameOrMobileModelBackend(object):
    """ Authenticate user by username or email or mobile number """
    def authenticate(self, username=None, password=None):

        if '@' in username:
            kwargs = {'email': username}
        elif username[0] <= '9':
            kwargs = {'mobile': username}
        else:
            kwargs = {'username': username}
        try:

            user = User.objects.get(**kwargs)
            if user.check_password(password):
                print 'is valid'
                return user
            else:
                print 'is not valid'
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id=None):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None