from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hamburguesa, Ingrediente, IngredienteEnHamburguesa

from hamburguesa import serializers

class HamburguesaView(APIView):

    serializer_class = serializers.HamburguesaSerializer

    def get(self, request,format=None):

        data = Hamburguesa.objects.all()
        serializer = self.serializer_class(data, many=True)
        result = serializer.data
        for index in range(len(result)):
            result[index]['ingredientes'] = []
            hamburguesa_id = result[index]['id']
            ingredientes = IngredienteEnHamburguesa.objects.filter(hamburguesa_id=hamburguesa_id)
            for element in ingredientes:
                result[index]['ingredientes'].append({'path':'https://burgerrestaurantapi.herokuapp.com/ingrediente/' + str(element.pk)})

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        
        data = request.data

        for parametro in data:
            if parametro not in ("nombre", "precio", "descripcion", "imagen"):
                return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            result = serializer.data
            result['ingredientes']=[]
            return Response(result, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
class HamburguesaIdView(APIView):

    serializer_class = serializers.HamburguesaSerializer

    def get(self, request, hamburguesa_id, format=None):
        hamburguesa_id = str(hamburguesa_id)
        if not hamburguesa_id.isnumeric():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            data = Hamburguesa.objects.get(pk=hamburguesa_id)
            serializer = self.serializer_class(data)
            result = serializer.data
            result['ingredientes']=[]
            ingredientes = IngredienteEnHamburguesa.objects.filter(hamburguesa_id=hamburguesa_id)
            for element in ingredientes:
                result['ingredientes'].append({'path':'https://burgerrestaurantapi.herokuapp.com/ingrediente/'+ str(element.pk)})
            return Response(result, status=status.HTTP_200_OK)

        except Hamburguesa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, hamburguesa_id, format=None):
        
        hamburguesa_id = str(hamburguesa_id)
        if not hamburguesa_id.isnumeric():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = request.data

        for parametro in data:
            if parametro not in ("nombre", "precio", "descripcion", "imagen"):
                return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            hamburguesa = Hamburguesa.objects.get(pk=hamburguesa_id)
            serializer = self.serializer_class(hamburguesa, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                result = serializer.data
                result['ingredientes']=[]
                ingredientes = IngredienteEnHamburguesa.objects.filter(hamburguesa_id=hamburguesa_id)
                for element in ingredientes:
                    result['ingredientes'].append({'path':'https://burgerrestaurantapi.herokuapp.com/ingrediente/' + str(element.pk)})
                return Response(result, status=status.HTTP_200_OK)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except Hamburguesa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



    def delete(self, request, hamburguesa_id, format=None):

        hamburguesa_id = str(hamburguesa_id)
        if not hamburguesa_id.isnumeric():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            data = Hamburguesa.objects.get(pk=hamburguesa_id)
            data.delete()
            return Response(status=status.HTTP_200_OK)
        except Hamburguesa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class IngredienteEnHamburguesaView(APIView):

    serializer_class = serializers.IngredienteEnHamburguesaSerializer

    def put(self, request, hamburguesa_id, ingrediente_id, format=None):

        ingrediente_id = str(ingrediente_id)
        hamburguesa_id = str(hamburguesa_id)
        if not ingrediente_id.isnumeric() or not hamburguesa_id.isnumeric():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            hamburguesa = Hamburguesa.objects.get(pk=hamburguesa_id)
        except Hamburguesa.DoesNotExist:
            return Response(status=status.HTTP_400__BAD_REQUEST)
        
        try:
            ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
        except Ingrediente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            ingr_hamb = IngredienteEnHamburguesa.objects.get(hamburguesa_id=hamburguesa_id,ingrediente_id=ingrediente_id)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except IngredienteEnHamburguesa.DoesNotExist:
                
            serializer = self.serializer_class(data={"hamburguesa_id":int(hamburguesa_id), "ingrediente_id":int(ingrediente_id)})

            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, hamburguesa_id, ingrediente_id, format=None):

        ingrediente_id = str(ingrediente_id)
        hamburguesa_id = str(hamburguesa_id)
        if not ingrediente_id.isnumeric() or not hamburguesa_id.isnumeric():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            hamburguesa = Hamburguesa.objects.get(pk=hamburguesa_id)
        except Hamburguesa.DoesNotExist:
            return Response(status=status.HTTP_400__BAD_REQUEST)
        try:
            data = IngredienteEnHamburguesa.objects.get(hamburguesa_id=hamburguesa_id, ingrediente_id=ingrediente_id)
            data.delete()
            return Response(status=status.HTTP_200_OK)
        except IngredienteEnHamburguesa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class IngredienteView(APIView):

    serializer_class = serializers.IngredienteSerializer

    def get(self, request,format=None):

        data = Ingrediente.objects.all()
        serializer = self.serializer_class(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        
        data = request.data
        
        for parametro in data:
            if parametro not in ("nombre", "descripcion"):
                return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()           
            result = serializer.data

            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredienteIdView(APIView):

    serializer_class = serializers.IngredienteSerializer

    def get(self, request, ingrediente_id, format=None):
        
        ingrediente_id_id = str(ingrediente_id)
        if not ingrediente_id.isnumeric():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            data = Ingrediente.objects.get(pk=ingrediente_id)
            serializer = self.serializer_class(data)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Ingrediente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, ingrediente_id, format=None):

        ingrediente_id_id = str(ingrediente_id)
        if not ingrediente_id.isnumeric():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        ingr_hamb = IngredienteEnHamburguesa.objects.filter(ingrediente_id=ingrediente_id)
        if ingr_hamb.count()>0:
            return Response(status=status.HTTP_409_CONFLICT)

        try:
            data = Ingrediente.objects.get(pk=ingrediente_id)
            data.delete()
            return Response(status=status.HTTP_200_OK)
        except Ingrediente.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
