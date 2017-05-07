import graphene
from graphene_django import DjangoObjectType
from posts.models import Post as PostModel


class Post(DjangoObjectType):
    class Meta:
        model = PostModel


class Query(graphene.ObjectType):
    posts = graphene.List(Post)

    @graphene.resolve_only_args
    def resolve_posts(self):
        return Post.objects.all()


schema = graphene.Schema(query=Query)
