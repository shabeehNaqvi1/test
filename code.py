





class Collection(models.Model):
	title = models.CharField(max_length =255)
class Product(models.Model):
	productTitle = models.ForeignKey(Collection,on_delete=models.PROTECT)

class Customer(models.Model):
	name = models.CharField(max_length = 255)
class Order(models.Model):
	orderDetails = models.ForeignKey(Customer,on_delete=models.PROTECT)

class Cart(models.Model):
	title = models.CharField(max_length =200)
	created_at = models.DateTimeField(auto_now_add = True)

class Item(models.Model):
	itemtitle = models.ForeignKey(Cart,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)

