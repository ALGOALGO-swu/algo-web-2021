from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Algo_UserManager(BaseUserManager):
    # 유저 생성 
    def create_user(self, web_id, discord_id, student_id, baekjoon_id, name, email, password=None):
    
        if not web_id:
            raise ValueError('Users must have an id')

        user = self.model(
            web_id=web_id,
            discord_id=discord_id,
            student_id=student_id,
            baekjoon_id=baekjoon_id,
            name=name,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    #관리자 생성 
    def create_superuser(self, web_id, discord_id, student_id, baekjoon_id, name, email, password=None):

        user = self.model(
            web_id=web_id,
            discord_id=discord_id,
            student_id=student_id,
            baekjoon_id=baekjoon_id,
            name=name,
            email=self.normalize_email(email),
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class Algo_User(AbstractBaseUser):
    # 아이디, 비밀번호 이미 AbstractBaseUser에 구현됨. 
    # 추가 : 디스코드 아이디, 학번, 백준 아이디, 이름, 이메일 
    web_id = models.CharField(unique=True, max_length=45)
    discord_id = models.CharField(unique=True, max_length=45)
    student_id = models.CharField(unique=True, max_length=45)
    baekjoon_id = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=45,)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = Algo_UserManager()

    USERNAME_FIELD ='web_id' # 로그인시 id로 사용되는 필드 지정. 
    REQUIRED_FIELDS = ['discord_id', 'student_id', 'baekjoon_id','name','email'] #필수로 입력 받을 값 


    def __str__(self):
        return self.web_id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    



# 실제 AlgoAlgo DB의 Member 테이블 
class Member(models.Model):
    discord_id = models.CharField(unique=True, max_length=45)
    student_id = models.CharField(unique=True, max_length=45)
    name = models.CharField(max_length=45)
    point = models.IntegerField()
    map_location = models.IntegerField()
    status = models.IntegerField()
    items = models.TextField(blank=True, null=True)
    daily_steps = models.IntegerField(blank=True, null=True)
    baekjoon_id = models.CharField(max_length=45, blank=True, null=True)
    bj_solved = models.TextField(blank=True, null=True)
    bj_solv_contd = models.IntegerField()
    bj_rank = models.CharField(max_length=45, blank=True, null=True)
    bj_today = models.IntegerField()
    

    class Meta:
        managed = False
        db_table = 'member'
