import mimetypes
import boto3
from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile


@api_view(["POST"])
@permission_classes([AllowAny])
def upload_avatar(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    # 確保檔案上傳
    avatar = request.FILES.get("avatar")
    if not avatar:
        return Response({"error": "請上傳圖片"}, status=status.HTTP_400_BAD_REQUEST)

    # 嘗試判斷圖片類型並設定
    content_type, _ = mimetypes.guess_type(avatar.name)

    # 使用 boto3 上傳到 S3
    s3 = boto3.client("s3")

    try:
        s3.upload_fileobj(
            Fileobj=avatar,
            Bucket="shopeasy",  
            Key=f"avatars/{avatar.name}",  # 存儲在 S3 的路徑和文件名
            ExtraArgs={"ContentType": content_type},  # 設置 Content-Type
        )

        # 儲存圖片的 URL（假設您已配置好 S3 的 URL）
        avatar_url = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/avatars/{avatar.name}"

        return Response(
            {"message": "大頭貼上傳成功！", "avatar_url": avatar_url},
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    data = request.data
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    password2 = data.get('password2')

    if password != password2:
        return Response({'error': '密碼不一致！'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({'error': '使用者名稱已被註冊！'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email 已被註冊！'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'message': '使用者註冊成功！'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({'error': '登入失敗！'}, status=status.HTTP_401_UNAUTHORIZED)
    
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'message': '登入成功！'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({'message': '登出成功！'}, status=status.HTTP_200_OK)
