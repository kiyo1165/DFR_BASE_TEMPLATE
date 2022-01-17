from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import UserSerializers, ProfileSerializer, MessageSerializer
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from user.models import Profile, Message


# ユーザー登録
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializers
    #settingsでアクセス制限をしているため、新規登録は解除している。
    permission_classes = (permissions.AllowAny, )
#ユーザー一覧
class ListUserView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers

# GET、PUT、PATCH
class LoginUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializers

    # ログインしている自身の情報を取得
    def get_object(self):
        return self.request.user

    # 更新はさせない。
    def update(self, request, *args, **kwargs):
        response = {'message': 'PUTメソッドは許可されていません。'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


#CRUD：プロフィールの更新
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    #ログインしている自身をsaveする。
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)

    # 削除させない
    def destroy(self, request, *args, **kwargs):
        response = {'message': 'DELETE method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # 一部更新をさせない
    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

# CRUD
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, )

    # ログインしている自身だけのメッセージを表示
    def get_queryset(self):
        return self.queryset.filter(sender=self.request.user)

    # ログインしているユーザーをsenderに登録
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

#受信箱を作る
class InboxListViewSet(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = (permissions.IsAuthenticated,)

    #自分宛のメッセージのみ
    def get_queryset(self):
        return self.queryset.filter(receiver=self.request.user)





