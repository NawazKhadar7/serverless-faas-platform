class TenantPolicy:
    def __init__(self,quota=1000):
        if quota<1:raise ValueError('positive request quota required')
        self.quota=quota;self.used={}
    def admit(self,tenant):
        if not isinstance(tenant,str) or not tenant or len(tenant)>64:raise ValueError('invalid tenant')
        count=self.used.get(tenant,0)
        if count>=self.quota:return False
        self.used[tenant]=count+1;return True
