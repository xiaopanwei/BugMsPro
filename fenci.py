import jieba


def get_search_list(content):
    search_list=[]
    result=jieba.cut(content)
    for re in result:
        search_list.append(re)

    return search_list