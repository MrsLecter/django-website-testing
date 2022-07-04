from django.shortcuts import render
import website.data_access

def basket(request):
    basket_data = request.session.get('basket', {})
    goods_ids = basket_data.keys()
    amount = len(goods_ids)
    temp_obj = {}
    total_price = 0
    data_arr = []
    for indx, id in enumerate(goods_ids):
        item = website.data_access.getObjectById(id, "goods")
        total_price += item['price']
        data_arr.append(item)

    return render(request, 'basket/basket.html', {"data":  data_arr, "amount": amount, "total": total_price })

def complete_purchase(request):
    return render(request, 'basket/complete_purchase.html')