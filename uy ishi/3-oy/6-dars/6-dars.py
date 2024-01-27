class Person:
    __id=0
    yosh_list=[]
    name_list=[]
    objects_list=[]
    def __init__(self, ism ,familya, yosh, jins):
        Person.__id=Person.__id+1
        self.__id=Person.__id
        self.ism=ism
        self.familya=familya
        self.yosh=yosh
        self.jins=jins
        object_list=[self.__id,self.ism,self.familya,self.yosh,self.jins]
        Person.objects_list.append(object_list)
        Person.yosh_list.append(self.yosh)
        Person.name_list.append(self.ism)

    @property
    def get_id(self):
        return self.__id

    def yosh_avg(self):
            a=sum(Person.yosh_list)
            natija=a//len(Person.yosh_list)
            return f"O'rtacha yosh:{natija}  "

    def max_name(self):
        max_leng=0
        max_name=""
        for i in Person.name_list:
            if len(i)>max_leng:
                max_leng=len(i)
                max_name=i
        return f"eng uzun ism:{max_name}"

    def min_name(self):
        min_leng=100000000000000
        min_name=""
        for i in Person.name_list:
            if len(i)<min_leng:
                min_leng=len(i)
                min_name=i
        return f"eng qisqa ism:{min_name}"

    def age_filter(self,inpyosh,belgi):
        filter_obj = []
        for i in Person.objects_list:
            if len(i) >= 4:
                if belgi == ">" and i[3] > inpyosh:
                    filter_obj.append(i)
                elif belgi == "<" and i[3] < inpyosh:
                    filter_obj.append(i)
                elif belgi == ">=" and i[3] >= inpyosh:
                    filter_obj.append(i)
                elif belgi == "<=" and i[3] <= inpyosh:
                    filter_obj.append(i)
                elif belgi == "==" and i[3] == inpyosh:
                    filter_obj.append(i)
                elif belgi == "!=" and i[3] != inpyosh:
                    filter_obj.append(i)
                
        return filter_obj




person3=Person("Ali","Anvarov",30,"erkak")
person1=Person("Zaxiriddin","Xatamov",20,"erkak")
person2=Person("Javohir","odilov",22,"erkak")
person4=Person("Aziz","komilov",10,"erkak")


print(Person.yosh_avg(Person.yosh_list))
print(Person.max_name(Person.name_list))
print(Person.min_name(Person.name_list))
print(Person.age_filter(Person.objects_list,20,">"))

