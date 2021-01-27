from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# 수정 2021.01.27
class Algo_UserManager(BaseUserManager):
    # 유저 생성 
    def create_user(self, web_id, discord_id, student_id, baekjoon_id, name, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
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
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
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
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    



'''

# 커스텀 유저 모델 사용
class member(AbstractUser):
    tel = models.CharField(max_length=20, null=True, blank=True)
    student_id = models.CharField(unique=True, max_length=45)
    baekjoon_id = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.username
'''