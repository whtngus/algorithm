
class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton,cls).__new__(cls)
        return cls.instance

# 두 s, s1은 같은 객체
s = Singleton()
print("Object created ",s)
s1 = Singleton()
print("Object created ",s1)