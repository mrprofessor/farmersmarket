# farmersmarket
A checkout system for farmer's market


## Application structure

It will have some cli commands also for accepting the inputs and printing 
the receipt.

The cli and the business logic would be separate as I am planning to create
a tiny web app with a database using flask and probably mongodb.

For CLI We would be using Click as it's already integrated with Flask and we 
could reuse some of that logic.

```
    root
        server/(tentative)
        cli/
        marketservice/
        tests/
    config
    requirements.txt
```

## Code brainstorming
    1. The input model adapter should accept databases, csv or manual seed
    2. We would start with database design and implement those in models.

        - Table Product
            id name code price
        - Table Coupon
            id name description
        - Table BasketItem
            id product_id coupon_id discount

    3. The marketservice application will have all the rules and logic to 
        calulate the final price of each product and hence all products.



