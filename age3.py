driving = input('請問你有開過車嗎? ')
if driving != '有' and driving != '沒有':
    raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
    if age >= 18:
        print('強喔')
    else:
        print('不行拉小弟弟')
elif driving == '沒有':
    if age >= 18:
        print('你可以考駕照了啊幹嘛不考')
    else:
        print('很好毛多點再考')
else:
    print('只能輸入有跟沒拉')