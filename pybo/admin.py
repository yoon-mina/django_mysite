from django.contrib import admin

from .models import Question
# Register your models here.

class QuestionAdmin (admin.ModelAdmin): # 검색 기능
    search_fields = ['subject'] # 제목으로 질문 찾기

admin.site.register(Question, QuestionAdmin) #장고 어드민에서 모델 관리하기