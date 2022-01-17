from rest_framework import serializers
from user.models import User, Profile, Message



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']
        extra_fields = {'password': {
            'write_only': True, 'required': True
        }
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):


    class Meta:
        model = Profile
        fields = [
            'id', 'gender', 'age', 'zip_code', 'img',
            'build_name', 'self_description', 'address',
            'created_at', 'updated_at', 'user_profile',
        ]

        extra_fields = {
            'user_profile':{
                'read_only': True
            },
            'created_at': {
                'read_only': True
            },
            'updated_at': {
                'read_only': True
            },
        }



class MessageSerializer(serializers.ModelSerializer):

    #リレーション先の名前を表示させる。
    sender = serializers.ReadOnlyField(source='user.name')


    class Meta:
        model = Message
        fields = ['id', 'created_at', 'message', 'sender', 'receiver']
        extra_fields = {
            'created_at': {
                'read_only': True
            }
        }


