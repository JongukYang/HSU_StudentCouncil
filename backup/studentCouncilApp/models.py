from django.db import models
from accounts.models import UserProfile

# Create your models here.
class Post(models.Model):
    # 게시글ID, 회원ID, 장르ID, 제목, 내용, 작성시간, 수정시간, 썸네일, 비디오
    # 게시글ID는 primarykey로서 이미 있음
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # 회원ID # User 모델의 pk를 가져옴
    title = models.CharField(max_length=200) # 제목
    body = models.TextField() # 게시물 설명
    created_at = models.DateTimeField(auto_now_add=True) # 처음 업로드 시간
    updated_at = models.DateTimeField(auto_now=True) # 수정 시간
    image = models.ImageField(blank=True, null=True, upload_to='postImage') # 썸네일 # upload_to : static/blog_photo 로 저장해줘
    video = models.FileField(blank=True, null=True, upload_to='video') # 배포시에는 models.FilePathField()사용
    hits = models.PositiveIntegerField(default=0) # 조회수

    def __str__(self):
        return self.title