import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery
from graphene import relay
import graphql_auth.relay as relay_auth

from .models import CustomUser

class UsersNode(DjangoObjectType):
    class Meta:
        model = CustomUser
        filter_fields = ['id', 'is_active', 'is_staff', 'is_superuser']
        interfaces = (relay.Node,)



class Users(graphene.ObjectType):
    user = relay.Node.Field(UsersNode)
    users = DjangoFilterConnectionField(UsersNode)


class AuthMutation(graphene.ObjectType):
   register = relay_auth.Register.Field()
   verify_account = relay_auth.VerifyAccount.Field()
   update_account = relay_auth.UpdateAccount.Field()
   resend_activation_email = relay_auth.ResendActivationEmail.Field()
   send_password_reset_email = relay_auth.SendPasswordResetEmail.Field()
   password_reset = relay_auth.PasswordReset.Field()
   password_change = relay_auth.PasswordChange.Field()
   delete_account = relay_auth.DeleteAccount.Field()

   # django-graphql-jwt inheritances
   token_auth = relay_auth.ObtainJSONWebToken.Field()
   verify_token = relay_auth.VerifyToken.Field()
   refresh_token = relay_auth.RefreshToken.Field()
   revoke_token = relay_auth.RevokeToken.Field()

