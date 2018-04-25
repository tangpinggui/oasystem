

def disappear(self):
    redis_msg = self.conn.delete('message:%s' % self.current_user.name)
