console.log('js connected...')

let buttons_addToBasket = document.getElementsByClassName("add-basket");


for (let i = 0; i < buttons_addToBasket.length; i++) {
  buttons_addToBasket[i].addEventListener("click", function () {
    //add to basket 
    let currentProductsAmount = document.getElementById('basket_counter').innerHTML;
    document.getElementById('basket_counter').innerHTML = +currentProductsAmount + 1;
    //take info about product
    const productId = this.dataset.product;
    const actionOfButton = this.dataset.action;
    console.log(productId, actionOfButton);
    //ask about user auth
    /*
    if (user === "AnonymousUser") {
      console.log("not auth");
    } else {
      console.log("auth true");
    }
    */
    updateUserOrder(productId, actionOfButton);
  });
}


async function updateUserOrder(productId, actionOfButton){
    console.log('user is auth, send data');
    const url = `http://127.0.0.1:8000/item/${productId}/add/`;
    console.log('url: ' + url)
    await fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': actionOfButton})
    })
    .than((response) => {
        return response.json();
    })
    .than((data)=>{
        console.log('data: ' +data)
        location.reload();
    })
    .catch(err => console.log(err))
}

