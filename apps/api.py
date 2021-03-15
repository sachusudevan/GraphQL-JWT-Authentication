import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery
from .users.schema import Users , AuthMutation




class Query(Users, UserQuery, MeQuery, graphene.ObjectType):
    pass

class Mutation(AuthMutation, graphene.ObjectType):
   pass

schema = graphene.Schema(query=Query, mutation=Mutation)