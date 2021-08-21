from rest_framework import serializers
from kitaplar.models import Kitap, Yorum



class YorumSerializers(serializers.ModelSerializers):
    class Meta:
        model = Yorum
        fields = '__all__'



class KitapSerializers(serializers.ModelSerializers):
    yorumlar = YorumSerializers(many)
    class Meta:
        model = Kitap
        fields = '__all__'


