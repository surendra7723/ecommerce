from djoser.serializers import UserSerializer as BaseUserSerializer
class UserCreateSerializer(BaseUserSerializer):
    birth_date=(serial)
    fields=['id','username','password','email','first_name','last_name']
    
class UserSerializer(BaseUserSerializer):
    
    class Meta(BaseUserSerializer.Meta):
        fields=['id','username','email','first_name','last_name']
    
        