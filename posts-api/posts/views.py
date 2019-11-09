from rest_framework import generics, status
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Post, User, Comment
from .serializers import UserSerializer, UserPostSerializer, PostSerializer, PostsCommentsSerializer, CommentSerializer


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request):
        return Response({
            "posts" : reverse(PostList.name, request=request),
            "users" : reverse(UserList.name, request=request),
            "user-posts" : reverse(UserPostsList.name, request=request),
            "post-comments" : reverse(PostCommentsList.name, request=request),
        })


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserPostsList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPostSerializer
    name = 'user-posts-list'


class PostCommentsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsCommentsSerializer
    name = 'post-comments-list'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)

            return Response(data=user, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'Message' : 'Usuário não encontrado!'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        User.objects.create(name=request.data['name'], username=request.data['username'], email=request.data['email'])

        return Response({'Message' : 'Usuário salvo com sucesso!'}, status=status.HTTP_201_CREATED)
        
    def delete(self, request, id):
        user = User.objects.get(id=id)
        user.delete()

        return Response({'Message' : 'Usuário excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)


class PostDetail():
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)

            return Response(data=post, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'Message' : 'Post não encontrado!'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        user = User.objects.get(request.data['user'])
        Post.objects.create(request.data['title'], request.data['body'], user=user)

        return Response({'Message' : 'Post salvo com sucesso!'}, status=status.HTTP_201_CREATED)
        
    def delete(self, request, id):
        user = User.objects.get(id=id)
        user.delete()

        return Response({'Message' : 'Post excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)



class ImportDatabase(generics.GenericAPIView):
    name = 'import-database'

    def import_database(self):
        file = open("db.json")
        content = json.load(file)

        for user in content['users']:
            adress = Address.objects.create(street=user['adress']['street'], city=user['adress']['city'], suite=user['adress']['suite'], zipcode=user['adress']['zipcode'])
            User.object.create(name=user['adress'], username=user['username'], email=user['email'], adress=adress)

        for post in data['posts']:
            user = User.objects.get(id=post['userId'])
            Post.objects.create(title=post['title'], body=post['body'], user=user)

    for comment in data['comments']:
        post = Post.objects.get(id=comment['postId'])
        Comment.objects.create(id=comment['id'], name=comment['name'], email=comment['email'], body=comment['body'], post=post)