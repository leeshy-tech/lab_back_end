"""
关键词搜索模块
"""
import jieba

def get_score(book_dict):
    return book_dict["match_score"]

def search_by_keyword(keyword,book_list):
    """
    关键词搜索
    in:keyword[str],book_list[list:(dict:ISBN,name)]
    out:ISBN[list:str]
    """
    search_result = []
    keyword_cut = jieba.lcut(keyword)
   
    for book_dict in book_list:
        book_name_cut = jieba.lcut(book_dict["name"])

        # 匹配分数，比较关键词和书籍名称的匹配程度
        match_score = 0
        match_number = 0

        for word in keyword_cut:
            if word in book_name_cut:
                match_number += 1

        match_score = match_number / len(book_name_cut)
        book_dict["match_score"] = match_score

    # 根据匹配分数排序
    book_list.sort(key=get_score,reverse=True)
    # 生成搜索结果，最多五条
    for i in range(min(5,len(book_list))):
        if book_list[i]["match_score"] > 0:
            search_result.append(book_list[i]["ISBN"])

    return search_result

# test
"""
book_list = [
    {
        "ISBN":"1",
        "name":"通信原理"
    },
    {
        "ISBN":"2",
        "name":"毛泽东选集"
    },
    {
        "ISBN":"3",
        "name":"通信原理习题集"
    }
]
keyword = "通信"

print(search_by_keyword(keyword,book_list))
"""