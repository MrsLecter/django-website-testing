from django.shortcuts import render
import re

from numpy import integer
import website.data_access


def search(request):
    # if something found - True
    find_something_flag = False

    # ----fill search form----
    all_items = website.data_access.getAllObject("goods")
    # find all categories
    db_category = []
    db_ids = []
    prices= []
    for item in all_items:
        db_category.append(item['category'])
        db_ids.append(item['_id'])
        prices.append(item['price'])
    unique_category = set(db_category)
    prices.sort()
    # ----/fill search form-----
    keyword = request.GET.get('keyword') or None
    price_from = request.GET.get('price_from') or prices[0]
    price_to = request.GET.get('price_to') or prices[len(prices)-1]
    category = request.GET.get('category') or None

    print(keyword, price_from, price_to, category)
    # general filter
    main_filter = {}
    # filter by keyword
    filter_goods = {'goods_name': re.compile(f".*{keyword}.*", re.IGNORECASE)}
    # filter category
    filter_category = {'category': category}
    # filter price
    filter_price = {"price" : { "$gt" : price_from, "$lt" : price_to}}

    if(keyword is not None) or (category is not None) or(price_from is not None) or (price_to is not None):
        find_something_flag = True
        # build main filter
        if(keyword is not None):
            main_filter.update(filter_goods)
        
        if(price_from is not None) or (price_to is not None):
            main_filter.update(filter_price)

        if (category is not None):
            main_filter.update(filter_category)
            
        filtered_goods = website.data_access.getFilteredItems(main_filter)
    else:
        find_something_flag = False
        filtered_goods = all_items

    return render(request, "search/search.html", {"ifFind": find_something_flag,"category": unique_category, "goods": filtered_goods, "items": all_items, "ids": db_ids})
    
