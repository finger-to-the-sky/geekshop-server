window.onload = function (){
    $('.basket_list').on('click', 'input[type="number"]', function (){
        let target = event.target;
        let basketID = target.name;
        let basket_quantity = target.value;

        $.ajax({
            url: '/baskets/basket-edit/' + basketID + '/' + basket_quantity + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        })
    })
}