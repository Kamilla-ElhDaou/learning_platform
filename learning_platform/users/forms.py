from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


User = get_user_model()


class UserProfileUpdateForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
