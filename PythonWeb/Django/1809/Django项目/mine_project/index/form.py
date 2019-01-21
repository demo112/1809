from django import forms
from index.models import *


LEVEL_CHOICE = (
    ('1', '好评'),
    ('2', '中评'),
    ('3', '差评'),
)


class RemarkForm(forms.Form):
    """表示评论内容的表单控件们"""
    # 控件1 评论标题（subject），文本框
    subject = forms.CharField(label='标题')
    # 控件2 email，Email框
    email = forms.EmailField(label='邮箱')
    # 控件3 评论内容（messgae），Textarea框
    message = forms.CharField(widget=forms.Textarea, label='内容')
    # 控件4 评论级别（level），select
    level = forms.ChoiceField(label='级别', choices=LEVEL_CHOICE, help_text='请选择')
    # 控件5 是否保存，checkbox
    isSaved = forms.BooleanField(label="是否保存")


class RegisterForm(forms.Form):
    """手动生成form类"""
    # uname = forms.CharField(max_length=30)
    uname = forms.CharField(label='姓名')
    # upwd = forms.CharField(max_length=30)
    upwd = forms.CharField(label='密码', widget=forms.PasswordInput)
    # uage = forms.IntegerField
    uage = forms.CharField(label='年龄', widget=forms.NumberInput)
    # uemail = forms.CharField(max_length=30)
    uemail = forms.EmailField(label="邮箱", widget=forms.EmailInput)


class ModelRegisterForm(forms.ModelForm):
    """将form关联到Model类，为其生成forms类"""
    class Meta:
        # 指定关联model
        model = Users
        # 指定要生成控件的字段们
        fields = "__all__"
        # 指定每个属性对应的label
        labels = {
            'uname': '姓名',
            'upwd': '密码',
            'uage': '年龄',
            'uemail': '邮件',
        }


class ModelLoginForm(forms.ModelForm):
    """为自动生成的forms标签添加widgets小部件并一同用attr添加属性"""
    class Meta:
        model = Users
        fields = ['uname', 'upwd']
        labels = {
            "uname": '姓名',
            'upwd': "密码",
        }
        widgets = {
            'uname': forms.TextInput(
                attrs={
                    'placeholder': '请输入用户名'
                }),
            'upwd': forms.PasswordInput,
        }


class WidgetForm(forms.Form):
    # 带属性使用
    test13 = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': '通过attrs添加的属性',
            'class': 'form-control',
        }
    ), label='TextInput')

    # 基本使用
    test1 = forms.CharField(widget=forms.TextInput, label='TextInput')
    test2 = forms.IntegerField(widget=forms.NumberInput, label='NumberInput')
    test3 = forms.EmailField(widget=forms.EmailInput, label='EmailInput')
    test4 = forms.URLField(widget=forms.URLInput, label='URLInput')
    test5 = forms.CharField(widget=forms.PasswordInput, label='PasswordInput')
    test6 = forms.CharField(widget=forms.HiddenInput, label='HiddenInput')
    test7 = forms.CharField(widget=forms.DateInput, label='DateInput')
    test8 = forms.CharField(widget=forms.DateTimeInput, label='DateTimeInput')
    test9 = forms.CharField(widget=forms.TimeInput, label='TimeInput')
    test0 = forms.CharField(widget=forms.Textarea, label='Textare')
    test01 = forms.CharField(widget=forms.FileInput, label='FileInput')
    test02 = forms.CharField(widget=forms.ClearableFileInput, label='ClearableFileInput')
    test03 = forms.CharField(widget=forms.MultipleHiddenInput, label='MultipleHiddenInput')
    test04 = forms.CharField(widget=forms.SplitDateTimeWidget, label='SplitDateTimeWidget')
    test05 = forms.CharField(widget=forms.SplitHiddenDateTimeWidget, label='SplitHiddenDateTimeWidget')
    test06 = forms.CharField(widget=forms.CheckboxInput, label='CheckboxInput')
    test07 = forms.CharField(widget=forms.Select, label='Select')
    test08 = forms.CharField(widget=forms.NullBooleanSelect, label='NullBooleanSelect')
    test09 = forms.CharField(widget=forms.SelectMultiple, label='SelectMultiple')
    test11 = forms.ChoiceField(widget=forms.RadioSelect, choices=LEVEL_CHOICE, label='RadioSelect')
    test12 = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=LEVEL_CHOICE, label='CheckboxSelectMultiple')
