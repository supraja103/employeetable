from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return self.dname+self.loc

class Emp(models.Model):
    empno=models.IntegerField(primary_key=100)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename+self.job

class Salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.IntegerField()
    hisal=models.IntegerField()


class Bonus(models.Model):
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()
    comm=models.IntegerField()

    def __str__(self):
        return self.ename+self.job