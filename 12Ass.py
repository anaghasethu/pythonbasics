
import camelcase

class products:
    def __init__(self,p_id,p_name,p_category,p_cost):
        self.p_id = p_id
        self.p_name = p_name
        self.p_category = p_category
        self.p_cost = p_cost

    def findcost(self):
        return f'{self.p_name} costs {self.p_cost}'

product = products(1000,"tshirt","fashion",599)

c=camelcase.CamelCase()

print(c.hump(product.findcost()))

