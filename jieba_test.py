import jieba #結巴中文模組

jieba.load_userdict('user.txt')

seg_list = jieba.cut("我來自國立台北商業大學資訊管理系", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式
