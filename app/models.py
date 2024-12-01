from django.db import models
import uuid
import random
# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    # BaseModel class is registered as Base class in which we can inherit with every class
    class Meta:
        abstract = True

class Category(BaseModel):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

# related field help in reverse relation
class Question(BaseModel):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question
    
    def get_answer(self):
        answer_obj = list(Answer.objects.filter(question=self))
        data = []
        random.shuffle(answer_obj)
        for answer_o in answer_obj:
            data.append({
                'answer':answer_o.answer,
                'is_correct':answer_o.is_correct
            })
        return data    

class Answer(BaseModel):
    question =  models.ForeignKey(Question,on_delete=models.CASCADE,related_name='question_answer')
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


